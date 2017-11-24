Iterables
=========

- **Comprehensions**
  - Concise syntax for describing lists, sets, and dictionaries
  - Operate on an iterable source object and apply an optional predicate filter and a mandatory expression
  - Iterables are objects over which we can iterate item by item
  - We retrieve an iterator from an iterable object using the `iter()` built-in
  - Iterators product items one-by-one from the underlying iterable series each time they're passed into the `next()` built-in
  - When iteration is exhausted, iterables raise a `StopIteration` exception

- **Generators**
  - Generator functions allow us to describe series using imperative code
  - They contain at least one use of the `yield` keyword
  - Generators are iterators. When advancing with `next()`, the generator starts or resumes execution up to and including the next `yield`
  - Each call to a generator function creates a new generator object
  - Generators can maintain explicit state in local variables between iterations
  - They are lazy, so they can model infinite series of data
  - Generator _expressions_ have a similar syntactic form to list comprehensions, and allow for more declarative and concise creation of generator objects

- **Iteration Tools**
  - Built-ins:
    - `sum()`
    - `any()`
    - `zip()`
    - `all()`
    - `min()`
    - `max()`
    - `enumerate()`
  - Standard lib `itertools` module:
    - `chain()`
    - `islice()`
    - `count()`
    - & more...
