# C++ Style Guide

This guide specifically addresses C++ development, focusing on idiomatic practices, patterns, and
C++-specific considerations.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for the purpose, scope, and general principles of our coding standards.
    type: abstract
///
[//]: # (@formatter:on)

## Formatting

While our C++ formatting guidelines follows the [Foundational Code Standards][fnd-formatting] for
formatting, summarized below:

- **Indentation:** Use 4 spaces for indentation.
- **Continuation indent:** Use 8 spaces for line continuations.

Otherwise, adhere to the general formatting guidelines outlined in the foundational standards and
briefly summarized below.

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

/// details | Formatted C++ Example Code
    type: example
```cpp
#include <iostream>
#include <vector>

// Attributes used for demonstration
[[nodiscard]] class Example {
public:
    // Constructor with initializer list
    Example(int x, int y) : x_(x), y_(y) {}

    // Method declaration
    void doSomething();

private:
    int x_;
    int y_;

    // Inner class
    class Inner {
    public:
        void innerMethod() {
            std::cout << "Inside innerMethod" << std::endl;
        }
    };

    // Example of a static method
    static void staticMethod() {
        if (true) {
          std::cout << "Static method called" << std::endl;
        }
    }
};

void Example::doSomething() {
    Inner inner;
    inner.innerMethod();

    int sum = x_ + y_; // Demonstrating space around operator
    std::cout << "Sum: " << sum << std::endl;

    // For loop demonstrating continuation indent and spaces
    for (int i = 0; i < 10; i += 2) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // If-else structure
    if (sum > 10) {
        std::cout << "Sum is greater than 10" << std::endl;
    } else {
        std::cout << "Sum is 10 or less" << std::endl;
    }

    // Try-catch block
    try {
        throw std::runtime_error("Example exception");
    } catch (const std::runtime_error& e) {
        std::cout << "Caught an exception: " << e.what() << std::endl;
    }
}

int main() {
    Example example(5, 8);
    example.doSomething();
    Example::staticMethod();

    return 0;
}
```

///

[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for Kotlin adhere to our [Foundational Code Standards][fnd-naming]
with no exceptions.

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with "is" or "has" for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

[//]: # (TODO: Add good/bad examples for naming conventions)

## Documentation and Comments

Refer to the [Foundational Code Standards][fnd-docs] for general commenting and documentation
guidelines.

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
 * std::cout << (billy.isHappy(3) ? "True" : "False") << std::endl; // Outputs "True" or "False" based on the number of meals.
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

int main() {
    Goat billy("Billy", 5);
    std::cout << "Billy is " << (billy.isHappy(3) ? "happy" : "not happy") << std::endl;

    return 0;
}
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
- [**Effective Modern C++
  **](https://www.oreilly.com/library/view/effective-modern-c/9781491908419/): A book by Scott
  Meyers that covers the effective use of the C++11 and C++14 standards.
- [**The C++ Programming Language**](http://www.stroustrup.com/4th.html): Written by Bjarne
  Stroustrup, the creator of C++, this book provides comprehensive coverage of the C++ language,
  including its standard library and key design techniques.
- [**LearnCpp**](https://www.learncpp.com/): An online resource offering free tutorials on various
  aspects of C++ programming, from basics to advanced topics.

[//]: # (@formatter:off)
[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[//]: # (@formatter:on)