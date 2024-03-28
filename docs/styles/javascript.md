# JavaScript Style Guide

This guide focuses on best practices and conventions for writing clean, understandable, and
maintainable JavaScript code. It emphasizes adherence to contemporary JavaScript standards and
practices while also incorporating unique aspects of JavaScript programming.

[//]: # (@formatter:off)
/// admonition | 
    type: abstract
[Foundational Code Standards][fnd]{:target="_blank"} provide the foundation, this guide extends them for JavaScript.
///
[//]: # (@formatter:on)

## Formatting

The formatting guidelines for JavaScript adhere to our
[Foundational Code Standards][fnd-formatting]. Here is a brief overview:

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

/// details | Formatted JavaScript Example Code
type: example

```javascript
class Example {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  performOperations() {
    const inner = new Inner();
    inner.display();

    const sum = this.x + this.y; // Space around operators
    console.log(`Sum: ${sum}`);

    // Ternary operator with spaces
    const message = sum > 10 ? 'Greater than 10' : 'Not greater than 10';
    console.log(message);

    // If-else with spacing and brace style
    if (sum % 2 === 0) {
      console.log('Sum is even');
    } else {
      console.log('Sum is odd');
    }

    // For loop demonstrating continuation indent
    for (let i = 0; i < 5; i++) {
      process.stdout.write(`${i} `); // Demonstrate space in concatenation
    }
    console.log(); // New line after loop

    // Try-catch-finally block
    try {
      throw new Error('Demo exception');
    } catch (e) {
      console.log(`Caught exception: ${e.message}`);
    } finally {
      console.log('Finally block executed');
    }
  }

  // Inner class
  static innerClass() {
    class Inner {
      display() {
        console.log('Inside Inner class');
      }
    }

    return Inner;
  }
}

// Using the inner class functionality
const Inner = Example.innerClass();

function main() {
  const example = new Example(3, 7);
  example.performOperations();
}

main();
```
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

## Commenting and Documentation

### Inline Comments

* **Clarity**: Use inline comments sparingly and only when they add significant value or
  clarification to the code.
* **Placement**: Place inline comments on the same line as the statement they refer to, separated by
  at least two spaces from the code, followed by a `#` and a single space before the comment text.

```{.javascript title="Example"}
feed_time = True # Goats are fed at sunrise and sunset
```

### JSDoc for Documentation

Use [JSDoc](https://jsdoc.app/) to document function signatures, class definitions, and module
interfaces. This aids in understanding the structure and intended use of your code.

### Use Verb-Noun Naming for Functions

* **Verb-Noun Pattern**: Name functions starting with a verb that describes the action followed by a
  noun indicating what the function acts upon. This convention clarifies the function's purpose.

```javascript
function translateToGoat(message) {
  const emojiDictionary = {
    happy: '😊🐐',
    food: '🌿',
    play: '🐾🐐'
  };
  return message.split(' ').map(word => emojiDictionary[word] || word).join(' ');
}
```

### Handling Acronyms

* **Capitalize Acronyms**: When using acronyms in names, capitalize them if they are at the
  beginning of the name. If the acronym is not at the start, only capitalize the first letter.

```javascript
function decodeBLEGTMessage(blegtCode) {
  // B.L.E.G.T: Binary Language Encoding for Goat Transmission
  const bleatDictionary = {
    '1100': 'baaaa',
    '1010': 'maaaa',
    '1111': 'baaa-bleet'
  };

  const message = bleatDictionary[blegtCode] || 'unknown transmission';
  console.log(`Decoded B.L.E.G.T message: ${message}`);
}

decodeBLEGTMessage('1100');
```

### Use of TODO and FIXME

* **TODO for Future Actions**: Utilize `TODO` comments to mark places in the code that require
  future action, enhancement, or implementation. However, instead of leaving `TODO` comments as
  vague reminders, link them directly to tickets in your project’s issue tracking system whenever
  possible. This approach ensures that the tasks are tracked, prioritized, and not forgotten.

```javascript
// TODO: [Ticket #123] Implement dynamic playlist feature based on the current mood of goats
function generateDynamicPlaylist(mood) {
  console.log(`Generating playlist for ${mood} mood.`);
}
```

* **FIXME for Immediate Issues**: Use `FIXME` annotations to highlight code that needs immediate
  attention due to bugs or significant issues affecting functionality. Like `TODO` comments,
  associate `FIXME` notes with tickets in your tracking system to ensure they are addressed promptly
  and not overlooked.

```javascript
// FIXME: [Ticket #456] Resolve issue where hay allergies are not correctly filtering hay types
function filterHayForAllergies(hayTypes, goatAllergies) {
  // Current filtering logic omitted
  console.log("Filtered hay based on allergies.");
}
```

#### Preference for Tickets

By referencing specific tickets in your project's issue or bug tracking system within `TODO`
and `FIXME` comments, you create a reliable method for tracking these tasks beyond the codebase.
This practice helps prevent tasks from being lost or ignored and facilitates better planning and
prioritization in project management.

## Idioms and Best Practices

Understanding and utilizing JavaScript's unique idioms and patterns empowers developers to write
more efficient, readable, and idiomatic code.

### Arrow Functions

* **Arrow Functions and `this`**: Use arrow functions for anonymous functions or when you need to
  preserve the lexical value of `this`. They provide a concise syntax and are particularly useful
  for callbacks.

    ```javascript
    const goatClass = {
      students: ['Billy', 'Daisy', 'Goatee'],
      className: 'Intro to Grazing',
      printStudents() {
        this.students.forEach(student => {
          console.log(`${student} is enrolled in ${this.className}.`);
        });
      }
    };
    ```

### Consistent Use of `const` and `let`

* **Immutable Variables**: Prefer `const` for all variables that do not get reassigned after
  initialization. Use `let` for variables that will change. This approach not only makes the code
  more readable but also helps in identifying variables that are meant to be immutable.

    ```javascript
    const gameTitle = 'Goat Jump Adventure';
    let currentLevel = 1;
    
    function advanceLevel() {
      currentLevel += 1;
      console.log(`Advanced to level ${currentLevel}`);
    }
    ```

### Error Handling

* **Try/Catch for Asynchronous Code**: Utilize `try/catch` blocks within `async` functions to handle
  errors gracefully. This ensures that errors in asynchronous operations do not go uncaught.

    ```javascript
    async function sendMessage(message) {
      try {
        await chatService.send(message);
        console.log('Message sent successfully');
      } catch (error) {
        console.error('Failed to send message', error);
      }
    }
    ```

### Function Purity

* **Pure Functions**: Whenever possible, write functions that are pure. A pure function’s output
  should solely depend on its input, and it should not cause side effects. This makes your code more
  predictable and easier to test.

    ```javascript
    // Calculates the next song to play based on the goat's current mood.
    // This is a pure function as it only depends on its input and has no side effects.
    function nextSong(mood) {
      const moodToSong = {
        happy: 'Barnyard Dance',
        sad: 'Goat Blues',
        energetic: 'Hoof Stomper'
      };
      return moodToSong[mood] || 'Chewin\' on Grass';
    }
    ```

### Modular Code

* **Modularization**: Break down your code into smaller, reusable modules or functions. This not
  only helps in organizing the code better but also facilitates easier testing and debugging.

    ```javascript
    // Modular function to add a goat to the leaderboard
    function addToLeaderboard(leaderboard, goat) {
      leaderboard.push(goat);
      leaderboard.sort((a, b) => b.score - a.score);
    }
    
    // Modular function to display the leaderboard
    function displayLeaderboard(leaderboard) {
      console.log('GOAT Leaderboard:');
      leaderboard.forEach((goat, index) => {
        console.log(`${index + 1}. ${goat.name} - ${goat.score}`);
      });
    }
    ```

### Use of Template Literals

* **String Concatenation**: Prefer template literals over string concatenation for readability,
  especially when embedding variables or expressions within strings.

    ```javascript
    function logGoatMessage(name, message) {
      console.log(`${name} says: ${message}`);
    }
    
    logGoatMessage('Billy', 'Baaa baaa baaa');
    ```

### Asynchronous Programming

* **Promises and Async/Await**: Embrace the use of Promises and the async/await syntax for handling
  asynchronous operations. This approach leads to cleaner, more readable code compared to
  traditional callback patterns.

### Destructuring for Clarity

* **Object and Array Destructuring**: Embrace destructuring for its ability to extract multiple
  properties from objects or arrays succinctly, improving code clarity, especially in function
  parameters.

    ```javascript
    function prepareGoatMeal({name, favoriteSnack}) {
      console.log(`Preparing ${favoriteSnack} for ${name}.`);
    }
    
    const goatDetails = {
      name: 'Buttercup',
      favoriteSnack: 'Apples'
    };
    
    prepareGoatMeal(goatDetails);
    ```

### Template Literals for Dynamic Strings

* **Leverage Template Literals**: Adopt template literals for constructing dynamic strings. Their
  readability and support for expression interpolation and multi-line strings make them superior to
  traditional string concatenation.

    ```javascript
    
    function createWelcomeMessage(user, message) {
      return `Welcome ${user}! ${message}`;
    }
    
    console.log(createWelcomeMessage('BillyTheGoat', 'Ready to bleat-chat?'));
    ```

### Spread and Rest Operators for Flexible Collections

* **Spread Operator for Collections**: Use the spread operator (`...`) to elegantly combine arrays,
  insert elements, or clone objects and arrays, thereby enhancing code flexibility and readability.

    ```javascript
    const initialGoats = ['Billy', 'Daisy'];
    const newGoats = ['Ginny', 'Clover'];
    
    const allGoats = [...initialGoats, ...newGoats];
    console.log(allGoats);
    ```

    * **Rest Parameters for Indefinite Arguments**: Utilize rest parameters to collect an indefinite
      number of arguments into an array, simplifying the handling of function arguments.

      ```javascript
      function calculateTotalScores(...scores) {
        return scores.reduce((total, score) => total + score, 0);
      }
    
      console.log(calculateTotalScores(50, 75, 100, 120));
      ```

## Tools and IDE Setup

For JavaScript developers, configuring the right tools and Integrated Development Environment (IDE)
setup is pivotal for enhancing productivity, ensuring code quality, and facilitating collaboration.

### Integrated Development Environments (IDEs) and Editors

* **[Visual Studio Code](https://code.visualstudio.com/) (VS Code)**: Highly recommended for
  JavaScript development due to its extensive ecosystem of extensions, built-in terminal, and Git
  integration. Install the ESLint extension to enforce style rules and Prettier for code formatting.

* **[WebStorm](https://www.jetbrains.com/webstorm/)**: A powerful IDE for JavaScript, offering
  intelligent coding assistance, navigation tools, and advanced refactoring capabilities. WebStorm
  includes built-in support for modern frameworks and testing tools.

### Linting and Formatting Tools

* **[ESLint](https://github.com/eslint/eslint)**: An indispensable tool for identifying and fixing
  problems in JavaScript code. Integrate ESLint into your project to enforce coding standards and
  catch errors early.

    ```{.shell .copy}
    npm install eslint --save-dev npx eslint --init
    ```

* **[Prettier](https://github.com/prettier/prettier)** is an opinionated code formatter that
  supports many languages, including JavaScript. It enforces a consistent style by parsing your code
  and reprinting it with its own rules.

    ```{.shell .copy}
    npm install --save-dev --save-exact prettier
    ```

### Package Management

* **[npm](https://www.npmjs.com/) or [Yarn](https://yarnpkg.com/)**: Manage project dependencies and
  scripts using a package manager like npm or Yarn. These tools are essential for managing
  libraries, frameworks, and tools in your JavaScript project.

### Task Runners and Module Bundlers

* **[Webpack](https://github.com/webpack/webpack)**: Bundle your JavaScript applications for
  optimization and deployment. Webpack can transform and bundle assets, such as JavaScript, CSS, and
  images.

* **[Babel](https://github.com/babel/babel)**: Use Babel to compile modern JavaScript code into
  backwards compatible versions for
  broader browser support.

### Additional Resources

* **[Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)**: A comprehensive guide
  to writing cleaner JavaScript code.
* **[MDN Web Docs](https://developer.mozilla.org)**: An invaluable resource for learning about
  JavaScript features, APIs, and best practices.

[//]: # (@formatter:off)
[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[Roslyn]: https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview
[//]: # (@formatter:on)
