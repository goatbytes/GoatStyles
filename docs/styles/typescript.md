# TypeScript Style Guide

This guide specifically addresses TypeScript development, focusing on idiomatic practices, patterns,
and TypeScript-specific considerations.

[//]: # (@formatter:off)
/// admonition | 
    type: abstract
[Foundational Code Standards][fnd]{:target="_blank"} provide the foundation, this guide extends them for TypeScript.
///
[//]: # (@formatter:on)

## Formatting

The formatting guidelines for TypeScript closely adhere to
our [Foundational Code Standards][fnd-formatting]. Here is a brief overview:

- **Consistent Indentation:** Use 2 spaces for indentation.
- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Whitespace:** Use spaces around operators, after colons and semicolons, and before open braces
  for clarity.
- **Brace Style:** Use 1TBS (the one true brace style) where the opening brace is on the same line.
- **Semicolons:** Use semicolons at the end of statements for clarity.

[//]: # (@formatter:off)
/// admonition |
    type: info
Remember, these are guidelines; adapt them for your project's needs while keeping readability in focus.
///

## Naming Conventions

Adhere to our [Foundational Code Standards][fnd-naming] with the following TypeScript-specific clarifications:

- **Interfaces:** Use PascalCase without an `I` prefix.
- **Types:** Use PascalCase for type aliases and enum types.
- **Members:** Public members should not have an underscore prefix.

## Documentation and Comments

Refer to the [Foundational Code Standards][fnd-docs] for general commenting and documentation
guidelines. In TypeScript, use [TSDoc][TSDoc] for documenting code. Document all public APIs clearly
with examples where applicable.

## Idioms and Best Practices

### Use TypeScript’s Type System Effectively

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

```{.typescript .good-code title="Good"}
function safelyParse(jsonString: string): unknown {
  return JSON.parse(jsonString);
}
```
```{.typescript .bad-code title="Avoid"}
function parse(jsonString: string): any {
  return JSON.parse(jsonString);
}
```

### Enums and Union Types for State Management

*   **Prefer Union Types Over Enums for Simplicity:** While enums can be useful, consider using union types for states or categories to reduce complexity and enhance tree-shaking.

```{.typescript .good-code title="Good"}
type GoatMood = 'happy' | 'hungry' | 'sleepy';
```
```{.typescript .bad-code title="Less preferred for simple cases"}
enum GoatMood {
    Happy,
    Hungry,
    Sleepy,
}
```

### Embrace Null Safety

*   **Optional Chaining and Nullish Coalescing:** Use optional chaining (`?.`) and nullish coalescing (`??`) operators to write cleaner, safer code that elegantly handles null and undefined values.


```{.typescript .good-code title="Good"}
const goatName = goat?.name ?? 'Unknown Goat';
```
```{.typescript .bad-code title="Avoid"}
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

```{.typescript .good-code title="Good"}
function feedGoat(goat: Goat, food: string): Goat {
  return { ...goat, lastFedWith: food };
}
```
```{.typescript .bad-code title="Avoid"}
function feedGoat(goat: Goat, food: string): void {
  goat.lastFedWith = food;
}
```

### Prefer Interfaces over Types for Object Shapes
Use interfaces for defining object shapes due to their extendability.

```typescript
interface Goat {
  name: string;
  age: number;
}
```

### Async/Await over Promises
Use async/await for asynchronous code for better readability and error handling.

### Modularize Code
Organize code into modules and use explicit import and export statements.

## Tools and Resources

Ensuring a consistent development environment and utilizing static analysis tools are crucial steps for maintaining high code quality in TypeScript projects.

### Recommended Static Analysis Tools for TypeScript

Static analysis tools help identify potential issues early in the development process. For TypeScript, several tools are particularly effective:

- [**TSLint**](https://palantir.github.io/tslint/): A linter that checks TypeScript code for readability, maintainability, and functionality errors.
- [**ESLint**](https://eslint.org/): A pluggable and configurable linter tool for identifying and reporting on patterns in JavaScript/TypeScript.

### Additional Resources

To further enhance your TypeScript development skills and knowledge, consider exploring the following resources:

- [**TypeScript Documentation**](https://www.typescriptlang.org/docs/): The official TypeScript documentation, offering in-depth guides and reference materials.
- [**DefinitelyTyped**](https://definitelytyped.org/): A repository of high-quality TypeScript type definitions.

[//]: # (links @formatter:off)

[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[fnd-docs]: foundation.md#documentation-and-comments
[TSDoc]: https://tsdoc.org/
[//]: # (links @formatter:on)
