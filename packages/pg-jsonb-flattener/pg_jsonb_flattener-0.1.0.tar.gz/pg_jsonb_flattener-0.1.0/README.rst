pg_jsonb_flattener
##################

The `pg_jsonb_flattener` is a tool to ease selection of Postgresql table which
contains JSONB typed fields.

Provided with a description of the data (a sort of jsonschema) contained in a
JSONB field, it is able to build a selectable sqlalchemy expression which can
be used as a plain Postgresql table for SELECT queries.


Usage
*****

The tool is used by instantiating a `JsonbTable` providing it:

* a sqlaclehmy table description as the only positionnal argument
* a *JSON data description* for each *JSONB field* to flatten as named arguments
  where the argument name is the *JSONB field* name and the argument value is
  the *JSON data description*.

The code below illustrates how the tool can be used to obtain a
`flat selectable` from a data description written in a JSON file.

.. code-block:: python

   from sqlalchemy import create_engine, MetaData, Table
   from pg_jsonb_flattener import JsonbTable

   ENGINE = create_engine('some database URL')
   METADATA = MetaData()
   ONE_JSON_FIELD_TABLE = Table(
       'one_json_field_table', METADATA,
       Column('field_one', JSONB)
   )
   DATA_DESCRIPTION = json.load('path/to/data_description.json')

   jsonb_table = JsonbTable(ONE_JSON_FIELD_TABLE, field_one=DATA_DESCRIPTION)

   flat_selectable = jsonb_table.get_query()

   with engine.connect() as conn:
       result = conn.execute(flat_selectable).fetchall()

Then, the ``flat_selectable`` variable contains a selectable expression which acts
as a table where the JSONB `field_one` field has been replaced by several
scalar typed fields whose names are build from the original JSONB field name
and the path of the data in the data structure, with a double undercore as
separator.

You can execute directly the ``flat_selectable`` to inspect what it contains
(this is what is done in the example to get the ``result`` variable) or use it as
a plain table to build more complex queries.

See below examples for more details.


Simple types
============

Given the following data description::

   {
     "type": "object",
     "properties": {
       "integer": {"type": "integer"},
       "number": {"type": "number"},
       "string": {"type": "string"}
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__integer``
* ``field_one__number``
* ``field_one__string``

Given the following JSON data in one record::

   {
     "integer": 42,
     "number": 3.141592,
     "string": "pouet"
   }

The ``result`` variable would contain this:

+-----------------------+----------------------+----------------------+
| field_one__integer    | field_one__number    | field_one__string    |
+=======================+======================+======================+
| 42                    | 3.141592             | pouet                |
+-----------------------+----------------------+----------------------+


Simple objects
==============

Given the following data description::

   {
     "type": "object",
     "properties": {
       "object": {
         "type": "object",
         "properties": {
           "obj_int": {"type": "integer"},
           "obj_num": {"type": "number"},
           "obj_str": {"type": "string"}
         }
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__object__obj_int``
* ``field_one__object__obj_num``
* ``field_one__object__obj_str``

Given the following JSON data in one record::

   {
     "object": {
       "obj_int": 42,
       "obj_num": 3.141592,
       "obj_str": "pouet"
     }
   }

The ``result`` variable would contain this:

+----------------------------------+----------------------------------+----------------------------------+
| field_one__object__obj_int       | field_one__object__obj_num       | field_one__object__obj_str       |
+==================================+==================================+==================================+
| 42                               | 3.141592                         | pouet                            |
+----------------------------------+----------------------------------+----------------------------------+


Simple arrays
=============

Given the following data description::

   {
     "type": "object",
     "properties": {
       "int_arr": {
         "type": "array",
         "items": {"type": "integer"}
       },
       "num_arr": {
         "type": "array",
         "items": {"type": "number"}
       },
       "str_arr": {
         "type": "array",
         "items": {"type": "string"}
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__int_arr__item``
* ``field_one__int_arr__item__index``
* ``field_one__num_arr__item``
* ``field_one__num_arr__item__index``
* ``field_one__str_arr__item``
* ``field_one__str_arr__item__index``

.. note::

   As you can see each array field is suffixed by an `item` part and each array
   data is identified by an index which allows to retrieve the order of the
   data in the JSONB array.

Given the following JSON data in one record::

   {
     "int_arr": [42, 77, 1664],
     "num_arr": [3.141592, 1.618034, 37.2],
     "str_arr": ["pouet", "foo", "bar"]
   }

The ``result`` variable would contain this:

+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| field_one__int_arr__item | field_one__int_arr__item__index | field_one__num_arr__item | field_one__num_arr__item__index | field_one__str_arr__item | field_one__str_arr__item__index |
+==========================+=================================+==========================+=================================+==========================+=================================+
| 42                       | 1                               | NULL                     | NULL                            | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| 77                       | 2                               | NULL                     | NULL                            | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| 1664                     | 3                               | NULL                     | NULL                            | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | 3.141592                 | 1                               | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | 1.618034                 | 2                               | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | 37.2                     | 3                               | NULL                     | NULL                            |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | NULL                     | NULL                            | pouet                    | 1                               |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | NULL                     | NULL                            | foo                      | 2                               |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+
| NULL                     | NULL                            | NULL                     | NULL                            | bar                      | 3                               |
+--------------------------+---------------------------------+--------------------------+---------------------------------+--------------------------+---------------------------------+


Array of objects
================

Given the following data description::

   {
     "type": "object",
     "properties": {
       "array": {
         "type": "array",
         "items": {
           "type": "object",
           "properties": {
             "obj_int": {"type": "integer"},
             "obj_num": {"type": "number"},
             "obj_str": {"type": "string"}
           }
         }
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__array__item__index``
* ``field_one__array__item__obj_int``
* ``field_one__array__item__obj_num``
* ``field_one__array__item__obj_str``

Given the following JSON data in one record::

   {
     "array": [
       {
         "obj_int": 42,
         "obj_num": 3.141592,
         "obj_str": "pouet"
       },
       {
         "obj_int": 77,
         "obj_num": 1.618034,
         "obj_str": "toto"
       }
     ]
   }

The ``result`` variable would contain this:

+-------------------------------+---------------------------------+---------------------------------+---------------------------------+
| field_one__array__item__index | field_one__array__item__obj_int | field_one__array__item__obj_num | field_one__array__item__obj_str |
+===============================+=================================+=================================+=================================+
| 1                             | 42                              | 3.141592                        | pouet                           |
+-------------------------------+---------------------------------+---------------------------------+---------------------------------+
| 2                             | 77                              | 1.618034                        | toto                            |
+-------------------------------+---------------------------------+---------------------------------+---------------------------------+


Arrays in object
================

Given the following data description::

   {
     "type": "object",
     "properties": {
       "object": {
         "type": "object",
         "properties": {
           "int_arr": {
             "type": "array",
             "items": {"type": "integer"}
           },
           "num_arr": {
             "type": "array",
             "items": {"type": "number"}
           },
           "str_arr": {
             "type": "array",
             "items": {"type": "string"}
           }
         }
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__object__int_arr__item``
* ``field_one__object__int_arr__item__index``
* ``field_one__object__num_arr__item``
* ``field_one__object__num_arr__item__index``
* ``field_one__object__str_arr__item``
* ``field_one__object__str_arr__item__index``

Given the following JSON data in one record::

   {
     "object": {
       "int_arr": [42, 77, 1664],
       "num_arr": [3.141592, 1.618034, 37.2],
       "str_arr": ["pouet", "foo", "bar"]
     }
   }

The ``result`` variable would contain this:

+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| field_one__object__int_arr__item | field_one__object__int_arr__item__index | field_one__object__num_arr__item | field_one__object__num_arr__item__index | field_one__object__str_arr__item | field_one__object__str_arr__item__index |
+==================================+=========================================+==================================+=========================================+==================================+=========================================+
| 42                               | 1                                       | NULL                             | NULL                                    | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| 77                               | 2                                       | NULL                             | NULL                                    | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| 1664                             | 3                                       | NULL                             | NULL                                    | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | 3.141592                         | 1                                       | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | 1.618034                         | 2                                       | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | 37.2                             | 3                                       | NULL                             | NULL                                    |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | NULL                             | NULL                                    | pouet                            | 1                                       |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | NULL                             | NULL                                    | foo                              | 2                                       |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+
| NULL                             | NULL                                    | NULL                             | NULL                                    | bar                              | 3                                       |
+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+----------------------------------+-----------------------------------------+


Nested objects
==============

Given the following data description::

   {
     "type": "object",
     "properties": {
       "object": {
         "type": "object",
         "properties": {
           "nested": {
             "type": "object",
             "properties": {
               "obj_int": {"type": "integer"},
               "obj_num": {"type": "number"},
               "obj_str": {"type": "string"}
             }
           }
         }
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__object__nested__obj_int``
* ``field_one__object__nested__obj_num``
* ``field_one__object__nested__obj_str``

Given the following JSON data in one record::

   {
     "object": {
       "nested": {
         "obj_int": 42,
         "obj_num": 3.141592,
         "obj_str": "pouet"
       }
     }
   }

The ``result`` variable would contain this:

+------------------------------------+------------------------------------+------------------------------------+
| field_one__object__nested__obj_int | field_one__object__nested__obj_num | field_one__object__nested__obj_str |
+====================================+====================================+====================================+
| 42                                 | 3.141592                           | pouet                              |
+------------------------------------+------------------------------------+------------------------------------+


Nested arrays
=============

Given the following data description::

   {
     "type": "object",
     "properties": {
       "nested_arrays": {
         "type": "array",
         "items": {
           "type": "array",
           "items": {"type": "string"}
         }
       }
     }
   }

``flat_selectable`` would provide the following fields:

* ``field_one__nested_arrays__item__index``
* ``field_one__nested_arrays__item__item__index``
* ``field_one__nested_arrays__item__item``

Given the following JSON data in one record::

   {
     "nested_arrays": [
       ["abc", "def"],
       ["tuw", "xyz"]
     ]
   }

The ``result`` variable would contain this:

+---------------------------------------+---------------------------------------------+--------------------------------------+
| field_one__nested_arrays__item__index | field_one__nested_arrays__item__item__index | field_one__nested_arrays__item__item |
+=======================================+=============================================+======================================+
| 1                                     | 1                                           | abc                                  |
+---------------------------------------+---------------------------------------------+--------------------------------------+
| 1                                     | 2                                           | def                                  |
+---------------------------------------+---------------------------------------------+--------------------------------------+
| 2                                     | 1                                           | tuw                                  |
+---------------------------------------+---------------------------------------------+--------------------------------------+
| 2                                     | 2                                           | xyz                                  |
+---------------------------------------+---------------------------------------------+--------------------------------------+
