File & Resource Management - Summary
====================================

- `open(filename, [mode, encoding, ...])`
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
  - `close()`
    - in most cases, `close()` should be called inside `try...finally` to ensure its execution

- File objects support the iterator protocol
