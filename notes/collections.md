Collections - Summary
=====================

- **Tuples**
  - Immutable sequence types
  - Literal syntax: optional parens around comma-separated list
  - Single element tuples must use trailing comma
  - Unpacking useful for multiple return vals and idiomatic swapping

- **Strings**
  - Immutable sequence types of _Unicode codepoints_
  - String concatenation is most efficiently performed with `join()` on an empty separator
  - The `partition()` method is a useful and elegant parsing tool
    - Takes a "separator" as an argument, returning a 3-tuple
  - The `format()` has a powerful API for string interpolation

- **Ranges**
  - Integer sequences of arithmetic progression at regular intervals
  - The `enumerate()` function is often a superior alternative

- **Lists**
  - Heterogeneous mutable sequence types
  - Negative indexes work backwards from the end
  - Slicing allows us to copy all or part of a list
    - _half-open_, or they omit the stop value
    - `arr[start:stop]`
  - common idioms for copying lists:
    1. _full slice_ => `arr[:]`
    2. `arr.copy()`
    3. `list(arr)`
  - List (and other collection) copies are shallow
  - List repetition is shallow

- **Dictionaries**
  - Map from immutable keys to mutable values
  - Iteration and membership testing is done via keys
  - Order is arbitrary
  - `keys()`, `values()`, and `items()` provide views onto different aspects of a dict, permitting convenient iteration techniques

- **Sets**
  - Unordered collections of unique elements
  - Support powerful and expressive set algebra operations and predicates
      - `union()` or `|` (commutative)
      - `intersection()` or `&` (commutative)
      - `difference()` or `-` (non-commutative)
      - `symmetric_difference()` or `^` (commutative)
      - `issubset()`
      - `issuperset()`
      - `isdisjoint()`

- **Collection Protocols**
  - A set of operations or methods that a type must support if it is to implement that protocol
  - _Container_
    - `str`, `list`, `range`, `tuple`, `bytes`, `set`, `dict`
    - Membership testing using `in` and `not in`
  - _Sized_
    - `str`, `list`, `range`, `tuple`, `bytes`, `set`, `dict`
    - Determine number of elements with `len(s)`
  - _Iterable_
    - `str`, `list`, `range`, `tuple`, `bytes`, `set`, `dict`
    - Can produce an _iterator_ with `iter(s)`
    - `for item in iterable: ...`
  - _Sequence_
    - `str`, `list`, `range`, `tuple`, `bytes`
    - Retrieve elements by index
      - `item = seq[index]`
    - Find items by value
      - `index = seq.index(item)`
    - Count items
      - `n = seq.count(item)`
    - Produce a reversed sequence
      - `r = reversed(seq)`
  - _Mutable Sequence_
    - `list`
  - _Mutable Set_
    - `set`
  - _Mutable Mapping_
    - `dict`

- **Notes**
  - Underscores (`_`) are conventionally used for dummy or superflous variables
    - e.g. seperators in `string.partition()`
  - `pprint` module supports pretty-printing complex data structures
