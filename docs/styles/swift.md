# Swift Style Guide

This guide focuses on the best practices for writing Swift code, emphasizing readability,
maintainability, and adherence to modern Swift idioms.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for the overarching purpose, scope, and general principles that guide our coding standards.
    type: abstract
///
[//]: # (@formatter:on)

The formatting guidelines for Swift adhere to our [Foundational Code Standards][fnd-formatting].
Here is a brief overview:

- **Consistent Indentation:** Use 2 spaces for indentation, 4 spaces for continuation lines.
- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Whitespace:** Use spaces around operators, parentheses, braces, colons, commas, and keywords.
- **Brace Style:** Follow K&R style (opening brace on same line, closing brace on new line).
- **Blank Lines:** Use 1 line to separate code sections.
- **Alignment:** Align elements in documentation comments and parameter lists.

[//]: # (@formatter:off)
/// admonition |
    type: info
Remember, these are guidelines; adapt them for your project's needs while keeping readability in
focus.
///
[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for Swift adhere to our [Foundational Code Standards][fnd-naming]
with the following exceptions:

- **camelCase** for constants to follow Swift's convention.

Otherwise, follow the conventions outlined in the foundational standards, briefly summarized below:

- **PascalCase** for classes, structs, enums, and protocols.
- **camelCase** for functions, variables, constants, and enum cases.

### Protocol Naming

* **Descriptive Nouns**: Protocols that describe what something is should be named as nouns
  (e.g., `Collection`).
* **Capabilities**: Protocols that describe capabilities should end in `-able`, `-ible`, or `-ing`
  (e.g., `Equatable`, `ProgressReporting`).

### Initializers

* **Property Correspondence**: Initializer arguments that directly correspond to stored properties
  should share the same name, using `self.` to disambiguate.

## Commenting and Documentation

Documentation plays a crucial role in Swift development, serving as a guide for future developers,
including the future you, and facilitating understanding and maintenance of the codebase. This
section outlines the conventions and best practices for writing documentation comments in Swift.

### Documentation Format

Documentation comments in Swift are written using triple slashes (`///`). Block
comments (`/** ... */`), common in other languages for documentation purposes, are not used in
Swift.

```swift
/// Fetches the list of available goats from the server.
///
/// This function contacts the server and retrieves the current list of goats available for adoption.
/// It uses an asynchronous call and returns the data in a completion handler.
func fetchAvailableGoats(completion: @escaping ([Goat]) -> Void) {
  // Implementation
}
```

### Single-Sentence Summary

Documentation comments should start with a brief single-sentence summary that concisely describes
the purpose of the function, method, or property. This summary may span multiple lines if necessary
but should be kept as succinct as possible.

If further detail is required, additional paragraphs, each separated by a blank line, can follow the
summary. The summary itself should avoid starting with redundant phrases such as "This method..." as
the context is implied.

```swift
/// Returns the calculated age of a goat based on its birth date.
///
/// The age is calculated with respect to the current date. This method considers leap years.
/// The calculation does not include the time of day the goat was born, considering only the date.
///
/// - Parameter birthDate: The birth date of the goat.
/// - Returns: The age of the goat in years.
func calculateGoatAge(birthDate: Date) -> Int {
  // Implementation
}
```

### Parameter, Returns, and Throws Tags

Document the parameters, return value, and errors a function or method may throw using
the `Parameter(s)`, `Returns`, and `Throws` tags, respectively. These tags should not be left with
empty descriptions, and their content should end with a period, even if they form a phrase rather
than a complete sentence.

When a description does not fit on a single line, continuation lines should be indented by two
spaces.

```swift
/// Enrolls a goat in a specified class.
///
/// This method enrolls a goat in the class if it meets the prerequisites. It throws an error if
/// the goat is already enrolled in the maximum number of classes or if the class is full.
///
/// - Parameters:
///   - goat: The goat to enroll.
///   - className: The name of the class to enroll the goat in.
/// - Returns: A boolean indicating whether the enrollment was successful.
/// - Throws: `GoatEnrollmentError.classFull` if the class is full,
///           `GoatEnrollmentError.maxEnrollmentsReached` if the goat has reached the maximum number of enrollments.
func enrollGoat(goat: Goat, className: String) throws -> Bool {
  // Implementation
}
```

### Apple’s Markup Format

Using Apple’s markup format in documentation comments is encouraged to add rich formatting. This
markup differentiates symbolic references from descriptive text and supports rendering by Xcode and
documentation generation tools.

* Use `backticks` for inline code and symbol names.
* Use triple backticks (\`\`\`) to denote multi-line code blocks.
* Emphasize text with _asterisks_ or _underscores_.

### Where to Document

At a minimum, provide documentation comments for every `open` or `public` declaration, and
every `open` or `public` member of such declarations. Exceptions include:

* Enum cases that are self-explanatory may not require documentation unless they have associated
  values that need clarification.
* Overrides, protocol requirement implementations, or default protocol requirement implementations
  may omit documentation if the super declaration is adequately documented, except to describe new
  behavior.

Keep documentation focused, relevant, and concise to ensure it remains useful and maintainable.
Documentation comments are optional but recommended for test classes and methods, particularly for
functional tests or shared helper methods.

### Comments

Comments should be used judiciously to explain why a piece of code does something. Avoid redundant
comments that simply describe what the code does.

## Best Practices and Idioms

### Embrace Swift's Type System

Swift's type system is designed to be both powerful and expressive. Leverage the type system for
safer and more readable code.

* **Prefer Strong Typing Over Casting**: Use specific types over general types (e.g., prefer `Int`
  over `Any`) to avoid unnecessary casting.
* **Type Inference**: Utilize Swift's type inference capabilities to keep code clean and concise
  without sacrificing type safety.

### Error Handling

Swift introduces a robust error handling model. Use `throw` and `catch` to handle errors in a clear
and predictable manner.

* **Use** `throws` Judiciously: Only use `throws` in functions where error handling adds clear
  value.
* **Prefer Enums for Error Types**: When defining your own errors, use enums that conform to
  the `Error` protocol to categorize error states.

### Optionals

Optionals are a powerful feature of Swift, allowing variables to have a 'no value' state.

* **Use Optionals When Nil Is a Valid Value**: Only use optionals for variables that can
  legitimately have a `nil` value.
* **Prefer** `if let` and `guard let` Over Forced Unwrapping: Use optional binding to safely unwrap
  optionals and avoid runtime crashes.

### Code Organization

Organize code logically and consistently to enhance readability and maintainability.

* **Group Related Functionality**: Use extensions to organize your code into logical blocks. This
  practice is particularly useful for conforming to protocols.
* **Minimize Global Functions**: Encapsulate functions within types when they're highly related to a
  specific operation or functionality.

### Use of Self

The explicit use of `self` is unnecessary in most cases in Swift, except where required by the
compiler or for clarity in closures.

* **Implicit Self**: Prefer omitting `self` when accessing properties or methods to reduce
  verbosity.

### Closures

Closures are first-class citizens in Swift and should be used effectively to write concise and
readable code.

* **Trailing Closure Syntax**: Use trailing closure syntax for the last closure parameter to make
  the code cleaner.
* **Closure Parameter Names**: Omit the parameter names in short, non-nested closures for
  conciseness.

### Protocol Conformance

Conform to protocols to leverage Swift's powerful protocol-oriented programming paradigm.

* **Separate Protocol Conformance**: Use extensions to clearly separate protocol conformance in your
  class or struct implementations.
* **Prefer Composition Over Inheritance**: Use protocols for shared functionality across types
  rather than class inheritance.

### Constants and Variables

Use `let` to declare constants and `var` for variables. Prefer immutability wherever possible to
make your code safer and clearer.

### Avoiding Magic Numbers

Prefer named constants over in-line literals to make your code more readable and maintainable. Magic
numbers in the code can lead to confusion and errors.

### Leverage Value Types

Swift's preference for value types (structs and enums) over reference types (classes) for data
encapsulation ensures immutability and thread safety.

* **Use Structs for Data Models**: Prefer structs for simple data holding models, taking advantage
  of automatic memberwise initializers and value semantics.

### Protocol-Oriented Programming

Swift is renowned for its powerful protocol-oriented programming model.

* **Favor Protocols Over Base Classes**: Design APIs around protocols and protocol extensions. This
  approach promotes loose coupling and enhances code reusability.

### Functional Programming Patterns

Swift's support for first-class functions and closures encourages the use of functional programming
techniques.

* **Embrace Higher-Order Functions**: Utilize functions like `map`, `filter`, `reduce` for concise
  operations on collections, promoting clearer and more expressive code.

### Avoid Force Unwrapping

Force unwrapping optionals (`!`) bypasses safety checks and can lead to runtime crashes.

* **Safe Unwrapping**: Always unwrap optionals using safe methods (e.g., optional binding, nil
  coalescing `??`) unless you're absolutely certain the value isn't `nil`.

### Use of `guard` Statements

Guard statements are a distinctive Swift feature, allowing for early exits and ensuring that
variables have valid values before proceeding.

* **Early Exit**: Use `guard` for conditions that must be met for the function to continue
  execution. This reduces nesting and enhances readability.

## Tools and Resources

### Linting and Formatting Tools

- **SwiftLint:** A tool to enforce Swift style and conventions.
- **SwiftFormat:** An automatic code formatter for Swift.

### Static Analysis Tools

- **Swift Compiler Warnings:** Utilize the Swift compiler's built-in static analysis to catch common
  errors and code smells.
- **Xcode Analyze:** Use Xcode's Analyze feature to detect potential bugs and issues in your code.

### Additional Resources

- [Swift Programming Language Guide][Swift Programming Guide]: The official guide to Swift, offering
  a comprehensive overview of the language.
- [Swift API Design Guidelines][Swift API Design Guidelines]: Guidelines for designing Swift APIs
  that are expressive and easy to use.
- [Ray Wenderlich's Swift Style Guide][Ray Wenderlich Guide]: A community-driven style guide for
  Swift.

[//]: # (links @formatter:off)

[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[Swift Programming Guide]: https://docs.swift.org/swift-book/
[Swift API Design Guidelines]: https://swift.org/documentation/api-design-guidelines/
[Ray Wenderlich Guide]: https://www.raywenderlich.com/1997706-swift-style-guide-for-raywenderlich-com

[//]: # (links @formatter:on)
