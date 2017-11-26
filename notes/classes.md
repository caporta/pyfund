Classes - Summary
=================

- All types in Python have a class
- Classes define the structure and behavior of an object
- Class is determined when object is created
  - normally fixed for lifetime of object
- Methods called using `instance.method()`
  - Syntactic sugar for passing `self` instance to method
- Optional `__init__()` method initializes new instances
  - Not the constructor
  - If present, the constructor calls `__init__()`

- Instance attributes are created simply by assigning to them
- Implementation details are denoted by leading underscore convention
  - No `public`, `protected`, or `private` access modifiers
- "Class invariants" should be established in the initializer
  - Raise exceptions to signal failure if invariants can't be established
- Method calls must be preceded with `self`, even within object
- Modules can contain any mix and number of classes and functions
  - Common to group together related classes and global functions

- Polymorphism is achieved through duck typing, not through shared base classes or interfaces
- Class inheritance should be limited primarily for sharing implementation
- All methods are inherited, including special methods

