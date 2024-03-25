# Swift Style Guide
## Introduction

Welcome to the Swift Style Guide. This document is crafted to guide developers navigating through Swift projects, ensuring the code remains clean, maintainable, efficient, and consistent across various development scenarios. Designed to support both new initiatives and ongoing projects, this guide aims to ensure high-quality contributions that are easy to integrate and understand, fostering seamless collaboration and elevating project standards.

Swift, developed by Apple Inc. for iOS, macOS, watchOS, tvOS, and beyond, is a powerful and intuitive programming language that enables developers to create next-generation applications with ease. As Swift continues to evolve, so too does the need for a comprehensive style guide that reflects current best practices and promotes code excellence.

### Purpose

The primary aim of this style guide is to enhance collaboration and elevate code quality by establishing a consistent set of standards for formatting, naming conventions, documentation, and programming practices specific to Swift development. By aligning on these conventions, we aim to streamline the code review process, facilitate seamless teamwork across projects, and ultimately raise the bar for code quality in our Swift projects.

### Scope

This guide is intended for developers working on a wide range of Swift projects, from mobile and desktop applications to cloud services and beyond. The recommendations provided are designed to be broadly applicable, ensuring relevance and utility in diverse Swift development contexts, including but not limited to applications for Apple platforms.

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

Ensuring proper formatting is fundamental in Swift development to maintain readability, guarantee consistency throughout the codebase, and adhere to both community and language-specific standards. The guidelines outlined in this section specify the formatting principles and rules tailored for Swift code.

### Column Limit

A maximum column limit of 100 characters is established for Swift code. Any line exceeding this limit must undergo line-wrapping in accordance with the detailed instructions provided in the Line-Wrapping section.

**Exceptions**:

*   Lines where adherence to the column limit results in the disruption of a meaningful unit of text (such as a lengthy URL within a comment).
*   `import` statements.
*   Code produced by another tool.

### Braces

The arrangement of braces in Swift code adopts a conventional style aimed at maximizing readability and consistency, especially for non-empty blocks. Specific adjustments tailored to Swift's syntax and usage patterns are as follows:

*   The opening brace (`{`) is placed on the same line as its preceding code statement without a line break, except in cases where line-wrapping is necessitated.
*   A line break is inserted immediately after the opening brace (`{`), with the exception of closures. In closures, if the signature fits within the line limit, it remains on the same line as the opening brace, followed by a line break after the `in` keyword.
*   For empty blocks, a concise `{}` representation is permissible.
*   Line breaks are positioned both before and after the closing brace (`}`), except in scenarios where it concludes an empty block or is directly followed by another control flow keyword (such as `else`).

```swift
// Correct usage of braces in a Swift function
func fetchGoatDetails() {
  guard let goatURL = URL(string: "https://goatbytes.io/goats") else {
    return
  }

  URLSession.shared.dataTask(with: goatURL) { data, response, error in
    guard let data = data, error == nil else {
      print("Error fetching goat details")
      return
    }
    // Process the data
    print("Fetched Goat Data: \(data)")
  }.resume()
}
```

This approach ensures a structured and visually clear delineation of code blocks, enhancing both readability and maintainability within the Swift codebase.

### Semicolons

In Swift, semicolons (`;`) are not utilized to terminate or segregate statements, with the exception being within string literals or comments.

### One Statement Per Line

Each line is limited to a single statement, succeeded by a line break, except when the line concludes with a block containing zero or one statements.

```swift
// Correct usage of one statement per line
let goatName = "Billy"
let goatAge = 3
let isGoatFriendly = true
print(goatName)
print("Age: \(goatAge), Friendly: \(isGoatFriendly)")
```

### Line-Wrapping

Line-wrapping is applied to split code across multiple lines that would otherwise fit on a single line. Adhere to the following principles when wrapping lines:

*   Prefer a single line if the entire declaration, statement, or expression can be accommodated.

*   For comma-delimited lists, choose either a horizontal or vertical layout without mixing the two. Vertically-oriented lists should include a line break before the first element and subsequent to each element, including the final one.

### Function Declarations

Function declarations requiring line-wrapping should indent subsequent lines by two spaces, aligning with the parameter wrapping rules set forth in the line-wrapping guidelines.

```swift
// Example of a Swift function declaration with line-wrapping
func enrollGoatInSurfingClass(goatName: String, skillLevel: Int, completion: (Bool) -> Void) {
  // Assume this function enrolls a goat in a surfing class based on its skill level
  completion(true)
}
```

### Control Flow Statements

Control flow statements (`if`, `guard`, `while`, `switch`) adhere to the indentation rules of their respective blocks and include a line break before the opening brace (`{`) unless the entire statement fits on one line.

```swift
// Using control flow statements with correct formatting
func checkGoatEligibility(goatAge: Int) {
  if goatAge > 1 {
    print("Goat is eligible for advanced classes.")
  } else {
    print("Goat is too young for advanced classes.")
  }
}
```

### Horizontal and Vertical Whitespace

*   **Horizontal Whitespace**: Used judiciously, only enhancing readability where necessary.

*   **Vertical Whitespace**: Employs a single blank line to segregate logical sections of code and between type members.

## Naming

Proper naming is vital in Swift development for clarity, readability, and maintainability. This section outlines naming conventions and principles that promote clear, fluent, and precise usage.

### Promote Clear Usage

*   **Clarity at the Point of Use**: Names should be unambiguous and descriptive, conveying essential information without redundancy. Avoid using terms that do not contribute meaningful information.

*   **Role over Type**: Prefer naming variables, parameters, and associated types according to their roles rather than their type constraints. Enhance names with relevant type information only when necessary to clarify a parameter's role.

### Strive for Fluent Usage

*   **Grammatical Phrases**: Method and function names should enable use sites to form grammatical English phrases.

*   **Factory Methods**: Begin factory method names with “make” (e.g., `x.makeIterator()`).

*   **Initializers**: Avoid forming a phrase starting with the base name for the first argument to initializers and factory methods (e.g., avoid `x.makeWidget(cogCount: 47)`).

### Naming Based on Side-Effects

*   **Noun Phrases for Non-Mutating**: Functions and methods without side-effects should be named as noun phrases (e.g., `x.distance(to: y)`).

*   **Verb Phrases for Mutating**: Those with side-effects should use imperative verb phrases (e.g., `x.sort()`).

*   **Consistent Mutating/Nonmutating Pairs**: Name mutating/nonmutating method pairs consistently. Use imperative for mutating methods and “ed” or “ing” suffix for nonmutating counterparts.

    *   **Mutating**: `x.sort()`

    *   **Nonmutating**: `z = x.sorted()`

### Boolean Methods and Properties

*   Boolean methods and properties should read as assertions about the receiver (e.g., `x.isEmpty`).

### Protocol Naming

*   **Descriptive Nouns**: Protocols that describe what something is should be named as nouns (e.g., `Collection`).

*   **Capabilities**: Protocols that describe capabilities should end in `-able`, `-ible`, or `-ing` (e.g., `Equatable`, `ProgressReporting`).

### Initializers

*   **Property Correspondence**: Initializer arguments that directly correspond to stored properties should share the same name, using `self.` to disambiguate.

### Global Constants

*   **Lower Camel Case**: Global constants are named using `lowerCamelCase`, emphasizing their immutable nature and role within your code.

```swift
// Definition of global constants in lowerCamelCase
let maximumGoatLoad = 120 // The maximum load (in kg) a goat can carry
let goatFarmLocation = "North Field" // The primary location of the goat farm
```

### Use Terminology Well

*   **Accuracy**: Use terms of art accurately to avoid misleading or confusing the reader. Avoid obscure terms if a more common word conveys the same meaning.

*   **Avoid Abbreviations**: Abbreviations can obscure meaning and should be avoided unless their meaning is clear and widely understood.

*   **Embrace Precedent**: Adhere to established terminology within the programming domain, prioritizing terms that are familiar to most programmers over simplifications that may be more accessible to beginners.

## Documentation

Documentation plays a crucial role in Swift development, serving as a guide for future developers, including the future you, and facilitating understanding and maintenance of the codebase. This section outlines the conventions and best practices for writing documentation comments in Swift.

### General Format

Documentation comments in Swift are written using triple slashes (`///`). Block comments (`/** ... */`), common in other languages for documentation purposes, are not used in Swift.

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

Documentation comments should start with a brief single-sentence summary that concisely describes the purpose of the function, method, or property. This summary may span multiple lines if necessary but should be kept as succinct as possible.

If further detail is required, additional paragraphs, each separated by a blank line, can follow the summary. The summary itself should avoid starting with redundant phrases such as "This method..." as the context is implied.

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

Document the parameters, return value, and errors a function or method may throw using the `Parameter(s)`, `Returns`, and `Throws` tags, respectively. These tags should not be left with empty descriptions, and their content should end with a period, even if they form a phrase rather than a complete sentence.

When a description does not fit on a single line, continuation lines should be indented by two spaces.

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

Using Apple’s markup format in documentation comments is encouraged to add rich formatting. This markup differentiates symbolic references from descriptive text and supports rendering by Xcode and documentation generation tools.

*   Use `backticks` for inline code and symbol names.

*   Use triple backticks (\`\`\`) to denote multi-line code blocks.

*   Emphasize text with _asterisks_ or _underscores_.

### Where to Document

At a minimum, provide documentation comments for every `open` or `public` declaration, and every `open` or `public` member of such declarations. Exceptions include:

*   Enum cases that are self-explanatory may not require documentation unless they have associated values that need clarification.

*   Overrides, protocol requirement implementations, or default protocol requirement implementations may omit documentation if the super declaration is adequately documented, except to describe new behavior.

Keep documentation focused, relevant, and concise to ensure it remains useful and maintainable. Documentation comments are optional but recommended for test classes and methods, particularly for functional tests or shared helper methods.

## Programming Practices

Adhering to sound programming practices in Swift not only enhances code quality but also promotes maintainability and readability. This section consolidates practices advocated by Google's Swift Style Guide, Swift API Design Guidelines, and other respected community resources.

### Embrace Swift's Type System

Swift's type system is designed to be both powerful and expressive. Leverage the type system for safer and more readable code.

*   **Prefer Strong Typing Over Casting**: Use specific types over general types (e.g., prefer `Int` over `Any`) to avoid unnecessary casting.

*   **Type Inference**: Utilize Swift's type inference capabilities to keep code clean and concise without sacrificing type safety.

### Error Handling

Swift introduces a robust error handling model. Use `throw` and `catch` to handle errors in a clear and predictable manner.

*   **Use** `throws` Judiciously: Only use `throws` in functions where error handling adds clear value.

*   **Prefer Enums for Error Types**: When defining your own errors, use enums that conform to the `Error` protocol to categorize error states.

### Optionals

Optionals are a powerful feature of Swift, allowing variables to have a 'no value' state.

*   **Use Optionals When Nil Is a Valid Value**: Only use optionals for variables that can legitimately have a `nil` value.

*   **Prefer** `if let` and `guard let` Over Forced Unwrapping: Use optional binding to safely unwrap optionals and avoid runtime crashes.

### Code Organization

Organize code logically and consistently to enhance readability and maintainability.

*   **Group Related Functionality**: Use extensions to organize your code into logical blocks. This practice is particularly useful for conforming to protocols.

*   **Minimize Global Functions**: Encapsulate functions within types when they're highly related to a specific operation or functionality.

### Use of Self

The explicit use of `self` is unnecessary in most cases in Swift, except where required by the compiler or for clarity in closures.

*   **Implicit Self**: Prefer omitting `self` when accessing properties or methods to reduce verbosity.

### Closures

Closures are first-class citizens in Swift and should be used effectively to write concise and readable code.

*   **Trailing Closure Syntax**: Use trailing closure syntax for the last closure parameter to make the code cleaner.

*   **Closure Parameter Names**: Omit the parameter names in short, non-nested closures for conciseness.

### Protocol Conformance

Conform to protocols to leverage Swift's powerful protocol-oriented programming paradigm.

*   **Separate Protocol Conformance**: Use extensions to clearly separate protocol conformance in your class or struct implementations.

*   **Prefer Composition Over Inheritance**: Use protocols for shared functionality across types rather than class inheritance.

### Constants and Variables

Use `let` to declare constants and `var` for variables. Prefer immutability wherever possible to make your code safer and clearer.

### Naming Conventions

Follow Swift's naming conventions for a consistent and predictable codebase.

*   **CamelCase**: Use UpperCamelCase for types and protocols, lowerCamelCase for everything else.

*   **Descriptive Names**: Choose clear and descriptive names, even if they are longer. Aim for readability and clarity.

### 6.10 Comments

Comments should be used judiciously to explain why a piece of code does something. Avoid redundant comments that simply describe what the code does.

### 6.11 Avoiding Magic Numbers

Prefer named constants over in-line literals to make your code more readable and maintainable. Magic numbers in the code can lead to confusion and errors.

## Language-Specific Idioms and Patterns

### Leverage Value Types

Swift's preference for value types (structs and enums) over reference types (classes) for data encapsulation ensures immutability and thread safety.

*   **Use Structs for Data Models**: Prefer structs for simple data holding models, taking advantage of automatic memberwise initializers and value semantics.

### Protocol-Oriented Programming

Swift is renowned for its powerful protocol-oriented programming model.

*   **Favor Protocols Over Base Classes**: Design APIs around protocols and protocol extensions. This approach promotes loose coupling and enhances code reusability.

### Functional Programming Patterns

Swift's support for first-class functions and closures encourages the use of functional programming techniques.

*   **Embrace Higher-Order Functions**: Utilize functions like `map`, `filter`, `reduce` for concise operations on collections, promoting clearer and more expressive code.

### Use of Optionals

Optionals signify the absence of a value. Swift's approach to optionals helps prevent `nil` reference errors common in other languages.

*   **Optional Chaining**: Use optional chaining (`?.`) for concise, safe access to properties and methods of optional values.

*   **Optional Binding**: Prefer `if let` or `guard let` to unwrap optionals safely, ensuring variables are only used when they hold non-nil values.

### Avoid Force Unwrapping

Force unwrapping optionals (`!`) bypasses safety checks and can lead to runtime crashes.

*   **Safe Unwrapping**: Always unwrap optionals using safe methods (e.g., optional binding, nil coalescing `??`) unless you're absolutely certain the value isn't `nil`.

### Constants and Variables

Embrace immutability when possible. Use `let` to define constants and `var` only for values that need to change.

*   **Immutability by Default**: Declare variables as constants (`let`) by default and only change them to variables (`var`) if necessary.

### Error Handling

Swift's error handling model is robust and expressive, enabling you to handle recoverable errors elegantly.

*   **Throwing Functions**: Mark functions that can throw errors with `throws` and call them using `try`, `try?`, or `try!`.

*   **Define Custom Error Types**: Use enums conforming to the `Error` protocol to represent possible error conditions clearly.

### Naming Conventions

Follow Swift's naming conventions for clarity and consistency throughout your codebase.

*   **Descriptive Names**: Choose names that are clear and descriptive. Use names that can be pronounced and that are not ambiguous.

*   **Concise Names**: Be concise without sacrificing clarity. Avoid unnecessary words in names.

### Closures and Capture Lists

Closures can capture and store references to any constants and variables from the context in which they are defined.

*   **Capture Lists**: Use capture lists to break strong reference cycles when capturing `self` or other objects in closures.

### 7.10 Use of `guard` Statements

Guard statements are a distinctive Swift feature, allowing for early exits and ensuring that variables have valid values before proceeding.

*   **Early Exit**: Use `guard` for conditions that must be met for the function to continue execution. This reduces nesting and enhances readability.

## Tools and IDE Setup

Setting up your development environment properly is crucial for productivity and ensuring that your Swift projects adhere to the style guide and best practices. This section provides guidance on configuring Xcode and other IDEs, like AppCode, for Swift development.

### Xcode Setup

Xcode is the primary IDE for Swift development, offering integrated support for Swift's features and conventions.

#### Formatting in Xcode

Xcode includes tools and features that help maintain consistent code formatting and style. To leverage these, consider the following setup:

*   **SwiftLint Integration**: SwiftLint is a widely used tool for enforcing Swift style and conventions. It can be integrated into your Xcode project to automatically highlight issues and enforce style rules.

    1.  Install SwiftLint via Homebrew with `brew install swiftlint`.

    2.  Navigate to your Xcode project's build phases and add a new "Run Script Phase".

    3.  Include the script: `swiftlint`.

*   **Editor Configuration**:

    1.  **Indentation**: Navigate to Xcode's Preferences (`Cmd + ,`), select Text Editing → Indentation. Here, you can set your preferred indentation width (e.g., 2 spaces) and whether to indent using spaces or tabs.

    2.  **Automatic Formatting**: Under the same section, enable `Automatically trim trailing whitespace` and `Including whitespace-only lines` to keep your code clean.

### AppCode Setup

AppCode, developed by JetBrains, is another IDE popular among iOS developers for its robust refactoring tools and support for various languages including Swift.

#### Formatting in AppCode

To ensure your code formatting aligns with your project's or team's guidelines in AppCode:

*   **Code Style Settings**: Accessible via Preferences (`Cmd + ,`) → Editor → Code Style → Swift. Here, you can customize your formatting preferences such as indentation, spaces, and wrapping options.

*   **SwiftLint Plugin**: AppCode supports SwiftLint integration directly through plugins.

    1.  Open Preferences (`Cmd + ,`) → Plugins.

    2.  Search for "SwiftLint" in the Marketplace and install the plugin.

    3.  Configure the SwiftLint plugin settings according to your project's requirements.

### Other Tools

*   **SwiftFormat**: Another tool for enforcing Swift style and conventions. SwiftFormat can be configured with a `.swiftformat` file in your project directory to define rules.

*   **Git Hooks**: Integrate SwiftLint or SwiftFormat with Git hooks to automatically format your code before committing. This helps ensure that all committed code conforms to your style guidelines.