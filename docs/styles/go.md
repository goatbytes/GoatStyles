# Go Style Guide

## Introduction

This document outlines the Go Style Guide for software development projects at GoatBytes.IO. Adherence to these guidelines promotes consistent, maintainable, and high-quality Go code across development teams. The guide details best practices for formatting, naming conventions, comments and documentation, programming practices, language-specific idioms and patterns, and tools and IDE setup. Following these guidelines ensures code readability, efficiency, and reduces the potential for errors.

## General Principles

This section outlines the overarching principles that guide your Go coding practices within the company. Adhering to these principles promotes well-structured, maintainable, and efficient Go code:

- **Readability and Maintainability:** Strive for clarity and conciseness in your code. Utilize meaningful variable and function names, proper indentation, and clear comments to enhance understanding for both yourself and others.
- **Modularity:** Organize your code effectively using well-defined packages, functions, and modules. This promotes reusability and simplifies maintenance by compartmentalizing functionalities.
- **Error Handling:** Anticipate potential errors and exceptions that might occur during program execution. Implement robust error handling mechanisms like `try-catch` blocks or error codes to gracefully handle errors and prevent unexpected program crashes.
- **Resource Management:** Manage resources like files, network connections, and memory efficiently. Open and close resources properly within their scope to avoid resource leaks and potential program crashes. Consider using RAII (Resource Acquisition Is Initialization) principles for streamlined resource management.
- **Testing:** Write unit tests to verify the functionality of individual functions and packages. This helps ensure your code behaves as expected and catches potential bugs early in the development process. Consider adopting a Go testing framework like Google Test (gtest) or Catch2 to facilitate efficient testing.

Following these general principles establishes a solid foundation for crafting high-quality Go code within your development projects.

## Formatting

Consistent formatting is essential for improving Go code readability and maintainability. This section outlines the recommended formatting conventions for your Go codebase, drawing insights from the provided resources:

### Indentation

- Use tabs for indentation. **Do not use spaces.** This ensures consistent indentation across different editors and viewers.

**Example:**

```go
func simulateGoatJump(goatName string, jumpHeight int) {
	fmt.Printf("%s jumps %d meters high!\n", goatName, jumpHeight)
}
```

### Line Length

- Aim for a maximum line length of 80 characters. This improves readability and avoids the need for horizontal scrolling.
- Break longer lines strategically using parentheses, operators, or logical breaks to enhance readability.

**Example:**

```go
package main

import (
	"fmt"
	"strings"
)

// decodeBinaryBleat takes a string of binary code (represented as goat "bleats")
// and decodes it to a textual representation for humans. It demonstrates how
// to break longer lines for readability.
func decodeBinaryBleat(bleats string) string {
	// Splitting the binary string into segments for easier processing,
	// ensuring each line stays within the 80-character limit.
	binaryWords := strings.Split(bleats, " ")
	var decodedMessage strings.Builder

	for _, word := range binaryWords {
		if word == "101" {
			decodedMessage.WriteString("Hi ")
		} else if word == "111" {
			decodedMessage.WriteString("from ")
		} else if word == "1010" {
			decodedMessage.WriteString("goats")
		}
		// Add more decoding logic here, ensuring to break lines logically.
	}

	return decodedMessage.String()
}

func main() {
	binaryBleat := "101 111 1010"
	decodedMessage := decodeBinaryBleat(binaryBleat)
	fmt.Println("Decoded Message:", decodedMessage)
}
```

The example keeps the code readable and manageable, illustrating the strategic breaking of lines to fit the recommended maximum line length.

### Spacing

- Use a single space after commas, semicolons, and colons.
- Avoid unnecessary spaces around operators (e.g., `+`, `-`, `*`, `/`).

**Example:**

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// generateDanceMoves generates a random list of dance moves for the goats at the disco.
// It showcases the proper use of spaces around commas, semicolons, and operators.
func generateDanceMoves(goatName string, moves int) []string {
	danceMoves := []string{"twist", "spin", "jump", "shuffle"}
	rand.Seed(time.Now().UnixNano())

	var goatMoves []string
	for i := 0; i < moves; i++ {
		move := danceMoves[rand.Intn(len(danceMoves))]
		goatMoves = append(goatMoves, move)
	}

	fmt.Printf("%s's dance moves: ", goatName)
	return goatMoves
}

func main() {
	goatName := "Jellybean"
	moves := generateDanceMoves(goatName, 5)
	for _, move := range moves {
		fmt.Printf("%s, ", move)
	}
}
```

### Blank Lines

- Use blank lines strategically to separate logical sections of code and improve readability. Consider adding blank lines before and after functions, loops, and conditional statements.

**Example:**

```go
package main

import "fmt"

func checkMilkSupply(goatID int, milkLiters float64) {
	if milkLiters < 10 {
		fmt.Println("Low milk supply for Goat", goatID)
	}

	fmt.Println("Supply check complete.")
}

func main() {
	checkMilkSupply(1, 8.5)
}
```

## Naming Conventions

### Packages

- Use lowercase, single-word names for packages. Avoid abbreviations or underscores unless absolutely necessary to prevent naming conflicts.

**Example:**

- `goatbytes` (preferred)
- `goat_bytes` (acceptable, but less readable)

### Variables

- Use lowercase with underscores (`snake_case`) for variable names.
- Choose descriptive names that reflect the variable's purpose or content.

**Example:**

- `goatName`
- `goatAge`
- `totalHayNeeded`
- `isHappy` (boolean variable)

### Functions

- Use lowercase with underscores for function names, adhering to snake_case.
- Function names should clearly indicate their action or the value they return.

**Example:**

- `getHappinessLevel`
- `calculateHayRequirement`
- `feedGoat`

### Types (Structs)

- Use PascalCase (first letter of each word capitalized) for struct names.
- Struct names should represent the data they encapsulate.

**Example:**

- `Goat`
- `Food`
- `Herd`

### Constants

- Use uppercase with underscores for constant names (ALL_CAPS_WITH_UNDERSCORES).
- Constants should represent their fixed value clearly.

**Example:**

- `MAX_GOAT_AGE`
- `HAY_NUTRITION_VALUE`
- `MIN_FOOD_LEVEL`

### Interfaces

- Use PascalCase with the `er` suffix for interface names, indicating their behavior.

**Example:**

- `Eater`
- `FoodProvider`

## Comments and Documentation

### Code Comments

- Use comments to explain complex logic, non-obvious code sections, or the purpose of specific functions or variables.
- Avoid redundant comments that simply restate the code itself.
- Strive for concise and informative comments that enhance understanding without being verbose.

**Example:**

```go
package main

import (
	"fmt"
	"strings"
)

// goatQuestionParser analyzes a question submitted by a goat to the "Stack Overflow for Goats"
// platform, identifying key programming concepts mentioned.
// It avoids redundancy by explaining the logic behind keyword extraction, not what each line of code does.
func goatQuestionParser(question string) []string {
	keywords := []string{"graze", "bleat", "code"}
	var foundKeywords []string

	// Split the question into words for individual analysis.
	for _, word := range strings.Fields(question) {
		for _, keyword := range keywords {
			if strings.Contains(word, keyword) {
				foundKeywords = append(foundKeywords, keyword)
			}
		}
	}

	return foundKeywords
}

func main() {
	question := "How do I bleat in code?"
	foundKeywords := goatQuestionParser(question)

	fmt.Println("Keywords found:", foundKeywords)
}
```

### Package Documentation

- Utilize Go's built-in package comments (godoc) to document your packages.
- Provide a concise description of the package's purpose and functionality.
- Include details about exported functions, types, and variables within the package.

**Example:**

```go
// Package goatyacademy offers a collection of tutorials and exercises for goats
// learning programming. It includes lessons on Go basics, debugging techniques,
// and advanced concepts like concurrency. Exported functions support interactive
// learning and progress tracking.
```

### API Documentation

- Consider using tools like Swagger or Martini to generate API documentation if your Go program exposes functionalities through an API.
- This documentation should clearly explain API endpoints, request parameters, response formats, and error handling mechanisms.

## Programming Practices

### Error Handling

- Implement robust error handling to gracefully manage unexpected situations that might occur during program execution.
- Utilize techniques like returning errors from functions and checking for errors before proceeding. Consider using Go's built-in `error` interface for consistent error handling.

**Example:**

```go
package main

import (
	"errors"
	"fmt"
)

// simulateGoatJump attempts to simulate a goat's jump and returns an error if the jump height is unrealistic.
func simulateGoatJump(height int) error {
	if height > 10 { // Assume the maximum realistic jump height is 10 units.
		return errors.New("height exceeds realistic goat jump capabilities")
	}
	fmt.Println("Goat jump simulated successfully.")
	return nil
}

func main() {
	err := simulateGoatJump(12)
	if err != nil {
		fmt.Println("Error:", err)
	}
}
```

### Memory Management

- Go handles memory management automatically through garbage collection. However, understanding memory allocation principles can optimize performance.
- Avoid creating unnecessary copies of large data structures or holding onto unused objects for extended periods.

**Example:**

```go
type Herd struct {
  goats []*Goat // Use pointers to goats to avoid copying entire goat structs
}

func (h *Herd) AddGoat(goat *Goat) {
  h.goats = append(h.goats, goat)
}
```

### Concurrency (if applicable)

- If the project involves concurrency, utilize Go's concurrency primitives like goroutines and channels effectively.
- Manage concurrency carefully to avoid race conditions and ensure data consistency. Consider using synchronization mechanisms like mutexes when necessary.

**Example:**

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// simulateGoatDance simulates a single goat dancing on the dance floor using a goroutine.
func simulateGoatDance(goatName string) {
	fmt.Printf("%s starts dancing...\n", goatName)
	time.Sleep(2 * time.Second) // Simulate dance time.
	fmt.Printf("%s stops dancing.\n", goatName)
}

func main() {
	var wg sync.WaitGroup
	goatNames := []string{"Billy", "Daisy", "Ginny"}

	for _, name := range goatNames {
		wg.Add(1)
		// Start a new goroutine for each goat's dance.
		go func(goatName string) {
			defer wg.Done()
			simulateGoatDance(goatName)
		}(name)
	}

	wg.Wait() // Wait for all goroutines to finish.
	fmt.Println("All goats have finished dancing.")
}
```

**Note:** This example demonstrates a basic use case of goroutines. Concurrency can be complex, so ensure a thorough understanding of Go's concurrency features before implementing them in your project.

### Unit Testing

- Write unit tests to verify the functionality of individual functions and packages. This helps ensure your code behaves as expected and catches potential bugs early in the development process.
- Utilize a Go testing framework like `testing` or `testify` to streamline the testing process.

**Example:**

```go
package main

import (
	"fmt"
	"testing"
)

// teachGoatCoding simulates teaching coding to a goat.
func teachGoatCoding(goatName string, language string) string {
	return fmt.Sprintf("%s has learned %s!", goatName, language)
}

func TestTeachGoatCoding(t *testing.T) {
	expected := "Billy has learned Go!"
	result := teachGoatCoding("Billy", "Go")
	if result != expected {
		t.Errorf("Expected %s, got %s", expected, result)
	}
}
```

## Go-Specific Idioms and Patterns

### Pointers and Dereferencing

- Go allows passing by value and by reference using pointers. Utilize pointers effectively to modify data structures within functions and avoid unnecessary copies of large objects.

**Example:**

```go
package main

import "fmt"

// Goat represents a character in the game.
type Goat struct {
	Name  string
	Score int
}

// increaseScore uses a pointer to modify the Goat's score.
func increaseScore(g *Goat, points int) {
	g.Score += points
}

func main() {
	billy := Goat{Name: "Billy", Score: 10}
	increaseScore(&billy, 5)
	fmt.Printf("%s's new score: %d\n", billy.Name, billy.Score)
}
```

### Interfaces

- Interfaces define a set of behaviors that a type must implement. Utilize interfaces to promote code flexibility and allow different types to fulfill the same role (e.g., various food types can implement an `Edible` interface).

**Example:**

```go
package main

import "fmt"

// Edible defines behavior for food items that can be consumed by goats.
type Edible interface {
	Eat()
}

// Hay is a type of food that can be eaten by goats.
type Hay struct{}

func (h Hay) Eat() {
	fmt.Println("Hay is being eaten.")
}

// Treat is another type of food for goats.
type Treat struct{}

func (t Treat) Eat() {
	fmt.Println("Treat is being eaten.")
}

func feedGoat(e Edible) {
	e.Eat()
}

func main() {
	hay := Hay{}
	treat := Treat{}

	feedGoat(hay)
	feedGoat(treat)
}
```

### Slices and Maps

- Go offers slices (dynamically sized arrays) and maps (key-value pairs) for efficient data storage and retrieval. Utilize slices to manage collections of goats within your herd and maps for storing goat attributes that might not be common to all (e.g., favorite toys).

**Example:**

```go
package main

import "fmt"

func main() {
	// Slice of goat names attending the disco.
	goatNames := []string{"Billy", "Daisy", "Ginny"}

	// Map to store each goat's favorite dance move.
	favoriteMoves := map[string]string{
		"Billy": "Twist",
		"Daisy": "Shuffle",
		"Ginny": "Spin",
	}

	for _, name := range goatNames {
		fmt.Printf("%s's favorite move: %s\n", name, favoriteMoves[name])
	}
}
```

### Channels

- Channels facilitate communication between goroutines. Utilize channels to coordinate feeding schedules or manage communication between different parts of the program that operate concurrently.

**Example:**

```go
package main

import (
	"fmt"
	"time"
)

// sendMessage simulates sending a message through a channel.
func sendMessage(ch chan<- string, message string) {
	time.Sleep(2 * time.Second) // Simulate delay.
	ch <- message
}

func main() {
	messageChannel := make(chan string)
	go sendMessage(messageChannel, "Lesson 1 completed")
	message := <-messageChannel
	fmt.Println("Received:", message)
}
```

### Error Handling with `defer`

- The `defer` statement allows you to execute a function after the surrounding function finishes (regardless of normal execution or errors). Utilize `defer` to ensure resources are properly closed or cleanup tasks are performed even if errors occur.

**Example:**

```go
package main

import (
	"fmt"
	"os"
)

// processOrder simulates processing an order and uses defer for cleanup.
func processOrder(filename string) error {
	f, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer f.Close() // Ensure the file is closed even if an error occurs.

	// Process the order here.
	fmt.Println("Processing order from", filename)
	return nil
}

func main() {
	err := processOrder("order.txt")
	if err != nil {
		fmt.Println("Error:", err)
	}
}
```

## Tools and IDE Setup

### Essential Tools

- **Go Toolchain:** The Go toolchain, including the `go` command, is essential for compiling, running, and testing your Go programs. Download and install the Go toolchain from the official website for your operating system: [https://go.dev/doc/install](https://go.dev/doc/install)
- **Code Editor or IDE:** Choose a code editor or IDE that provides features and functionalities specifically suited for Go development. Here are some popular options:
- **GoLand:** A commercial IDE by JetBrains specifically designed for Go development. It offers advanced features like code completion, refactoring, debugging, and integration with various testing frameworks. ([https://www.jetbrains.com/go/](https://www.jetbrains.com/go/))
- **Visual Studio Code (VS Code):** A free, open-source code editor by Microsoft with extensive customization options and support for various programming languages, including Go. You can install extensions like Go extension pack to enhance Go development functionalities within VS Code. ([https://code.visualstudio.com/](https://code.visualstudio.com/ "https://code.visualstudio.com/"))

### Additional Tools

- **Static Code Analysis Tools:** Tools like `go fmt`, `golint`, and `staticcheck` can help identify formatting issues, potential errors, and code smells within your Go program.
- **Debuggers:** Utilize a debugger like Delve (command-line) or the integrated debugger within your IDE to step through your code line by line, inspect variables, and identify issues during program execution.
