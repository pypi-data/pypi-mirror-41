Reference
#########


.. py:currentmodule:: pg_jsonb_flattener


The `pg_jsonb_flattener` module has only one public entry-point which is the
:class:`JsonbTable` class:

.. autoclass:: JsonbTable
   :members:
   :undoc-members:
   :private-members:


----


All other classes and functions are not intended to be used but are also
documented below.

.. autoclass:: _Fragment
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _Array
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _Object
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _String
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _Integer
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _Number
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _JsonbField
   :members:
   :undoc-members:
   :private-members:

.. autofunction:: _fragment_factory


----


Finally the following classes and function are used to handle :mod:`sqlalchemy`
limitation concerning the use of Postgresql `WITH ORDINALITY` clause applied
to some Postgresql functions.

.. autoclass:: _OrdinableFunctionElement
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _JsonbArrayElements
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: _JsonbArrayElementsText
   :members:
   :undoc-members:
   :private-members:

.. autofunction:: _compile_orinable_function_element
