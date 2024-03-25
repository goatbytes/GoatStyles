# TypeScript Style Guide
## Introduction

Welcome to the TypeScript Style Guide, a comprehensive resource tailored for developers engaged in crafting modern web applications, backend services, and libraries with TypeScript. As a superset of JavaScript, TypeScript introduces static typing, enabling developers to write more robust and maintainable code. This guide aims to establish a set of coding standards and best practices that leverage TypeScript's features to their fullest potential.

### Purpose

The objective of this style guide is to promote code quality, enhance readability, and facilitate collaboration across TypeScript projects. By adhering to these guidelines, developers can ensure consistent code formatting, naming conventions, and programming practices, leading to a codebase that is easier to understand, debug, and extend.

### Scope

This guide is intended for developers working on a wide array of TypeScript projects. Whether you are developing client-side applications with frameworks like Angular, React, or Vue.js, building server-side applications with Node.js, or creating reusable libraries and packages, the practices outlined in this document are designed to be broadly applicable. By following this guide, TypeScript developers can create high-quality, scalable, and maintainable applications and libraries, contributing to the overall success of their projects and the wider TypeScript community.

## General Principles

The foundation of our TypeScript Style Guide is rooted in general principles that promote excellence in software development. These principles are designed to guide developers in creating TypeScript code that is not only high quality but also consistent, maintainable, and efficient.

### Clarity and Simplicity

*   **Strive for Readability:** Write code as if the next person to maintain it has just started programming in TypeScript. Code should be easily understandable, avoiding unnecessary complexity.

### Consistency

*   **Adhere to Established Patterns:** Consistency in coding style and practices across the codebase facilitates collaboration and code review processes. Follow established patterns and conventions within the TypeScript community and your specific project.

### Type Safety

*   **Leverage TypeScript’s Type System:** Maximally utilize TypeScript’s static typing capabilities to catch errors at compile time, making your code more robust and maintainable.

### Scalability and Maintainability

*   **Code for the Future:** Write code with future expansion and maintenance in mind. Favor patterns and structures that make it easy to add new features and fix bugs.

### Efficiency

*   **Balance Performance and Readability:** While performance is important, it should not compromise the code's readability or maintainability. Optimize only when necessary, and prefer clear, maintainable code for complex logic.

### DRY (Don't Repeat Yourself)

*   **Avoid Redundancy:** Aim to write reusable code. Avoid repeating code blocks by utilizing functions, classes, and TypeScript features like generics and modules to encapsulate reusable logic.

### Testing

*   **Emphasize Testing:** Write unit tests for your code to ensure reliability and facilitate refactoring. Use TypeScript’s features, like types and interfaces, to mock dependencies and write comprehensive tests.

### Documentation

*   **Document Your Code:** Use comments and TypeScript’s JSDoc support to document your code. Well-documented interfaces, types, functions, and classes make your codebase more accessible to new developers and your future self.

### Collaborative Development

*   **Code as a Team:** Recognize that software development is a team effort. Write code that is easy to understand, review, and integrate into the larger codebase. Engage in code reviews and discussions to collectively improve the code quality.

### Embracing Modern Features

*   **Stay Up to Date:** TypeScript is continually evolving. Stay informed about new features and improvements in the language, and incorporate them where appropriate to improve your code’s safety and expressiveness.

## Formatting

Proper formatting in TypeScript is crucial for maintaining readability and consistency throughout the codebase. This section outlines the formatting rules and principles for TypeScript development, focusing on line length, indentation, whitespace, and syntax conventions, tailored around the engaging topic of goats.

### Line Length

*   **Maximum Line Length:** Aim to limit lines to a maximum of 120 characters. This helps ensure readability across various environments and devices.

```typescript
// Good 
const goatNames = ['Billy', 'Daisy', 'Spot'].map(name => `${name} the Goat`);

// Avoid 
const goatNames = ['Billy', 'Daisy', 'Spot'].map(name => `This is ${name}, and they are one of the best goats in the barn!`);
```

### Indentation

*   **Spaces for Indentation:** Use 2 spaces per indentation level. This keeps the code visually aligned and consistent across different editors.

```typescript
// Good
if (goat.isHungry) {
    feedGoat(goat);
}

// Avoid using tabs or different number of spaces
if (goat.isHungry) {
    feedGoat(goat);
}
```

### Whitespace

*   **Strategic Use of Whitespace:** Use whitespace around operators and after commas to enhance readability. Also, avoid extra spaces inside parentheses and brackets.

```typescript
// Good 
const totalFeed = goatFeed + barnFeed; 

// Avoid 
const totalFeed=goatFeed+barnFeed;
```

### Semicolons

*   **Consistent Use of Semicolons:** Use semicolons to terminate statements, maintaining consistency and preventing potential pitfalls in code execution.

```typescript
// Good
const goatName = 'Billy';
feedGoat(goatName);

// Avoid missing semicolons
const goatName = 'Billy'
feedGoat(goatName)
```

### Trailing Commas

*   **Use Trailing Commas in Multi-line Constructs:** This practice makes it easier to add new lines to the list and improves the clarity of version control diffs.

```typescript
// Good
const goats = [
    'Billy',
    'Daisy',
    'Spot',
];

// Avoid in multi-line constructs
const goats = [
    'Billy',
    'Daisy',
    'Spot'
];
```

### Braces

*   **K&R Style for Braces:** Place the opening brace on the same line as the statement and the closing brace on its own line.

```typescript
// Good
if (goat.isHungry) {
    feedGoat(goat);
} else {
    letGoatGraze();
}

// Avoid
if (goat.isHungry)
{
    feedGoat(goat);
}
else
{
    letGoatGraze();
}
```

### Quotes

*   **Prefer Single Quotes:** Use single quotes for string literals for consistency unless you are writing JSON or the string contains single quotes.

```typescript
// Good
const goatName = 'Billy';

// Avoid using double quotes where not necessary
const goatName = "Billy";
```

By adhering to these formatting guidelines, TypeScript codebases become more readable, maintainable, and consistent across different development environments. This encourages better collaboration and code quality in projects involving the delightful subject of goats or any other theme.

## Naming Conventions

Adopting clear and consistent naming conventions is essential in TypeScript development, as it enhances code readability, facilitates maintenance, and ensures codebase consistency. This section outlines the principles and rules for naming variables, functions, classes, interfaces, and other identifiers in TypeScript, illustrated with examples themed around goats.

### Variables and Constants

*   **Use CamelCase:** Variables and constants should be named using camelCase. For constants that act as hard-coded values, UPPER\_SNAKE\_CASE can be used.

```typescript
// Good
let goatCount = 5;
const MAX_GOATS = 100;

// Avoid
let GoatCount = 5;
const maxGoats = 100;
```

### Functions

*   **Descriptive Names:** Function names should be clear and descriptive, using camelCase. Incorporate verbs that clearly describe the function's action.

```typescript
// Good
function feedAllGoats(goats: Goat[]) {
    goats.forEach(feedGoat);
}

// Avoid
function feed(goats: Goat[]) {
    // Implementation
}
```

### Classes and Interfaces

*   **Use PascalCase:** Classes and interfaces should be named using PascalCase. Names should be nouns or noun phrases that clearly describe what the class or interface represents.

```typescript
// Good
class GoatFeeder {
    feedGoat(goat: Goat) {
        // Implementation
    }
}

interface Feedable {
    feed(): void;
}

// Avoid
class goatFeeder {
    // Implementation
}

interface feedable {
    // Implementation
}
```

### Enums

*   **PascalCase for Enum Types, UPPER\_SNAKE\_CASE for Values:** Enum names should be singular and use PascalCase, while enum values should be in UPPER\_SNAKE\_CASE.

```typescript
// Good
enum GoatMood {
    HAPPY = 'HAPPY',
    SAD = 'SAD',
    HUNGRY = 'HUNGRY',
}

// Avoid
enum goatMoods {
    happy = 'happy',
    sad = 'sad',
    hungry = 'hungry',
}
```

### Type Aliases

*   **Use PascalCase:** Type aliases should be named using PascalCase, similar to classes and interfaces.

```typescript

// Good
type GoatFeed = {
    type: string;
    quantity: number;
};

// Avoid
type goatFeed = {
    type: string;
    quantity: number;
};
```

### Avoiding Ambiguity and Redundancy

*   **Contextual and Precise Naming:** Choose names that are clear within the context they are used. Avoid redundancy or unnecessary prefixes/suffixes that do not add meaning.

```typescript
// Good
class Goat {
    name: string;
    feed() {
        // Implementation
    }
}

// Avoid
class GoatClass {
    goatName: string;
    feedGoat() {
        // Implementation
    }
}
```

By adhering to these naming conventions, TypeScript developers ensure their code is not only consistent and readable but also aligns with common practices in the broader TypeScript and JavaScript communities. This facilitates easier collaboration, code reviews, and maintenance in projects ranging from small teams to large-scale enterprise applications.

## Comments and Documentation

Effective commenting and comprehensive documentation play a pivotal role in maintaining the clarity, understandability, and usability of TypeScript code. This section delves into best practices for writing inline comments, documentation comments, and leveraging TypeScript-specific features to enrich the documentation.

### Inline Comments

*   **Purposeful and Concise:** Inline comments should add value by explaining "why" behind a code decision, providing context, or clarifying complex portions of code.

```typescript
// Good
// Check if the goat is hungry before attempting to feed
if (goat.isHungry) {
    feedGoat(goat);
}

// Avoid comments that state the obvious
// Set isHungry to true
goat.isHungry = true;
```

### Documentation Comments

*   **Use JSDoc for Public APIs:** Employ JSDoc comments to document classes, interfaces, functions, and parameters. This not only aids in code comprehension but also enhances tooling support, such as IntelliSense in IDEs.

```typescript
/**
 * Represents a goat in the farm system.
 *
 * @param name The name of the goat.
 * @param age The age of the goat in years.
 */
class Goat {
    constructor(public name: string, public age: number) {}
}

/**
 * Feeds a specified goat.
 *
 * @param goat The goat to be fed.
 * @returns True if feeding was successful.
 */
function feedGoat(goat: Goat): boolean {
    // Implementation
}
```

### Keeping Comments Up-to-Date

*   **Reflect Code Changes:** Ensure that comments and documentation are updated in tandem with code changes. Outdated documentation can be misleading and diminish the value of comments.

### TODO Comments

*   **Track Action Items with Ticket Numbers:** Use `TODO:` comments for marking incomplete implementation details or future improvements, ideally including a ticket or issue number for easier tracking.

```typescript
// TODO: [ISSUE-123] Optimize goat feeding logic for efficiency
function feedGoat(goat: Goat) {
    // Placeholder implementation
}
```

### Avoid Commented-Out Code

*   **Prefer Version Control for History:** Instead of leaving commented-out code blocks, rely on version control systems like Git to keep a history of changes. Commented-out code can clutter the codebase and lead to confusion.

```typescript
// Good
// Removed outdated goat feeding mechanism

// Avoid
// feedGoat(goat, "Hay");
// console.log("Feeding completed");
```

### Use of Annotations

*   **Leverage TypeScript Annotations for Clarity:** Beyond regular comments, TypeScript's type annotations and decorators themselves serve as a form of documentation, clearly indicating the intended use and structure of code.

```typescript
// Good
@deprecated
function oldFeedMethod() {
    // Old implementation
}

// Using type annotations for clarity
function monitorGoatHealth(goat: Goat): HealthStatus {
    // Implementation
}
```

By adhering to these commenting and documentation guidelines, TypeScript developers ensure that their code remains understandable and maintainable. This practice not only benefits the original author but also aids other developers who may work on the codebase, fostering a culture of clarity and collaboration.

## Programming Practices

Adopting effective programming practices is essential for writing clean, efficient, and maintainable TypeScript code. This section highlights key practices that TypeScript developers should follow to enhance code quality and leverage TypeScript's powerful features to their full potential.

### Strong Typing

*   **Leverage TypeScript's Type System:** Make the most of TypeScript's static typing to catch errors early in the development process and improve code readability.

```typescript
// Good
function feedGoat(goat: Goat, amount: number): void {
    // Implementation
}

// Avoid
function feedGoat(goat, amount) {
    // Implementation
}
```

### Interface and Type Aliases

*   **Prefer Interfaces Over Type Aliases for Objects:** While both can be used for shaping objects, interfaces offer more flexibility and are easier to extend.

```typescript
// Good
interface Goat {
    name: string;
    age: number;
}

// Acceptable, but less extendable
type Goat = {
    name: string;
    age: number;
};
```

### Enums and Union Types

*   **Use Enums for a Known Set of Values:** Enums are great for defining a set of named constants. For more flexible constructs, consider using union types.

```typescript
// Good
enum GoatMood { Happy, Hungry, Sleepy }

// For more flexible constructs
type AlertLevel = 'low' | 'medium' | 'high';
```

### Null Checks

*   **Utilize TypeScript's Null Checking:** Use TypeScript's strict null checking features and avoid using `null` or `undefined` as acceptable values unless absolutely necessary.

```typescript
// Good - with strict null checks
function playWithGoat(goat: Goat | null) {
    if (goat !== null) {
        console.log(`${goat.name} is playing!`);
    }
}

// Avoid ignoring strict null checks
function playWithGoat(goat: Goat) {
    console.log(`${goat.name} is playing!`);
}
```

### Asynchronous Programming

*   **Prefer async/await Over Promises:** `async/await` syntax makes asynchronous code more readable and easier to understand than traditional promise chains.

```typescript
// Good
async function feedAllGoats(goats: Goat[]): Promise<void> {
    for (const goat of goats) {
        await feedGoat(goat);
    }
}

// Avoid using complex promise chains
function feedAllGoats(goats: Goat[]): Promise<void> {
    return goats.reduce((promise, goat) => promise.then(() => feedGoat(goat)), Promise.resolve());
}
```

### Modularization

*   **Use ES Modules:** Organize your code into reusable modules. This enhances code organization and makes it easier to manage dependencies.

```typescript
// Good - in goat.ts
export class Goat {
    constructor(public name: string) {}
}

// In main.ts
import { Goat } from './goat';
```

### Immutable Data Patterns

*   **Prefer Immutable Data Structures:** Whenever possible, use immutable data patterns. This makes your application's state more predictable and easier to debug.

```typescript
// Good
const goats: ReadonlyArray<Goat> = [new Goat('Billy'), new Goat('Daisy')];

// Avoid - mutable array
const goats: Goat[] = [new Goat('Billy'), new Goat('Daisy')];
```

### Decorators

*   **Use Decorators for Meta-programming:** Decorators provide a way to add annotations and a meta-programming syntax for class declarations and members. Use them judiciously to enhance functionality without obscuring the underlying logic.

```typescript
// Good
@Component({
    selector: 'app-goat',
    templateUrl: './goat.component.html',
    styleUrls: ['./goat.component.css']
})
export class GoatComponent {
    // Implementation
}
```

By adhering to these programming practices, TypeScript developers can ensure their code is not only performant and robust but also easy to understand and maintain. This forms the foundation of a high-quality TypeScript codebase that leverages the language's features to their fullest.

## Language-Specific Idioms and Patterns

Embracing TypeScript's language-specific idioms and patterns can significantly enhance the quality, readability, and maintainability of your code. This section outlines key TypeScript idioms and patterns, inspired by best practices within the TypeScript community and aligned with general programming principles.

### Use TypeScript’s Type System to its Full Potential

*   **Leverage Advanced Types:** TypeScript offers powerful features like generics, enums, union types, and intersection types. Use these to create precise and flexible type definitions.

```typescript
type Action =
    | { type: 'FEED_GOAT'; payload: { goatId: string; food: string } }
    | { type: 'PET_GOAT'; payload: { goatId: string } };

function handleGoatAction(action: Action) {
    // Implementation
}
```

### Avoid Using `any` Type

*   **Specify Types Explicitly:** Minimize the use of the `any` type to maintain the benefits of TypeScript's static typing. Use `unknown` if the type is genuinely uncertain and validate it.

```typescript
// Good
function safelyParse(jsonString: string): unknown {
    return JSON.parse(jsonString);
}

// Avoid
function parse(jsonString: string): any {
    return JSON.parse(jsonString);
}
```

### Enums and Union Types for State Management

*   **Prefer Union Types Over Enums for Simplicity:** While enums can be useful, consider using union types for states or categories to reduce complexity and enhance tree-shaking.

```typescript
// Good
type GoatMood = 'happy' | 'hungry' | 'sleepy';

// Less preferred for simple cases
enum GoatMood {
    Happy,
    Hungry,
    Sleepy,
}
```

### Embrace Null Safety

*   **Optional Chaining and Nullish Coalescing:** Use optional chaining (`?.`) and nullish coalescing (`??`) operators to write cleaner, safer code that elegantly handles null and undefined values.

```typescript
// Good
const goatName = goat?.name ?? 'Unknown Goat';

// Avoid verbose checks
const goatName = goat && goat.name ? goat.name : 'Unknown Goat';
```

### Modular Code Organization

*   **Organize Code with ES Modules:** Structure your project using modules to encapsulate functionality and promote reuse. Import and export types, interfaces, functions, and classes to keep the codebase organized and maintainable.

```typescript
// In goat.ts
export class Goat {
    constructor(public name: string) {}
}

// In main.ts
import { Goat } from './goat';
```

### Use Decorators for Cross-Cutting Concerns

*   **Apply Decorators Wisely:** TypeScript's experimental decorator feature can be used to annotate and modify classes and properties elegantly, especially in frameworks like Angular.

```typescript
// Good
@Component({
    selector: 'goat-list',
    templateUrl: './goat-list.component.html',
})
export class GoatListComponent {
    // Component logic
}
```

### Functional Programming Techniques

*   **Immutability and Pure Functions:** Adopt functional programming principles where appropriate. Use immutable data patterns and write pure functions to improve predictability and facilitate testing.

```typescript
// Good
function feedGoat(goat: Goat, food: string): Goat {
    return { ...goat, lastFedWith: food };
}

// Avoid mutating input arguments
function feedGoat(goat: Goat, food: string): void {
    goat.lastFedWith = food;
}
```

By incorporating these TypeScript-specific idioms and patterns, developers can write code that is not only type-safe and robust but also clear and concise, leveraging the full power of TypeScript to create maintainable and scalable applications.

## Tools and IDE Setup

A well-configured development environment is crucial for productive TypeScript development. This section provides guidance on setting up tools and Integrated Development Environments (IDEs) to support TypeScript coding standards, improve efficiency, and ensure high-quality code.

### TypeScript Compiler Configuration

*   **tsconfig.json:** Central to any TypeScript project, `tsconfig.json` defines compiler options and project settings. Use this file to enforce strict type checking, specify the target JavaScript version, and configure module resolution.

```typescript
{
    "compilerOptions": {
        "target": "es2024", // Compile TypeScript to ES2024 or latest compatible version
            "module": "commonjs", // Keep commonjs module format
            "strict": true, // Enforce strict mode for better type safety
            "esModuleInterop": true, // Allow smooth interoperability with ES modules
            "skipLibCheck": true, // Optional: Skip library check if you trust your dependencies
            "outDir": "./dist", // Output directory for compiled JavaScript files
            "watch": true, // Optional: Enable automatic compilation on file changes (for development)
            "sourceMap": true // Optional: Generate source maps for debugging compiled code
    }
}
```

### Linting and Formatting

*   **ESLint:** Adopt ESLint with TypeScript-specific plugins and configurations to enforce coding standards and catch common errors. Integrate ESLint into your build process and IDE to get real-time feedback.

```shell
npm install eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin --save-dev
```

*   **Prettier:** Use Prettier for code formatting. Configure Prettier to ensure consistency with your TypeScript style guide, and integrate it with your IDE and version control system for automatic formatting.

```typescript
// .prettierrc
{
    "semi": true,
    "singleQuote": true
}
```

### IDEs and Editors

#### Visual Studio Code (VS Code)

*   **TypeScript Support:** VS Code provides built-in support for TypeScript, including syntax highlighting, IntelliSense, and debugging.

*   **Extensions:** Enhance your development experience with extensions like `ESLint`, `Prettier`, and `GitLens`.

*   **Task Runners:** Configure task runners to compile TypeScript, run linters, and execute tests directly from the IDE.

#### WebStorm and Other JetBrains IDEs

*   **Rich TypeScript Support:** WebStorm offers advanced coding assistance for TypeScript, including refactoring, navigation, and real-time error detection.

*   **Integrated Tools:** Leverage built-in tools for version control, testing, and linting, ensuring a seamless development workflow.

### Version Control Integration

*   **Pre-commit Hooks:** Use tools like Husky to set up pre-commit hooks that run linters and formatters, ensuring that only code adhering to your style guide is committed.

```shell
npm install husky --save-dev
```

### Testing Frameworks

*   **Unit Testing:** Adopt a testing framework like Jest or Mocha for unit testing. Use `ts-jest` or `ts-node` with Mocha to run tests written in TypeScript.

```shell
npm install jest ts-jest @types/jest --save-dev
```

By leveraging these tools and configuring your IDE properly, you can create a robust TypeScript development environment that supports coding best practices, enhances productivity, and ensures the delivery of high-quality code.