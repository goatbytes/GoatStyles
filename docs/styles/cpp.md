# C++ Style Guide

## Introduction

This document outlines the C++ style guide for all development projects within GoatBytes.IO. Adherence to this guide promotes consistent, maintainable, and high-quality C++ code across our teams.

The guide details best practices for formatting, naming conventions, comments and documentation, programming practices, language-specific idioms and patterns, and tools and IDE setup. Following these guidelines ensures code readability, efficiency, and reduces the potential for errors.

This style guide is intended for all developers working on C++ projects within the company, regardless of their prior C++ experience. We encourage developers to familiarize themselves with the contents of this document and integrate these practices into their development workflow.

## General Principles

This section outlines the overarching principles that guide our C++ coding practices within the company. Adhering to these principles promotes well-structured, maintainable, and efficient C++ code:

- **Readability and Maintainability:** Strive for clarity and conciseness in your code. Utilize meaningful variable and function names, proper indentation, and clear comments to enhance understanding for both yourself and others.

- **Modularity:** Organize your code effectively using well-defined classes, functions, and modules. This promotes reusability and simplifies maintenance by compartmentalizing functionalities.

- **Error Handling:** Anticipate potential errors and exceptions that might occur during program execution. Implement robust error handling mechanisms like `try-catch` blocks or error codes to gracefully handle errors and prevent unexpected program crashes.

- **Resource Management:** Manage resources like files, network connections, and memory efficiently. Open and close resources properly within their scope to avoid resource leaks and potential program crashes. Consider using RAII (Resource Acquisition Is Initialization) principles for streamlined resource management.

- **Testing:** Write unit tests to verify the functionality of individual classes and functions. This helps ensure your code behaves as expected and catches potential bugs early in the development process. Consider adopting a C++ testing framework like Google Test (gtest) or Catch2 to facilitate efficient testing.

Following these general principles establishes a solid foundation for crafting high-quality C++ code within your development projects.

## Formatting

Formatting plays a crucial role in code readability and maintainability. Consistent formatting makes your C++ code easier to understand for yourself and others, improving collaboration and reducing errors.

### Indentation

- Use four-space indentation consistently throughout your code. This standard indentation level improves readability and visually represents code blocks.

**Example:**

```cpp
class Goat {
public:
  Goat(const std::string& name, int age);
  void eat(const Food& food);
  std::string get_name() const;
  int get_age() const;

private:
  std::string name_;
  int age_;
};
```

### Line Length

- Maintain a reasonable line length, ideally around 80 characters with a maximum line-length of 100 characters. This helps prevent horizontal scrolling and improves code readability on most screen sizes.

**Example:**

```cpp
// **Bad (exceeds line length):**
std::string veryLongVariableNameThatWouldDefinitelyCauseHorizontalScrolling
    = getIncrediblyLongGoatNameFromExternalLibrary(someVeryLongInputString);

// **Good (wrapped to multiple lines):**
std::string very_long_variable_name_that_would_definitely_cause_horizontal_scrolling =
    getIncrediblyLongGoatNameFromExternalLibrary(someVeryLongInputString);
```

### Spacing

- Use spaces around operators (except for `->` and `::`), after commas, and before parentheses to enhance readability.

**Example:**

```cpp
Goat billy("Billy", 2);
int happiness = billy.get_happiness();
if (happiness < 50) {
  std::cout << "Billy the goat is looking a bit hangry!" << std::endl;
}
```

### Blank Lines

- Strategically use blank lines to separate logical code blocks, function definitions, and class definitions. This improves code organization and visual clarity.

**Example:**

```cpp
void Goat::eat(const Food& food) {
  happiness_ += food.get_nutrition();
  // ... (other logic related to eating)
}

std::string Goat::get_name() const {
  return name_;
}
```

## Naming Conventions

### Variable and Function Naming

- Use lowercase letters with underscores (`_`) to separate words in variable and function names (snake_case).

**Example:**

```cpp
void Goat::eat(const Food& food) {
  happiness_ += food.get_nutrition();
  // ... (other logic related to eating)
}

std::string Goat::get_name() const {
  return name_;
}
```

- Consider using prefixes or suffixes to indicate specific data types or purposes (e.g., `is_happy`, `num_goats`).

**Example:**

```cpp
bool is_goat_healthy(const Goat& goat); int get_num_goats_in_herd();
```

### Class and Struct Naming

- Use PascalCase (uppercase first letter for each word) for class and struct names.

**Example:**

```cpp
class GoatManager; struct FoodType;
```

### Constants

- Use uppercase letters with underscores to separate words in constant names.

**Example:**

```cpp
static const int MAX_HERD_SIZE = 100; static const double HAY_NUTRITION_VALUE = 50.0;
```

### Hungarian Notation (Optional)

- Hungarian Notation (using prefixes to indicate variable type) is an optional approach. While not widely used in modern C++, it can be helpful in some specific contexts.

**Example:**

```cpp
int iAge; // Integer variable for age std::string strName; // String variable for name
```

### Naming Consistency

- Maintain consistency in your naming conventions throughout your codebase. This promotes a clean and unified style, making the code easier to understand and navigate.

## Comments and Documentation

### Comprehensive Documentation

- **Header Files:** Include header files (`.h` files) for all public classes, functions, and structs. These headers should provide a high-level overview of the functionality offered and any collaborators (other header files) required.

**Example:**

```cpp
void Goat::eat(const Food& food) {
  happiness_ += food.get_nutrition();
  // ... (other logic related to eating)
}

std::string Goat::get_name() const {
  return name_;
}
```

- **Class Documentation:** Provide detailed comments within class definitions using Doxygen comments or a similar format. This documentation should cover:

    - A clear and concise class description explaining its purpose and role in the program.

    - Member variable documentation, including data type, purpose, and usage guidelines (e.g., access restrictions, thread safety).

    - Member function documentation, including purpose, parameters, return value, side effects, and any exceptions that might be thrown.

**Example:**

```cpp
/**
 * @class Goat
 * @brief Represents a single goat within the herd management system.

 * This class encapsulates information and behavior related to a goat in the herd.
 * It provides methods for interacting with the goat, such as feeding and retrieving
 * information about its state.
 */
class Goat {
public:
  /**
   * Constructor for the Goat class.
   *
   * @param name The name of the goat.
   * @param age The age of the goat in years.
   */
  Goat(const std::string& name, int age);

  // ... (other member function declarations with Doxygen comments)

private:
  // ... (member variable declarations with comments)
};
```

- **Function Documentation:** For all public functions, provide clear Doxygen comments or equivalent documentation that includes:

    - A concise description of the function's purpose.

    - A list of parameters with data types and descriptions of their purpose and expected usage.

    - The return value type and its meaning.

    - Any side effects the function might have on program state (e.g., modifying global variables).

    - A description of potential exceptions that might be thrown and how they should be handled.

**Example:**

```
/**
 * Feeds a goat with a specific food type, updating its happiness level.
 *
 * This function attempts to feed the specified goat with the provided food. If the
 * goat eats the food, its happiness level will be increased.
 *
 * @param goat The goat to be fed.
 * @param food The type of food to feed the goat.
 *
 * @return true if the goat eats the food successfully, false otherwise (e.g., goat
 * is not hungry or dislikes the food).
 *
 * @throws std::runtime_error - If the goat object is invalid or in an unexpected state.
 */
bool feed_goat(Goat& goat, const Food& food);
```

### Code Comments

In addition to comprehensive class and function documentation, utilize code comments strategically to explain non-obvious logic, complex algorithms, or design choices within your code:

- Use clear and concise comments to improve code readability, especially for sections that might be less intuitive.

- Avoid excessive commenting on trivial code that can be easily understood by reading the code itself.

- Maintain consistent formatting for code comments to enhance readability.

## Programming Practices

### Readability and Maintainability

- **Focus on code clarity:** Strive to write code that is easy to understand for both yourself and others. Use meaningful variable and function names, proper indentation, and clear comments as discussed in previous sections.

- **Organize code effectively:** Structure your code using well-defined classes, functions, and modules. This promotes modularity and reusability, making the code easier to maintain and modify.

### Memory Management

- **Understand ownership semantics:** In C++, you are responsible for managing the lifetime of memory objects. Utilize techniques like RAII (Resource Acquisition Is Initialization) and smart pointers (e.g., `std::unique_ptr`, `std::shared_ptr`) to ensure proper memory allocation and deallocation, preventing memory leaks and dangling pointers.

**Example** (using `std::unique_ptr`):

```cpp
std::unique_ptr<Goat> billyGoat = std::make_unique<Goat>("Billy", 2);
// ... (interact with billyGoat)
// billyGoat will be automatically deallocated when it goes out of scope
```

### Error Handling

- **Implement robust error handling:** Anticipate potential errors and exceptions that might occur during program execution. Utilize techniques like `try-catch` blocks or error codes to handle these errors gracefully, preventing unexpected program crashes and ensuring data integrity.

**Example (Handling Missing Food Type):**

```cpp
FoodType get_favorite_food(const std::string& goat_name) {
  // ... (logic to find favorite food)
  if (favorite_food.empty()) {
    throw std::runtime_error("Favorite food unknown for goat: " + goat_name);
  }
  return favorite_food;
}
```

### Resource Management

- **Manage resources efficiently:** This includes managing files, network connections, and other system resources. Open and close resources properly within their scope to avoid resource leaks and potential program crashes. Consider using RAII principles for resource management as well.

**Example:**

```cpp
std::ifstream goat_data_file("goats.dat");
if (goat_data_file.is_open()) {
  // ... (read goat data from the file)
} else {
  std::cerr << "Error opening goat data file!" << std::endl;
}
// goat_data_file will be automatically closed when it goes out of scope
```

### Testing

- **Write unit tests:** Create unit tests to verify the functionality of individual classes and functions. This helps ensure your code behaves as expected and catches potential bugs early in the development process. Consider using a C++ testing framework like Google Test (gtest) or Catch2 to streamline the testing process.

**Example:**

```cpp
TEST(GoatTest, GetHappiness) {
  Goat billy("Billy", 2);
  billy.eat(FoodType::Hay);
  EXPECT_GT(billy.get_happiness(), 50);  // Assert happiness is greater than 50
}
```

## Language-Specific Idioms and Patterns

### Smart Pointers and Memory Management

- Go beyond basic memory management practices and embrace smart pointers like `std::unique_ptr`, `std::shared_ptr`, and `std::weak_ptr`. These tools help automate memory deallocation and prevent memory leaks, especially when managing complex ownership scenarios within your goat herd (e.g., a Herd class containing multiple Goat objects).

**Example:**

```cpp
std::shared_ptr<Goat> billyGoat = std::make_shared<Goat>("Billy", 2);
std::shared_ptr<Goat> buttercupGoat = std::make_shared<Goat>("Buttercup", 1);

std::shared_ptr<Herd> myHerd = std::make_shared<Herd>();
myHerd->add_goat(billyGoat);
myHerd->add_goat(buttercupGoat);

// Both billyGoat and buttercupGoat will be automatically deallocated
// when the last shared_ptr pointing to them goes out of scope.
```

- Consider using RAII (Resource Acquisition Is Initialization) principles with smart pointers for even more robust memory management.

### Iterators and Algorithms

- Utilize C++'s powerful iterators and algorithms from the `<algorithm>` header to manipulate collections and data structures efficiently. Algorithms like `std::find`, `std::sort`, and `std::for_each` can simplify tasks like finding a specific goat in the herd or iterating over all goats to feed them.

**Example:**

```cpp
auto happiestGoat = std::max_element(herd.goats_.begin(), herd.goats_.end(),
                                     [](const std::shared_ptr<Goat>& a, const std::shared_ptr<Goat>& b) {
                                       return a->get_happiness() < b->get_happiness();
                                     });

if (happiestGoat != herd.goats_.end()) {
  std::cout << (*happiestGoat)->get_name() << " is the happiest goat in the herd!" << std::endl;
}
```

### Templates and Generic Programming

- Leverage C++ templates to create generic functions and classes that can work with various data types.

**Example:**

```cpp
template <typename FoodType>
void feed(Goat& goat, const FoodType& food) {
  goat.eat(food);
}
```

### Exceptions and Error Handling

- Utilize C++ exceptions for robust error handling. Throw exceptions to indicate exceptional circumstances and allow for handling them at appropriate points in your program. Ensure proper exception handling to prevent program crashes and maintain data integrity.

**Example:**

```cpp
void feed_goat(Goat& goat, const FoodType& food) {
  if (!goat.likes(food)) {
    throw std::runtime_error("Goat " + goat.get_name() + " dislikes this food!");
  }
  goat.eat(food);
}
```

## Tools and IDE Setup

### Essential Tools

- **Compiler:** A C++ compiler is needed to translate your C++ code into machine code executable by your computer. Here are two popular options:

    - **[GNU Compiler Collection (GCC)](https://gcc.org/):** A free, open-source compiler suite widely used for C and C++ development.

    - **[Clang](https://clang.llvm.org/get_started.html):** Another open-source compiler known for its speed, performance, and integration with various development tools.

- **Build Tool:** A build tool automates the compilation process, managing dependencies and simplifying project building. Consider these options:

    - **[CMake](https://cmake.org/):** A cross-platform build system used for various programming languages, including C++.

    - **Make:** A traditional build tool often used in conjunction with GCC.

### IDE Selection

Choosing an IDE depends on your personal preferences and workflow style. Here are some popular options with C++ support:

- **[Visual Studio (VS)](https://visualstudio.microsoft.com/):** A powerful, commercially-licensed IDE from Microsoft with comprehensive features for C++ development, including debugging, code completion, and project management.

- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/):** A free, open-source code editor from Microsoft that can be extended with plugins to provide C++ development capabilities. It's known for its customizability and lightweight nature.

- **[CLion](https://www.jetbrains.com/clion/):** A cross-platform IDE from JetBrains specifically designed for C and C++ development. It offers advanced features like code analysis, refactoring, and integration with debuggers and version control systems.

- **[Eclipse](https://eclipseide.org/) (with CDT Plugin):** A free, open-source IDE with a plugin (CDT - C/C++ Development Toolkit) enabling C++ development functionalities.

### Additional Tools

- **Debugger:** A debugger is a valuable tool for identifying and resolving issues within your code. Debuggers allow you to step through code execution line by line, inspect variables, and set breakpoints. GDB (GNU Debugger) is a popular option for command-line debugging, while IDEs often have integrated debuggers.
