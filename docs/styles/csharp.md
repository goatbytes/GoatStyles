# C# Style Guide

This guide specifically addresses C# development, focusing on idiomatic practices, patterns, and
C#-specific considerations.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for the purpose, scope, and general principles of our coding standards.
    type: abstract
///
[//]: # (@formatter:on)

## Formatting

The formatting guidelines for C# closely adhere to
our [Foundational Code Standards][fnd-formatting]. Here is a brief overview:

- **Consistent Indentation:** Use 2 spaces for indentation, 4 spaces for continuation lines.
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

/// details | Formatted C# Example Code
    type: example
```csharp
using System;

// Attribute used for demonstration
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method)]
public class DemoAttribute : Attribute {}

[Demo]
public class Example {
  private int x;
  private int y;

  // Constructor
  public Example(int x, int y) {
    this.x = x;
    this.y = y;
  }

  // Method demonstrating various style rules
  public void PerformOperations() {
    Inner inner = new Inner();
    inner.Display();

    int sum = x + y; // Space around operators
    Console.WriteLine($"Sum: {sum}");

    // Ternary operator with spaces
    string message = sum > 10 ? "Greater than 10" : "Not greater than 10";
    Console.WriteLine(message);

    // If-else with spacing and brace style
    if (sum % 2 == 0) {
      Console.WriteLine("Sum is even");
    } else {
      Console.WriteLine("Sum is odd");
    }

    // For loop demonstrating continuation indent
    for (int i = 0; i < 5; i++) {
      Console.Write(i + " "); // Demonstrate space in concatenation
    }
    Console.WriteLine();

    // Try-catch-finally block
    try {
      throw new InvalidOperationException("Demo exception");
    } catch (InvalidOperationException ex) {
      Console.WriteLine($"Caught exception: {ex.Message}");
    } finally {
      Console.WriteLine("Finally block executed");
    }
  }

  // Inner class
  private class Inner {
    public void Display() {
      Console.WriteLine("Inside Inner class");
    }
  }
}

class Program {
  static void Main(string[] args) {
    Example example = new Example(3, 7);
    example.PerformOperations();
  }
}
```
///
[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for C# adhere to our [Foundational Code Standards][fnd-naming] with no
exceptions.

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with "is" or "has" for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** for namespaces, concatenated words (avoid underscores).

[//]: # (TODO: Add good/bad examples for naming conventions)

## Documentation and Comments

Refer to the [Foundational Code Standards][fnd-docs] for general commenting and documentation
guidelines.

## Idioms and Best Practices

C# offers a wealth of idiomatic practices and patterns that can make your code more concise,
readable, and idiomatic. This section focuses on leveraging C#'s unique features effectively.

### Properties and Auto-Properties

Use properties and auto-properties to encapsulate fields and provide a clear, consistent interface
to class and struct members.

```csharp
public class Goat {
    public string Name { get; set; }
    public int Age { get; private set; }

    public Goat(string name, int age) {
        Name = name;
        Age = age;
    }
}
```

### LINQ for Data Manipulation

Utilize Language Integrated Query (LINQ) for querying and manipulating collections in a declarative
manner.

```csharp
var adultGoats = goats.Where(goat => goat.Age >= 2).ToList();
```

### Async/Await for Asynchronous Programming

Employ async/await for managing asynchronous operations, improving responsiveness and scalability of
your applications.

```csharp
public async Task FeedAllGoatsAsync(IEnumerable<Goat> goats) {
    foreach (var goat in goats) {
        await goat.FeedAsync();
    }
}
```

### Expression-bodied Members

Use expression-bodied members for single-line methods and properties.

```csharp
public class Goat {
    public string Name { get; }
    public int Age { get; }

    public Goat(string name, int age) => (Name, Age) = (name, age);

    public void MakeSound() => Console.WriteLine($"{Name} says 'Meeeh'");
}
```

### Null-coalescing and Null-conditional Operators

Leverage null-coalescing (`??`) and null-conditional (`?.`) operators to simplify null checks and
default value assignment.

```csharp
public string GetGoatName(Goat goat) => goat?.Name ?? "Unknown";
```

### Pattern Matching

Use pattern matching to simplify type checks and conditional logic.

```csharp
public void FeedAnimal(object animal) {
    if (animal is Goat goat) {
        Console.WriteLine($"Feeding {goat.Name}");
    }
}
```

## Tools and Resources

Ensuring a consistent development environment and utilizing static analysis tools are crucial steps
for maintaining high code quality in C# projects.

### Recommended Static Analysis Tools for C#

Static analysis tools help identify potential issues early in the development process. For C#,
several tools are particularly effective:

- [**Roslyn Analyzers**][Roslyn]: A set of analyzers that use the .NET Compiler Platform ("Roslyn")
  to offer comprehensive code analysis for C#.
- [**StyleCop**](https://github.com/StyleCop/StyleCop): A static code analysis tool that checks C#
  code for conformance to StyleCop's coding standards.
- [**SonarLint for Visual Studio**](https://www.sonarlint.org/visualstudio/): Extends SonarLint's
  capabilities to C#, offering code smells detection, bugs tracking, and code quality metrics.

### Additional Resources

- [**.NET Documentation**](https://docs.microsoft.com/en-us/dotnet/csharp/): The official .NET
  documentation, providing comprehensive information on C# language features, .NET libraries, and
  best practices.
- [**C# Programming Guide**](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/):
  Offers detailed guidance on C# programming concepts, language features, and application
  development techniques.
- [**C# Corner**](https://www.c-sharpcorner.com/): A community and educational site offering
  articles, tutorials, and forums on C# programming and .NET development.

[//]: # (@formatter:off)
[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[Roslyn]: https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview
[//]: # (@formatter:on)
