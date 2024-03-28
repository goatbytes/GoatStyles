# Python Style Guide

This guide is dedicated to writing clean, Pythonic code that adheres to best practices and embraces
the nuances of Python development. It underscores idiomatic usage, performance, and maintainability.

[//]: # (@formatter:off)
/// admonition | 
    type: abstract
[Foundational Code Standards][fnd]{:target="_blank"} provide the foundation, this guide extends them for Python.
///
[//]: # (@formatter:on)

## Formatting

While Python's PEP 8 provides comprehensive formatting guidelines,
our [Foundational Code Standards][fnd-formatting] also apply. Key Python-specific considerations
include:

- **Indentation:** Use 4 spaces per indentation level.
- **Line Length:** Limit lines to 79 characters (and docstrings/comments to 72).
- **Imports:** Group imports into standard library, third-party, and local application/library
  specific, separated by blank lines.
- **Whitespace:** Use whitespace sparingly inside parentheses, brackets, and braces.

## Naming Conventions

Pythonic naming favors readability and conciseness:

- **Classes:** Use `CamelCase` for class names without underscores.
- **Functions and Variables:** Use `snake_case` for function names, variables, and method names.
- **Constants:** Define constants in `UPPER_SNAKE_CASE`.
- **Protected and Private:** Use `_protected` and `__private` naming conventions for non-public
  methods and variables.

## Commenting and Documentation

### Inline Comments

Inline comments should be used sparingly and must be meaningful. Explain "why" rather than "what".

### Docstrings

Follow PEP 257 for docstring conventions. Use triple double quotes and describe the function's
effect as a command:

```python
def feed_goat(goat, food):
    """
    Feed a goat with the specified food.

    Args:
        goat (Goat): The goat to be fed.
        food (str): The type of food.

    Returns:
        bool: True if feeding is successful, False otherwise.
    """
```

Error Handling
Prefer explicit exception handling over silent failures. Catch specific exceptions whenever possible:

```python
try:
    # risky operation
except ValueError as e:
    # specific error handling
except Exception as e:
    # generic error handling
```

## Idioms and Best Practices

### List Comprehensions

Use list comprehensions to create lists in a concise and readable manner:

```python
squared = [x**2 for x in range(10)]
```

### The Zen of Python

Embrace the Zen of Python (import this) as a guiding philosophy. Prioritize readability, simplicity, and the "Pythonic" way of accomplishing tasks.

### Generators

Leverage generators to create iterators without storing the entire sequence in memory:

```python
def goat_names():
    for goat in goat_herd:
        yield goat.name
```

## Tools and Resources

### Algorithms and Design Patterns

* Algorithms
    * [algorithms](https://github.com/keon/algorithms) - Minimal examples of data structures and algorithms.
    * [python-ds](https://github.com/prabhupant/python-ds) - A collection of data structure and algorithms for coding interviews.
    * [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) - Fast and pure-Python implementation of sorted collections.
    * [thealgorithms](https://github.com/TheAlgorithms/Python) - All Algorithms implemented in Python.
* Design Patterns
    * [pypattyrn](https://github.com/tylerlaberge/PyPattyrn) - A simple yet effective library for implementing common design patterns.
    * [python-patterns](https://github.com/faif/python-patterns) - A collection of design patterns in Python.
    * [transitions](https://github.com/pytransitions/transitions) - A lightweight, object-oriented finite state machine implementation.

### IDEs and Editor Plugins

* [PyCharm](https://www.jetbrains.com/pycharm/) - Commercial Python IDE by JetBrains.
* [Visual Studio](https://visualstudio.microsoft.com/) with [PTVS](https://github.com/Microsoft/PTVS)
* [Visual Studio Code](https://code.visualstudio.com/) with [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [spyder](https://github.com/spyder-ide/spyder) - Open Source Python IDE.

### Static Analysis

- [Black](https://black.readthedocs.io/en/stable/): The uncompromising Python code formatter that adheres to PEP 8 and improves code readability.
- [Flake8](https://github.com/PyCQA/flake8): A tool that enforces PEP 8 style guide and helps catch common programming errors.
- [MyPy](https://github.com/python/mypy): A static type checker for Python that supports gradual typing.
- [Pytest](https://docs.pytest.org/en/latest/): Utilize pytest for testing and coverage analysis.
- [Sphinx](https://github.com/sphinx-doc/sphinx/) - Python Documentation generator.: Use Sphinx for generating documentation from docstrings.
- [Pylint](https://github.com/pylint-dev/pylint): A source code analyzer that checks for errors in Python code.

[//]: # (@formatter:off)
