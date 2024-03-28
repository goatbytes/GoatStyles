# C# Style Guide

This guide specifically addresses C# development, focusing on idiomatic practices, patterns, and
C#-specific considerations.

[//]: # (@formatter:off)
/// admonition |
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for C#.
///
[//]: # (@formatter:on)

## Formatting

The formatting rules for C# adhere to our foundational [formatting standards][FORMATTING]:

- **Consistent Indentation:** Use 2 spaces for indentation, 4 spaces for continuation lines.
- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Whitespace:** Use spaces around operators, parentheses, braces, colons, commas, and keywords.
- **Brace Style:** Follow K&R style (opening brace on same line, closing brace on new line).
- **Blank Lines:** Use 1 line to separate code sections.
- **Alignment:** Align elements in documentation comments and parameter lists.

[//]: # (@formatter:off)
/// admonition |
    type: info
Remember, these are guidelines; adapt them for your project's needs while keeping readability in focus.
///
[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for C# adhere to our foundational [naming conventions][NAMING]:

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with `is` or `has` for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** for namespaces, concatenated words (avoid underscores).

---

**Example**

```csharp
/**
 * This class demonstrates proper code formatting following the specified style guide.
 *
 * **Formatting Rules:**
 * - Indentation: 2 spaces (C# standard).
 * - Max line length of 100 characters.
 * - Spaces around operators, control structures, and keywords.
 * - K&R brace style (opening brace on the same line as the statement).
 * - Consistent spacing for parameter lists and constructor arguments.
 * - Doc comments with aligned descriptions.
 */
public class WellFormattedCode { // (1)!
  /**
   * This method calculates the factorial of a given positive integer.
   *
   * @param n The non-negative integer for which to calculate the factorial.
   * @return  The factorial of n, or throws an ArgumentOutOfRangeException if n is negative.
   * @throws ArgumentOutOfRangeException If the provided number (n) is negative.
   */
  public static long CalculateFactorial(int n) { // (2)!
    if (n < 0) { // (3)!
      throw new ArgumentOutOfRangeException(nameof(n), "Factorial is not defined for negative numbers.");
    }

    long result = 1;
    for (int i = 2; i <= n; i++) { // (4)!
      result *= i;
    }
    return result;
  }
}
```

1.    Class name in PascalCase with a doc comment.
2.    Method name in camelCase with a doc comment.
3.    K&R brace style for blocks.
4.    Proper spacing around operators and control structures.

[//]: # (@formatter:on)

---

## Documentation and Comments

Refer to the [Foundational Code Standards][DOCS] for general commenting and documentation
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
[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments
[Roslyn]: https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview
[//]: # (@formatter:on)
