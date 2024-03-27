# Java Style Guide

This guide outlines best practices for writing clean, consistent, and understandable Java code,
focusing on readability, maintainability, and idiomatic usage.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for the purpose, scope, and general principles guiding our coding practices.
    type: abstract
///
[//]: # (@formatter:on)

## Formatting

The formatting guidelines for Kotlin adhere to our [Foundational Code Standards][fnd-formatting].
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

The naming conventions for Kotlin adhere to our [Foundational Code Standards][fnd-naming]
with no exceptions.

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with "is" or "has" for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

## Documentation and Comments

### Commenting Code

* **Purpose and Clarity**: Comments should clarify the purpose of the code, covering "why" it does
  something, not just "what" it does. Avoid redundant comments.
* **Keep Comments Updated**: As code changes, ensure comments are updated to reflect current
  functionality. Outdated comments can be more misleading than no comments at all.

    ```java
    // Correct use of comments to explain the "why"
    // Adjusts goat happiness level based on feeding time; longer feeding times make happier goats.
    goat.adjustHappiness(feedingTimeMinutes *HAPPINESS_FACTOR);
    ```

### Documentation Comments

* **Classes and Interfaces**: Provide a summary at the beginning of each class and interface,
  describing its purpose and role within the application.
* **Methods**: Document every method, including a description of its behavior, parameters, return
  values, and any exceptions thrown.
* **JavaDoc Conventions**: Use JavaDoc standard tags (`@param`, `@return`, `@throws`) to describe
  method signatures. Inline `{@code}` for code references and `{@link}` for related classes or
  methods.

    ```{.java title="Example"}
    /**
     * Represents a goat in the farm simulation.
     * <p>
     * This class provides methods to manage the goat's state, including its hunger and happiness levels.
     */
    public class Goat {
      private final String name;
      private final int age;
  
      /**
       * Constructs a new Goat with the specified name and age.
       *
       * @param name the name of the goat
       * @param age the age of the goat
       */
      public Goat(String name, int age) {
        this.name = name;
        this.age = age;
      }
  
      /**
       * Feeds the goat, adjusting its hunger level.
       *
       * @param foodType The type of food being fed to the goat.
       * @param quantity The amount of food in kilograms.
       * @return The health status after feeding.
       * @throws OverfeedingException If the quantity of food exceeds the goat's dietary restrictions.
       */
      public String feed(String foodType, double quantity) throws OverfeedingException {
        // Implementation omitted
        return "Healthy";
      }
    }
    ```

### Inline Comments

* **Use Sparingly**: Inline comments are intended for complex code segments where the logic's
  purpose or action isn't immediately clear from the code itself.
* **Location**: Place inline comments on the line above the code segment they describe, not at the
  end of the line of code.

    ```java
    // Calculate the optimal feeding time based on the goat's current activity level
    int feedingTime = calculateFeedingTime(goat.getActivityLevel());
    ```

### Documentation for Public APIs

* **Comprehensive Coverage**: Every public class, method, and member variable should be documented,
  offering clear insights into the component's purpose, use, and behavior. Documentation should be
  precise and comprehensive, especially for software that may be used in critical systems. Consider
  the principles of security, reliability, and transparency in your documentation practices.

### TODOs and FIXMEs

* **Ticket-Based Tracking Preferred**: While `TODO:` and `FIXME:` comments can highlight areas
  needing attention or improvement within the codebase, utilizing a ticket-based tracking system is
  preferred for managing tasks and issues. This approach facilitates better prioritization,
  tracking, and resolution of tasks.
* **Include Ticket Numbers**: When using `TODO:` or `FIXME:` comments, always include the
  corresponding ticket number from your project's issue tracking system. This practice links code
  comments directly to detailed descriptions, discussions, and updates on the issue or task at hand,
  ensuring actionable and trackable comments.
  
    ```java
    // TODO: [TICKET-1234] Implement happiness adjustment based on the current weather conditions
    // FIXME: [TICKET-5678] Resolve issue where feeding time exceeds 24 hours in edge cases
    ```

## Best Practices and Idioms

### Error Handling

* **Prefer Exceptions to Return Codes**: Use exceptions to indicate errors or exceptional
  conditions. This approach avoids cluttering your code with error handling and makes error paths
  clear.
* **Catch Specific Exceptions**: Whenever possible, catch the most specific exception type rather
  than generic ones like `Exception` or `Throwable`.
* **Throw Specific Exceptions**: Throw exceptions that accurately represent the error condition.
  Custom exception types can be defined to provide more detailed error information.
* **Resource Handling**: Use try-with-resources statements for resource management to ensure that
  resources are closed properly and efficiently.

    ```{.java title="Example"}
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        return br.readLine();
    } catch (IOException e) {
        throw new MySpecificException("Failed to read from file: " + path, e);
    }
    ```

### Control Structures

* **Consistent Bracing**: Use the "Egyptian style" for braces where the opening brace is at the end
  of the line that begins the block, and the closing brace is aligned with the start of the line
  that begins the block.
* **No Empty Loops or Ifs**: Avoid empty loop bodies or `if` statements; use comments to explain the
  reasoning if necessary.

### Class, Method, and Modifier Organization

* **Class Member Ordering**: Logical or temporal grouping should guide the ordering of class
  members. Typically, variables should be declared at the top of the class, followed by constructors
  and methods. Similar functions should be grouped together or placed in a logical sequence.
* **Method Length**: Keep methods short and focused. A method should represent a single logical
  operation or action. If a method grows too large, consider breaking it into smaller helper
  methods.
* **Modifiers**: Use the Java Language Specification (JLS) recommended order of
  modifiers: `public`, `protected`, `private`, `abstract`, `static`, `final`, `transient`, 
  `volatile`, `synchronized`, `native`, `strictfp`.

    ```{.java title="Example"}
    public static final synchronized void petGoat() {
      // Method body
    }
    ```

### Switch Statements

* **Fall-through**: Mark intentional fall-throughs with a comment to distinguish them from
  missing `break` statements.
* **Default Case**: Always include a `default` case in switch statements, even if it simply throws
  an exception. This ensures that all possibilities are explicitly handled.

    ```{.java title="🌿 Example"}
    public void chooseMarijuanaType(String desiredEffect) {
      String strainType;
      switch (desiredEffect) {
        case "relax":
          strainType = "Indica";
          break;
        case "energize":
          strainType = "Sativa";
          break;
        case "balance":
          // fall-through: Suitable for both relaxation and energy
        case "meditate":
          strainType = "Hybrid";
          break;
        default:
          throw new IllegalArgumentException("Effect not recognized");
      }
      System.out.println("Recommended strain type: " + strainType);
    }
    ```

## Language-Specific Idioms and Patterns

Adhering to Java's idiomatic patterns enhances code readability, efficiency, and maintainability,
crucial for both Android and other Java environments. This section emphasizes best practices that
are compatible across various Java versions.

### Effective Use of Collections

Leverage standard Java Collections Framework effectively. Opt for the appropriate interface
(e.g., `List`, `Set`, `Map`) to convey the collection's characteristics and intended use.

```{.java title="🐐 Example"}
// List for ordered collection with duplicates allowed
List<Goat> goatHerd = new ArrayList<>();
// Set for a unique collection, no duplicates
Set<Goat> uniqueGoats = new HashSet<>();
```

### Using Interfaces for Type Definitions

Prefer using interface types (e.g., `List`, `Map`) in variable declarations, method returns, and
parameters. This approach increases flexibility by decoupling the code from specific
implementations.

### Consistent Error Handling

Use exceptions to handle errors. Define custom exception classes when you need to convey specific
error information. Catch exceptions at a level where you can handle them meaningfully.

```{.java title="Example"}
try {
  feedGoats(goatHerd);
} catch (InsufficientFoodException e) {
  log.error("Not enough food for the goats", e);
  // Handle error gracefully
}
```

### Avoiding Magic Numbers

Replace magic numbers with named constants to improve code readability and maintainability.

```{.java title="Example"}
public class GoatFeeder {
  private static final int MAX_FEED_PER_GOAT_KG = 5;

  public void feedGoat(Goat goat, int feedKg) {
    if (feedKg > MAX_FEED_PER_GOAT_KG) {
      throw new IllegalArgumentException("Too much feed for one goat");
    }
    // Feed the goat
  }
}
```

## Tools and Resources

### Static Analysis Tools

*   **Checkstyle**: Ensures that the code adheres to a coding standard, helping maintain consistency across the project.
*   **PMD**: Scans code for potential bugs, unused variables, unnecessary object creation, and more.
*   **SpotBugs**: Focuses on identifying potential bugs in code through bytecode analysis.
*   **SonarQube**: Provides a comprehensive overview of code quality, highlighting bugs, vulnerabilities, and code smells. It also offers detailed code metrics and history.
*   **JaCoCo**: Offers code coverage analysis to ensure that your tests cover a significant portion of your codebase.

### Additional Resources

- [Oracle's Java Tutorials][Oracle Java Tutorials]: Comprehensive tutorials on Java programming
  language features and libraries.
- [Effective Java][Effective Java]: A book by Joshua Bloch, providing best practices for writing
  effective Java code.

[//]: # (links @formatter:off)

[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[Oracle Java Tutorials]: https://docs.oracle.com/javase/tutorial/
[Effective Java]: https://www.pearson.com/us/higher-education/program/Bloch-Effective-Java-3rd-Edition/PGM334830.html

[//]: # (links @formatter:on)
