Objects - Summary
=================

- *Think of named references to objects rather than variables*
  - Assignment attaches a name to an object
  - Assigning from one reference to another puts two name tags on the same object
- *The garbage collector reclaims unreachable objects*
- *`id()` returns a unique and constant identifier*
  - Rarely used in production
- *The `is` operator determines equality of identity*
- *Test for equivalence using `==`*
- *Function arguments are passed by object -reference*
  - Functions can modify mutable arguments
- *Reference is lost if a formal function argument is rebound*
  - To change a mutable argument, replace its _contents_
- *`return` also passes by object-reference*

- *Function arguments can be specified with defaults*
- *Default argument expressions evaluated once, when `def` is executed*
- *Python uses dynamic typing*
  - Types are not specified in advance
- *Python uses strong typing*
  - Types are not coerced to match
- *Names are looked up in up to four nested scopes*
  - _LEGB_ rule: (L)ocal, (E)nclosing, (G)lobal, (B)uilt-Ins
- *Global references can be read from a local scope*
  - Use `global`

- *Everything in Python is an object*
  - Including modules & functions; they can be treated like any other obj
- *`import` and `def` result in binding to named references*
- *`type` can be used to determine the type of an object*
- *`dir()` can be used to introspect on an object and get its attributes*
- *The name of a function of module object can be accessed through `__name__`*
- *The docstring for a function or module object can be accessed through `__doc__`

- *Use `len()` to measure the length of a string*
- *You can multiply a string by an integer*
  - Produces a new string with multiple copies of the operand
    - This is called the "repetition operation"
