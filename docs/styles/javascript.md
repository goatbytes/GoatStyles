# JavaScript Style Guide

## Introduction

Welcome to the JavaScript Style Guide! This comprehensive guide is designed to help developers write clean, readable, and maintainable JavaScript code. Whether you're a seasoned JavaScript developer or just starting out, adhering to consistent coding standards and best practices is essential for producing high-quality software.

### Purpose

The goal of this style guide is to enhance collaboration and code quality by establishing a consistent set of standards for code formatting, naming conventions, and programming practices. Aligning on these conventions, we aim to streamline the code review process and facilitate seamless teamwork, ultimately improving the quality of our projects.

### Scope

Developers at GoatBytes.IO, whether working on client-side or server-side JavaScript, web applications, or Node.js projects, can rely on this style guide to ensure consistency, readability, and maintainability in their codebases. It covers a wide range of topics, including formatting, naming conventions, commenting and documentation, programming practices, and language-specific idioms and patterns.

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

Effective formatting is essential in JavaScript development to ensure code readability, maintain consistency across the codebase, and adhere to best practices.

### Indentation

*   **Use 2 Spaces for Indentation**: Consistently use two spaces per indentation level to delineate hierarchical relationships in code. Avoid using tabs to maintain consistency across different editors and viewing environments.


### Line Length

*   **Maximum Line Length**: Limit lines to 100 characters. For lines exceeding this length, consider breaking them into more manageable segments, using appropriate syntax for the context (e.g., commas, operators).


### Semicolons

*   **Use Semicolons**: Terminate statements with semicolons to explicitly mark the end. This practice prevents potential pitfalls related to JavaScript's automatic semicolon insertion (ASI).


### Quotes

*   **Prefer Single Quotes**: Use single quotes for strings unless you are using template literals for interpolation or multi-line strings, in which case backticks are appropriate.

```javascript
const greeting = 'Hello, world!';
const farewell = `Goodbye,
world!`;
```


### Variable Declarations

*   **Use** `let` and `const`: Prefer `const` for variables that will not be reassigned. Use `let` for variables that will change. Avoid `var` to maintain block scope.


```javascript
const playerName = 'Billy the Kid';
let playerScore = 0; // This can change as the game progresses
```


### Whitespace

*   **Whitespace Usage**: Use whitespace to improve readability. Include spaces after keywords and before braces, and around operators.

```javascript
if (playerScore > highScore) {
  console.log('New high score!');
}
```

### Commas

*   **Leading or Trailing Commas**: Use trailing commas in multi-line objects and arrays. This practice leads to cleaner git diffs.

```javascript
const goats = [
  'Billy',
  'Daisy',
  'Spot',
];
```

### Functions

*   **Arrow Functions**: Prefer arrow functions for anonymous functions. They provide a concise syntax and lexically bind the `this` value.

```javascript
const getGoatNames = () => {
  return goats.map(goat => goat.name);
};
```

### Objects and Arrays

*   **Object Literal Syntax**: Use object literal syntax for object creation. For arrays, use the array literal syntax.

```javascript
const goat = {
  name: 'Billy',
  age: 3,
};

const goatNames = ['Billy', 'Daisy', 'Spot'];
```


### 3.10 Control Structures

*   **Braces with Control Structures**: Always use braces with `if`, `else`, `for`, `while`, and `do` statements, even if the body contains only a single statement. Place the opening brace on the same line as the control statement.

### 3.11 Blocks and Padding

*   **Blocks**: Use a space before the opening brace of blocks. Start the block on the same line as its associated statement.

```javascript
for (let i = 0; i < levels.length; i++) {
  console.log(levels[i]);
}
```

### 3.12 Comments

*   **Inline Comments**: Place inline comments above the line they refer to, and start the comment text with a space after the `//`.

```javascript
// Check if the goat is hungry before feeding
if (goat.isHungry) {
  feedGoat();
}
```

## Naming Conventions

### General Principles

*   **Descriptive Names**: Choose names that clearly describe the purpose or function of the variable, function, or class. Avoid overly generic names that do not provide insight into their use.


### Variables and Constants

*   **camelCase for Variables and Constants**: Use `camelCase` for naming variables and constants. For constants that have a static, unchanging value, use `UPPER_CASE`.

```javascript
const MAX_POWER_UPS = 5;
let availablePowerUps = ['speedBoost', 'extraLife', 'shield'];
```

### Functions

*   **Verb-Noun Pattern**: Name functions starting with a verb that describes the action followed by a noun indicating what the function acts upon. This convention clarifies the function's purpose.

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

### Classes and Constructors

*   **PascalCase for Classes**: Use `PascalCase` for classes and constructor functions. This distinguishes class constructors from regular functions.

```javascript
class GoatLeaderboard {
  constructor() {
    this.hallOfFame = [];
  }

  addGoat(goat) {
    this.hallOfFame.push(goat);
  }
}
```

### Properties and Methods

*   **camelCase for Properties and Methods**: For object properties and methods, continue to use `camelCase`. This maintains consistency across the codebase.

```javascript
const goatishDisco = {
  danceFloorCapacity: 20,
  currentGoatsDancing: 0,

  canAddGoatToDanceFloor() {
    return this.currentGoatsDancing < this.danceFloorCapacity;
  }
};
```

### Boolean Variables and Functions

*   **is/has Prefix**: Use prefixes like `is` or `has` for boolean variables and functions. These prefixes make it clear that the variable or function returns a boolean value.

```javascript
const goatyAcademy = {
  certifiedGoats: ['Billy', 'Daisy'],

  isGoatCertified(goatName) {
    return this.certifiedGoats.includes(goatName);
  }
};
```

### Handling Acronyms

*   **Capitalize Acronyms**: When using acronyms in names, capitalize them if they are at the beginning of the name. If the acronym is not at the start, only capitalize the first letter.

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


### Avoiding Abbreviations

*   **Clarity Over Brevity**: Avoid abbreviations unless they are well-known and widely understood. Full names are preferable for clarity.

```javascript
function debugHayOrder(goatInventory) {
  goatInventory.forEach(goat => {
    if (goat.hasAllergies) {
      console.log(`Adjusting diet for ${goat.name}`);
    }
  });
}
```

## Comments and Documentation

Well-documented code is as crucial as the code itself in JavaScript development, aiding maintainability, clarity, and team collaboration.

### Writing Comments

*   **Use Comments Sparingly**: Your code should be as self-explanatory as possible. Use comments to explain "why" something is done rather than "what" is done, which should be apparent from the code.

```javascript
// Adjusts course difficulty based on the goat's learning pace. This approach helps in personalizing
// the learning experience, ensuring that goats remain engaged and challenged.
function adjustCourseDifficulty(goat, pace) {
  const difficulty = pace > 5 ? 'Advanced' : 'Beginner';
  console.log(`${goat}'s course is set to ${difficulty} level.`);
}
```

*   **Inline Comments**: Place inline comments above the line of code they refer to, not at the end of the line. Start the comment with a space after the `//`.

```javascript
const bleatToBinary = {
  'baaaa': '1100',
  'maaaa': '1010'
};

// Convert goat bleat to binary code for transmission
function convertBleatToBinary(bleat) {
  return bleatToBinary[bleat] || '0000';
}
```

*   **Documentation Comments**: Use JSDoc-style comments for functions, classes, and methods. Include descriptions, parameters, returns, and any exceptions.

```javascript
/**
 * Translates a human message into GoatChat language.
 *
 * @param {string} message - The message to be translated.
 * @returns {string} The translated message in GoatChat language.
 * @throws {Error} Throws an error if the message is empty.
 */
function translateToGoatChat(message) {
  if (!message) throw new Error("Message cannot be empty.");
  // Translation logic omitted for brevity
  return "Translated message";
}
```

### Use of TODO and FIXME

*   **TODO for Future Actions**: Utilize `TODO` comments to mark places in the code that require future action, enhancement, or implementation. However, instead of leaving `TODO` comments as vague reminders, link them directly to tickets in your project’s issue tracking system whenever possible. This approach ensures that the tasks are tracked, prioritized, and not forgotten.

```javascript
// TODO: [Ticket #123] Implement dynamic playlist feature based on the current mood of goats
function generateDynamicPlaylist(mood) {
  console.log(`Generating playlist for ${mood} mood.`);
}
```

*   **FIXME for Immediate Issues**: Use `FIXME` annotations to highlight code that needs immediate attention due to bugs or significant issues affecting functionality. Like `TODO` comments, associate `FIXME` notes with tickets in your tracking system to ensure they are addressed promptly and not overlooked.

```javascript
// FIXME: [Ticket #456] Resolve issue where hay allergies are not correctly filtering hay types
function filterHayForAllergies(hayTypes, goatAllergies) {
  // Current filtering logic omitted
  console.log("Filtered hay based on allergies.");
}
```

#### Preference for Tickets

By referencing specific tickets in your project's issue or bug tracking system within `TODO` and `FIXME` comments, you create a reliable method for tracking these tasks beyond the codebase. This practice helps prevent tasks from being lost or ignored and facilitates better planning and prioritization in project management.

## Programming Practices

Effective programming practices are essential for writing clean, maintainable, and efficient JavaScript code.

### Consistent Use of `const` and `let`

*   **Immutable Variables**: Prefer `const` for all variables that do not get reassigned after initialization. Use `let` for variables that will change. This approach not only makes the code more readable but also helps in identifying variables that are meant to be immutable.

```javascript
const gameTitle = 'Goat Jump Adventure';
let currentLevel = 1;

function advanceLevel() {
  currentLevel += 1;
  console.log(`Advanced to level ${currentLevel}`);
}
```

### Error Handling

*   **Try/Catch for Asynchronous Code**: Utilize `try/catch` blocks within `async` functions to handle errors gracefully. This ensures that errors in asynchronous operations do not go uncaught.

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

*   **Pure Functions**: Whenever possible, write functions that are pure. A pure function’s output should solely depend on its input, and it should not cause side effects. This makes your code more predictable and easier to test.

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

*   **Modularization**: Break down your code into smaller, reusable modules or functions. This not only helps in organizing the code better but also facilitates easier testing and debugging.

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

*   **String Concatenation**: Prefer template literals over string concatenation for readability, especially when embedding variables or expressions within strings.

```javascript
function logGoatMessage(name, message) {
  console.log(`${name} says: ${message}`);
}

logGoatMessage('Billy', 'Baaa baaa baaa');
```

### Arrow Functions and `this`

*   **Arrow Functions**: Use arrow functions for anonymous functions or when you need to preserve the lexical value of `this`. They provide a concise syntax and are particularly useful for callbacks.

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

### Asynchronous Programming

*   **Promises and Async/Await**: Embrace the use of Promises and the async/await syntax for handling asynchronous operations. This approach leads to cleaner, more readable code compared to traditional callback patterns.

## Language-Specific Idioms and Patterns

Understanding and utilizing JavaScript's unique idioms and patterns empowers developers to write more efficient, readable, and idiomatic code.

### Destructuring for Clarity

*   **Object and Array Destructuring**: Embrace destructuring for its ability to extract multiple properties from objects or arrays succinctly, improving code clarity, especially in function parameters.

```javascript
function prepareGoatMeal({ name, favoriteSnack }) {
  console.log(`Preparing ${favoriteSnack} for ${name}.`);
}

const goatDetails = {
  name: 'Buttercup',
  favoriteSnack: 'Apples'
};

prepareGoatMeal(goatDetails);
```

### Template Literals for Dynamic Strings

*   **Leverage Template Literals**: Adopt template literals for constructing dynamic strings. Their readability and support for expression interpolation and multi-line strings make them superior to traditional string concatenation.

```javascript

function createWelcomeMessage(user, message) {
  return `Welcome ${user}! ${message}`;
}

console.log(createWelcomeMessage('BillyTheGoat', 'Ready to bleat-chat?'));

```

### Spread and Rest Operators for Flexible Collections

*   **Spread Operator for Collections**: Use the spread operator (`...`) to elegantly combine arrays, insert elements, or clone objects and arrays, thereby enhancing code flexibility and readability.

```javascript
const initialGoats = ['Billy', 'Daisy'];
const newGoats = ['Ginny', 'Clover'];

const allGoats = [...initialGoats, ...newGoats];
console.log(allGoats);
```

*   **Rest Parameters for Indefinite Arguments**: Utilize rest parameters to collect an indefinite number of arguments into an array, simplifying the handling of function arguments.

```javascript
function calculateTotalScores(...scores) {
  return scores.reduce((total, score) => total + score, 0);
}

console.log(calculateTotalScores(50, 75, 100, 120));
```

### Modules for Clean Code Organization

*   **ES6 Modules**: Structure and organize code using ES6 modules. This approach encourages clearer dependency management and modularization, contributing to a well-organized codebase.

```javascript
// goat.js
export class Goat {
  constructor(name) {
    this.name = name;
  }
}

// app.js
import { Goat } from './goat.js';
const billy = new Goat('Billy');
console.log(`New goat added: ${billy.name}`);
```

## Tools and IDE Setup

For JavaScript developers, configuring the right tools and Integrated Development Environment (IDE) setup is pivotal for enhancing productivity, ensuring code quality, and facilitating collaboration.

### Integrated Development Environments (IDEs) and Editors

*   **Visual Studio Code (VS Code)**: Highly recommended for JavaScript development due to its extensive ecosystem of extensions, built-in terminal, and Git integration. Install the ESLint extension to enforce style rules and Prettier for code formatting.

*   **WebStorm**: A powerful IDE for JavaScript, offering intelligent coding assistance, navigation tools, and advanced refactoring capabilities. WebStorm includes built-in support for modern frameworks and testing tools.

### Linting and Formatting Tools

*   **ESLint**: An indispensable tool for identifying and fixing problems in JavaScript code. Integrate ESLint into your project to enforce coding standards and catch errors early.

```shell
npm install eslint --save-dev npx eslint --init
```

*   **Prettier**: Automate code formatting to maintain consistency across your codebase. Configure Prettier to run on save in your IDE or as a pre-commit hook.

```shell
npm install --save-dev --save-exact prettier
```

### Package Management

*   **npm or Yarn**: Manage project dependencies and scripts using a package manager like npm or Yarn. These tools are essential for managing libraries, frameworks, and tools in your JavaScript project.

### Browser Developer Tools

*   **Chrome Developer Tools**: Utilize browser developer tools for debugging, performance analysis, and testing. The Chrome Developer Tools, in particular, offer a wide range of features for inspecting and debugging JavaScript in the browser.

### Task Runners and Module Bundlers

*   **Webpack**: Bundle your JavaScript applications for optimization and deployment. Webpack can transform and bundle assets, such as JavaScript, CSS, and images.

*   **Babel**: Use Babel to compile modern JavaScript code into backwards compatible versions for broader browser support.

### Continuous Integration and Deployment

*   **GitHub Actions or Travis CI**: Automate testing and deployment processes using CI tools. Set up workflows to run tests, lint code, and deploy your application automatically upon each push or pull request.
