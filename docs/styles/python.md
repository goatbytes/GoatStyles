# Python Style Guide
## Introduction
Welcome to the Python Style Guide! This guide serves as a comprehensive resource for developers at GoatBytes.IO to maintain consistency and clarity in Python code across all projects.

### Purpose
The purpose of this style guide is to establish a set of conventions, best practices, and guidelines for writing Python code within GoatBytes.IO. By following these guidelines, developers can ensure that their code is not only clean and readable but also maintainable and scalable. Consistent coding practices across projects facilitate collaboration, reduce code review overhead, and enhance the overall quality of our software products.

### Scope
This style guide applies to all Python code written within GoatBytes.IO, including web applications, data analysis scripts, automation tools, and more. It covers various aspects of Python programming, including coding style, naming conventions, documentation practices, and programming practices. Whether you're writing backend APIs, machine learning models, or utility scripts, the guidelines outlined in this document are designed to be applicable and beneficial across all Python projects at GoatBytes.IO.

## General Principles
This guide is underpinned by core principles that guide our approach to software development in Kotlin. These principles are not mere rules but embody our vision for creating enduring, adaptable, and efficient code.

### Readability
Code is often read more frequently than it is written. We prioritize clarity and simplicity in our codebase, ensuring that it can be easily navigated and understood by any developer with Java knowledge, regardless of their familiarity with the specific project details.
### Consistency
A consistent codebase is key to a smooth development process and aids significantly in code comprehension. While we value the innovative solutions our developers bring to complex problems, we recognize the broader benefits of adhering to a unified set of coding standards.
### Efficiency
We strive for code that is not only performant but also mindful of resources. However, efficiency should not compromise the code's readability or maintainability. Optimizations are encouraged when clearly justified, ensuring that our focus on efficiency complements our core goals of clarity and maintainability.
### Scalability and Maintainability
Our coding practices are designed with the future in mind, aiming to produce a codebase that can evolve gracefully. This foresight allows for the integration of new features and technologies without disproportionate effort or disruption.
### Collaborative Development
Recognizing that software development is inherently collaborative, our code is written to facilitate teamwork. Through practices like code reviews and open discussions, we leverage the collective expertise of our team to refine and enhance our codebase.

## Formatting
Proper formatting in Python is crucial for maintaining readability, consistency across the codebase, and adherence to the community and language standards.

### Line Length
*   **Maximum Line Length**: Limit all lines to a maximum of 79 characters for code. For comments and docstrings, the limit is 72 characters. This ensures readability across various environments and devices.
### Indentation
*   **Use 4 Spaces for Indentation**: Consistently use four spaces per indentation level. Avoid using tabs, except to remain consistent with code that is already indented with tabs.
### Whitespace
*   **In Expressions and Statements**: Use whitespace sparingly inside parentheses, brackets, or braces. Around operators, use spaces for readability when prioritizing by precedence.

```python
# Good 
feed_count = (goats * 2) + (lambs * 3) 

# Avoid 
feed_count=(goats*2)+(lambs*3)
```

*   **Avoid Trailing Whitespace**: Ensure there is no space at the end of a line, maintaining cleanliness in the codebase.

### Imports
*   **Grouping and Ordering**: Group imports first (standard library imports, third-party imports, then local application/library specific imports) and separate each group with a blank line. Alphabetize them within each group.

```python
# Standard library imports
import os
import sys

# Third-party imports
from flask import Flask

# Local application imports
from local_module import local_class
```

### Blank Lines
*   **Top-Level Definitions**: Surround top-level function and class definitions with two blank lines.
*   **Method Definitions**: Use one blank line to separate method definitions inside classes.

### Source File Encoding
*   **UTF-8 Encoding**: Files should be encoded in UTF-8 without a BOM. UTF-8 is highly recommended for compatibility and internationalization.

### Import Formatting
*   **Avoid Wildcard Imports**: Explicitly state the imports rather than using wildcard imports (`from module import *`), as it makes the code clearer and avoids name conflicts.

### Naming Conventions
*   **Modules and Packages**: Use short, lowercase names, and underscore if it improves readability.
*   **Classes**: Use the CapWords convention.
*   **Functions and Variables**: Use lowercase with underscores between words.

### Comments and Docstrings
*   **Comments**: Should be complete sentences and used sparingly for clarifying complex parts of the code.
*   **Docstrings**: Write descriptive docstrings for all public modules, functions, classes, and methods.

**Example**
```python
class GoatPen:
    """Represents a pen containing goats."""

    def __init__(self, capacity=10):
        """Initialize the goat pen with an optional capacity."""
        self.capacity = capacity
        self.goats = []

    def add_goat(self, goat_name):
        """Add a goat to the pen by name."""
        if len(self.goats) < self.capacity:
            self.goats.append(goat_name)
        else:
            print("Pen is full. Cannot add more goats.")

    def feed_goats(self):
        """Feed all goats in the pen."""
        for goat in self.goats:
            print(f"Feeding {goat}.")

# Using the class
pen = GoatPen(capacity=5)
pen.add_goat("Billy")
pen.add_goat("Daisy")
pen.feed_goats()
```

## Naming Conventions
Adhering to consistent naming conventions is vital in Python development, as it enhances readability, facilitates code maintenance, and ensures codebase consistency.
### General Principles
*   **Descriptive Names**: Choose names that clearly describe their purpose or function, avoiding ambiguity and promoting ease of understanding.
*   **Conciseness**: While being descriptive, strive to keep names concise to maintain readability and avoid excessive verbosity.

### Specific Conventions
#### Variables and Functions
*   Use lowercase words separated by underscores for variable and function names, adhering to the snake\_case convention.

```python
def feed_goat(goat_name):
    print(f"Feeding {goat_name}")
```

#### Classes and Exceptions
*   Class and exception names follow the CapWords convention, capitalizing the first letter of each word.

```python
class GoatPen:
    pass

class GoatEscapeError(Exception):
    pass
```

#### Constants
*   Constants are defined at the module level and use uppercase letters with underscores separating words.

```python
MAX_GOATS_IN_PEN = 5
```

#### Modules and Packages
*   Module names should be concise, lowercased, and avoid underscores whenever feasible. Packages should also adhere to short, lowercase naming, with underscores used only when necessary for readability.

```python
# Module name example 
import goatcare
```

### Avoiding Ambiguity and Redundancy
*   Names should not be redundant with their context, as this can lead to verbosity without adding clarity. For instance, avoid prefixing names with the name of the class or module.

```python
# Avoid
class Goat:
    goat_name = None

# Prefer
class Goat:
    name = None
```

### Use of Underscores
*   **Private or "Protected" Attributes**: Use a single leading underscore to denote "protected" or non-public attributes within classes. For internal use, prepend with a double underscore to invoke Python's name mangling.

```python
class Goat:
    _name = "Private Name"
    __hidden_attribute = "Not Directly Accessible"
```

### Special Considerations
*   **Name Mangling**: When using double underscores, Python alters the way the name can be accessed to prevent accidental modification. However, this feature should be used judiciously, primarily to avoid name clashes in subclasses.
*   **Dunder Names**: System-defined names that have a special meaning to the interpreter, like `__init__` and `__call__`, should only be used as documented.

## Documentation and Comments
Effective documentation and clear commenting are key to maintaining readability and understandability in Python code.
### Documentation Strings (Docstrings)
*   **Purpose**: Provide clear documentation for all public modules, functions, classes, and methods. Docstrings should follow the triple double-quote (`"""`) format and explain the object’s purpose and behavior.
*   **Conventions**: Adhere to PEP 257 for docstring conventions. For functions and methods, document their parameters, return values, and possible side effects.
*   **Accessibility**: Use the built-in `help()` function to make the documentation accessible.

#### Example:
```python
def herd_goats(goats):
    """Guide a list of goats back to their pen.

    Args:
        goats (list of str): A list containing the names of the goats.

    Returns:
        None
    """
    for goat in goats:
        print(f"Guiding {goat} back to the pen.")
```

### Inline Comments
*   **Clarity**: Use inline comments sparingly and only when they add significant value or clarification to the code.
*   **Placement**: Place inline comments on the same line as the statement they refer to, separated by at least two spaces from the code, followed by a `#` and a single space before the comment text.

#### Example:
```python
feed_time = True # Goats are fed at sunrise and sunset
```

### Block Comments
*   **Format**: Block comments apply to some or all of the code that follows them and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space.
*   **Purpose**: Use block comments to explain complex parts of the code or to provide an overview of the upcoming code.

**Example**
```python
# Check if it's time to feed the goats
# If so, guide them to the feeding area
if feed_time:
    herd_goats(['Billy', 'Daisy'])
```

### Commenting Out Code
*   **Caution**: Avoid leaving large blocks of commented-out code in your final source files. If the code is important enough to keep, consider archiving it separately.

### Use of TODO Comments
*   **Indication of Incompleteness**: Use `TODO` comments for code that is temporary, a short-term solution, or good enough but not perfect.
*   **Format**: Mark `TODO` comments with your initials and an action item or a question.

#### Example:
```python
# TODO: [TICKET-123] Improve goat herding efficiency - perhaps use a goat dog?
```

## Programming Practices
Adopting effective programming practices is essential for writing clean, efficient, and maintainable Python code.
### Use of Globals
*   **Minimize Global Variables**: Limit the use of global variables to constants or when absolutely necessary. Global variables can introduce dependencies and unpredictability in your code.

### Exception Handling
*   **Explicit is Better Than Implicit**: Handle exceptions explicitly whenever possible and avoid catching broad exceptions. Use specific exception types to handle anticipated error conditions.

```python
try:
    open_goat_pen()
except PenLockedError:
    unlock_pen()
    open_goat_pen()
```

### Comparisons
*   **Simplicity in Conditional Expressions**: Use the implicit boolean nature of objects in Python rather than comparing directly to `True` or `False` or checking for emptiness.

```python
if goats_in_pen:
    feed_goats()
```

### Looping Techniques
*   **Iterate Directly Over Objects**: Use Python's direct iteration capabilities over lists and dictionaries rather than iterating over indexes.

```python
for goat in goats:
    print(f"Feeding {goat}")
```

### Comprehensions
*   **Use Comprehensions Sparingly**: While list, dict, and set comprehensions are powerful and expressive, ensure they remain readable. Avoid overly complex expressions.

```python
fed_goats = {goat.name for goat in goats if goat.is_hungry}
```

### Function Arguments
*   **Default Arguments**: Use default argument values for more concise and clear function signatures. Avoid mutable default arguments to prevent unexpected behavior.

```python
def add_goat_to_pen(goat, pen=None):
    if pen is None:
        pen = []
    pen.append(goat)
```

## Language-Specific Idioms and Patterns
Understanding and utilizing Python's unique idioms and patterns can significantly enhance code quality and efficiency.
### The Zen of Python
*   **Readability Counts**: Embrace Python's philosophy for simplicity and clarity, as encapsulated in the Zen of Python (`import this`). Strive for readable and understandable code.

### Using Underscores
*   **Single Leading Underscore**: Indicate "internal use" or "protected" attributes with a single leading underscore. It's a hint for other programmers and does not affect the Python runtime behavior.

```python
class Goat:
    def __init__(self):
        self._name = "Billy"
```

### Resource Management
*   **Context Managers**: Use context managers (`with` statement) for resource management to ensure resources are properly managed without explicit cleanup codes.

```python
with open('goat_log.txt', 'w') as file:
    file.write("Goat entered the pen.")
```

### Using `get()` for Dictionaries
*   **Safe Dictionary Access**: Use the `get()` method to access dictionary elements to avoid `KeyError` exceptions.

```python
goat_feed = goat_feeds.get('Billy', 'default_feed')
```

### Dynamic Typing
*   **Type Hinting**: Use type hints to clarify the expected types of function arguments and return values, enhancing readability and supporting static analysis tools.

```python
from typing import List

def herd_goats(goats: List[str]) -> None:
    pass
```

## Tools and IDE Setup
For the modern Python engineer, setting up an efficient development environment is crucial. This section guides you through configuring your tools and IDE (Integrated Development Environment) to enhance productivity and ensure your code adheres to the style guide, with a focus on Python development.
### IDE Configuration
#### **PyCharm**
PyCharm by JetBrains is a popular IDE for Python development, offering a wide range of features to support coding, debugging, and testing Python applications.
*   **Code Style**: Configure code style settings in PyCharm under `Preferences` → `Editor` → `Code Style` → `Python`. Here, you can set indentation, line length, and other formatting options to align with PEP 8.
*   **PEP 8 Checks**: Enable real-time PEP 8 compliance checks under `Editor` → `Inspections` → `Python` → `PEP 8 coding style violation`. PyCharm will highlight deviations from PEP 8 as you type.

#### **Visual Studio Code (VS Code)**
VS Code is a lightweight, open-source code editor that supports Python through extensions.
*   **Python Extension**: Install the Python extension by Microsoft to get rich support for Python. This extension offers features like IntelliSense, linting, debugging, and more.
*   **Formatting**: Use auto-formatting features by configuring your preferred formatter (e.g., `black`, `autopep8`) in the settings (`Preferences` → `Settings`), under `Python` → `Formatting`. You can format a file automatically on save by enabling `Editor: Format On Save`.

### Linting and Formatting Tools
*   **Flake8**: Integrates with most IDEs and editors to check your code base against coding style (PEP 8), programming errors, and complexity.
*   **Black**: Known as the uncompromising code formatter, Black can be configured to automatically format your code to adhere to PEP 8, with minor deviations for improved readability.
*   **isort**: Automatically sorts and sections your Python imports. Configure it to match your project's import ordering conventions.

### Virtual Environments
Using virtual environments is a best practice for managing project-specific dependencies and avoiding conflicts between different projects.
*   **venv**: Use Python's built-in `venv` module to create isolated environments for your projects. Activate a virtual environment before installing project dependencies with pip.

```shell
python -m venv my_project_env
source my_project_env/bin/activate  # On Unix/macOS
my_project_env\Scripts\activate.bat # On Windows
```
