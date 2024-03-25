# C# Style Guide

## Introduction

This document serves as a comprehensive style guide for writing clean, consistent, and maintainable C# code. It outlines best practices, procedures, and guidelines to promote code readability, maintainability, and adherence to established coding conventions. Following this style guide fosters a collaborative development environment where developers can write code that is easy to understand, modify, and extend.

This guide is structured to provide clear and actionable guidance for C# developers. Each section focuses on a specific aspect of code style, offering recommendations and examples. By following these guidelines, you can contribute to a high-quality C# codebase and enhance the overall maintainability and professionalism of your projects.

## General Principles

This section establishes the core principles that underpin magood C# code style. These principles serve as a foundation for writing clean, consistent, and maintainable code.

- **Readability:** Strive for code that is easy for humans to understand. Favor clear and concise naming conventions, well-structured code blocks, and meaningful comments to enhance code comprehension.

- **Consistency:** Maintain consistent formatting, naming conventions, and coding practices throughout the codebase. Consistency promotes code readability and reduces the mental overhead required for developers to navigate the codebase.

- **Efficiency:** Write efficient code that utilizes language features and algorithms effectively to optimize performance without compromising readability or maintainability.

- **Maintainability:** Write code that is easy to understand, modify, and extend. Effective commenting, proper organization, and adherence to best practices all contribute to maintainable code.

- **Modularity:** Structure code into well-defined modules (classes, functions) that promote reusability, encapsulation, and loose coupling between code components.

- **Testability:** Write code that is easily testable. Consider factors like unit testability and separation of concerns while designing and implementing code.

## Formatting

Proper formatting is essential for maintaining readability and consistency across the C# codebase. This section provides guidelines on indentation, line length, whitespace, and the use of blank lines, all aimed at enhancing the clarity and professionalism of the code.

### Indentation

- Use four spaces for indentation. Avoid using tabs as they can be interpreted differently on various systems.

- Indent the body of a code block (e.g., following an if statement, inside a loop, or within a method definition) one level (four spaces) from the opening statement.

- Maintain consistent indentation throughout the codebase for improved readability.

### Line Length

- Aim for a maximum line length of 100 characters. This improves readability, especially when viewing code on screens with limited width.

- Break longer lines by wrapping code within parentheses, brackets, or braces onto a new line, aligning it appropriately with the previous line.

- Use judgment and consider the context when dealing with long lines of code. Complex expressions might benefit from staying on one line for better comprehension, while long variable declarations might be better split for readability.

### Whitespace

- Include a space before opening parentheses `(`, except in method declarations or calls.

- Surround operators (e.g., `=`, `+`, `-`) with spaces, except for unary operators and the method reference double colon `::`.

- Include a space before the left brace `{` in class declarations, method declarations, and control flow statements (e.g., `if`, `for`, `while`).

- Include a space before keywords like `if`, `for`, `while`.

- Use spaces around the components `?` and `:` of the ternary operator.

- Include a space after commas in lists (e.g., method arguments, array initializers).

- Include a space after semicolons `;` in a `for` loop.

- Include a space after a type cast.

- Include a space before the colon in a `foreach` loop.

### Blank Lines

- Strategically placed blank lines can significantly enhance the readability of your code.

- Include one blank line between methods or fields within a class.

- Use one blank line to separate sections like the header and package statement, after package statements, before and after imports, around class/interface declarations, and around initializer blocks.

**Example:**

```csharp
public class GoatFeeder
{
    public void FeedGoats(List<Goat> goats)
    {
        for (Goat goat in goats)
        {
            goat.Feed(
                new GoatFood("Grass", 5),
                new GoatFood("Hay", 3));
        }
    }
}
```

## Naming Conventions

Consistent naming conventions enhance code readability and maintainability by making it easier for developers to understand the structure and purpose of the code at a glance. Here are the recommended naming conventions for C#, incorporating best practices from the provided resources:

### Classes and Interfaces

- Use PascalCase (uppercase first letter for each word) for class and interface names.

- Names should be nouns or noun phrases that reflect the class's or interface's purpose.

**Examples:**

```csharp
public class GoatFeeder { }

public interface IFeedable { }
```

### Methods

- Use PascalCase for method names.

- Names should be verbs or verb phrases that describe the action the method performs.

**Examples:**

```csharp
public void FeedGoats(List<Goat> goats) { }

public int CalculateGoatHappiness(Goat goat) { }
```

### Variables and Fields

- Use camelCase (lowercase first letter, with uppercase for subsequent words) for local variables, instance fields, and static fields.

- Names should be descriptive and clearly convey the variable's purpose or value.

**Examples:**

```csharp
private int goatCount;
private static readonly int MAX_GOATS_ALLOWED = 100;

public string goatName { get; set; }
```

### Constants

- Use all uppercase letters with underscores separating words for constant names.

**Examples:**

```csharp
public const double PI = 3.14159;

public enum GoatMood { HAPPY, SAD, HUNGRY }
```

### Namespaces

- Use all lowercase letters with periods separating words (similar to domain names) for namespace names.

**Examples:**

```csharp
using System.Collections.Generic;

namespace com.goatfarm.feeding
{
}
```

### Enums

- Use PascalCase for enum types, aligning with class and interface naming conventions.

- Use all uppercase letters with underscores separating words for enum constants.

**Example:**

```csharp
public enum GoatMood { HAPPY, SAD, HUNGRY }
```

**Additional Considerations:**

- Avoid abbreviations or acronyms unless they are widely understood (e.g., `XML`, `HTTP`).

- Favor clarity over brevity when choosing names.

- Use prefixes or suffixes consistently for specific types of classes or interfaces (e.g., `I` prefix for interfaces, `Manager` suffix for manager classes).

## Commenting and Documentation

Effective commenting and comprehensive documentation are crucial for maintaining code quality, facilitating future modifications, and ensuring codebase accessibility for new and existing developers. Here's a breakdown of best practices for C# comments and documentation, drawing insights from the provided resources:

### Code Comments

- **Clarity and Purpose:** Comments should explain the "why" behind the code, not just the "what" it does. Avoid redundant comments that simply repeat the code itself.

- **Maintainability:** As code evolves, keep comments up-to-date to reflect the current functionality. Outdated comments can be more misleading than no comments at all.

**Example:**

```csharp
// Adjusts goat happiness level based on feeding time; longer feeding times make happier goats.
goat.AdjustHappiness(feedingTimeMinutes * HAPPINESS_FACTOR);

// This method validates user input to prevent feeding goats harmful substances.
public bool ValidateFoodType(string foodType) {
    // ... validation logic ...
}
```

### Documentation Comments

- **Document Classes and Interfaces:** Provide a summary at the beginning of each class and interface, describing its purpose and role within the application.

- **Document Methods:** Document every method, including a description of its behavior, parameters, return values, and any exceptions thrown.

- **Use Standard Tags:** Utilize XMLDoc standard tags (`<summary>`, `<param>`, `<returns>`, `<exception>`) to clearly describe method signatures. Additionally, use inline tags like `<code>` for code references and `<see cref="..."/>` for linking to related classes or methods within the documentation.

**Example:**

```csharp
/// <summary>
/// Represents a goat in the farm simulation.
/// <para>
/// This class provides methods to manage the goat's state, including its hunger and happiness levels.
/// </para>
/// </summary>
public class Goat
{

    /// <summary>
    /// Feeds the goat, adjusting its hunger level.
    /// </summary>
    /// <param name="foodType">The type of food being fed to the goat.</param>
    /// <param name="quantity">The amount of food in kilograms.</param>
    /// <returns>The goat's happiness level after feeding.</returns>
    /// <exception cref="OverfeedingException">Thrown if the quantity of food exceeds the goat's dietary restrictions.</exception>
    public int Feed(string foodType, double quantity) throws OverfeedingException {
        // ... method implementation ...
    }
}
```

### Inline Comments

- **Use Sparingly:** Reserve inline comments for complex code segments where the logic's purpose or action isn't immediately clear from the code itself.

- **Placement:** Position inline comments on the line above the code segment they describe, not at the end of the line of code.

**Example:**

```csharp
// Calculate the optimal feeding time based on the goat's current activity level
int feedingTime = CalculateFeedingTime(goat.ActivityLevel);
```

### Public API Documentation

- **Comprehensive Coverage:** Document every public class, method, and member variable comprehensively. Provide clear insights into the component's purpose, use, and behavior. Strive for detailed and accurate documentation, especially for critical software components. Consider security, reliability, and transparency principles in your documentation practices.

### TODOs and FIXMEs

- **Issue Tracking Preferred:** While TODO: and FIXME: comments can highlight areas needing attention, utilizing a ticket-based tracking system (e.g., Jira, Azure Boards) is generally preferred for managing tasks and issues. This approach facilitates better prioritization, tracking, and resolution of tasks.

- **Include Ticket Numbers:** If using TODO: or FIXME: comments, always include the corresponding ticket number from your project's tracking system. This practice links code comments directly to detailed descriptions, discussions, and updates on the issue or task, ensuring actionable and trackable comments.

**Example:**

```csharp
// TODO: [TICKET-1234] Implement happiness adjustment based on weather conditions
// FIXME: [TICKET-5678] Investigate edge cases where feeding time exceeds 24 hours
```

## Programming Practices

This section outlines best practices for writing clean, efficient, and maintainable C# code.

### Error Handling

- **Embrace Exception Handling:** Utilize exceptions to manage errors and unexpected situations gracefully. Aim for specific exception types to provide meaningful error messages for improved troubleshooting and debugging.

- **Catch and Handle Exceptions:** Don't ignore exceptions within a `try...catch` block. Handle the exception appropriately, either by logging the error, providing informative feedback to the user, or recovering from the error if possible. Avoid using a catch-all (`catch (Exception ex)`) unless necessary for critical error handling to prevent the application from crashing unexpectedly.

- **Favor Specific Over General Exceptions:** Catching specific exception types allows for more targeted handling of different error scenarios. General exceptions like `System.Exception` should be used cautiously.

### Control Flow Statements

- **Use Clear and Concise Conditions:** Strive for well-defined conditions in `if`, `else if`, and `while` statements. Complex conditions can be broken down into smaller, more readable expressions.

- **Favor** `switch` Statements for Multi-Way Branching: When dealing with multiple branching scenarios based on a single value, consider using a `switch` statement for improved readability compared to a series of nested `if` statements.

- **Limit Nesting Depth:** Deeply nested control flow statements can make code hard to understand. Extract complex logic into separate methods or utilize techniques like the 'guard clause' pattern to simplify nested conditions.

### Class Organization

- **Single Responsibility Principle:** Each class should have a single, well-defined responsibility. This promotes modularity, reusability, and easier testing.

- **Proper Encapsulation:** Utilize public properties and methods to control access to a class's internal state, while encapsulating implementation details within private methods and fields. This fosters data protection and promotes loose coupling between classes.

- **Favor Composition Over Inheritance:** When possible, favor composition (has-a relationship) over inheritance (is-a relationship) for code reusability. Composition allows for more flexible object creation and avoids the complexities of deeply nested inheritance hierarchies.

### Modifiers

- Use `public` Sparingly: Reserve the `public` access modifier for members (methods, fields) that need to be accessed from other classes. Consider using `private` or `protected` for members that should only be used within the class or its derived classes, respectively.

- Use `readonly` for Immutable Data: Declare variables and properties as `readonly` whenever possible to indicate that their value cannot be changed after initialization. This enhances thread safety and code clarity.

- Use `static` for Class-Level Members: Utilize the `static` modifier for fields and methods that belong to the class itself, rather than to instances of the class.

## Language-Specific Idioms and Patterns

This section explores common C# language idioms and patterns that enhance code readability, efficiency, and adherence to best practices.

### Collections

- **Use** `foreach` for Iteration: Utilize the `foreach` loop for iterating over elements within a collection. It offers a concise and readable way to process each element without explicit index management.

- **Leverage Linq for Queries:** Consider using Language Integrated Query (LINQ) for performing complex queries on collections. LINQ provides a powerful and expressive syntax for filtering, sorting, and transforming data within collections.

### Interfaces

- **Favor Interfaces for Contracts:** Define interfaces to specify the behavior expected of a class. This promotes loose coupling and allows for polymorphism, where different classes can implement the same interface.

- **Dependency Injection:** Implement dependency injection principles by injecting dependencies (required objects) through constructors or methods, rather than creating them directly within the class. This enhances testability and promotes looser coupling.

### Error Handling

- Use `try...finally` for Resource Management: Employ the `try...finally` block to ensure that critical resources (e.g., database connections, file streams) are properly disposed of, even if exceptions occur. The `finally` block guarantees execution of cleanup code, regardless of whether an exception is thrown within the `try` block.

### Magic Numbers

- **Define Constants:** Avoid using "magic numbers" (literal values scattered throughout the code) by defining meaningful constants. This improves code readability, maintainability, and allows for easier modification of these values in a centralized location.

## Tools and IDE Setup

This section provides recommendations for tooling and IDE configuration to promote code quality, maintainability, and adherence to the style guide.

### IDE Configuration

- **Static Code Analysis:** Integrate static code analysis tools like StyleCop, ReSharper, or SonarLint into your IDE. These tools can automatically identify and report style violations, potential bugs, and code smells, promoting code quality and adherence to best practices.

- **Code Formatting:** Configure your IDE to automatically format code according to the style guide's formatting conventions (discussed in Section 3). This ensures consistency and readability throughout the codebase.

**Popular IDEs and their Configuration Options:**

- **Visual Studio:** Utilize extensions like ReSharper or EditorConfig to enforce style rules and formatting preferences.

- **Visual Studio Code:** Install and configure ESLint with a C# extension like CSharp formatter to enforce coding standards.

- **JetBrains Rider:** Leverage built-in code inspections and style customization options to adhere to the style guide.

**Additional Tips:**

- **Code Snippets:** Create code snippets for frequently used patterns or boilerplate code to expedite development and ensure consistency.

- **Version Control Integration:** Use a version control system like Git for code versioning, collaboration, and tracking changes aligned with the style guide.

### Testing Tools

- **Unit Testing:** Employ a unit testing framework like NUnit, xUnit, or MSTest to write unit tests for your code. Unit tests ensure the correctness of individual units (classes, methods) and promote code maintainability and refactoring confidence.

- **Integration Testing:** Utilize integration testing tools to verify how different parts of your application interact with each other. This helps to identify issues related to integration between components.
