

<!-- termynal: {"prompt_literal_start": ["$", ">>>", "PS >"], title: powershell, buttons: windows} -->
```
// code
```

/// admonition | Some title
type: warning

``` { .kotlin .copy .annotate }
# Code block content
// this is code
/**
 * This is a comment
 */
fun main() {
    println("Hello, World!")
}
```

```shell
some code
```
///

HELLO :octocat: :smile: :+1:

/// tab | Java
```java
public static void main(String[] args) {
    System.out.println("Hello, World!");
}
```
///


/// tab | Kotlin
```kotlin
fun main() {
    println("Hello, World!")
}
```
///

---

``` yaml
theme:
  features:
    - content.code.annotate # 
#(1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

---

/// tab | Java
```{.kotlin .good-code}
data class User(val id: Int, val name: String)

fun fetchUserData(userId: Int): User? {
    // Simulate fetching user data that might return null
    return User(userId, "John Doe") // Assume this could be null in real scenarios
}

fun displayUserName(userId: Int) {
    val user = fetchUserData(userId)
    user?.let {
        println("User Name: ${it.name}")
    } ?: run {
        println("User not found")
    }
}

fun main() {
    displayUserName(1) // Output: User Name: John Doe
}
```
///

/// tab | Kotlin

```{.kotlin .bad-code}
class User {
    var id: Int = 0
    var name: String? = null
}

fun fetchUserData(userId: Int): User? {
    // Simulate fetching user data that might return null
    val user = User()
    user.id = userId
    user.name = "John Doe" // Assume this could be null in real scenarios
    return user
}

fun displayUserName(userId: Int) {
    val user = fetchUserData(userId)
    if (user != null) {
        if (user.name != null) {
            println("User Name: ${user.name}")
        } else {
            println("User name is null")
        }
    } else {
        println("User not found")
    }
}

fun main() {
    displayUserName(1) // Output: User Name: John Doe
}
```
///

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>