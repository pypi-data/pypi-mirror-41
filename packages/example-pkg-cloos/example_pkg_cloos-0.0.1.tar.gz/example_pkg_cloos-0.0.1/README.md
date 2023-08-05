# example_pkg_cloos

[![image](https://img.shields.io/pypi/v/example_pkg_cloos.svg)](https://pypi.org/project/example-pkg-cloos)
[![image](https://img.shields.io/pypi/l/example_pkg_cloos.svg)](https://pypi.org/project/example-pkg-cloos)
[![image](https://img.shields.io/pypi/pyversions/example_pkg_cloos.svg)](https://pypi.org/project/example-pkg-cloos)

A example package to learn and test Python packaging.

https://packaging.python.org/tutorials/packaging-projects/

## Development workflow

Checkout git repository:

```shell
git clone git@github.com:cloos/python_example_pkg_cloos.git
```

Create virtualenv:

```shell
make venv
```

Activate virtualenv:

```shell
source venv/bin/activate
```

Install/Upgrade packaging tools:

```shell
make install
```

Install package in 'development mode':

```shell
make develop
```

Upload to https://test.pypi.org/:

```shell
make upload_test
```

Upload to https://pypi.org/:

```shell
make upload
```

## Usage

```shell
pip install example-pkg-cloos
```

### Cli

```shell
example-pkg-cloos --help
```

### Library

```python
from example_pkg_cloos.utils import print_bar, print_foo

print_bar()
print_foo()
```
