# Dart Style Guide

This guide offers comprehensive insights into writing idiomatic, clean, and maintainable Dart code,
aligning with Dart's conventions and best practices.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for the overarching principles, purpose, and scope that guide our coding practices.
    type: abstract
///
[//]: # (@formatter:on)

## Formatting

Dart formatting is automated with `dartfmt`, ensuring consistent code style across all Dart
projects:

- **Indentation:** Use 2 spaces for indentation.
- **Line Length:** While the default line length for Dart is 80 characters, we recommend adjusting
  this to 100 characters for better readability.
- **Braces:** Opening braces are placed on the same line as the statement.

## Naming Conventions

Dart employs specific naming conventions to enhance readability and maintain consistency:

- **PascalCase** for classes, enum types, and type parameters.
- **snake_case** for libraries, packages, directories, and source files.
- **camelCase** for functions, variables, properties.
    - Prefix booleans with "is" or "has" for clarity.
- **camelCase** for functions, variables, constants, and parameters.
    - Prefix global constants with a lowercase `k` before `CamelCase`.

## Commenting and Documentation

### DartDoc

Use DartDoc to document public APIs. Comments should be clear and concise, providing valuable
insights into the code's purpose and usage.

### Inline Comments

* **Use Sparingly:** Inline comments should clarify complex algorithms, decisions not immediately
  obvious, or provide context not readily apparent from the code itself.

    ```{.dart .bad-code title="Avoid excessive or obvious comments"}
    // Avoid excessive or obvious comments
    // Increment goatCount by 1
    goatCount += 1;
    ```

### Documentation Comments

* **Use** `///` for Public APIs: Document classes, methods, variables, and parameters using
  Dart’s `///` syntax. This aids consumers of your code and supports Dart's documentation generation
  tools.

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

* **Describe Parameters and Return Types:** For methods and functions, describe each parameter and
  the return type. Use square brackets `[]` around parameter names to link them within generated
  docs.

    ```dart
    /// Feeds a [goat] with the specified [food].
    ///
    /// Returns `true` if the goat was fed successfully.
    bool feedGoat(Goat goat, String food) {
    // Implementation
    }
    ```

### Keeping Comments Up-to-Date

* **Reflect Code Changes:** Ensure comments are updated with code changes. Outdated comments can
  mislead and confuse, diminishing code quality.

### TODO Comments

* **Track Future Enhancements with Ticket Numbers:** Use `TODO:` comments to mark areas of the code
  requiring further work, including a brief description and a ticket number for tracking.

    ```dart
    // TODO: [TICKET-123] Implement the feed scheduling logic
    void scheduleFeeding() {}
    ```

### Avoid Commented-Out Code

* **Remove, Don’t Comment-Out:** Commented-out code can clutter your codebase. Remove code that's no
  longer needed or store it elsewhere if it might be useful later.

    ```{.dart .good-code title="Good"}
    // Removed outdated goat feeding algorithm
    ```

    ```{.dart .bad-code title="Avoid"}
    // Avoid leaving commented-out code
    // feedGoat(goat, "Hay");
    // console.log("Feeding completed");
    ```

## Idioms and Best Practices

### Effective Dart Guidelines

Adhere to the [Effective Dart Guidelines][Effective Dart] for tips on writing clear, idiomatic Dart
code.

### Error Handling

* **Use** `try-catch` for Exception Handling: Leverage Dart's exception handling features to
  gracefully handle errors and exceptions. Provide clear feedback or recovery options when possible.

    ```{.dart .good-code title="Good"}
    try {
      final goat = findGoatByName('Billy');
      goat.feed();
    } catch (e) {
      print('Failed to feed goat: $e');
    }
    ```
    ```{.dart .bad-code title="Avoid ignoring exceptions"}
    try {
      final goat = findGoatByName('Billy');
      goat.feed();
    } catch (e) {
      // Silent catch
    }
    ```

### Type Annotations

* **Prefer Type Annotations in Public APIs:** While Dart supports type inference, explicitly
  annotating types in public APIs and complex code enhances clarity and ensures that your intentions
  are clear.

    ```{.dart .good-code title="Good"}
    // Good
    void feedGoat(Goat goat) {
      // Implementation
    }
    ```
    ```{.dart .bad-code title="Avoid in public APIs"}
    // Avoid in public APIs
    var feedGoat = (Goat goat) {
      // Implementation
    };
    ```

### Immutable Collections

* **Favor Immutability for Collections:** When collections are not meant to change, use Dart’s
  built-in support for immutable collections to prevent accidental or unintended modifications.

    ```{.dart .good-code title="Good"}
    final List<Goat> goats = const [Goat(name: 'Billy'), Goat(name: 'Daisy')];
    ```
    ```{.dart .bad-code title="Avoid"}
    List<Goat> goats = [Goat(name: 'Billy'), Goat(name: 'Daisy')]; // Mutable
    ```

### Avoiding Global Mutable State

* **Minimize Use of Global State:** Global mutable state can lead to code that is hard to reason
  about and debug. Prefer passing objects explicitly through function parameters or using dependency
  injection.

    ```{.dart .good-code title="Good"}
    class GoatFeeder {
      final GoatPen _goatPen;
    
      GoatFeeder(this._goatPen);
    
      void feedAll() {
        // Implementation
      }
    }
    ```
    ```{.dart .bad-code title="Avoid"}
    GoatPen globalGoatPen = GoatPen();
    
    void feedAllGoats() {
      // Implementation using globalGoatPen
    }
    ```

### Using `final` and `const`

* **Prefer** `final` and `const` Where Possible: Use `final` for variables that you only want to
  assign once, and `const` for compile-time constants. This practice enhances the predictability and
  safety of your code.

    ```{.dart .good-code title="Good"}
    final goatName = 'Billy';
    const maxGoatsAllowed = 10;
    ` ``
    ```{.dart .bad-code title="Avoid unnecessary mutability"}
    var goatName = 'Billy'; // Could be final
    ```

### Asynchronous Programming

* **Embrace Asynchronous Programming:** Dart’s `async` and `await` keywords facilitate writing
  asynchronous code that is clean, straightforward, and maintainable.

    ```{.dart .good-code title="Good"}
    Future<void> feedAllGoats() async {
      final goats = await fetchGoats();
      await Future.wait(goats.map((goat) => goat.feed()));
    }
    ```
    ```{.dart .bad-code title="Avoid nested callbacks"}
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

* **Use Extensions to Add Functionality:** Dart’s extension methods allow you to add functionality
  to existing classes without modifying them or creating subclasses, keeping your codebase flexible
  and clean.

    ```.dart
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

### Leveraging Null Safety

* **Make Use of Null Safety Features:** Dart’s sound null safety is designed to eliminate null
  dereference errors. Use nullable types (`?`) and default values to ensure your code is more
  predictable and safe.

    ```{.dart .good-code title="Good"}
    String? getGoatName(Goat? goat) => goat?.name;
    ```
    ```{.dart .bad-code title="Avoid"}
    String getGoatName(Goat goat) => goat.name; // Unsafe if 'goat' is null
    ```

### Effective Use of Collections

* **Utilize Collection Literals:** Dart supports list, map, and set literals. Use these for creating
  collections more succinctly and readably.

    ```{.dart .good-code title="Good"}
    // Good
    final goats = ['Billy', 'Daisy'];
    final goatAges = {'Billy': 2, 'Daisy': 3};
    ```
    ```{.dart .bad-code title="Avoid"}
    final goats = List<String>.from(['Billy', 'Daisy']);
    final goatAges = Map<String, int>.from({'Billy': 2, 'Daisy': 3});
    ```

### Functional Programming Patterns

* **Embrace Functional Programming Constructs:** Take advantage of Dart’s support for first-class
  functions and higher-order functions to write cleaner and more expressive code.

    ```{.dart .good-code title="Good"}
    goats.forEach((goat) => print(goat));
    final adultGoats = goats.where((goat) => goat.age > 1).toList();
    ```
    ```{.dart .bad-code title="Avoid traditional for loops for simple iterations"}
    for (var goat in goats) {
      print(goat);
    }
    ```

### Extension Methods

* **Extend Existing Classes:** Use extension methods to add functionality to existing classes
  without modifying them or creating subclasses, keeping your codebase flexible and modular.

    ```{.dart .good-code title="Good"}
    extension GoatExtensions on Goat {
      bool get isAdult => age > 1;
    }
    
    // Usage
    if (goat.isAdult) {
      print('Goat is an adult');
    }
    ```

### Cascades

* **Use Cascades to Chain Operations:** Dart’s cascade (`..`) operator allows you to perform a
  sequence of operations on the same object. This can make your code more fluent and less verbose.

    ```{.dart .good-code title="Good"}
    final goatPen = GoatPen()
      ..add(Goat(name: 'Billy'))
      ..add(Goat(name: 'Daisy'))
      ..close();
    ```
    ```{.dart .bad-code title="Avoid"}
    final goatPen = GoatPen();
    goatPen.add(Goat(name: 'Billy'));
    goatPen.add(Goat(name: 'Daisy'));
    goatPen.close();
    ```

### Asynchronous Programming

* **Prefer async/await Over Futures:** Use `async` and `await` for handling asynchronous operations
  to write code that is clean, simple, and easy to understand.

    ```{.dart .good-code title="Good"}
    Future<void> feedAllGoats() async {
      final goats = await fetchGoats();
      for (var goat in goats) {
        await goat.feed();
      }
    }
    ```
    ```{.dart .bad-code title="Avoid using then() for complex chains of futures"}
    fetchGoats().then((goats) {
      goats.forEach((goat) {
        goat.feed().then((_) {
          // Nested then()
        });
      });
    });
    ```

### Using Generics

* **Generics for Type Safety and Flexibility:** Use generics to write flexible and reusable code
* components while maintaining type safety.

    ```dart
    class GoatList<T extends Goat> {
      final List<T> _goats = [];
    
      void add(T goat) => _goats.add(goat);
      List<T> get all => _goats;
    }
    
    // Usage
    final myGoats = GoatList<Goat>();
    myGoats.add(Goat(name: 'Billy'));
    ```

Adopting these Dart-specific idioms and patterns not only enhances code readability and efficiency
but also ensures that your Dart codebase is robust, maintainable, and idiomatic. This approach
leverages Dart’s full potential to create high-quality applications.

## Tools and Resources

Setting up a productive development environment is crucial for Dart developers. This section guides
on configuring tools and Integrated Development Environments (IDEs) to enhance productivity, ensure
code quality, and align with Dart style guidelines.

### IDE Support

#### Visual Studio Code (VS Code)

* **Extensions:** Install the Dart and Flutter (if using Flutter) extensions from the VS Code
  marketplace to get syntax highlighting, code completion, and debug support.

* **Format on Save:** Enable "Format On Save" to automatically format your code according to Dart's
  formatting rules. Go to Settings → search for "Format On Save" → check the box.

* **Problem View:** Use the Problems tab to quickly navigate and address issues identified by the
  Dart analyzer.

#### IntelliJ IDEA / Android Studio

* **Dart and Flutter Plugins:** Install the Dart and Flutter plugins via Preferences → Plugins.
  These provide comprehensive Dart support, including syntax highlighting, code completion, and
  debugging.

* **Code Style Configuration:** Configure Dart formatting in Preferences → Editor → Code Style →
  Dart. You can adjust settings to match your team’s style guide.

* **Dart Analysis:** Use the Dart Analysis window to view and navigate to issues in your codebase.
  Customize analysis options with `analysis_options.yaml`.

### Formatting Tools

* **dart format:** Use the `dart format` command to automatically format your Dart code. Integrate
  this command into your version control pre-commit hooks to ensure consistent formatting.

### Linting

* **Effective Dart:** Use the linter package to enforce Dart best practices. Customize
  your `analysis_options.yaml` to enable preferred lint rules.

```dart
include: package:lints/recommended.yaml
```

### Dependency Management

* **Pub:** Use Dart’s package manager, pub, to manage dependencies. Regularly update your
  dependencies to get the latest features and security updates.

```shell
dart pub upgrade
```

### dartfmt

Utilize `dartfmt` to automatically format your code, ensuring consistency with Dart's style guide.

### Dart Analyzer

Use the Dart Analyzer to identify potential code issues, including syntax errors, type issues, and
deprecated API usage.

### Linter

Incorporate [Dart Linter][Dart Linter] in your project to detect additional stylistic discrepancies
and potential problems.

### Additional Resources

- [Dart Language Tour][Dart Language Tour]: Offers a comprehensive overview of Dart's features and
  syntax.
- [Dart Effective Dart][Effective Dart]: Provides a set of guides for styling, authoring, and using
  Dart effectively.

[//]: # (links @formatter:off)

[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[Effective Dart]: https://dart.dev/guides/language/effective-dart
[Dart Language Tour]: https://dart.dev/guides/language/language-tour
[Dart Linter]: https://dart.dev/tools/linter-rules

[//]: # (links @formatter:on)
