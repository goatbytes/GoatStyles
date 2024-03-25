# Java Style Guide
## Introduction

Welcome to our Java Style Guide. This document is designed to serve as a compass for developers engaged in Java projects, including Android applications and broader Java-based software initiatives. Through clear, practical guidelines, this guide aims to foster clean, maintainable, and efficient Java code. It's crafted to support both new projects and ongoing work, ensuring that all contributions are of high quality and easy to integrate and understand.

### Purpose

The goal of this style guide is to enhance project collaboration and code quality by establishing a consistent set of standards for code formatting, naming conventions, documentation, and programming practices. By aligning on these conventions, we aim to streamline the code review process, facilitate seamless collaboration across teams, and ultimately raise the bar for code quality in our projects.

### Scope

This guide targets developers working across the spectrum of Java projects, from compact Android apps to expansive enterprise systems. The recommendations provided are crafted to be broadly applicable, ensuring relevance and utility in diverse Java development contexts.

## General Principles

The foundation of this style guide is built upon a set of core principles that guide our approach to Java software development. These principles are not mere rules but embody our vision for creating enduring and adaptable code.

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

Proper formatting is crucial for maintaining readability and consistency across the codebase. This section provides guidelines on indentation, line length, whitespace, and the use of blank lines, all aimed at enhancing the clarity and professionalism of the code.

### Indentation

*   **Tab size**: 2 characters.
*   **Indent**: 2 characters for new blocks.
*   **Continuation indent**: 4 characters for line continuations.

Spaces are preferred over tabs to maintain consistent appearance across various environments.

**Example**
```java
public class GoatLeaderboard {
  public void displayLeaderboardDetails(String competitionName,
                                        ArrayList<String> goatNames, int year) {
    System.out.println("Competition: " + competitionName + " Year: " + year);
    for (String goat : goatNames) {
      System.out.println(goat + " participated.");
    }
  }

  public static void main(String[] args) {
    ArrayList<String> goats = new ArrayList<>();
    goats.add("Billy");
    goats.add("Ginny");
    goats.add("Daisy");
    new GoatLeaderboard().displayLeaderboardDetails("Mountain Climbing", goats, 2024);
  }
}
```

### Line Length
*   **Maximum line length**: 100 characters.

For better readability, lines exceeding this length should be broken into multiple lines.

### Whitespace

Correct use of whitespace improves code readability. Follow these whitespace conventions:
  
* **Before parentheses**: Include a space before an opening parenthesis `(`, except in method declarations or calls.
*   **Around operators**: Include spaces around operators (e.g., `=`, `+`, `-`), except for unary operators and the method reference double colon `::`.
*   **Before left brace** `{`: Include a space before the left brace in class declarations, method declarations, and control flow statements.
*   **Before keywords**: Include a space before keywords like `if`, `for`, `while`.
*   **In ternary operator**: Include spaces around the components (`?` and `:`) of the ternary operator.
*   **After commas** `,`: Include a space after commas in lists (e.g., method arguments, array initializers).
*   **After** `for` semicolons `;`: Include a space after the semicolons in a `for` loop.
*   **After type cast**: Include a space after a type cast.
*   **Before colon in** `foreach`: Include a space before the colon.

**Example**
```java
public class GoatFeedingSchedule {
  public void scheduleFeedingTimes(List<Goat> goats) {
    for (Goat goat : goats) {
      String feedingTime = (goat.isHungry()) ? "now" : "later";
      System.out.println("Feeding time for " + goat.getName() + ": " + feedingTime);
    }
  }
}
```

### Blank Lines
Strategically placed blank lines can significantly enhance the readability of your code. Adhere to these guidelines:
*   **Between declarations**: 1 blank line between methods or fields.
*   **Between header and package, after package statement, before and after imports, around class/interface, and around initializer blocks**: 1 blank line to separate these sections clearly.

**Example**
```java
package com.goatbytes.academy;

import java.util.List;

public class CodingCourse {

  private String courseName;

  public CodingCourse(String courseName) {
    this.courseName = courseName;
  }

  public void enrollStudent(String studentName) {
    System.out.println(studentName + " has enrolled in " + courseName);
  }

  public static void main(String[] args) {
    CodingCourse course = new CodingCourse("Intro to Java");
    course.enrollStudent("Billy");
  }
}
```

## Naming Conventions

Consistent naming conventions enhance code readability and maintainability by making it easier for developers to understand the structure and purpose of the code at a glance.

### Classes and Interfaces

*   **Convention**: CamelCase, starting with an uppercase letter.
*   **Rationale**: Classes and interfaces represent entities or concepts; thus, their names should be nouns or noun phrases.
*   **Example**: `Goat`, `GoatHerd`, `GoatFeeder`

```java
public class Goat {
  private String name;
  public Goat(String name) {
    this.name = name;
  }
}

interface GoatFeeder {
  void feedGoats();
}
```

### Methods
*   **Convention**: camelCase, starting with a lowercase letter.
*   **Rationale**: Methods perform actions, so their names should be verbs or verb phrases.
*   **Example**: `feedGoats`, `calculateGoatHappiness`, `retrieveGoatByName`

```java
public class GoatCare {
  public void feedGoats() {
    System.out.println("Feeding the goats.");
  }

  public int calculateGoatHappiness(String goatName) {
    // Implementation
    return 0; // Placeholder return value
  }

  public Goat retrieveGoatByName(String name) {
    // Implementation
    return new Goat(name); // Placeholder return
  }
}
```

### Variables

*   **Local Variables and Instance Fields**: camelCase, starting with a lowercase letter. Descriptive, conveying the meaning directly.
*   **Constants**: ALL\_CAPS with underscores separating words.
*   **Rationale**: Variable names should clearly indicate their purpose or value. Constants are often final variables with a static value, and their all-caps naming makes them stand out.
*   **Example**: `goatCount`, `isGoatHungry`, `MAX_GOATS_ALLOWED`

```java
public class GoatFarm {
  private int goatCount = 10;
  private boolean isGoatHungry = true;
  public static final int MAX_GOATS_ALLOWED = 100;

  public void manageGoats() {
    // Use variables within a method
    System.out.println("Total goats: " + goatCount);
    System.out.println("Is any goat hungry? " + isGoatHungry);
  }
}
```

### Packages

*   **Convention**: All lowercase, multiple words concatenated together (no underscores).
*   **Rationale**: Package names are used as part of the namespace, so they should avoid conflict with class names.
*   **Example**: `com.goatfarm.feeding`, `com.goatfarm.management`

```java
package com.goatfarm.feeding;
```

### Enums

*   **Convention**: Enums can be named using CamelCase (PascalCase), starting with an uppercase letter for types. Enum constants should use ALL\_CAPS with underscores separating words.
*   **Rationale**: Enums represent fixed sets of constants. Allowing PascalCase for enum types gives flexibility in naming conventions, aligning with the naming of classes and interfaces, while the ALL\_CAPS convention for enum constants clearly distinguishes them as fixed values.
*   **Example**: `GoatMood { HAPPY, SAD, HUNGRY }`; alternative PascalCase usage for more descriptive enums or when integrating with existing code bases might be `GoatMoodEnum`.

```java
public enum GoatMood {
    HAPPY, SAD, HUNGRY;
}

// Example of alternative PascalCase usage
public enum GoatMoodEnum {
    Happy, Sad, Hungry;
}
```

## Commenting and Documentation

Effective commenting and comprehensive documentation are pivotal in maintaining code quality, facilitating maintenance, and ensuring codebase accessibility for new and existing developers.

### Commenting Code

*   **Purpose and Clarity**: Comments should clarify the purpose of the code, covering "why" it does something, not just "what" it does. Avoid redundant comments.
*   **Keep Comments Updated**: As code changes, ensure comments are updated to reflect current functionality. Outdated comments can be more misleading than no comments at all.

```java
// Correct use of comments to explain the "why"
// Adjusts goat happiness level based on feeding time; longer feeding times make happier goats.
goat.adjustHappiness(feedingTimeMinutes * HAPPINESS_FACTOR);
```

### Documentation Comments

*   **Classes and Interfaces**: Provide a summary at the beginning of each class and interface, describing its purpose and role within the application.
*   **Methods**: Document every method, including a description of its behavior, parameters, return values, and any exceptions thrown.
*   **JavaDoc Conventions**: Use JavaDoc standard tags (`@param`, `@return`, `@throws`) to describe method signatures. Inline `{@code}` for code references and `{@link}` for related classes or methods.

**Example**
```java
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
*   **Use Sparingly**: Inline comments are intended for complex code segments where the logic's purpose or action isn't immediately clear from the code itself.
*   **Location**: Place inline comments on the line above the code segment they describe, not at the end of the line of code.

```java
// Calculate the optimal feeding time based on the goat's current activity level
int feedingTime = calculateFeedingTime(goat.getActivityLevel());
```

### Documentation for Public APIs
*   **Comprehensive Coverage**: Every public class, method, and member variable should be documented, offering clear insights into the component's purpose, use, and behavior. Documentation should be precise and comprehensive, especially for software that may be used in critical systems. Consider the principles of security, reliability, and transparency in your documentation practices.

### TODOs and FIXMEs
*   **Ticket-Based Tracking Preferred**: While `TODO:` and `FIXME:` comments can highlight areas needing attention or improvement within the codebase, utilizing a ticket-based tracking system is preferred for managing tasks and issues. This approach facilitates better prioritization, tracking, and resolution of tasks.
*   **Include Ticket Numbers**: When using `TODO:` or `FIXME:` comments, always include the corresponding ticket number from your project's issue tracking system. This practice links code comments directly to detailed descriptions, discussions, and updates on the issue or task at hand, ensuring actionable and trackable comments.

```java
// TODO: [TICKET-1234] Implement happiness adjustment based on the current weather conditions
// FIXME: [TICKET-5678] Resolve issue where feeding time exceeds 24 hours in edge cases
```

## Programming Practices
This section outlines best practices for programming in Java, focusing on error handling, control structures, class and method organization, and specific guidelines for modifiers and switch statements.
### Error Handling
*   **Prefer Exceptions to Return Codes**: Use exceptions to indicate errors or exceptional conditions. This approach avoids cluttering your code with error handling and makes error paths clear.
*   **Catch Specific Exceptions**: Whenever possible, catch the most specific exception type rather than generic ones like `Exception` or `Throwable`.
*   **Throw Specific Exceptions**: Throw exceptions that accurately represent the error condition. Custom exception types can be defined to provide more detailed error information.
*   **Resource Handling**: Use try-with-resources statements for resource management to ensure that resources are closed properly and efficiently.

**Example**
```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
  return br.readLine();
} catch (IOException e) {
  throw new MySpecificException("Failed to read from file: " + path, e);
}
```

### Control Structures

*   **Consistent Bracing**: Use the "Egyptian style" for braces where the opening brace is at the end of the line that begins the block, and the closing brace is aligned with the start of the line that begins the block.
*   **No Empty Loops or Ifs**: Avoid empty loop bodies or `if` statements; use comments to explain the reasoning if necessary.

### Class, Method, and Modifier Organization

*   **Class Member Ordering**: Logical or temporal grouping should guide the ordering of class members. Typically, variables should be declared at the top of the class, followed by constructors and methods. Similar functions should be grouped together or placed in a logical sequence.
*   **Method Length**: Keep methods short and focused. A method should represent a single logical operation or action. If a method grows too large, consider breaking it into smaller helper methods.
*   **Modifiers**: Use the Java Language Specification (JLS) recommended order of modifiers: `public`, `protected`, `private`, `abstract`, `static`, `final`, `transient`, `volatile`, `synchronized`, `native`, `strictfp`.

**Example**
```java
public static final synchronized void petGoat() {
  // Method body
}
```

### Switch Statements
*   **Fall-through**: Mark intentional fall-throughs with a comment to distinguish them from missing `break` statements.
*   **Default Case**: Always include a `default` case in switch statements, even if it simply throws an exception. This ensures that all possibilities are explicitly handled.

**Example**
```java
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

Adhering to Java's idiomatic patterns enhances code readability, efficiency, and maintainability, crucial for both Android and other Java environments. This section emphasizes best practices that are compatible across various Java versions.

### Effective Use of Collections

Leverage standard Java Collections Framework effectively. Opt for the appropriate interface (e.g., `List`, `Set`, `Map`) to convey the collection's characteristics and intended use.

**Example**
```java
// List for ordered collection with duplicates allowed
List<Goat> goatHerd = new ArrayList<>();
// Set for a unique collection, no duplicates
Set<Goat> uniqueGoats = new HashSet<>();
```

### Using Interfaces for Type Definitions

Prefer using interface types (e.g., `List`, `Map`) in variable declarations, method returns, and parameters. This approach increases flexibility by decoupling the code from specific implementations.

### Consistent Error Handling

Use exceptions to handle errors. Define custom exception classes when you need to convey specific error information. Catch exceptions at a level where you can handle them meaningfully.

**Example**
```java
try {
  feedGoats(goatHerd);
} catch (InsufficientFoodException e) {
  log.error("Not enough food for the goats", e);
  // Handle error gracefully
}
```

### Avoiding Magic Numbers

Replace magic numbers with named constants to improve code readability and maintainability.

**Example**
```java
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

## Tools and IDE Setup

Ensuring a consistent development environment across the team is crucial for maintaining code quality and adhering to this style guide. This section covers the setup for IntelliJ IDEA, one of the most popular Integrated Development Environments (IDE) for Java development, and recommends static analysis tools to catch potential issues early in the development process.

### IntelliJ IDEA Configuration

To align with the coding standards outlined in this guide, we provide a custom IntelliJ IDEA code style configuration. This configuration ensures that your IDE automatically adheres to the formatting rules and conventions specified herein.

**Importing Code Style Settings**
1.  Download the code style configuration file.
2.  Open IntelliJ IDEA.
3.  Go to `File` > `Settings` (on Windows and Linux) or `IntelliJ IDEA` > `Preferences` (on macOS).
4.  Navigate to `Editor` > `Code Style`.
5.  Click on the gear icon (`⚙️`) next to the `Scheme` dropdown at the top of the window and select `Import Scheme` > `IntelliJ IDEA code style XML`.
6.  Find and select the downloaded XML file, then click `OK`.
7.  Ensure the newly imported scheme is selected in the `Scheme` dropdown.
8.  Click `Apply` and `OK` to save the changes.

These steps will configure your IntelliJ IDEA environment to use the code style defined for our projects, promoting consistency and easing the code review process.

### Recommended Static Analysis Tools

Static analysis tools play a vital role in identifying potential issues, such as bugs, code smells, and security vulnerabilities, early in the development cycle. Here are some commonly used tools in Java projects:

*   **Checkstyle**: Ensures that the code adheres to a coding standard, helping maintain consistency across the project.
*   **PMD**: Scans code for potential bugs, unused variables, unnecessary object creation, and more.
*   **SpotBugs**: Focuses on identifying potential bugs in code through bytecode analysis.
*   **SonarQube**: Provides a comprehensive overview of code quality, highlighting bugs, vulnerabilities, and code smells. It also offers detailed code metrics and history.
*   **JaCoCo**: Offers code coverage analysis to ensure that your tests cover a significant portion of your codebase.

Integrating these tools into your development and continuous integration processes can significantly improve code quality and project maintainability.