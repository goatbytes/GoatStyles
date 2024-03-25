
```{.kotlin .good-code linenums="1" title="Good"}
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

```{.kotlin .bad-code linenums="1" title="BAD"}
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