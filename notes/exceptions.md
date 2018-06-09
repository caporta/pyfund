Exception Handling
==================

- `raise` without args will re-raise the original exception
- `raise` can accomodate tuples of exceptions as args
- exceptions are as much a part of a function's spec as its arguments
  - exceptions are included in protocol definitions
    - e.g. sequence types should raise `IndexError` for out-of-range indecies
- use common exceptions when possible
  - `ValueError` -> right type, wrong value
  - `KeyError` -> mapping lookup fails
- avoid guarding against `TypeError`
