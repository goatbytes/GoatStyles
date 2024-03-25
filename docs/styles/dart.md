# Dart Style Guide

## Introduction

Welcome to the Dart Style Guide. This comprehensive guide is designed to support developers working on Dart projects by establishing a consistent framework for writing clean, maintainable, and efficient Dart code. Dart, developed by Google, powers a wide range of applications, from front-end web applications with AngularDart to mobile apps using Flutter. As the language continues to evolve, maintaining a standard approach to Dart coding practices becomes essential for productivity and collaboration.

### Purpose

The primary aim of this style guide is to foster code quality and collaborative efficiency by delineating a consistent set of coding standards for Dart. These standards cover code formatting, naming conventions, documentation, and best programming practices tailored specifically to Dart development. By adhering to these guidelines, developers can ensure their code is not only high-quality but also integrates seamlessly with existing codebases, facilitating easier code reviews and collaborative development efforts.

### Scope

This guide is intended for use by developers engaged in a variety of Dart projects, encompassing both client-side and server-side applications. Whether you're building dynamic web applications with AngularDart, creating cross-platform mobile applications with Flutter, or working on server-side Dart applications, the principles outlined in this guide apply broadly. The recommendations provided are crafted to be universally applicable, ensuring their relevance and utility across the diverse landscape of Dart development, including but not limited to:

*   AngularDart web applications
*   Flutter mobile and desktop applications
*   Command-line tools and server applications written in Dart


Embracing these guidelines will not only enhance individual project outcomes but also contribute to the greater Dart community's coherence and success. This style guide is dynamically maintained to reflect the evolving nature of Dart and its ecosystem, ensuring its continued relevance and utility for Dart developers worldwide.

## General Principles

The foundation of this Dart Style Guide is a set of overarching principles designed to guide Dart software development. These principles aim to foster a codebase that is readable, maintainable, and efficient, aligning with Dart's design and the broader objectives of software craftsmanship.

### Readability

Readability is paramount. Dart code should be written as if the next person to maintain it is unfamiliar with the project but well-versed in Dart. Code should be self-explanatory, with a clear structure that guides the reader through its logic.

### Consistency

Consistency in coding practices promotes a cohesive codebase that enhances collaborative development and code review processes. Adhere to established patterns and conventions within the Dart community and your project.

### Efficiency

Efficiency pertains not only to the performance of the code at runtime but also to the efficiency of maintenance and extension. Dart code should strike a balance between runtime performance and ease of understanding and modification.

### Scalability and Maintainability

Design Dart code with future growth in mind. Scalability and maintainability are key to accommodating new features, technologies, and changes without significant refactoring. Emphasize modular design, reusable components, and clear separation of concerns.

### Collaborative Development

Software development is a team effort. Writing Dart code that is easy to understand, review, and integrate encourages a productive and inclusive development environment. Foster practices that support collaboration, such as code reviews, pair programming, and documentation.

### Embracing Dart's Features

Leverage Dart's rich set of features and idioms appropriately. From null safety to extension methods, Dart offers tools to write safer and more expressive code. Use these features judiciously to solve problems in ways that are idiomatic to Dart.

### Testing

Testing is integral to the development process. Dart code should be accompanied by thorough unit, integration, and possibly end-to-end tests, ensuring robustness, preventing regressions, and facilitating refactoring.

### Documentation

While code should be self-explanatory as much as possible, effective documentation is crucial. Documenting public APIs, complex algorithms, or design decisions aids in understanding and maintaining the code.

Adherence to these general principles lays the foundation for high-quality Dart software development, aligning technical solutions with the project's goals and ensuring a sustainable and collaborative development process.

## Formatting

Proper formatting is essential for maintaining code readability and consistency across the Dart codebase. This section outlines the formatting rules and principles for Dart development, focusing on line length, indentation, whitespace, and syntax conventions.

### Line Length

*   **Maximum Line Length:** Aim to limit lines to 80 characters, with a maximum line length of 100 characters. This enhances code readability and ensures compatibility with various editors and tools.

```dart
// Good
final goatFeedTimes = goatFeeds.map((feed) => feed.timeScheduled).toList();

// Avoid
final goatFeedTimes = goatFeeds.map((feed) => feed.timeScheduled).where((time) => time.isAfter(DateTime.now())).toList();
```

### Indentation

*   **Spaces for Indentation:** Use 2 spaces for indentation, no tabs. This keeps the indentation consistent across different environments.

```dart
// Good
void feedGoats(List<Goat> goats) {
  for (var goat in goats) {
    goat.feed();
  }
}

// Avoid using tabs
void feedGoats(List<Goat> goats) {
  	for (var goat in goats) {
    	goat.feed();
  	}
}
```

### Whitespace

*   **Vertical Whitespace:** Use vertical spacing judiciously to separate logical blocks of code. Include a blank line before and after control flow blocks.

```dart
// Good
void checkGoats() {
  final goatsReadyForFeed = [];

  for (final goat in goats) {
    if (goat.isHungry) {
      goatsReadyForFeed.add(goat);
    }
  }

  feedGoats(goatsReadyForFeed);
}

// Avoid unnecessary vertical whitespace
void checkGoats() {
  final goatsReadyForFeed = [];
  for (final goat in goats) {
    if (goat.isHungry) {
      goatsReadyForFeed.add(goat);
    }
  }
  feedGoats(goatsReadyForFeed);
}
```

*   **Horizontal Whitespace:** Include horizontal space around operators and after commas to enhance readability.

```dart
// Good
var speed = time / distance;

// Avoid
var speed=time/distance;
```

### Braces

*   **Brace Placement:** Place the opening brace on the same line as the control flow statement or declaration. For single-line if statements, loops, or functions, braces are optional but recommended for clarity.

```dart
// Good
if (goat.isHungry) {
  feed(goat);
}

// Acceptable for single-line statements
if (goat.isHungry) feed(goat);
```

### Trailing Commas

*   **Use Trailing Commas:** Especially in multi-line lists, maps, and parameter lists. This improves formatting consistency and version control diff readability.

```dart
// Good
final goats = [
  Goat(name: 'Billy'),
  Goat(name: 'Daisy'),
];

// Avoid
final goats = [
  Goat(name: 'Billy'),
  Goat(name: 'Daisy') // No trailing comma
];
```

### Named Parameters

*   **Named Parameters Formatting:** Use named parameters to enhance the readability of function calls. Break long parameter lists into multiple lines.

```dart
// Good
final billy = Goat(
  name: 'Billy',
  age: 2,
  isHungry: true,
);

// Avoid
final billy = Goat(name: 'Billy', age: 2, isHungry: true);
```

### Dart Syntax Conventions

*   **Leverage Dart’s Syntax Features:** Make use of Dart’s syntax features such as the cascade operator (`..`) for consecutive operations on the same object.

```dart
// Good
final pen = GoatPen()
  ..add(Goat(name: 'Billy'))
  ..add(Goat(name: 'Daisy'))
  ..close();
```

Adhering to these formatting guidelines ensures that Dart code is easy to read, maintain, and consistent across different development environments. Next, we’ll move on to naming conventions to further enhance code clarity and readability.

## Naming Conventions

Following clear and consistent naming conventions is crucial in Dart development, as it enhances code readability, facilitates maintenance, and ensures codebase consistency. This section outlines the principles and rules for naming variables, functions, classes, and other identifiers in Dart, with examples demonstrating these concepts.

### Variables

*   **Lower Camel Case:** Use lowerCamelCase for naming variables and constants. Names should be descriptive, avoiding abbreviations and single-letter names unless they are local within very short methods.

```dart
// Good
var goatCount = 5;
const maxGoatsAllowed = 100;

// Avoid
var GC = 5;
const MAX_G = 100;
```

### Functions and Methods

*   **Descriptive Names:** Function and method names should be clear and descriptive, using lowerCamelCase. Names typically include verbs indicating what the function performs.

```dart
// Good
void feedAllGoats(List<Goat> goats) {
  // Implementation
}

// Avoid
void feed(List<Goat> g) {
  // Implementation
}
```

### Classes and Enumerations

*   **Upper Camel Case:** Use UpperCamelCase for classes, enums, and typedefs. Names should be noun phrases or adjectives describing the role or characteristic.

```dart
// Good
class GoatFeeder {
  // Implementation
}

enum GoatMood { happy, sad, hungry }

// Avoid
class goat_feeder {
  // Implementation
}

enum mood { happy, sad, hungry }
```

### Constants

*   **Lower Camel Case for Local Constants:** For local constants within a function, use lowerCamelCase. For global constants, consider using lowerCamelCase prefixed by a known class or prefix related to its use case.

```dart
// Good
class Farm {
  static const int maxGoats = 10;
}

// Local constant
void checkGoats() {
  const localMaxGoats = 5;
  // Implementation
}

// Avoid
const MAX_GOATS = 10;
```

### Type Parameters

*   **Upper Camel Case with Prefixes:** Use UpperCamelCase for generic type parameters. To indicate the purpose, prefix the name with the letter `T` or use descriptive names related to the role.

```dart
// Good
class Box<T> {
  // Implementation
}

class Graph<Node, Edge> {
  // Implementation
}

// Avoid
class Box<t> {
  // Implementation
}
```

### Libraries and Packages

*   **Lowercase With Underscores:** Name libraries, packages, and import prefixes using lowercase\_with\_underscores.

```dart
// Good
import 'goat_feeder.dart' as goat_feeder;

// Avoid
import 'GoatFeeder.dart' as GoatFeeder;
```

### Avoiding Ambiguity and Redundancy

*   **Contextual Naming:** Avoid redundancy in naming. Context should inform what an entity does without needing to repeat information.

```dart
// Good
class Goat {
  void feed() {
    // Implementation
  }
}

// Avoid
class Goat {
  void feedGoat() {
    // Implementation
  }
}
```

Following these naming conventions will help maintain a clear, intuitive, and consistent codebase, making it easier for developers to understand, maintain, and extend the Dart projects they work on. Next, we will discuss comments and documentation to further ensure code clarity and maintainability.

## Comments and Documentation

Effective commenting and comprehensive documentation are key to maintaining code quality and understandability in Dart code. This section outlines best practices for inline comments, documentation comments, and strategic usage to convey intent and functionality.

### Inline Comments

*   **Use Sparingly:** Inline comments should clarify complex algorithms, decisions not immediately obvious, or provide context not readily apparent from the code itself.

```dart
// Good
// Check if the goat is hungry and the pen is accessible before feeding
if (goat.isHungry && pen.isOpen) {
  pen.feed(goat);
}

// Avoid excessive or obvious comments
// Increment goatCount by 1
goatCount += 1;
```

### Documentation Comments

*   **Use** `///` for Public APIs: Document classes, methods, variables, and parameters using Dart’s `///` syntax. This aids consumers of your code and supports Dart's documentation generation tools.

```dart
/// Represents a goat in a farm management system.
///
/// Stores information about the goat's name and feeding status.
class Goat {
  /// The name of the goat.
  final String name;

  /// Creates a [Goat] with the given [name].
  Goat(this.name);
}
```

*   **Describe Parameters and Return Types:** For methods and functions, describe each parameter and the return type. Use square brackets `[]` around parameter names to link them within generated docs.

```dart
/// Feeds a [goat] with the specified [food].
///
/// Returns `true` if the goat was fed successfully.
bool feedGoat(Goat goat, String food) {
  // Implementation
}
```

### Keeping Comments Up-to-Date

*   **Reflect Code Changes:** Ensure comments are updated with code changes. Outdated comments can mislead and confuse, diminishing code quality.

### TODO Comments

*   **Track Future Enhancements with Ticket Numbers:** Use `TODO:` comments to mark areas of the code requiring further work, including a brief description and a ticket number for tracking.

```dart
// TODO: [TICKET-123] Implement the feed scheduling logic
void scheduleFeeding() {}
```

### Avoid Commented-Out Code

*   **Remove, Don’t Comment-Out:** Commented-out code can clutter your codebase. Remove code that's no longer needed or store it elsewhere if it might be useful later.

```dart
// Good
// Removed outdated goat feeding algorithm

// Avoid leaving commented-out code
// feedGoat(goat, "Hay");
// console.log("Feeding completed");
```

### Use of Annotations

*   **Leverage Dart Annotations:** Use annotations (`@deprecated`, `@override`, etc.) to provide additional information. These can inform users about the intended use or lifecycle stage of elements.

```dart
// Marking a method as deprecated
@deprecated
void oldFeedMethod() {
  // Implementation
}
```

By adhering to these commenting and documentation guidelines, Dart developers ensure their code is not only understandable and maintainable for themselves but also for anyone who might work on the codebase in the future. This promotes better collaboration and knowledge sharing within and across teams.

## Programming Practices

Adopting effective programming practices is crucial for writing robust, efficient, and maintainable Dart code. This section highlights key practices that Dart developers should follow to improve the quality and performance of their code.

### Error Handling

*   **Use** `try-catch` for Exception Handling: Leverage Dart's exception handling features to gracefully handle errors and exceptions. Provide clear feedback or recovery options when possible.

```dart
// Good
try {
  final goat = findGoatByName('Billy');
  goat.feed();
} catch (e) {
  print('Failed to feed goat: $e');
}

// Avoid ignoring exceptions
try {
  final goat = findGoatByName('Billy');
  goat.feed();
} catch (e) {
  // Silent catch
}
```

### Type Annotations

*   **Prefer Type Annotations in Public APIs:** While Dart supports type inference, explicitly annotating types in public APIs and complex code enhances clarity and ensures that your intentions are clear.

```dart
// Good
void feedGoat(Goat goat) {
  // Implementation
}

// Avoid in public APIs
var feedGoat = (Goat goat) {
  // Implementation
};
```

### Immutable Collections

*   **Favor Immutability for Collections:** When collections are not meant to change, use Dart’s built-in support for immutable collections to prevent accidental or unintended modifications.

```dart
// Good
final List<Goat> goats = const [Goat(name: 'Billy'), Goat(name: 'Daisy')];

// Avoid
List<Goat> goats = [Goat(name: 'Billy'), Goat(name: 'Daisy')]; // Mutable
```

### Avoiding Global Mutable State

*   **Minimize Use of Global State:** Global mutable state can lead to code that is hard to reason about and debug. Prefer passing objects explicitly through function parameters or using dependency injection.

```dart
// Good
class GoatFeeder {
  final GoatPen _goatPen;

  GoatFeeder(this._goatPen);

  void feedAll() {
    // Implementation
  }
}

// Avoid
GoatPen globalGoatPen = GoatPen();

void feedAllGoats() {
  // Implementation using globalGoatPen
}
```

### Using `final` and `const`

*   **Prefer** `final` and `const` Where Possible: Use `final` for variables that you only want to assign once, and `const` for compile-time constants. This practice enhances the predictability and safety of your code.

```dart
// Good
final goatName = 'Billy';
const maxGoatsAllowed = 10;

// Avoid unnecessary mutability
var goatName = 'Billy'; // Could be final
```

### Asynchronous Programming

*   **Embrace Asynchronous Programming:** Dart’s `async` and `await` keywords facilitate writing asynchronous code that is clean, straightforward, and maintainable.

```dart
// Good
Future<void> feedAllGoats() async {
  final goats = await fetchGoats();
  await Future.wait(goats.map((goat) => goat.feed()));
}

// Avoid using complex callbacks
void feedAllGoats() {
  fetchGoats().then((goats) {
    for (final goat in goats) {
      goat.feed().then((_) {
        // Nested callback
      });
    }
  });
}
```

### Leveraging Extensions

*   **Use Extensions to Add Functionality:** Dart’s extension methods allow you to add functionality to existing classes without modifying them or creating subclasses, keeping your codebase flexible and clean.

```dart
// Good
extension GoatExtensions on Goat {
  void feedAndClean() {
    feed();
    clean();
  }
}

// Usage
final billy = Goat(name: 'Billy');
billy.feedAndClean();
```

By adhering to these programming practices, Dart developers can ensure their code is not only performant and robust but also easy to understand and maintain. This forms the foundation of a high-quality Dart codebase that leverages the language's features and idioms to their fullest.

## Language-Specific Idioms and Patterns

Embracing language-specific idioms and patterns is vital for writing efficient, readable, and idiomatic Dart code. This section covers Dart-specific practices that enhance code quality and leverage the unique features of the language.

### Leveraging Null Safety

*   **Make Use of Null Safety Features:** Dart’s sound null safety is designed to eliminate null dereference errors. Use nullable types (`?`) and default values to ensure your code is more predictable and safe.

```dart
// Good
String? getGoatName(Goat? goat) => goat?.name;
```
```dart
// Avoid
String getGoatName(Goat goat) => goat.name; // Unsafe if 'goat' is null
```

### Effective Use of Collections

*   **Utilize Collection Literals:** Dart supports list, map, and set literals. Use these for creating collections more succinctly and readably.

```dart
// Good
final goats = ['Billy', 'Daisy'];
final goatAges = {'Billy': 2, 'Daisy': 3};

// Avoid
final goats = List<String>.from(['Billy', 'Daisy']);
final goatAges = Map<String, int>.from({'Billy': 2, 'Daisy': 3});
```

### Functional Programming Patterns

*   **Embrace Functional Programming Constructs:** Take advantage of Dart’s support for first-class functions and higher-order functions to write cleaner and more expressive code.

```dart
// Good
goats.forEach((goat) => print(goat));
final adultGoats = goats.where((goat) => goat.age > 1).toList();

// Avoid traditional for loops for simple iterations
for (var goat in goats) {
  print(goat);
}
```

### Extension Methods

*   **Extend Existing Classes:** Use extension methods to add functionality to existing classes without modifying them or creating subclasses, keeping your codebase flexible and modular.

```dart
// Good
extension GoatExtensions on Goat {
  bool get isAdult => age > 1;
}

// Usage
if (goat.isAdult) {
  print('Goat is an adult');
}
```

### Cascades

*   **Use Cascades to Chain Operations:** Dart’s cascade (`..`) operator allows you to perform a sequence of operations on the same object. This can make your code more fluent and less verbose.

```dart
// Good
final goatPen = GoatPen()
  ..add(Goat(name: 'Billy'))
  ..add(Goat(name: 'Daisy'))
  ..close();

// Avoid
final goatPen = GoatPen();
goatPen.add(Goat(name: 'Billy'));
goatPen.add(Goat(name: 'Daisy'));
goatPen.close();
```

### Asynchronous Programming

*   **Prefer async/await Over Futures:** Use `async` and `await` for handling asynchronous operations to write code that is clean, simple, and easy to understand.

```dart
// Good
Future<void> feedAllGoats() async {
  final goats = await fetchGoats();
  for (var goat in goats) {
    await goat.feed();
  }
}

// Avoid using then() for complex chains of futures
fetchGoats().then((goats) {
  goats.forEach((goat) {
    goat.feed().then((_) {
      // Nested then()
    });
  });
});
```

### Using Generics

*   **Generics for Type Safety and Flexibility:** Use generics to write flexible and reusable code components while maintaining type safety.

```dart
// Good
class GoatList<T extends Goat> {
  final List<T> _goats = [];

  void add(T goat) => _goats.add(goat);
  List<T> get all => _goats;
}

// Usage
final myGoats = GoatList<Goat>();
myGoats.add(Goat(name: 'Billy'));
```

Adopting these Dart-specific idioms and patterns not only enhances code readability and efficiency but also ensures that your Dart codebase is robust, maintainable, and idiomatic. This approach leverages Dart’s full potential to create high-quality applications.

## Tools and IDE Setup

Setting up a productive development environment is crucial for Dart developers. This section guides on configuring tools and Integrated Development Environments (IDEs) to enhance productivity, ensure code quality, and align with Dart style guidelines.

### Dart Analysis

*   **Leverage** `dart analyze`: Use Dart's static analysis tool to identify potential code issues, including syntax errors, type issues, and adherence to Dart conventions. Configure `analysis_options.yaml` in your project to customize rules.

```dart
include: package:pedantic/analysis_options.yaml
linter:
  rules:
    prefer_single_quotes: true
    avoid_print: true
```

### IDE Support

#### Visual Studio Code (VS Code)

*   **Extensions:** Install the Dart and Flutter (if using Flutter) extensions from the VS Code marketplace to get syntax highlighting, code completion, and debug support.

*   **Format on Save:** Enable "Format On Save" to automatically format your code according to Dart's formatting rules. Go to Settings → search for "Format On Save" → check the box.

*   **Problem View:** Use the Problems tab to quickly navigate and address issues identified by the Dart analyzer.

#### IntelliJ IDEA / Android Studio

*   **Dart and Flutter Plugins:** Install the Dart and Flutter plugins via Preferences → Plugins. These provide comprehensive Dart support, including syntax highlighting, code completion, and debugging.

*   **Code Style Configuration:** Configure Dart formatting in Preferences → Editor → Code Style → Dart. You can adjust settings to match your team’s style guide.

*   **Dart Analysis:** Use the Dart Analysis window to view and navigate to issues in your codebase. Customize analysis options with `analysis_options.yaml`.

### Formatting Tools

*   **dart format:** Use the `dart format` command to automatically format your Dart code. Integrate this command into your version control pre-commit hooks to ensure consistent formatting.

### Linting

*   **Effective Dart:** Use the linter package to enforce Dart best practices. Customize your `analysis_options.yaml` to enable preferred lint rules.

```dart
include: package:lints/recommended.yaml
```

### Dependency Management

*   **Pub:** Use Dart’s package manager, pub, to manage dependencies. Regularly update your dependencies to get the latest features and security updates.

```dart
dart pub upgrade
```

By utilizing these tools and configuring your IDE properly, you can significantly enhance your Dart development workflow. This setup helps maintain high code quality, ensures consistency with Dart style guidelines, and streamlines the development process.