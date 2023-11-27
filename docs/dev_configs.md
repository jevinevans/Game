# Development Configurations

## Flake8 Config

- Updated version to include flake8-fixeme to see fixme, To Do, etc. comments

```bash
flake8 --version 
3.9.2 (flake8-fixme: 1.1.1, mccabe: 0.6.1, pycodestyle: 2.7.0, pyflakes: 2.3.1) CPython 3.8.10 on Linux
```

```bash
IGNS="E231,E266,E401,E501,W293"
flake8 --ignore=$INGS --count ./FUNCLG >> $REPORT
```

### Ignore List

- [E231] missing whitespace after ':'
- [E266] too many leading '#' for block comment
- [E401] multiple imports on one line
- [E501] line too long (161 > 79 characters)
- [W293] blank line contains whitespace

<!-- Links to Issues -->
[i28]: https://github.com/jevinevans/Game/issues/28
[i29]: https://github.com/jevinevans/Game/issues/29
