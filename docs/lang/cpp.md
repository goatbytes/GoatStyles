# C++ Style Guide

This guide specifically addresses C++ development, focusing on idiomatic practices, patterns, and
C++-specific considerations.

[//]: # (@formatter:off)
/// admonition |
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for C++.
///
[//]: # (@formatter:on)

## Formatting

The formatting rules for C++ adhere to our foundational [formatting standards][FORMATTING] with the
following exceptions:

- **Indentation:** Use 4 spaces for indentation.
- **Continuation indent:** Use 8 spaces for line continuations.

Otherwise, follow the conventions outlined in the foundational standards, summarized below:

- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Whitespace:** Use spaces around operators, parentheses, braces, colons, commas, and keywords for
  clarity.
- **Brace Style:** Follow K&R style (opening brace on same line, closing brace on new line).
- **Blank Lines:** Use 1 line to separate code sections.
- **Alignment:** Align elements in documentation comments and parameter lists.

[//]: # (@formatter:off)
/// admonition |
    type: info
Remember, these are guidelines; adapt them for your project's needs while keeping readability in focus.
///

## Naming Conventions

The naming conventions for Kotlin adhere to our foundational [naming conventions][NAMING]
with no exceptions.

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with `is` or `has` for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

---

**Example**

```cpp
/**
 * This class demonstrates proper code formatting following the specified style guide.
 *
 * **Formatting Rules:**
 * - 4 spaces for indentation (C++ exception).
 * - 8 spaces for continuation lines (C++ exception).
 * - Max line length of 100 characters.
 * - Spaces around operators, control structures, and keywords.
 * - K&R brace style.
 * - Consistent spacing for parameter lists and constructor arguments.
 * - Doc comments with aligned descriptions.
 */
class WellFormattedCode/*(1)!*/ {
public:
    /**
     * This method calculates the factorial of a given positive integer.
     *
     * @param n The non-negative integer for which to calculate the factorial.
     * @return  The factorial of n, or throws an std::invalid_argument exception if n is negative.
     * @throws std::invalid_argument If the provided number (n) is negative.
     */
    static long calculateFactorial/*(2)!*/(int n) {
        if (n < 0) {// (3)!
            throw std::invalid_argument("Factorial is not defined for negative numbers.");
        }

        long result = 1;
        for (int i = 2; i <=/*(4)!*/ n; ++i) {
            result *= i;
        }
        return result;
    }
};
```

1.    Class name in PascalCase with a doc comment.
2.    Method name in camelCase with a doc comment.
3.    K&R brace style for blocks.
4.    Proper spacing around operators and control structures.

[//]: # (@formatter:on)

---

## Documentation and Comments

Refer to the [Foundational Documentation and Comments Standards][DOCS] for general commenting and 
documentation guidelines.

### Documentation Example

```cpp
#include <stdexcept>
#include <string>
#include <iostream>

/**
 * Represents a goat with a name and age, offering functionality to determine its happiness.
 * 
 * This class encapsulates essential attributes for a goat and provides a method to assess
 * the goat's happiness based on the number of meals it has received within a day.
 *
 * **Usage Example:**
 * `
 * Goat billy("Billy", 5);
 * std::cout << (billy.isHappy(3) ? "True" : "False") << std::endl;
 * `
 * 
 * @author Author's Name
 * @param name The name of the goat.
 * @param age The age of the goat in years. Must be non-negative.
 * @throws std::invalid_argument if the age is negative.
 */
class Goat {
public:
    Goat(const std::string& name, int age) : name_(name), age_(age) {
        if (age < 0) {
            throw std::invalid_argument("Age cannot be negative");
        }
    }

    /**
     * Determines if the goat is happy based on the number of meals it has received today.
     * 
     * A goat is considered happy if it has been fed at least twice a day.
     * 
     * @param meals The number of meals the goat has received today.
     * @return true if the goat is happy (fed at least twice today), false otherwise.
     * @throws std::invalid_argument if the number of meals is negative.
     */
    bool isHappy(int meals) const {
        if (meals < 0) {
            throw std::invalid_argument("Meals cannot be negative");
        }
        return meals >= 2;
    }

private:
    std::string name_;
    int age_;
};

```

## Idioms and Best Practices

C++ offers a wealth of idiomatic practices and patterns that can enhance your code's efficiency,
readability, and safety. This section focuses on leveraging C++'s unique features effectively.

### Smart Pointers

Use smart pointers (std::unique_ptr, std::shared_ptr, std::weak_ptr) for dynamic memory management
to avoid leaks.

### RAII

Leverage Resource Acquisition Is Initialization (RAII) for managing resources like file handles and
mutexes.

### Move Semantics

Utilize move semantics to avoid unnecessary copying of objects, especially for return values and
function arguments.

### constexpr

Prefer constexpr for compile-time initialization of constants to improve performance.

### Rule of Five

Follow the Rule of Five for classes that manage resources directly, ensuring proper copy and move
semantics.

### Templates

Use templates for generic programming, allowing for code reuse across different data types.

## Tools and Resources

### Recommended Static Analysis Tools for C++

For ensuring code quality and adherence to this style guide, we recommend integrating the following
static analysis tools into your C++ development workflow:

- [**Cppcheck**](http://cppcheck.sourceforge.net/): A static analysis tool for C/C++ code that
  detects various types of errors, including memory leaks, misuses of the standard library, and
  more.
- [**Clang-Tidy**](https://clang.llvm.org/extra/clang-tidy/): Part of the LLVM project, this linter
  tool provides a framework for writing checks that detect errors, bugs, and stylistic issues in C++
  code.
- [**Coverity**](https://scan.coverity.com/): Offers static code analysis to identify software
  vulnerabilities and compliance issues.
- [**CodeSonar**](https://www.grammatech.com/products/codesonar): A comprehensive tool for static
  analysis, detecting bugs, security vulnerabilities, and compliance violations in C and C++
  codebases.

### Additional Resources

To further enhance your C++ development skills and knowledge, consider exploring the following
resources:

- [**C++ Core Guidelines**](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines): An
  extensive set of guidelines maintained by the C++ community and the Standard C++ Foundation to
  help C++ programmers achieve higher code quality.
- [**Effective Modern C++**][Effective Modern C++]: A book by Scott Meyers that covers the effective
  use of the C++11 and C++14 standards.
- [**The C++ Programming Language**](http://www.stroustrup.com/4th.html): Written by Bjarne
  Stroustrup, the creator of C++, this book provides comprehensive coverage of the C++ language,
  including its standard library and key design techniques.
- [**LearnCpp**](https://www.learncpp.com/): An online resource offering free tutorials on various
  aspects of C++ programming, from basics to advanced topics.

[//]: # (@formatter:off)
[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments
[Effective Modern C++]: https://www.oreilly.com/library/view/effective-modern-c/9781491908419/
[//]: # (@formatter:on)