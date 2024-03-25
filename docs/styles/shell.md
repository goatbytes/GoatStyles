# Shell Style Guide
## Introduction

Welcome to the Shell Style Guide! Shell scripting is a powerful tool for automating tasks, managing system configurations, and orchestrating workflows. However, without proper guidance, scripts can become messy and difficult to maintain. This style guide provides best practices, conventions, and recommendations for shell scripting.

### Purpose

The goal of this style guide is to enhance project collaboration and code quality by establishing a consistent set of standards for code formatting, naming conventions, documentation, and programming practices. By aligning on these conventions, we aim to streamline the code review process, facilitate seamless collaboration across teams, and ultimately raise the bar for code quality in our projects.

### Scope

The Shell Style Guide is intended for shell script developers, system administrators, and anyone involved in writing or maintaining shell scripts. Additionally, this guide can serve as a reference for teams and organizations looking to establish coding standards and conventions for their shell script projects. By adopting the guidelines outlined in this style guide, teams can promote consistency, improve code quality, and streamline collaboration across projects.

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

Adhering to a consistent formatting style in shell scripting enhances readability, maintainability, and can prevent common errors.

### Indentation

*   **Use 2 Spaces**: Indent your code with 2 spaces to mark different logic levels clearly. Avoid using tabs as they can appear differently in various editors and tools.


```shell
# Good
if [ "$goat" = "hungry" ]; then
  echo "Feeding goat..."
fi

# Avoid
if [ "$goat" = "hungry" ]; then
    echo "Feeding goat..."
fi
```

### Line Length

*   **Keep Lines Short**: Aim to limit your lines to 80 characters where possible. This tradition from early terminals helps ensure your code is easily readable without horizontal scrolling.


### Quoting Variables

*   **Always Quote Strings**: When referencing variables, especially within test `[ ]` brackets, always use double quotes to prevent word splitting and globbing issues.


```shell
# Good
if [ "$goatName" = "Billy" ]; then
  echo "Found Billy!"
fi

# Avoid
if [ $goatName = Billy ]; then
  echo "Found Billy!"
fi
```

### Function Declaration

*   **Use the** `function` Keyword: Declare functions using the `function` keyword followed by parentheses. This enhances readability and clarifies the definition in the script.


```shell
# Good
function feed_goat() {
  local goatName=$1
  echo "Feeding ${goatName}..."
}

# Avoid
feed_goat() {
  local goatName=$1
  echo "Feeding ${goatName}..."
}
```

### Conditional Expressions

*   **Use Double Brackets** `[[ ]]`: Prefer `[[ ]]` over `[ ]` for test expressions to prevent script errors and take advantage of advanced features like regex matching.


```shell
# Good
if [[ "$goatMood" =~ ^(happy|content)$ ]]; then
  echo "Goat is in a good mood!"
fi
```

### Use of Semicolons

*   **Avoid Unnecessary Semicolons**: Do not use semicolons to separate commands on the same line. Prefer separate lines unless you're writing a `then`, `do`, or similar construct.


```shell
# Good
feed_goat() {
  echo "Feeding goat"
}

# Avoid
feed_goat(); echo "Feeding goat"
```

### Loop and Control Structure Formatting

*   **Readable Loops and Conditions**: Format loops and if-else structures clearly with then/do on the same line as the condition/loop statement, followed by the actions on new lines.

```shell
# Good
for goat in "${goats[@]}"; do
  feed_goat "$goat"
done

# Avoid
for goat in "${goats[@]}"; do feed_goat "$goat"; done
```

## Naming Conventions in Shell Scripts

Naming conventions in shell scripts play a crucial role in ensuring code clarity, ease of maintenance, and the prevention of naming conflicts.

### Variable Names

*   **Lowercase with Underscores**: Use lowercase letters for local variable names, separating words with underscores to improve readability. This convention distinguishes local variables from environment variables, which are traditionally uppercase.


```shell
# Good
goat_count=5

# Avoid
GoatCount=5
GOAT_COUNT=5
```

*   **Environment Variables and Constants**: Use uppercase letters for environment variables and constants within your script, again separating words with underscores.


```shell
# Environment variable or script constant
MAX_GOATS=10
```

### Function Names

*   **Lowercase with Underscores**: Name functions using lowercase letters, separating words with underscores. This keeps function naming consistent with variable naming conventions and enhances readability.


```shell
# Good
function feed_goat() {
  echo "Feeding goat..."
}

# Avoid
function FeedGoat() {
  echo "Feeding goat..."
}
```

### Script File Names

*   **Lowercase with Dashes**: Name script files using lowercase letters, separating words with dashes (`-`). This convention is common in Unix and Linux environments and helps ensure compatibility across different systems.


```shell
# Good
manage-goat-farm.sh

# Avoid
manage_goat_farm.sh
ManageGoatFarm.sh
```

### Use Descriptive Names

*   **Clarity and Descriptiveness**: Choose names that clearly describe the purpose of the variable, function, or script without requiring additional context. Avoid overly generic or cryptic names.


```shell
# Good
function check_goat_hunger_status() {
  # Implementation
}

# Avoid
function cghs() {
  # Implementation
}
```

### Prefixing Temporary Variables

*   **Prefix for Temporaries**: When using temporary variables, especially in loops or conditionals, consider prefixing them with `tmp_` or `temp_` to clarify their transient nature.


```shell
# Good
for tmp_goat in "${goats[@]}"; do
  echo "Processing ${tmp_goat}..."
done
```

### Avoiding Name Reuse

*   **Unique Names for Different Entities**: Avoid using the same name for different types of entities (e.g., variables and functions) to prevent confusion and potential script errors.


## Commenting and Documentation in Shell Scripts

Effective commenting and documentation are crucial for maintaining shell scripts, especially as complexity grows or scripts are handed off between team members.

### Purpose of Comments

*   **Clarify "Why" Over "What"**: Comments should explain the rationale behind complex decisions and algorithms, not what the code does. Shell commands and syntax can describe the "what" adequately.


```shell
# Good: Explaining the reason behind the check
# Check if the goat pen is locked to prevent goats from escaping at night
if [ "$pen_status" = "locked" ]; then
  echo "All goats are secure for the night."
fi
```

### Inline Comments

*   **Use Sparingly**: Place inline comments on the same line as a command if they explain something non-obvious about the specific command.


```shell
move_goat_to_pen "$goat_name" # Moving to pen ensures the goat is safe at night
```

### Function Comments

*   **Documenting Functions**: At the beginning of every function, include a comment block that describes what the function does, its inputs, and its expected behavior. For complex functions, include any side effects or global variable dependencies.


```shell
# Feeds a named goat with the specified amount of food.
# Arguments:
#   1. Goat name
#   2. Amount of food (in kg)
# Outputs:
#   Prints a message confirming feeding.
function feed_goat() {
  local goat_name=$1
  local food_amount=$2
  echo "Feeding ${goat_name} ${food_amount}kg of food."
}
```

### Use of TODO Comments

*   **Marking Work to Be Done**: Use `TODO` comments to indicate future tasks, improvements, or questions. These comments should be clear and actionable. Optionally, include a name or ticket number for tracking.


`# TODO: [TICKET-123] Implement weight check for goats before feeding to adjust food amount`

### Header Comments

*   **Script Metadata**: At the top of each script file, include a comment block that provides a brief overview of the script, its purpose, author(s), and any usage instructions. This metadata is valuable for new users or contributors.

```shell
#!/bin/bash
# Script Name: manage-goat-farm.sh
# Description: This script manages daily activities in the goat farm.
# Author: GoatBytes.IO
# Usage: ./manage-goat-farm.sh [options]
```

### Commenting Out Code

*   **Avoid Leaving Outdated Code**: Commented-out code can quickly become outdated. It's better to remove it or, if necessary for historical purposes, explain why it's retained.


## Programming Practices in Shell Scripts

### Use of Shellcheck

*   **Leverage ShellCheck**: ShellCheck is a powerful tool for analyzing shell scripts, identifying syntax errors, semantic problems, and common pitfalls. Integrate ShellCheck into your development workflow to catch issues early and ensure script reliability.

```shell
# Check script.sh for issues
shellcheck script.sh
```

### Error Handling

*   **Fail Early and Verbosely**: Ensure scripts terminate immediately upon encountering errors to prevent cascading failures. Use `set -e` to enable automatic script termination upon command failure, and `set -u` to treat unset variables as errors.


```shell
set -euo pipefail
```

*   **Logging and Reporting**: Implement robust error logging mechanisms to capture errors, warnings, and informational messages for debugging and monitoring purposes. Use `logger` or custom logging functions to record script activity.

```shell
# Log an error message
logger -p err "Failed to execute command: $command"
```

### Filesystem Operations

*   **Sanitize Inputs**: Always sanitize inputs, especially those obtained from user input or external sources, to prevent security vulnerabilities and unexpected behavior. Validate file paths and ensure proper permissions before performing filesystem operations.

```shell
# Ensure directory exists before proceeding
if [ ! -d "$directory" ]; then
    echo "Directory does not exist: $directory"
    exit 1
fi
```

*   **File Backups**: Before modifying or deleting files, consider creating backups to preserve data integrity and facilitate rollback in case of errors. Use `cp` or `rsync` to create backups with timestamps or version numbers.

```shell
# Create a timestamped backup of a file
cp "$file" "$file.$(date +%Y%m%d%H%M%S)"
```

### Code Readability

*   **Follow Consistent Naming Conventions**: Use descriptive and meaningful variable names, following consistent casing conventions (e.g., snake\_case or camelCase). Avoid ambiguous abbreviations and acronyms.

```shell
# Good: Descriptive variable name
goat_count=10
```

*   **Modularize Code**: Break down complex scripts into smaller, modular functions or scripts to improve readability, maintainability, and reusability. Encapsulate related functionality within functions to promote code organization.

```shell
# Function to feed a goat
feed_goat() {
    local goat_name=$1
    local food_amount=$2
    echo "Feeding ${goat_name} ${food_amount}kg of food."
}
```

### Performance Considerations

*   **Optimize Resource Usage**: Minimize resource consumption by optimizing command usage, reducing unnecessary I/O operations, and avoiding inefficient constructs like excessive loops or nested subshells.
*   **Cache Expensive Operations**: Cache the results of expensive operations or commands to improve script performance and reduce execution time. Consider storing intermediate results in temporary files or variables.


## Language-Specific Idioms and Patterns

### Conditional Constructs

*   **Use** `[[` for Conditionals: Prefer the `[[` keyword for conditional constructs instead of `[` for improved readability and additional functionality such as pattern matching and logical operators.

```shell
if [[ $goat_count -gt 10 ]]; then
    echo "Herd is too large!"
fi
```

### Looping Constructs

*   **Use** `for` Loops for Iteration: Utilize `for` loops for iterating over lists of items, files, or directory contents. Avoid parsing `ls` output and prefer globbing or `find` commands for listing files.

```shell
for goat in "${goats[@]}"; do
    echo "Processing $goat..."
done
```

### Error Handling

*   **Check Command Return Codes**: Always check the return codes of commands and utilities to handle errors gracefully and prevent silent failures. Use `||` to execute fallback actions upon command failure.


```shell
rm "$file" || echo "Failed to delete $file"
```

### Function Definitions

*   **Declare Functions with** `function`: When defining functions, use the `function` keyword for improved clarity and portability across different shell environments.

```shell
function feed_goat() {
    local goat_name=$1
    local food_amount=$2
    echo "Feeding ${goat_name} ${food_amount}kg of food."
}
```

### Process Substitution

*   **Use Process Substitution**: Leverage process substitution `<(command)` and `>(command)` to pass the output of commands as input streams or arguments to other commands. This is especially useful for complex command pipelines.

```shell
diff <(sort file1) <(sort file2)
```

### Command Substitution

*   **Use Command Substitution**: Utilize command substitution `$(command)` to capture the output of commands and use them as arguments or assignments within scripts. Avoid using backticks for command substitution due to readability concerns.

```shell
file_size=$(wc -c < "$file")
```

### Case Statements

*   **Prefer** `case` Statements: Use `case` statements for multi-way branching based on patterns or values. This provides a more readable and structured alternative to nested `if` statements.

```shell
case $option in
    1)
        echo "Option 1 selected."
        ;;
    2)
        echo "Option 2 selected."
        ;;
    *)
        echo "Invalid option."
        ;;
esac
```

### Functionality Reuse

*   **Reuse Existing Functionality**: Whenever possible, leverage existing shell utilities, commands, and functions rather than reinventing the wheel. This promotes code reuse, reduces maintenance overhead, and encourages consistency.

```shell
# Use existing utility to count lines in a file
line_count=$(wc -l < "$file")
```

## Tools and IDE Setup

Setting up the right tools and IDE environment is crucial for efficient shell scripting and ensuring code quality. Here's a guide to configuring your development environment for optimal shell scripting productivity.

### ShellCheck

*   **Linting for Shell Scripts**: Integrate ShellCheck into your development workflow to catch common issues, syntax errors, and pitfalls in your shell scripts. ShellCheck provides valuable feedback on script correctness and adherence to best practices.


### Text Editors

*   **Choose a Suitable Text Editor**: Select a text editor with features tailored to shell scripting, such as syntax highlighting, code completion, and integration with shell interpreters. Popular choices include:

    *   **Visual Studio Code**: Offers extensive support for shell scripting with plugins like ShellCheck integration and Bash debugging.

    *   **Sublime Text**: Customizable editor with syntax highlighting and support for various shell script languages.

    *   **Atom**: Highly customizable text editor with a vibrant community and a wide range of shell script packages and themes.


### Terminal Emulators

*   **Optimize Your Terminal Environment**: Configure your terminal emulator to suit your shell scripting needs, including customizing the prompt, enabling syntax highlighting, and setting up keyboard shortcuts for common tasks.

    *   **iTerm2 (macOS)**: Feature-rich terminal emulator with support for split panes, customizable profiles, and integration with shell scripting tools.

    *   **GNOME Terminal (Linux)**: Default terminal emulator for GNOME desktop environments, offering easy customization and integration with shell scripting utilities.


### Version Control Systems

*   **Use Version Control**: Leverage version control systems like Git to track changes to your shell scripts, collaborate with team members, and manage script versions effectively. Host repositories on platforms like GitHub, GitLab, or Bitbucket for seamless collaboration and code sharing.


### Shell-Specific IDEs

*   **Consider Shell-Specific IDEs**: Explore integrated development environments (IDEs) designed specifically for shell scripting, offering advanced features like debugging, code navigation, and project management tailored to shell script development.

    *   **Bash IDE**: A lightweight IDE for Bash scripting with features like syntax highlighting, auto-completion, and code snippets.

    *   **ShellCheck Plugin**: Integrate the ShellCheck plugin into IDEs like IntelliJ IDEA or Eclipse for real-time linting and error checking as you write shell scripts.


### Package Managers

*   **Package Management for Shell Scripts**: Utilize package managers like Homebrew (macOS), APT (Linux), or Chocolatey (Windows) to install and manage dependencies for shell scripting tools and utilities. Package managers streamline the installation process and ensure consistent tool versions across development environments.