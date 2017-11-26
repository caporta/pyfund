File & Resource Management - Summary
====================================

- `open(filename, [mode, encoding, ...])` built-in
  - modes:
    - `r` => read (default)
    - `w` => write; truncate file first
    - `x` => exclusive creation; fails if file already exists
    - `a` => write; append to end of file if already exists

    - `b` => binary
    - `t` => text (default)
    - `+` => open disk file to update (read/write)
    - `U` universal newlines mode (legacy)

    - e.g. `wb` | `a+` | `rt`

  - methods:
    - `read([num codeponts])`
    - `readline()`
    - `readlines()` => list
    - `seek([codepoint])
    - `tell()` => offset from beginning to pointer
    - `close()`
      - in most cases, `close()` should be called inside `try...finally` to ensure its execution

- File objects support the iterator protocol
- **File objects are Context Managers**
  - `with` block provides resource cleanup with context managers
    - `with expression as var`
    - will invoke `close()` implictly
  - `open()` supports the context manager protocol
  - `import contextlib` module tools like `closing` to create our own context managers

- **Binary Files**
  - Device independent bitmaps

- **File-like objects**
  - Loosely defined set of behaviors for things that act like files
  - EAFP
