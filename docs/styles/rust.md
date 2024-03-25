# Rust Style Guide

## Introduction

Welcome to the Rust Style Guide for GoatBytes.IO! This guide provides a comprehensive set of conventions, best practices, and guidelines for writing Rust code within GoatBytes.IO projects. Our goal is to establish coding standards that promote readability, maintainability, and consistency across all Rust projects.

### Purpose

The purpose of this style guide is to ensure that our Rust codebase remains clear, efficient, and scalable. By following these guidelines, developers can produce code that is not only easy to understand but also robust and adaptable to future changes. Consistent coding practices facilitate collaboration among team members and contribute to the overall quality of our software products.

### Scope

This style guide applies to all Rust code written within GoatBytes.IO, including backend services, command-line tools, and libraries. It covers various aspects of Rust programming, including formatting, naming conventions, commenting, documentation, programming practices, and language-specific idioms. Whether you're writing code for goat management systems, data processing pipelines, or networking applications, the guidelines outlined in this document are designed to be applicable and beneficial across all Rust projects at GoatBytes.IO.

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

### Indentation:

- Use four spaces for indentation. Avoid using tabs as they can be interpreted differently on various systems.
- Indent the body of a code block (e.g., following an `if` statement, inside a loop, or within a function definition) one level (four spaces) from the opening statement.
- Maintain consistent indentation throughout the code to improve readability.

### Line Length:

- Aim for a maximum line length of 100 characters. This improves readability, especially when viewing code on screens with limited width.
- Break longer lines strategically using parentheses `()`, brackets `[]`, or braces `{}` on a new line, aligning them appropriately with the previous line.
- Use judgment and consider the context when dealing with long lines. Complex expressions might benefit from staying on one line for better comprehension, while long variable declarations might be better split for readability.

### Whitespace:

- Include a space before opening curly braces `{` in function definitions, block statements (e.g., `if`, `for`, `while`), and control flow structures like `match` expressions.
- Include a space after commas in function arguments, list comprehensions, and other comma-separated structures.
- Surround binary operators (e.g., `+`, `-`, `*`, `/`, `==`) with spaces, except for unary operators like `!` and dereference `*`.
- Use spaces around the `->` operator in function signatures and closures.

### Blank Lines:

- Strategically placed blank lines can significantly enhance the readability of your code.
- Include one blank line between functions or methods within a module.
- Use one blank line to separate sections like the module declaration and use statements, before and after imports, around data structures and enum definitions, and before and after `impl` blocks.

**Example:**

```rust
// Struct representing a goat
struct Goat {
    name: String,
    hunger: u8, // 0-100 hunger level
}

// Create a new goat with a name
impl Goat {
    fn new(name: &str) -> Goat {
        Goat { name: String::from(name), hunger: 50 }
    }
}

fn main() {
    let billy = Goat::new("Billy");
    println!("{} the goat is here!", billy.name);
}
```

## Naming Conventions

Following consistent naming conventions in Rust code enhances readability, maintainability, and adherence to community standards.

### Snake_case for Items

- Use snake_case (lowercase letters with underscores separating words) for most items in Rust, including:
    - Variable names (e.g., `goat_name`, `hunger_level`)
    - Function names (e.g., `create_goat`, `calculate_happiness`)
    - Module names (e.g., `goat_management`, `util`)
    - Struct field names (e.g., `name`, `is_happy`)

### PascalCase for Types

- Use PascalCase (uppercase first letter for each word) for types in Rust, including:
    - Struct names (e.g., `Goat`, `Point`)
    - Enum names (e.g., `Emotion`, `FoodType`)
    - Trait names (e.g., `Edible`, `Printable`)

### Constants

- Use all uppercase letters with underscores separating words for constants, similar to snake_case but fully uppercase (e.g., `MAX_HUNGER_LEVEL`, `HAPPY_THRESHOLD`).

### Lifetimes

- Use single quotes (`'`) to denote lifetime parameters in function signatures and trait bounds. Descriptive lifetime names can improve readability (e.g., `'a`, `'static`).

**Additional Tips:**

- Favor clarity over brevity: Choose names that clearly convey the purpose of the item.
- Avoid abbreviations or acronyms unless they are widely understood (e.g., `HTTP`, `XML`).
- Maintain consistency throughout the codebase for a uniform style.

**Example:**

```rust
// Module for our happy herd
mod happy_herd {

  // A content goat with a happy mood
  pub struct CheerfulChewer {
    pub name: String,
    happiness: u8,  // 0-100 happiness level
  }

  // Different types of food a goat enjoys
  pub enum GoatTreat {
    CloverCrunch,
    OatmealSurprise,
    HaystackDelight,
  }

  impl CheerfulChewer {
    // Create a new CheerfulChewer with a name
    pub fn new(name: &str) -> CheerfulChewer {
      CheerfulChewer { name: String::from(name), happiness: 70 }
    }

    // Feed the goat a treat (increases happiness)
    pub fn munch(&mut self, treat: GoatTreat) {
      // ... (implementation omitted for brevity)
    }
  }
}

fn main() {
  let buttercup = happy_herd::CheerfulChewer::new("Buttercup");
  buttercup.munch(happy_herd::GoatTreat::OatmealSurprise);

  println!("{} the CheerfulChewer is enjoying a treat!", buttercup.name);
}
```

## Comments and Documentation

### Purpose and Clarity

- Clearly explain the purpose and functionality of code sections using comments.
- Avoid redundant comments that simply restate the code itself.
- Use comments to clarify non-obvious logic, complex algorithms, or design choices.

**Example:**

```rust
// This function calculates the average weight (in kilograms) of a herd of goats.
// It takes a vector of goat weights as input and returns the average weight as a float.

fn average_goat_weight(weights: &[f32]) -> f32 {
    // Ensure there are goats in the herd (avoid division by zero)
    if weights.is_empty() {
        panic!("Cannot calculate average weight for an empty herd!");
    }

    // Calculate the sum of all goat weights
    let total_weight = weights.iter().sum::<f32>();

    // Calculate the average weight by dividing the total weight by the number of goats
    total_weight / weights.len() as f32
}

// Example usage: Find the average weight of a herd with recorded weights
fn main() {
    let goat_weights = vec![35.2, 42.1, 28.7, 48.9]; // Example weights in kilograms

    let average_weight = average_goat_weight(&goat_weights);
    println!("The average weight of the goats in the herd is {:.2} kg", average_weight);
}
```

### Documentation for Public Items

- Use doc comments for public items (functions, structs, enums) to provide a detailed description, usage examples, and relevant information for future developers using the code.
- Doc comments utilize a specific syntax starting with `///`.

**Example:**

````rust
/// This structure represents a single goat in a herd.
///
/// It stores information about a goat, including its name, age, and weight.
/// This information can be used for various purposes, such as managing a farm,
/// tracking goat growth, or simply keeping track of your favorite goats.
///
#[derive(Debug)]  // Include Debug trait for easy printing
pub struct Goat {
    /// The name of the goat.
    pub name: String,

    /// The age of the goat in years.
    pub age: u32,

    /// The weight of the goat in kilograms.
    pub weight: f32,
}

/// This function calculates the average weight (in kilograms) of a herd of goats.
///
/// It takes a slice of `Goat` structs as input and returns the average weight as a float.
/// This function can be helpful for monitoring the overall health and well-being of a goat herd.
///
/// # Errors
///
/// This function panics if there are no goats in the herd (to avoid division by zero).
/// Consider using a `Result` type for more granular error handling in the future.
///
/// # Examples
///
/// ```rust
/// let herd = vec![
///     Goat { name: String::from("Billy"), age: 2, weight: 35.2 },
///     Goat { name: String::from("Beatrice"), age: 1, weight: 42.1 },
///     Goat { name: String::from("George"), age: 4, weight: 48.9 },
/// ];
///
/// let average_weight = average_goat_weight(&herd);
/// println!("The average weight of the goats in the herd is {:.2} kg", average_weight);
/// ```
///
pub fn average_goat_weight(goats: &[Goat]) -> f32 {
    // Ensure there are goats in the herd (avoid division by zero)
    if goats.is_empty() {
        panic!("Cannot calculate average weight for an empty herd!");
    }

    // Calculate the sum of all goat weights
    let total_weight = goats.iter().map(|goat| goat.weight).sum::<f32>();

    // Calculate the average weight by dividing the total weight by the number of goats
    total_weight / goats.len() as f32
}

/// Example usage: Find the average weight of a herd with recorded information for each goat
fn main() {
    let herd = vec![
        Goat { name: String::from("Billy"), age: 2, weight: 35.2 },
        Goat { name: String::from("Beatrice"), age: 1, weight: 42.1 },
        Goat { name: String::from("George"), age: 4, weight: 48.9 },
    ]; // Example herd of goats

    let average_weight = average_goat_weight(&herd);
    println!("The average weight of the goats in the herd is {:.2} kg", average_weight);
}
````

### Level of Detail

- Tailor the level of detail in comments to the complexity of the code.
- Simpler code sections might require fewer comments, while intricate logic could benefit from more explanation.

**Example:**

- A simple function does not require a comment:

```rust
fn set_name(&mut self, new_name: &str) {
  self.name = String::from(new_name);
}
```

- A more complex algorithm for calculating a goat's ideal diet might require a detailed comment:

```rust
fn calculate_ideal_diet(&self) -> Vec<FoodType> {
  // ... (complex logic considering factors like age, breed, and activity level)
}
// Detailed doc comment explaining the logic and considerations.
```

### Consistency

- Maintain consistent formatting and style for comments throughout the codebase.
- Consider using tools or linters to enforce comment style guidelines.

## Programming Practices

### Ownership and Borrowing

- Understand and leverage Rust's ownership and borrowing system, a core concept that ensures memory safety and prevents common memory-related errors.

**Example:**

```rust
fn feed_goat(goat: &mut CheerfulChewer, food: FoodType) {
  // Goat is borrowed mutably (`&mut`) to modify its happiness level
  goat.happiness += 10; // Update happiness through the borrowed reference
}
```

### Pattern Matching

- Utilize pattern matching (`match` expressions) for handling different variants of enums, iterating over collections, and destructuring complex data structures.

**Example:**

```rust
fn express_emotion(goat: &CheerfulChewer) {
  match goat.calculate_happiness() {
    Emotion::Happy => println!("{} the goat is feeling happy!", goat.name),
    Emotion::Sad => println!("{} the goat looks a bit sad.", goat.name),
    // ... (handle other variants)
  }
}
```

### Iterators and Functional Programming

- Leverage Rust's powerful iterators and functional programming features for concise and expressive code, especially when dealing with collections like lists or vectors.

**Example:**

```rust
fn suggest_favorite_foods(goat: &CheerfulChewer) -> Vec<FoodType> {
  let all_foods = [FoodType::HaystackDelight, FoodType::OatmealSurprise, FoodType::CloverCrunch];
  all_foods.iter()
    .filter(|food| *food == goat.find_favorite_food().unwrap()) // Filter based on favorite food
    .cloned() // Clone the matched food type
    .collect() // Collect results into a vector
}
```

### Error Handling with `Result`

- Employ the `Result` type (`std::error::Result`) for robust error handling. It represents an operation that can either succeed with a value or fail with an error.

**Example:**

```rust
fn find_favorite_food(goat_name: &str) -> Result<FoodType, String> {
  // ... (logic to find the goat's favorite food)
  if goat_name == "Buttercup" {
    Ok(FoodType::OatmealSurprise)
  } else {
    Err(format!("Favorite food for {} unknown!", goat_name))
  }
}
```

### Propagating and Handling Errors

- Propagate errors up the call stack when an error occurs within a function. This allows for handling the error at an appropriate level in your program.

**Example:**

```rust
fn feed_goat(goat_name: &str, food: FoodType) -> Result<(), String> {
  let favorite_food = find_favorite_food(goat_name)?; // Propagate error from find_favorite_food
  if favorite_food != food {
    Err(format!("{} the goat only eats {}", goat_name, favorite_food))
  } else {
    Ok(())
  }
}
```

### Idiomatic Rust

- Familiarize yourself with idiomatic Rust practices, which are common patterns and techniques used by experienced Rust developers. These practices promote code readability, maintainability, and performance.

**Example (Using** `Option` type):

```rust
fn get_favorite_food(goat_name: &str) -> Option<FoodType> {
  // ... (logic to find the goat's favorite food)
  Some(FoodType::OatmealSurprise)  // Return Some(value) if found
  // or None if not found
}
```

By incorporating these programming practices, you can write elegant and efficient Rust code for your goat management application, contributing to a well-structured and maintainable codebase.

## Language-Specific Idioms and Patterns

### Option Type

- Utilize the `Option` type to represent the possibility of a value being absent. This is particularly useful for handling potential errors or missing data gracefully.

**Example:**

```rust
fn get_favorite_food(goat_name: &str) -> Option<FoodType> {
  // ... (logic to find the goat's favorite food)
  Some(FoodType::OatmealSurprise)  // Return Some(value) if found
  // or None if not found
}
```

### Iterators and Functional Programming Concepts

- Leverage Rust's powerful iterators and functional programming techniques like `map`, `filter`, and `fold` to manipulate collections and data structures concisely.

**Example:**

```rust
let all_foods = [FoodType::HaystackDelight, FoodType::OatmealSurprise, FoodType::CloverCrunch];
let favorite_food = FoodType::OatmealSurprise;
let favorite_food_index = all_foods.iter().position(|food| *food == favorite_food);

match favorite_food_index {
  Some(index) => println!("Favorite food found at index {}", index),
  None => println!("Favorite food not found in the list"),
}
```

### Generics

- Employ generics to write code that works with various data types, promoting code reusability and flexibility in your goat management program.

**Example:**

```rust
fn feed_goat<T: Food>(goat: &mut CheerfulChewer, food: T) {
  // ... (logic to feed the goat, potentially adjusting happiness based on food type T)
}
```

### Smart Pointers

- Understand and utilize smart pointers like `Rc` (reference counting) or `Arc` (atomic reference counting) for managing memory ownership scenarios where multiple references to the same data are needed. Consider these for complex data structures within your goat herd.

**Example**:

```rust
use std::rc::Rc;

struct Herd {
  goats: Vec<Rc<CheerfulChewer>>, // Shared ownership of goat data
}

// ... (functions operating on the Herd with shared goat references)
```

## Tools and IDE Setup

### Tools

- **Rustup:** The Rust installer and version manager. Use `rustup` to install, update, and manage different Rust toolchain versions on your system. ([![](https://www.rust-lang.org/static/images/favicon-16x16.png)Install Rust](https://www.rust-lang.org/tools/install) )
- **Cargo:** Rust's package manager for building, testing, and distributing Rust applications. It helps manage dependencies and simplifies project structure. ([![](https://www.rust-lang.org/static/images/favicon-16x16.png)Install Rust](https://www.rust-lang.org/tools/install) )
- **Clippy:** Rust's built-in linter that catches potential issues like unused variables, ownership errors, and stylistic inconsistencies. It helps maintain clean and efficient code. ([Introduction - Clippy Documentation](https://doc.rust-lang.org/clippy/) )
- **Rustfmt:** A code formatter for Rust that ensures consistent formatting across the codebase. Consistent formatting improves readability and maintainability. ([![](https://github.com/fluidicon.png)rust/rustfmt.toml at master · rust-lang/rust](https://github.com/rust-lang/rust/blob/master/rustfmt.toml) )

### IDE Setup:

- **Visual Studio Code (VS Code):** A popular, customizable code editor with a large Rust community and extensive Rust extension support. Extensions like "Rust Analyzer" and "Rustfmt" enhance development experience. ([https://code.visualstudio.com/](https://code.visualstudio.com/ "https://code.visualstudio.com/"))
- **CLion:** A cross-platform IDE with a focus on C and C++ development, but also offers excellent Rust support. Features like code completion, debugging, and project management are available. ([![](https://www.jetbrains.com/icon-512.png?r=1234)Download CLion: A Smart Cross-Platform IDE for C and C++](https://www.jetbrains.com/clion/download/))
- **Android Studio:** If you're developing Rust code for Android, Android Studio comes with built-in Rust support. It offers integration with the Android development environment and tools. ([![](https://www.gstatic.com/devrel-devsite/prod/v6a4bae072ae9669d6217313c389216806aa75e81d1febcbc308e083db2661d8e/android/images/favicon.png)Download Android Studio & App Tools - Android Developers](https://developer.android.com/studio))
- **Rust Rover (JetBrains):** A dedicated Rust IDE from JetBrains currently in preview. It provides a feature-rich environment specifically designed for Rust development, offering code completion, refactoring, debugging, and integration with tools like Cargo and Clippy. ([![](https://www.jetbrains.com/icon-512.png?r=1234)RustRover: Rust IDE by JetBrains](https://www.jetbrains.com/rust/))

**Choosing an IDE:** The ideal IDE depends on your personal preference and workflow. VS Code is a versatile option with a large Rust community, while CLion and Android Studio offer specific features for C/C++ and Android development, respectively. Rust Rover is a promising option specifically for Rust development.

### Additional Resources:

- **The Rust Programming Language Book - Tools:** [![](https://doc.rust-lang.org/book/favicon.svg)The Rust Programming Language - The Rust Programming Language](https://doc.rust-lang.org/book/)
- **Awesome Rust - A curated list of Rust libraries, frameworks, tools, and more:** [![](https://github.com/fluidicon.png)GitHub - awesome-rust-com/awesome-rust: Awesome Rust](https://github.com/awesome-rust-com/awesome-rust)

By utilizing these tools and setting up a suitable IDE, you can efficiently write, test, and debug your goat-themed Rust program, leading to a well-structured and maintainable codebase. Remember, the Rust community is active and helpful, so don't hesitate to seek assistance if needed!
