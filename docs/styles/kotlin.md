# Kotlin Style Guide
## Introduction

Welcome to our Kotlin Style Guide. This document is crafted to guide developers through Kotlin projects, ensuring code remains clean, maintainable, efficient, and consistent. Designed to support both new endeavors and ongoing work, this guide aims for high-quality contributions that are easy to integrate and understand, fostering seamless collaboration and elevating project standards.

### Purpose

The goal of this style guide is to enhance collaboration and code quality by establishing a consistent set of standards for code formatting, naming conventions, and programming practices. Aligning on these conventions, we aim to streamline the code review process and facilitate seamless teamwork, ultimately improving the quality of our projects.

### Scope

This guide is intended for developers engaged in various Kotlin projects. The recommendations are crafted to be broadly applicable, ensuring relevance across different Kotlin development contexts.

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

Proper formatting is essential for maintaining code readability and consistency. This section highlights key points with adjustments for our specific needs in Kotlin.

### Indentation

*   **Indent**: 2 spaces for a new block level.
*   **Continuation indent**: 2 spaces for line continuations.

### Whitespace

*   **Before parentheses**: Include a space before an opening parenthesis for control flow statements (`if`, `when`, `for`, and `while`).
*   **Operators**: Include spaces around operators (e.g., `=`, `+`, `-`), except for unary and range operators (`..`).
*   **After commas**: Include a space after commas.
*   **After colon**: Include a space after a colon in type declarations.
*   **Before and after colon in new type definitions**: Include a space before and after the colon.
*   **Around arrow in "when" clause and function types**: Include spaces around the `->`.
*   **Before lambda arrow**: Include a space before `->` in lambda expressions.

### Blank Lines

*   **Declarations**: Use 1 blank line between declarations within a class or object.
*   **In code**: Use 1 blank line to separate logical code blocks.
*   **Before '}'**: No blank line before closing braces.

**Kotlin Formatting Example:**

```kotlin
class GoatishDisco {

  private val playlist = mutableListOf<String>()
  private var danceFloorCapacity = 10
  private val goatsOnDanceFloor = mutableListOf<String>()

  fun addSong(song: String) {
    playlist.add(song)
  }

  fun admitGoat(goatName: String): Boolean {
    return if (goatsOnDanceFloor.size < danceFloorCapacity) {
      println("$goatName joins the dance floor!")
      goatsOnDanceFloor.add(goatName)
      true
    } else {
      println("Sorry, $goatName! The dance floor is full.")
      false
    }
  }

  fun startParty() {
    if (playlist.isEmpty()) {
      println("Can't start the party without music!")
      return
    }
    if (goatsOnDanceFloor.isEmpty()) {
      println("No goats on the dance floor yet.")
      return
    }
    println("Let's get this party started!")
    playlist.forEach { song ->
      println("Now playing: $song")
    }
  }
}

fun main() {
  val disco = GoatishDisco()
  disco.addSong("Baaa Baaa Black Sheep")
  disco.addSong("Hoofin' Beats")

  disco.admitGoat("Billy")
  disco.admitGoat("Daisy")
  disco.startParty()
}
```

## Naming Conventions

Consistent naming conventions enhance code readability and maintainability by making it easier for developers to understand the structure and purpose of the code at a glance.

### Classes and Interfaces

*   **Convention**: CamelCase, starting with an uppercase letter.
*   **Rationale**: Classes and interfaces represent entities or concepts; thus, their names should be nouns or noun phrases.
*   **Example**: `Goat`, `GoatHerd`, `GoatFeeder`

### Functions

*   **Convention**: camelCase, starting with a lowercase letter.
*   **Rationale**: Functions perform actions, so their names should be verbs or verb phrases.
*   **Example**: `feedGoats`, `calculateGoatHappiness`, `retrieveGoatByName`

### Properties and Variables

*   **Local Variables and Instance Fields**: camelCase, starting with a lowercase letter. Descriptive, conveying the meaning directly.
*   **Constants**: ALL\_CAPS with underscores separating words.
*   **Rationale**: Variable names should clearly indicate their purpose or value.
*   **Example**: `goatCount`, `MAX_GOATS_ALLOWED`

```kotlin
private const val MAX_GOATS_ALLOWED = 100
private var goatCount
```

### Enums

*   **Convention**: Enums can be named using CamelCase (PascalCase), starting with an uppercase letter for types. Enum constants should use ALL\_CAPS with underscores separating words.
*   **Rationale**: Enums represent fixed sets of constants. Allowing PascalCase for enum types gives flexibility in naming conventions, aligning with the naming of classes and interfaces, while the ALL\_CAPS convention for enum constants clearly distinguishes them as fixed values.

**Example:**

```kotlin
enum class GoatSounds(val sound: String) {
  BLEAT("Bleat"),
  MAA_MAA("MaaMaa"),
  BAA("Baa"),
  NAA("Naa");
}

// Alternative PascalCase usage: 
enum class GoatSounds {
  Bleat, MaaMaa, Baa, Naa;
}
```

## Commenting and Documentation

Effective commenting and comprehensive documentation are crucial for maintaining code quality, facilitating maintenance, and ensuring codebase accessibility for both new and existing developers.

### Commenting Code

**Purpose and Clarity**: Comments should clarify the purpose of the code, explaining "why" something is done, not just "what" is done. Avoid redundant comments.
**Keep Comments Updated**: As the code evolves, ensure comments reflect the current functionality. Outdated comments can be more misleading than no comments.

```kotlin
// Convert goat bleat to binary code for transmission
function convertBleatToBinary(bleat) {
  return bleatToBinary[bleat] || '0000';
}
```

### Documentation Comments

**Classes and Interfaces**: At the beginning of each class and interface, provide a summary describing its purpose and role within the application.
**Functions**: Document every function, including a description of its behavior, parameters, return values, and any exceptions thrown.
**KDoc Conventions**: Use KDoc tags (`@param`, `@return`, `@throws`, `@property`) to describe function signatures and class properties. Use `[ClassName]` for code references and related classes or methods.

**Example**

```kotlin
/**
 * Represents a translator for converting binary sequences into goat bleats,
 * allowing for customizable mappings between binary codes and goat communications.
 *
 * @param bleatMap A map of binary sequences to corresponding goat bleats.
 *                 Provides a default mapping but can be customized upon instantiation.
 */
class BinaryBleatTranslator(
  private val bleatMap: Map<String, String> = mapOf(
    "101" to "Hello",
    "010" to "Feed me",
    "111" to "Play time"
  )
) {

  /**
   * Translates a binary sequence into a goat's bleat.
   * If the binary code does not have a direct mapping in the bleatMap,
   * the function returns "Unknown bleat" to indicate an unmapped code.
   *
   * @param binaryCode The binary sequence to be translated.
   * @return The corresponding goat bleat or "Unknown bleat" if the code is not mapped.
   */
  fun translate(binaryCode: String): String = bleatMap[binaryCode] ?: "Unknown bleat"
}
```

### Inline Comments

**Use Sparingly**: Inline comments are intended for complex code segments where the logic's purpose or action isn't immediately clear from the code itself.
**Location**: Place inline comments on the line above the code segment they describe, not at the end of the line of code.

```kotlin
// Calculate the optimal feeding time based on the goat's current activity level
val feedingTime = calculateFeedingTime(goat.activityLevel)
```

### Documentation for Public APIs

**Comprehensive Coverage**: Every public class, function, and property should be documented, providing clear insights into the component's purpose, use, and behavior.

### TODOs and FIXMEs

**Ticket-Based Tracking Preferred**: Utilize a ticket-based tracking system for managing tasks and issues highlighted by `TODO` and `FIXME` comments.
**Include Ticket Numbers**: Always include the corresponding ticket number from your project's issue tracking system when using `TODO` or `FIXME` comments.

```kotlin
// TODO: [TICKET-33] Implement a method to add new binary-to-bleat mappings to the bleatMap.
// FIXME: [BLEAT-757] Address edge cases where binaryCode might be an empty string or null.
```

## Programming Practices

Adopting effective programming practices in Kotlin not only improves code quality but also leverages Kotlin's powerful features to write concise, readable, and efficient code.

### Null Safety

Kotlin's type system is designed to eliminate the danger of null references from code.

**Best Practice**: Utilize Kotlin's null safety features like `?.`, `?:`, and `!!` operators judiciously.

**Example**:

```kotlin
val name: String? = goat.getName()
println(name?.length ?: "No name")
```

### Data Classes

Kotlin's data classes simplify the creation of classes that primarily serve to hold data.

**Best Practice**: Use data classes when you need classes to hold data. They automatically generate `equals()`, `hashCode()`, `toString()`, `copy()`, and `componentN()` functions.

**Example**:

```kotlin
data class Goat(val name: String, val age: Int)
```

### Extension Functions

Extension functions allow you to add new functions to existing classes without inheritance.

**Best Practice**: Use extension functions to add utility functions to classes without modifying their code.

**Example**:

```kotlin
fun String.addGoatEmoji(): String = "$this 🐐"
```

### Collections and Ranges

Kotlin provides a rich set of operators for working with collections and ranges, making operations more concise and readable.

**Best Practice**: Use Kotlin's standard library functions for collection manipulation instead of traditional loops.

**Example**:

```kotlin
val goats = listOf(Goat("Billy", 3), Goat("Daisy", 1), Goat("Snow", 2))
val adultGoats = goats.filter { it.isAdult() }.map { it.name }
println("Adult goats: $adultGoats")
```

### Scope Functions: `apply`, `with`, `run`, `also`, `let`

Kotlin's scope functions (`apply`, `with`, `run`, `also`, `let`) are powerful tools that execute a block of code within the context of an object.

**Best Practice**: Choose the appropriate scope function based on the operation being performed and the desired result.

*   Use `apply` and `also` for object configuration and additional side effects, respectively, returning the context object.
*   Use `let`, `with`, and `run` for executing a block of code that computes a result, with `let` and `run` returning the lambda result and `with` being called on an instance as an argument.

**Examples**:

*   `apply` - for object configuration:

```kotlin
val billy = Goat("Billy", 1).apply {
  age = 2 // Billy had a birthday
}
```

*   `also` - for additional operations:

```kotlin
val newGoat = Goat("Lucy", 0).also {
  println("${it.name} just joined the herd!")
}
```

*   `let` - for operations on the result of a call chain:

```kotlin
getGoatName()?.let { name ->
  println("The goat's name is $name")
} ?: println("Name not available.")
```

*   `with` - for calling multiple methods on an object:

```kotlin
with(goats.first()) {
  println("The first goat is $name and is $age years old.")
}
```

*   `run` - for executing a block of code and returning the result:

```kotlin
val goatDetails = billy.run {
  "Goat's Name: $name, Age: $age"
}
println(goatDetails)
```

## Language-Specific Idioms and Patterns

Kotlin offers a wealth of idioms and patterns that can make your code more concise, readable, and idiomatic. This section highlights some of those practices, drawing from Kotlin's official documentation, coding conventions, and established community style guides.

### Utilize String Interpolation

**Best Practice**: Use string interpolation to insert variables into strings, rather than string concatenation.

**Example**:

```kotlin
val goatName = "Billy"
println("The goat's name is $goatName.")
```

### Leverage Type Inference

**Best Practice**: Let Kotlin infer the type of a variable or return type of a function where possible, rather than specifying it explicitly.

**Example**:

```kotlin
val herdSize = 10  // Int inferred
fun getGoatNames() = listOf("Billy", "Daisy")  // List<String> inferred
```

### Use Default and Named Arguments

**Best Practice**: Utilize default parameters and named arguments to reduce the number of overloaded functions and improve function call readability.

**Example**:

```kotlin
fun feedGoat(name: String, foodAmount: Int = 5) {
  println("Feeding $name with $foodAmount kg of food.")
}

feedGoat(name = "Billy", foodAmount = 10)
feedGoat(name = "Daisy") // List<String> inferred
```

### Use Coroutines for Asynchronous Programming

**Best Practice**: Adopt coroutines for managing background tasks and asynchronous operations in a more efficient and simpler way than traditional concurrency mechanisms like threads.

**Example**:

```kotlin
suspend fun getGoatDetails(id: Int): GoatDetails {
  return withContext(Dispatchers.IO) { // Perform network request on IO thread
    // Simulate network request
    GoatDetails(id, "Billy")
  }
}
```

### Favor Immutability

**Best Practice**: Use `val` over `var` where possible to make your variables immutable. Immutable objects are easier to reason about, less prone to errors, and more thread-safe.

**Example**:

```kotlin
val goatNames = listOf("Billy", "Daisy")  // Immutable list
```

### Use Sealed Classes for Type Hierarchies

**Best Practice**: Use sealed classes to represent restricted class hierarchies, where a value can have one of the types from a limited set, but cannot have any other type.

**Example**:

```kotlin
sealed class GoatBehavior {
  class Learning(val skill: String) : GoatBehavior()
  class Socializing(val peer: String) : GoatBehavior()
  object Mischief : GoatBehavior()
  object NapTime : GoatBehavior()
}

class GoatEducator {
  fun observeBehavior(goatName: String, behavior: GoatBehavior) {
    when (behavior) {
      is GoatBehavior.Learning -> println("$goatName is learning ${behavior.skill}.")
      is GoatBehavior.Socializing -> println("$goatName is socializing with ${behavior.peer}.")
      GoatBehavior.Mischief -> println("Uh-oh! $goatName is causing mischief.")
      GoatBehavior.NapTime -> println("$goatName is taking a nap. Shh!")
    }
  }
}

fun main() {
  val educator = GoatEducator()
  educator.observeBehavior("Billy", GoatBehavior.Learning("climbing"))
  educator.observeBehavior("Daisy", GoatBehavior.Socializing("Ginny"))
  educator.observeBehavior("Ginny", GoatBehavior.Mischief)
  educator.observeBehavior("Clover", GoatBehavior.NapTime)
}
```

## Tools and IDE Setup

Ensuring a consistent development environment and utilizing static analysis tools are crucial steps for maintaining high code quality in Kotlin projects. This section outlines the setup for development tools and recommends static analysis tools specifically useful for Kotlin development.

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

### Recommended Static Analysis Tools for Kotlin

Static analysis tools help identify potential issues early in the development process. For Kotlin, several tools are particularly effective:

*   **detekt**: A static code analysis tool for Kotlin that provides code style checks, complexity checks, and more. It is configurable and integrates well with Gradle and Maven.
*   **ktlint**: An anti-bikeshedding Kotlin linter with built-in formatter. It enforces a consistent code style and can automatically format code per the Kotlin coding standards.
*   **SonarQube with Kotlin plugin**: Extends SonarQube's capabilities to Kotlin, offering code smells detection, bugs tracking, and code quality metrics.
*   **Android Lint**: For Android projects, Android Lint includes specific checks for Kotlin code, ensuring best practices for Android development are followed.

By configuring your IDE to adhere to Kotlin's style conventions and integrating static analysis tools into your development process, you can significantly enhance code quality, readability, and maintainability. These tools not only help catch potential bugs early but also ensure your codebase remains clean and consistent with Kotlin best practices.