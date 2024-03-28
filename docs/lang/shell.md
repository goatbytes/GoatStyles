# Shell Style Guide

This guide provides recommendations for writing clean, maintainable, and robust shell scripts. It
focuses on best practices and idiomatic usage that enhance the readability and functionality of
scripts written in Bash or other shell languages.

[//]: # (@formatter:off)
/// admonition | 
    type: abstract
[Foundational Code Standards][FOUNDATION]{:target="_blank"} provide the foundation, this guide extends them for Shell.
///
[//]: # (@formatter:on)

## Formatting

Follow the [Foundational Formatting Standards][FORMATTING] with these shell-specific guidelines:

- **Indentation:** Use 2 spaces for indentation.
- **Line Length:** Aim for 80 characters, with a hard limit of 100 characters per line.
- **Use of Whitespace:** Use whitespace to separate commands from their arguments.
- **Quoting Variables:** Always quote variables to avoid issues with spaces and globbing: `"$var"`.

/// admonition | Remember, readability and portability are paramount.
    type: info
///

/// details | Example Formatted Shell Script
    type: example

```shell
#!/bin/bash

# Function demonstrating various style rules
perform_operations() {
  local x=$1
  local y=$2
  local sum=$((x + y)) # Space around operators

  echo "Sum: $sum"

  # Ternary-like operation using if-else
  if [[ $sum -gt 10 ]]; then
    message="Greater than 10"
  else
    message="Not greater than 10"
  fi
  echo "$message"

  # If-else with spacing
  if [[ $((sum % 2)) -eq 0 ]]; then
    echo "Sum is even"
  else
    echo "Sum is odd"
  fi

  # For loop demonstrating continuation indent
  for i in {0..4}; do
    echo -n "$i " # Demonstrate space in concatenation
  done
  echo # New line after loop

  # Try-catch-finally block emulation using trap
  {
    throw_error_demo
  } || {
    echo "Caught an error."
  }
}

# Emulate throwing an error
throw_error_demo() {
  return 1 # Simulate an error
}

# Main execution
if [[ $# -eq 2 ]]; then
  perform_operations "$1" "$2"
else
  echo "Usage: $0 <num1> <num2>"
  exit 1
fi
```
///

## Naming Conventions

Consistent naming conventions improve script readability and maintainability:

- **Functions:** Lowercase, with underscores to separate words. Define with parentheses and space
  before the brace: `my_function() { ... }`.
- **Variables:** Lowercase for local variables, UPPERCASE for exported or global variables.
- **Constants:** UPPERCASE with underscores separating words.

## Commenting and Documentation

### Inline Comments

Use inline comments sparingly to explain "why" rather than "what".

### Script Header

Start each script with a header indicating its purpose, usage, and any dependencies:

```bash
#!/bin/bash
# Purpose: Automate goat feeding schedule
# Usage: ./feed_goats.sh [options]
# Dependencies: curl, jq
```

### Function Comments

Document functions with a description, arguments, and return value:

```bash
# Feeds a specified number of goats.
# Globals:
#   FEED_BIN
# Arguments:
#   Number of goats
# Returns:
#   None
feed_goats() {
  local num_goats="$1"
  # implementation...
}
```

## Idioms and Best Practices

### Conditional Constructs

* **Use** `[[` for Conditionals: Prefer the `[[` keyword for conditional constructs instead of `[`
  for improved readability and additional functionality such as pattern matching and logical
  operators.

```shell
if [[ $goat_count -gt 10 ]]; then
    echo "Herd is too large!"
fi
```

### Looping Constructs

* **Use** `for` Loops for Iteration: Utilize `for` loops for iterating over lists of items, files,
  or directory contents. Avoid parsing `ls` output and prefer globbing or `find` commands for
  listing files.

```shell
for goat in "${goats[@]}"; do
    echo "Processing $goat..."
done
```

### Error Handling

* **Check Command Return Codes**: Always check the return codes of commands and utilities to handle
  errors gracefully and prevent silent failures. Use `||` to execute fallback actions upon command
  failure.

```shell
rm "$file" || echo "Failed to delete $file"
```

### Function Definitions

* **Declare Functions with** `function`: When defining functions, use the `function` keyword for
  improved clarity and portability across different shell environments.

```shell
function feed_goat() {
    local goat_name=$1
    local food_amount=$2
    echo "Feeding ${goat_name} ${food_amount}kg of food."
}
```

### Process Substitution

* **Use Process Substitution**: Leverage process substitution `<(command)` and `>(command)` to pass
  the output of commands as input streams or arguments to other commands. This is especially useful
  for complex command pipelines.

```shell
diff <(sort file1) <(sort file2)
```

### Command Substitution

* **Use Command Substitution**: Utilize command substitution `$(command)` to capture the output of
  commands and use them as arguments or assignments within scripts. Avoid using backticks for
  command substitution due to readability concerns.

```shell
file_size=$(wc -c < "$file")
```

### Case Statements

* **Prefer** `case` Statements: Use `case` statements for multi-way branching based on patterns or
  values. This provides a more readable and structured alternative to nested `if` statements.

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

* **Reuse Existing Functionality**: Whenever possible, leverage existing shell utilities, commands,
  and functions rather than reinventing the wheel. This promotes code reuse, reduces maintenance
  overhead, and encourages consistency.

```shell
# Use existing utility to count lines in a file
line_count=$(wc -l < "$file")
```

## Tools and IDE Setup

Setting up the right tools and IDE environment is crucial for efficient shell scripting and ensuring
code quality. Here's a guide to configuring your development environment for optimal shell scripting
productivity.

### Linting

* **[ShellCheck](https://www.shellcheck.net/)**: Integrate ShellCheck into your development workflow
  to catch common issues, syntax errors, and pitfalls in your shell scripts. ShellCheck provides
  valuable feedback on script correctness and adherence to best practices.

### Terminal Emulators

* **Optimize Your Terminal Environment**: Configure your terminal emulator to suit your shell
  scripting needs, including customizing the prompt, enabling syntax highlighting, and setting up
  keyboard shortcuts for common tasks.

    * **[iTerm2](https://iterm2.com/) (macOS)**: Feature-rich terminal emulator with support for
      split panes, customizable profiles, and integration with shell scripting tools.
    * **[Gnome Terminal](https://github.com/GNOME/gnome-terminal)** - A terminal emulator for GNOME.
    * **[Hyper](https://github.com/zeit/hyper)** - A terminal built on web technologies.

### Shell-Specific IDEs

* **[Bash IDE](https://github.com/bash-lsp/bash-language-server#readme)**: A lightweight IDE for
  Bash scripting with features like syntax highlighting, auto-completion, and code snippets.
* **[IntelliJ IDEA](https://www.jetbrains.com/help/idea/shell-scripts.html)**: IntelliJ IDEA
  provides coding assistance for shell script files

### Package Managers

* **Package Management for Shell Scripts**: Utilize package managers like Homebrew (macOS), APT (
  Linux), or Chocolatey (Windows) to install and manage dependencies for shell scripting tools and
  utilities. Package managers streamline the installation process and ensure consistent tool
  versions across development environments.

### Shells and Frameworks

* [bash](https://www.gnu.org/software/bash/) - GNU Project's shell (Bourne Again SHell)
* [fish](https://fishshell.com) - Smart and user-friendly command line shell
* [PowerShell](https://github.com/PowerShell/PowerShell) - PowerShell for every system!
* [powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview) a cross-platform task
  automation and configuration management framework, consisting of a command-line shell and
  scripting language
* [zsh](https://www.zsh.org) - Powerful shell with scripting language
* [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) - A delightful community-driven framework
  for managing your zsh configuration.

### Guides and Tutorials

* [Bash Official Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
* [Bash Hackers Wiki](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/)
* [Greg Wooledge's (aka "greycat") wiki](https://mywiki.wooledge.org).
* [Google's Shell Style Guide](https://google.github.io/styleguide/shell.xml)
* [The Linux Documentation Project: Bash Programming - Intro/How-to](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
* [The Linux Documentation Project: Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
* [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
* [A guide to learn bash](https://github.com/Idnan/bash-guide)

[FOUNDATION]: ../foundation.md
[FORMATTING]: ../foundation.md#formatting
[NAMING]: ../foundation.md#naming-conventions
[DOCS]: ../foundation.md#documentation-and-comments