Changelog
=========

:code:`mutatest` is alpha software, and backwards compatibility between releases is
not guaranteed while under development.


0.3.0
-----

    - Added new mutation support for :code:`NameConstant` in AST.
    - This includes substitutions for singleton assignments such as: :code:`True`, :code:`False`,
      and :code:`None`.
    - This is the first non-type mutation and required adding a :code:`readonly` parameter
      to the :code:`transformers.MutateAST` class. Additionally, the type-hints for the
      :code:`LocIndex` and :code:`MutationOpSet` were updated to :code:`Any` to support
      the mixed types. This was more flexible than a series of :code:`overload` signatures.


0.2.0
-----

    - Added new compare mutation support for:
        1. :code:`Compare Is` mutations e.g. :code:`is, is not`.
        2. :code:`Compare In` mutations e.g. :code:`in, not in`.

0.1.0
-----

    - Initial release!
    - Requires Python 3.7 due to the :code:`importlib` internal references for manipulating cache.
    - Run mutation tests using the :code:`mutatest` command line interface.
    - Supported operations:

        1. :code:`BinOp` mutations e.g. :code:`+ - / *` including bit-operations.
        2. :code:`Compare` mutations e.g. :code:`== >= < <= !=`.
        3. :code:`BoolOp` mutations e.g. :code:`and or`.
