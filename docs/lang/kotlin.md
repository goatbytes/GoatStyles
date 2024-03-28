# Kotlin Style Guide

This guide specifically addresses Kotlin development, focusing on idiomatic practices, patterns, and
Kotlin-specific considerations.

[//]: # (@formatter:off)
/// admonition |
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for Kotlin.
///
[//]: # (@formatter:on)

## Formatting

Adhere to the foundational [formatting stadards][FORMATTING]:

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
    Remember, these are guidelines; adapt them for your project's needs while keeping readability in
    focus.
    ///

/// details | Formatted Kotlin Example Code
    type: example

```kotlin
/**
 * This class demonstrates proper code formatting following the specified style guide.
 *
 * **Formatting Rules:**
 * - 2 spaces for indentation.
 * - 4 spaces for continuation lines.
 * - Max line length of 100 characters.
 * - Spaces around operators, control structures, and keywords.
 * - K&R brace style.
 * - Consistent spacing for parameter lists and constructor arguments.
 * - Doc comments with aligned descriptions.
 */
class WellFormattedCode { // (1)!

  /**
   * This method calculates the factorial of a given positive integer. // Doc comment for method
   *
   * @param n The non-negative integer for which to calculate the factorial.
   * @return  The factorial of n, or throws an IllegalArgumentException if n is negative.
   * @throws IllegalArgumentException If the provided number (n) is negative.
   */
  fun calculateFactorial(n: Int): Long { // (2)!
    if (n < 0) { // (3)!
      throw IllegalArgumentException("Factorial is not defined for negative numbers.")
    }

    var result = 1L
    for (i in 2..n) {  // (4)!
      result *= i
    }
    return result
  }
}
```

1.    Class name in PascalCase with a doc comment.
2.    Method name in camelCase with a doc comment.
3.    K&R brace style for blocks.
4.    Proper spacing around operators and control structures.

///
[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for Kotlin adhere to our foundational [naming conventions][NAMING]
with no exceptions.

- **PascalCase** for classes, interfaces, enums (definitions).
- **camelCase** for functions, variables, properties.
    - Prefix booleans with `is` or `has` for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

/// tab | Good

```{.kotlin .good-code title="Correct Usage"}
// Class following PascalCase for a data definition
class Goat {
    // Variable following camelCase for a property
    var isHappy = true

    // Function following camelCase with descriptive name
    fun eatGrass(amount: Int) {
        println("The goat munches on $amount kg of grass")
    }

    // Function with UPPER_SNAKE_CASE for a constant
    companion object {
        const val MAX_SPEED = 40 // km/h
    }
}
```

///
/// tab | Bad

```{.kotlin .bad-code title="Incorrect Usage"}  
// Inconsistent naming (should be Goat)
class goat {

  // Unclear variable name
  var happy = true

  // Unnecessary abbreviation in function name
  fun eat(amt: Int) {
    println("The goat munches on $amt kg of grass") // Should use descriptive variable 'amount'
  }

  // Unclear function name
  fun isHealthy(g: goat): String {
    val msg = if (g.happy) {
      "Goat happy!"
    } else {
      "Goat might be sick!"
    }
    return msg
  }

  companion object {
    // should be UPPER_SNAKE_CASE
    const val maxSpeed = 40 // km/h
  }
}

// Mixed naming convention (should be snake_case or camelCase)
fun PrintGoatInfo(goat: goat) {
    println("Goat is Happy: ${goat.happy}") // Should be isHappy
    println("Goat Max Speed: ${goat.maxSpeed}") // Should be MAX_SPEED
}
```

///

## Documentation and Comments

Refer to the [Foundational Code Standards][DOCS] for general commenting and documentation
guidelines.

#### Documentation Example

[//]: # (@formatter:off)

```kotlin
/**
 * Represents a goat with a name, age, and a method to determine if the goat is happy.
 * 
 * This data class simplifies the process of creating goat objects with essential attributes
 * and provides a method to assess the goat's happiness based on specific conditions.
 *
 * **Usage Example:**
 * `
 * val billy = Goat("Billy", 5)
 * println(billy.isHappy(3)) // Prints true or false depending on the number of meals.
 * `
 * 
 * @property name The name of the goat.
 * @property age The age of the goat in years.
 * @constructor Creates a goat object with the specified name and age.
 * @throws IllegalArgumentException if the age is negative.
 * @return A new instance of a Goat.
*/
data class Goat(val name: String, val age: Int) {
  init {
    if (age < 0) throw IllegalArgumentException("Age cannot be negative")
  }

  /**
   * Determines if the goat is happy based on the number of meals it has received.
   * 
   * A goat is considered happy if it has been fed at least twice a day.
   * 
   * @param meals The number of meals the goat has received today.
   * @return True if the goat is happy (fed at least twice today), false otherwise.
   * @throws IllegalArgumentException if the number of meals is negative.
   */
  fun isHappy(meals: Int): Boolean {
    if (meals < 0) throw IllegalArgumentException("Meals cannot be negative")
    return meals >= 2
  }
}
```

#### KDoc

Use [KDoc][KDoc] for documenting classes, functions, and properties.

#### Dokka

Use [Dokka][Dokka], an API documentation generator, for automatic documentation in various formats.

## Idioms and Best Practices

Kotlin offers a wealth of idiomatic practices and patterns that can make your code more concise,
readable, and idiomatic. This section focuses on leveraging Kotlin's unique features effectively.

### Collections and Ranges

Use Kotlin's standard library functions for collection manipulation.

```kotlin
val adultGoats = goats.filter { it.age >= 2 }.map { it.name }
```

### Null Safety

Utilize Kotlin's null safety features like `?.`, `?:`, and `!!` operators judiciously.

```kotlin
val name: String? = goat.getName()
println(name?.length ?: "No name")
```

### Lazy Initialization

Delegate property initialization to be calculated only when accessed for the first time.

```kotlin
class GoatTracker {
    private val numGoatsFed: Int by lazy {
        // This code to count goats is executed only on first access
        countGoatsInPen()
    }

    private fun countGoatsInPen(): Int {
        return 10 // Simulate counting goats
    }
}
```

### Data Classes

Use data classes for holding data. They provide `equals()`, `hashCode()`, `toString()`, `copy()`,
and `componentN()` functions automatically.

```kotlin
data class Goat(val name: String, val age: Int)
```

### Default Values

Assign default values to constructor parameters or function parameters for optional arguments.

```kotlin
class Goat(val name: String = "Billy", var age: Int = 1) {
    fun yell(sound: String = "Meeee!"): String {
        return "$name the goat yells: $sound"
    }
}

val myGoat = Goat() // Uses default name ("Billy") and age (1)
val grumpyGoat = Goat("Grumpy", 5, "Baaaaaah!") // Custom name, age, and sound
```

### Operator Overloading

Overload operators for custom classes using functions named after the operator.

```kotlin
data class Age(val years: Int) {
  operator fun plus(yearsToAdd: Int): Age {
    return Age(years + yearsToAdd)
  }
}

val goatAge = Age(2)
val olderGoatAge = goatAge + 3
```

[//]: (@formatter:on)

### Extension Functions

Add new functions to existing classes without inheritance.

```kotlin
fun String.addGoatEmoji(): String = "$this 🐐"
```

### Scope Functions

Use `apply`, `with`, `run`, `also`, and `let` for executing a block of code within the context of an
object.

```kotlin
val billy = Goat("Billy", 1).apply { age = 2 }
```

### String Interpolation

Embed expressions within strings using ${expression} syntax for dynamic string creation.

```kotlin
val goatName = "Buttercup"
val message = "The goat $goatName is ${if (myGoat.age > 3) "old" else "young"}."
```

### Instance Checks

Use `is` and `!is` operators for type checks and smart casts. Use `as?` for safe casts.

```kotlin
fun feed(animal: Any) {
  if (animal is Goat) {
    val goat = animal as Goat  // Safe cast if it's a Goat
    println("Feeding grass to ${goat.name}")
  } else {
    println("This animal doesn't eat grass!")
  }
}
```

## Tools and Resources

Ensuring a consistent development environment and utilizing static analysis tools are crucial steps
for maintaining high code quality in Kotlin projects.

### Recommended Static Analysis Tools for Kotlin

Static analysis tools help identify potential issues early in the development process. For Kotlin,
several tools are particularly effective:

* [**detekt**](https://detekt.dev/): A static code analysis tool for Kotlin that provides code style
  checks, complexity
  checks, and more. It is configurable and integrates well with Gradle and Maven.
* [**ktlint**](https://pinterest.github.io/ktlint/latest/): An anti-bikeshedding Kotlin linter with
  built-in formatter. It enforces a consistent
  code style and can automatically format code per the Kotlin coding standards.
* [**SonarQube for Kotlin**][SonarQube]: Extends SonarQube's capabilities to Kotlin, offering code
  smells
  detection, bugs tracking, and code quality metrics.
* [**Android Lint**][AndroidLint]: For Android projects, Android Lint includes specific checks for
  Kotlin code,
  ensuring best practices for Android development are followed.

### Additional Resources

* [**Kotlin Coding Conventions**][CodingConventions]: The official coding conventions for Kotlin by
  JetBrains.
* [**Android Kotlin Style Guide**][AndroidKotlinGuide]: The official style guide for Android
  development in Kotlin.
* [**Awesome Kotlin**][AwesomeKotlin]: A curated list of Kotlin resources, libraries, and tools.

### IntelliJ IDEA Configuration

To align with the coding standards outlined in this guide, we provide a custom IntelliJ IDEA code
style configuration. This configuration ensures that your IDE automatically adheres to the
formatting rules and conventions specified herein.

/// tab | EditorConfig

1. Download the .editorconfig.
2. Open IntelliJ IDEA.
3. Go to `File` > `Settings` (on Windows and Linux) or `IntelliJ IDEA` > `Preferences` (on macOS).
4. Navigate to `Editor` > `Code Style`.
5. Ensure the checkbox for Enable EditorConfig support is :checked: checked.
6. Rename the downloaded file to `.editorconfig`.
6. Add the `.editorconfig` file to your project root directory.

[EditorConfig File &nbsp;:fontawesome-solid-download:][JB_EDITORCONFIG]{ .md-button .md-button--primary }

///
/// tab | XML Config

1. Download the XML config file.
2. Open IntelliJ IDEA.
3. Go to `File` > `Settings` (on Windows and Linux) or `IntelliJ IDEA` > `Preferences` (on macOS).
4. Navigate to `Editor` > `Code Style`.
5. Click on the gear icon (`⚙️`) next to the `Scheme` dropdown at the top of the window and
   select `Import Scheme` > `IntelliJ IDEA code style XML`.
6. Find and select the downloaded XML file, then click `OK`.
7. Ensure the newly imported scheme is selected in the `Scheme` dropdown.
8. Click `Apply` and `OK` to save the changes.

[IntelliJ XML Config &nbsp;:fontawesome-solid-download:][JB_XML]{ .md-button .md-button--primary }

///

By configuring your IDE to adhere to Kotlin's style conventions and integrating static analysis
tools into your development process, you can significantly enhance code quality, readability, and
maintainability. These tools not only help catch potential bugs early but also ensure your codebase
remains clean and consistent with Kotlin best practices.

[//]: # (links @formatter:off) 

[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments
[KDoc]: https://kotlinlang.org/docs/kotlin-doc.html
[Dokka]: https://kotlinlang.org/docs/dokka-introduction.html
[Detekt]: https://deteky.dev
[Ktlint]: https://pinterest.github.io/ktlint/latest/
[SonarQube]: https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/languages/kotlin/
[AndroidLint]: https://developer.android.com/studio/write/lint
[JB_XML]: ../assets/files/kotlin-jetbrains.xml
[JB_EDITORCONFIG]: ../assets/files/kotlin.editorconfig
[CodingConventions]: https://kotlinlang.org/docs/coding-conventions.html
[AwesomeKotlin]: https://github.com/mcxiaoke/awesome-kotlin
[AndroidKotlinGuide]: https://developer.android.com/kotlin/style-guide

[//]: # (links @formatter:on)