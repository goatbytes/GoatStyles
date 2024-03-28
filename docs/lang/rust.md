# Rust Style Guide

This guide focuses on best practices and stylistic conventions for writing Rust code, aiming for
code that is not only efficient and safe but also clean, readable, and consistent.

[//]: # (@formatter:off)
/// admonition | 
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for Rust.
///
[//]: # (@formatter:on)

## Formatting

The formatting rules for Rust adhere to our [Foundational Formatting Standards][FORMATTING] with the
following exceptions:

- **Indentation:** Use 4 spaces per indentation level.

Otherwise, follow the conventions outlined in the foundational standards, summarized below:

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

- **UpperCamelCase (PascalCase)** for types (classes, structs, enums), and enum variants.
- **snake_case** for function and method names, local variables, struct fields, macro names, and
  properties.
- **SCREAMING_SNAKE_CASE** for constants (consts and immutable statics).
- **lowercase** for package names, using concatenated words (avoid underscores).
- Use a **raw identifier** (`r#`) or **trailing underscore** for names that are reserved words.

**Additional Tips:**

* Favor clarity over brevity: Choose names that clearly convey the purpose of the item.
* Avoid abbreviations or acronyms unless they are widely understood (e.g., `HTTP`, `XML`).
* Maintain consistency throughout the codebase for a uniform style.

## Commenting and Documentation

### Purpose and Clarity

* Clearly explain the purpose and functionality of code sections using comments.
* Avoid redundant comments that simply restate the code itself.
* Use comments to clarify non-obvious logic, complex algorithms, or design choices.

    ```{.rust title="Example"}
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

* Use doc comments for public items (functions, structs, enums) to provide a detailed description,
  usage examples, and relevant information for future developers using the code.
* Doc comments utilize a specific syntax starting with `///`.

    ```{.rust title="Example"}
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
    ```

### Level of Detail

* Tailor the level of detail in comments to the complexity of the code.
* Simpler code sections might require fewer comments, while intricate logic could benefit from more
  explanation.

    /// tab | Simple Function
    ```rust
    fn set_name(&mut self, new_name: &str) {
        self.name = String::from(new_name);
    }
    ```
    ///
    /// tab | Complex Function
    ```rust
    fn calculate_ideal_diet(&self) -> Vec<FoodType> {
        // ... (complex logic considering factors like age, breed, and activity level)
    }
    // Detailed doc comment explaining the logic and considerations.
    ```
    ///

### Consistency

* Maintain consistent formatting and style for comments throughout the codebase.
* Consider using tools or linters to enforce comment style guidelines.

## Best Practices and Idioms

### Ownership and Borrowing

* Understand and leverage Rust's ownership and borrowing system, a core concept that ensures memory
  safety and prevents common memory-related errors.

    ```{.rust title="Example"}
    fn feed_goat(goat: &mut CheerfulChewer, food: FoodType) {
        // Goat is borrowed mutably (`&mut`) to modify its happiness level
        goat.happiness += 10; // Update happiness through the borrowed reference
    }
    ```

### Pattern Matching

* Utilize pattern matching (`match` expressions) for handling different variants of enums, iterating
  over collections, and destructuring complex data structures.

    ```{.rust title="Example"}
    fn express_emotion(goat: &CheerfulChewer) {
        match goat.calculate_happiness() {
            Emotion::Happy => println!("{} the goat is feeling happy!", goat.name),
            Emotion::Sad => println!("{} the goat looks a bit sad.", goat.name),
            // ... (handle other variants)
        }
    }
    ```

### Iterators and Functional Programming

* Leverage Rust's powerful iterators and functional programming features for concise and expressive
  code, especially when dealing with collections like lists or vectors.

    ```{.rust title="Example"}
    fn suggest_favorite_foods(goat: &CheerfulChewer) -> Vec<FoodType> {
        let all_foods = [FoodType::HaystackDelight, FoodType::OatmealSurprise, FoodType::CloverCrunch];
        all_foods.iter()
            .filter(|food| *food == goat.find_favorite_food().unwrap()) // Filter based on favorite food
            .cloned() // Clone the matched food type
            .collect() // Collect results into a vector
    }
    ```

### Error Handling with `Result`

* Employ the `Result` type (`std::error::Result`) for robust error handling. It represents an
  operation that can either succeed with a value or fail with an error.

    ```{.rust title="Example"}
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

* Propagate errors up the call stack when an error occurs within a function. This allows for
  handling the error at an appropriate level in your program.

    ```{.rust title="Example"}
    fn feed_goat(goat_name: &str, food: FoodType) -> Result<(), String> {
        let favorite_food = find_favorite_food(goat_name)?; // Propagate error from find_favorite_food
        if favorite_food != food {
            Err(format!("{} the goat only eats {}", goat_name, favorite_food))
        } else {
            Ok(())
        }
    }
    ```

### Option Type

* Utilize the `Option` type to represent the possibility of a value being absent. This is
  particularly useful for handling potential errors or missing data gracefully.

    ```{.rust title="Example"}
    fn get_favorite_food(goat_name: &str) -> Option<FoodType> {
        // ... (logic to find the goat's favorite food)
        Some(FoodType::OatmealSurprise)  // Return Some(value) if found
        // or None if not found
    }
    ```

### Iterators and Functional Programming Concepts

* Leverage Rust's powerful iterators and functional programming techniques like `map`, `filter`,
  and `fold` to manipulate collections and data structures concisely.

    ```{.rust title="Example"}
    let all_foods = [FoodType::HaystackDelight, FoodType::OatmealSurprise, FoodType::CloverCrunch];
    let favorite_food = FoodType::OatmealSurprise;
    let favorite_food_index = all_foods.iter().position(|food| *food == favorite_food);
    
    match favorite_food_index {
        Some(index) => println!("Favorite food found at index {}", index),
        None => println!("Favorite food not found in the list"),
    }
    ```

### Generics

* Employ generics to write code that works with various data types, promoting code reusability and
  flexibility in your goat management program.

    ```{.rust title="Example"}
    fn feed_goat<T: Food>(goat: &mut CheerfulChewer, food: T) {
        // ... (logic to feed the goat, potentially adjusting happiness based on food type T)
    }
    ```

### Smart Pointers

* Understand and utilize smart pointers like `Rc` (reference counting) or `Arc` (atomic reference
  counting) for managing memory ownership scenarios where multiple references to the same data are
  needed. Consider these for complex data structures within your goat herd.

    ```{.rust title="Example"}
    use std::rc::Rc;
    
    struct Herd {
        goats: Vec<Rc<CheerfulChewer>>, // Shared ownership of goat data
    }
    
    // ... (functions operating on the Herd with shared goat references)
    ```

## Tools and Resources

### IDEs

* [RustRover | JetBrains IDE](https://www.jetbrains.com/rust/)
* [Visual Studio Code](https://code.visualstudio.com/)
    * [Prettier - Code formatter (Rust)](https://marketplace.visualstudio.com/items?itemName=jinxdash.prettier-rust) — Opinionated Rust code formatter that autofixes bad syntax ([Prettier](https://prettier.io/) community plugin)
    * [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) — An alternative rust language server to the RLS

### Formatters

* [rustfmt](https://github.com/rust-lang/rustfmt) — Rust code formatter maintained by the Rust team and included in cargo
* [dprint](https://github.com/dprint/dprint) — A pluggable and configurable code formatting platform
* [Prettier Rust](https://github.com/jinxdash/prettier-plugin-rust) — An opinionated Rust code formatter that autofixes bad syntax ([Prettier](https://prettier.io/) community plugin)

### Development Tools

* [bacon](https://github.com/Canop/bacon) — background rust code checker, similar to cargo-watch
* [clippy](https://crates.io/crates/clippy) — Rust lints
* [geiger](https://github.com/geiger-rs/cargo-geiger) — A program that list statistics related to usage of unsafe code in a crate and all its dependencies
* [hot-lib-reloader](https://github.com/rksm/hot-lib-reloader-rs) — Hot reload Rust code
* [Racer](https://github.com/racer-rust/racer) — code completion for Rust
* [Rustup](https://github.com/rust-lang/rustup) — the Rust toolchain installer

### Additional Resources

- [The Rust Programming Language][Rust Book]: The official book, an excellent resource for learning
  Rust.
- [Rust API Guidelines][Rust API Guidelines]: A set of Rust API design considerations.
- [Rust Style Guide][Rust Style Guide]: Official Rust style guide for code formatting and
  conventions.
- [Rust by Example][Rust by Example]: A collection of runnable examples that illustrate various Rust
  concepts and standard libraries.

[//]: # (links @formatter:off)

[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments
[Rust Book]: https://doc.rust-lang.org/book/
[Rust API Guidelines]: https://rust-lang.github.io/api-guidelines/
[Rust by Example]: https://doc.rust-lang.org/rust-by-example/
[Rust Style Guide]: https://doc.rust-lang.org/nightly/style-guide/index.html

[//]: # (links @formatter:on)
