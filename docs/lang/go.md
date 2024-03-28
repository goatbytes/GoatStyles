# Go Style Guide

This document outlines best practices and coding conventions for Go (Golang), aiming to foster code
that is clean, readable, maintainable, and idiomatic to the Go programming language.

[//]: # (@formatter:off)
/// admonition |
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for Go.
///
[//]: # (@formatter:on)

## Formatting

While our foundational [formatting standards][FORMATTING] provide comprehensive formatting
guidelines, you should also use `gofmt` to ensure consistency across all Go code.

- **Indentation:** `gofmt` uses tabs for indentation. **Do not use spaces.**
- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Braces:** Opening braces are placed on the same line.
- **Blank Lines:** Use 1 line to separate code sections.
- **Alignment:** Align elements in documentation comments and parameter lists.

## Naming Conventions

Adhere to the foundational [naming conventions][NAMING]:

- **PascalCase** for classes, protocols, and enumeration types
- **camelCase** for methods, variables, and properties.
  - Prefix booleans with `is` or `has` for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

In addition, adhere to Go's naming convention recommendations:

- **Local Variables:** Short, but descriptive names. Single letter names are common for small scopes
- **Acronyms:** Keep acronyms in uppercase. For example, use `HTTPRequest` instead of `HttpRequest`.
- **Exported Identifiers:** Start with an uppercase letter to make them public.
- **Receiver Names:** Keep receiver variable names short and consistent across methods.

## Commenting and Documentation

### Godoc

Godoc comments should precede package and public declarations. They should be complete sentences
that describe the purpose and usage of the package or identifier.

```{.go title="Example"}
// Package goatyacademy offers a collection of tutorials and exercises for goats
// learning programming. It includes lessons on Go basics, debugging techniques,
// and advanced concepts like concurrency. Exported functions support interactive
// learning and progress tracking.
```

### Inline Comments

Inline comments should be used sparingly, only when necessary to explain complex logic or decisions
that aren't obvious.

### API Documentation

* Consider using tools like [Swagger](https://swagger.io/) to generate API documentation if your Go
  program exposes functionalities through an API.
* This documentation should clearly explain API endpoints, request parameters, response formats, and
  error handling mechanisms.

## Idioms and Best Practices

### Pointers

Use pointers to modify an original value or to avoid copying large structures. However, use them
judiciously as they can complicate the code's understanding.

```{.go title="Example"}
package main

import "fmt"

// Goat represents a character in the game.
type Goat struct {
    Name  string
    Score int
}

// IncreaseScore increases the score of a Goat by the given number of points.
// The Goat's score is modified in place using a pointer receiver.
func IncreaseScore(g *Goat, points int) {
    g.Score += points
}

func main() {
    billy := Goat{Name: "Billy", Score: 10}
    IncreaseScore(&billy, 5) // Demonstrates how to use a pointer receiver to modify a struct's field.
    fmt.Printf("%s's new score: %d\n", billy.Name, billy.Score)
}

```

### Goroutines and Channels

Embrace Go's concurrency model using goroutines and channels for parallel execution paths. Keep
synchronization and data sharing simple to maintain readability and performance.

```{.go title="Example"}
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

### Interfaces

Define small, focused interfaces, preferably with one or two methods. This approach promotes modular
design and flexible integration of components.

```{.go title="Example"}
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

### Error Handling with `defer`

* The `defer` statement allows you to execute a function after the surrounding function finishes (
  regardless of normal execution or errors). Utilize `defer` to ensure resources are properly closed
  or cleanup tasks are performed even if errors occur.

**Example:**

```{.go title="Example"}
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

### Slices and Maps

* Go offers slices (dynamically sized arrays) and maps (key-value pairs) for efficient data storage
  and retrieval. Utilize slices to manage collections of goats within your herd and maps for storing
  goat attributes that might not be common to all (e.g., favorite toys).

```{.go title="Example"}
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

## Tools and Resources

### Essential Tools

* **[Go Toolchain](https://go.dev/doc/install)** The Go toolchain, including the `go` command, is
  essential for compiling, running, and testing your Go programs.
* **[GoLand](https://www.jetbrains.com/go/):** A commercial IDE by JetBrains specifically designed
  for Go development. It offers advanced features like code completion, refactoring, debugging, and
  integration with various testing frameworks.
* **[Visual Studio Code](https://code.visualstudio.com/) (VS Code):** A free, open-source code
  editor by Microsoft with extensive customization options and support for various programming
  languages, including Go. You can install extensions like Go extension pack to enhance Go
  development functionalities within VS Code.

### Static Analysis Tools

* [**Staticcheck**](https://staticcheck.io/) is a static analysis tool that helps you write better
  Go code by flagging errors, bugs, stylistic issues, and simplifications.

### Additional Resources

- [Effective Go](https://golang.org/doc/effective_go.html): Offers tips for writing clear, idiomatic
  Go code.
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments): A collection of
  common comments made during reviews of Go code.

[//]: # (links @formatter:off)

[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments
[gofmt]: https://pkg.go.dev/cmd/gofmt
[Staticcheck]: https://staticcheck.io/
[Effective Go]: https://golang.org/doc/effective_go.html
[Go Code Review Comments]: https://github.com/golang/go/wiki/CodeReviewComments

[//]: # (links @formatter:on)
