# Objective-C Style Guide

This guide is designed to foster clean, maintainable, and idiomatic Objective-C code. It aligns with
the community standards and best practices for Objective-C development.

[//]: # (@formatter:off)
/// admonition | Please refer to our [Foundational Code Standards][fnd] for general principles, purpose, and scope guiding our coding practices.
    type: abstract
///
[//]: # (@formatter:on)

## Formatting

The formatting guidelines for C++ adhere to our [Foundational Code Standards][fnd-formatting].
Here is a brief overview:

- **Consistent Indentation:** Use 2 spaces for indentation, 4 spaces for continuation lines.
- **Line Length:** Aim for 100 characters, but allow flexibility for readability.
- **Whitespace:** Use spaces around operators, parentheses, braces, colons, commas, and keywords.
- **Brace Style:** Follow K&R style (opening brace on same line, closing brace on new line).
- **Blank Lines:** Use 1 line to separate code sections.
- **Alignment:** Align elements in documentation comments and parameter lists.

[//]: # (@formatter:off)
/// admonition |
    type: info
Remember, these are guidelines; adapt them for your project's needs while keeping readability in
focus.
///
[//]: # (@formatter:on)

## Naming Conventions

The naming conventions for Objective-C adhere to our [Foundational Code Standards][fnd-naming]
_with no exceptions._

- **PascalCase** for classes, protocols, and enumeration types
- **camelCase** for methods, variables, and properties.
    - Prefix booleans with "is" or "has" for clarity.
- **UPPER_SNAKE_CASE** for constants.
- **lowercase** package names, concatenated words (avoid underscores).

## Documentation and Comments

Well-crafted comments and documentation are essential for maintaining the clarity,
understandability, and usability of Objective-C code. This section focuses on best practices for
effective commenting and leveraging Objective-C and Xcode features to create comprehensive
documentation.

### Inline Comments

* **Clarify Complex Logic:** Use inline comments to explain complex algorithms, decisions that are
  not immediately obvious, or to provide context that is not readily apparent from the code itself.

    ```{.objective-c title="Example of Inline Comment for Complex Logic (goat headbutt damage calculation)"}
    // Apply bonus damage based on goat's horn strength
    int headbuttDamage = baseDamage + (_goat.hornStrength * kHeadbuttStrengthMultiplier);
    ```

### Documentation Comments

* **Use Xcode's Markup for Documentation:** Employ documentation comments above methods, properties,
  and classes to describe their purpose and usage. Xcode's markup syntax allows you to format these
  comments and include them in the Quick Help.

    ```objective-c
    /**
     Feeds a particular goat with the specified food.
    
     @param goat The goat to be fed.
     @param food The type of food to feed the goat.
     @return A boolean indicating if the feeding was successful.
    */
    - (BOOL)feedGoat:(GTFGoat *)goat withFood:(NSString *)food;
    ```

### Header Documentation

* **Public Interfaces:** Document the public interfaces of your classes in the header files. This
  makes it easier for other developers to understand how to use your classes without needing to dive
  into the implementation details.

    ```objective-c
    // GTFGoatFeeder.h
    /**
     A class responsible for feeding goats.
    
     This class provides methods to feed goats efficiently and track their feeding status.
    */
    @interface GTFGoatFeeder : NSObject
    
    /**
     Feeds all hungry goats in the pen.
    
     @discussion This method iterates over all goats in the pen and feeds those that are hungry.
     @param pen The pen containing the goats to be fed.
    */
    - (void)feedHungryGoatsInPen:(GTFGoatPen *)pen;
    
    @end
    ```

### TODO and FIXME Comments

* **Highlight Areas Needing Work:** Use `TODO:` and `FIXME:` comments to mark areas of the code that
  need improvement or completion. Include your initials and the current date for traceability.

    ```objective-c
    // TODO: [TICKET-1234] Optimize goat feeding algorithm for larger pens
    // FIXME: [GOAT-420] Resolve crash when goat name is nil
    ```

### Deprecation Notices

* **Mark Deprecated Methods:** Use the `NS_DEPRECATED` macro to mark methods that are deprecated.
  Include a message directing developers to the preferred alternative.

    ```objective-c
    - (void)oldFeedMethod NS_DEPRECATED(10_0, 10_4, 2_0, 2_0, "Use -feedGoat:withFood: instead");
    ```

### Avoid Commented-Out Code

* **Remove Unused Code:** Instead of leaving commented-out code blocks in your codebase, rely on
  version control to keep a history of changes. Commented-out code can clutter your codebase and
  lead to confusion.

## Best Practices and Idioms

### Memory Management

* **Understand and Apply ARC Correctly:** Automatic Reference Counting (ARC) manages the memory of
  your Objective-C objects. Ensure you understand ARC's rules around ownership and references to
  prevent memory leaks and retain cycles.

    ```{.objective-c title="Example of ARC Management (using strong and weak references)"}
    // Goat owner strongly references the goat, while the hay is weakly referenced to avoid retain cycles
    Goat* strongGoat = [[Goat alloc] init];
    __weak Hay* weakHay = [self findNearestHay];
    [strongGoat eatHay:weakHay];  // Goat eats the hay without creating a retain cycle
    ```

### Use of Literals

* **Prefer Objective-C Literals:** Use Objective-C literals
  for `NSString`, `NSDictionary`, `NSArray`, and `NSNumber` to make your code more concise and
  readable.

    ```{.objective-c title="Example of Using Literals (cleaner and more readable approach)"}
    NSString* goatNickname = @"Headbutt McGee";
    NSDictionary* powerUpDetails = @{@"name": @"Jetpack", @"duration": @10};
    NSArray* availableHays = @[@"Oat Hay", @"Clover Hay"];
    ```

### Nullability Annotations

* **Specify Nullability in Headers:** Use nullability
  annotations (`NS_ASSUME_NONNULL_BEGIN`, `NS_ASSUME_NONNULL_END`, `nullable`, `nonnull`) in your
  headers to provide more information to the compiler, improving code safety and reducing the
  possibility of null pointer exceptions.

    ```{.objective-c title="Example of Nullability Annotations (specifying nonnull for goat parameter)"}
    @interface GoatManager
    - (void) feedHayToGoat:(nonnull Goat*)goat;
    @end
    ```

### Block Usage

* **Avoid Retain Cycles with Blocks:** When capturing `self` in a block, especially in asynchronous
  calls, use a weak reference to avoid retain cycles.

    ```{.objective-c title="Example of Block with Weak Reference (avoiding retain cycles)"}
    __weak Goat* weakSelf = self;
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
      // Perform asynchronous task
      if (weakSelf) {
        [weakSelf goatJumpedSuccessfully];  // Use weakSelf to avoid retain cycle
      }
    });
    ```

### Error Handling

* **Use NSError for Error Reporting:** When designing methods that can fail, use an `NSError`
  pointer to pass back error information to the caller.

    ```{.objective-c title="Example of Error Handling with NSError (checking for error during hay consumption)"}
    NSError* error = nil;
    BOOL hayConsumed = [goat eatHay:hay error:&error];
    if (!hayConsumed && error) {
      NSLog(@"Error eating hay: %@", error.localizedDescription);
    }
    ```

### Testing

* **Write Unit Tests:** Leverage XCTest framework to write unit tests for your Objective-C classes.
  Testing contributes significantly to the robustness and maintainability of your code.

    ```{.objective-c title="Example of Unit Test (testing goat movement using XCTest)"}
    - (void) testGoatMovement {
      Goat* goat = [[Goat alloc] init];
      goat.position = CGPointMake(100, 100);
      [goat moveForward];
      XCTAssertTrue(goat.position.x > 100, @"Goat should move forward");
    }
    ```

### Delegate Patterns

* **Use Delegates for Callbacks and Event Handling:** The delegate pattern is widely used in Cocoa
  and Cocoa Touch for callbacks and handling events. Define protocols for your delegates to ensure
  they implement the necessary methods.

    ```{.objective-c title="Example of Delegate Pattern (Goat informs Farmer about completion of task)"}
    
    @protocol GoatTaskCompletionDelegate
    
    - (void) goat:(Goat *)goat didCompleteTask:(NSString *)task;
    
    @end
    
    @interface Goat ()
    
    @property (nonatomic, weak) id<GoatTaskCompletionDelegate> delegate;
    
    @end
    
    - (void) performTask {
      // Simulate some work performed by the goat
      sleep(2);
      [self.delegate goat:self didCompleteTask:@"Hay delivery"];
    }
    ```

### Categories for Class Extensions

* **Extend Classes with Categories:** Use categories to add methods to existing classes, including
  framework classes, without subclassing them. This is particularly useful for adding utility
  methods.

    ```{.objective-c title="Example of Category (Adding a method to calculate goat age in years)"}
    
    @interface Goat (GoatAge)
    
    - (int) calculateAgeInYears;
    
    @end
    
    @implementation Goat (GoatAge)
    
    - (int) calculateAgeInYears {
      // Calculate age based on goat's birthdate
      NSCalendar *calendar = [NSCalendar currentCalendar];
      NSDateComponents *ageComponents = [calendar components:NSCalendarUnitYear fromDate:self.dateOfBirth toDate:[NSDate date] options:0];
      return (int)ageComponents.year;
    }
    
    @end
    ```

### Use of `instancetype`

* **Prefer** `instancetype` for Type-Specific Initializers: When defining initializers,
  return `instancetype` instead of `id` to ensure type safety and clarity.

    ```{.objective-c title="Example of Initializer with instancetype"}
    
    @interface Goat alloc initWithName:(NSString *)name birthDate:(NSDate *)birthDate;
    
    @end
    
    @implementation Goat
    
    - (instancetype)initWithName:(NSString *)name birthDate:(NSDate *)birthDate {
      self = [super init];
      if (self) {
        _name = name;
        _dateOfBirth = birthDate;
      }
      return self;
    }
    
    @end
    ```

### Collections and Fast Enumeration

* **Leverage Fast Enumeration and Collection Literals:** Use fast enumeration (`for...in` loops) for
  iterating over collections. Prefer collection literals for concise and readable collection
  initialization.

    ```{.objective-c title="Example of Fast Enumeration and Collection Literals (feeding all goats hay)"}
    
    NSArray<Hay*> *availableHay = ...; // Array of available hay objects
    
    for (Hay *hay in availableHay) {
      [[GoatManager sharedInstance] feedHay:hay toGoats:self.goats];
    }
    
    // ...
    
    @interface GoatManager
    
    + (instancetype)sharedInstance;
    
    - (void) feedHay:(Hay *)hay toGoats:(NSArray<Goat*> *)goats;
    
    @end
    ```

### Properties and Dot Syntax

* **Use Properties and Dot Syntax for Encapsulation:** Define properties for encapsulating data and
  accessing instance variables. Use dot syntax for property access, which is more concise and
  readable.

    ```{.objective-c title="Example of Properties and Dot Syntax (accessing goat's name)"}
    
    @interface Goat
    
    @property (nonatomic, strong) NSString *name;
    
    @end
    
    @implementation Goat
    
    // ...
    
    - (void) introduceMyself {
      NSLog(@"I am a goat, and my name is %@", self.name);
    }
    
    @end
    ```

### Nil Checking

* **Messages to** `nil` Are No-ops: Objective-C allows messages to be sent to `nil`, which
  simplifies nil checking in many cases. However, be mindful of cases where this behavior may lead
  to unexpected results, especially with methods expected to return non-nil values.

    ```{.objective-c title="Example of Nil Checking (checking for delegate before sending message)"}
    if (self.delegate) {
      [self.delegate goat:self didCompleteTask:@"Fence repaired"];
    } else {
      NSLog(@"No delegate assigned to receive task completion notification");
    }
    ```

### Avoiding Primitive Obsession

* **Use Strongly Typed Objects Over Primitives:** Instead of relying on primitives (
  e.g., `int`, `NSString *` for IDs), use more descriptive types or classes that can provide
  additional context and validation.

    ```{.objective-c title="Example of Primitive Obsession (using int for goat ID)"}
    int goatID = 123;
    
    // More descriptive approach (using GoatID class)
    @interface GoatID : NSObject
    
    @property (nonatomic, strong) NSString* identifier;
    
    @end
    
    @implementation GoatID
    
    - (instancetype)initWithID:(NSString *)identifier {
      self = [super init];
      if (self) {
        _identifier = identifier;
      }
      return self;
    }
    
    @end
    
    GoatID* strongGoatID = [[GoatID alloc] initWithID:@"GOAT123"];
    
    // Accessing the ID
    NSLog(@"Primitive Goat ID: %d", goatID);
    NSLog(@"GoatID object identifier: %@", strongGoatID.identifier);
    ```

## Tools and Resources

### Xcode

* **Primary IDE for Objective-C:** Xcode, developed by Apple, is the most comprehensive and powerful
  IDE for Objective-C development, offering advanced code editing, debugging, and UI design
  capabilities.
* **Code Formatting:** Utilize Xcode's built-in code formatting features to maintain consistency.
  Customize formatting options in Xcode preferences to align with your project's style guide.
* **Refactoring Tools:** Leverage Xcode's refactoring tools to safely rename symbols, extract
  methods, and more, ensuring your code remains clean and maintainable.
* **Static Analysis:** Regularly use Xcode's built-in static analysis tool to detect potential
  memory leaks, logical errors, and other issues early in the development cycle.

### Dependency Management

* **CocoaPods for Managing Libraries:** Use CocoaPods, an Objective-C dependency manager, to
  integrate third-party libraries into your projects easily.
* Define your project's dependencies in a `Podfile`, and use CocoaPods to manage library versions
  and updates seamlessly.

### Additional Resources

- [Objective-C Programming Language Guide][ObjC Guide]: Offers an in-depth look at Objective-C's
  syntax, features, and best practices.
- [Apple's Objective-C Coding Guidelines][Apple Coding Guidelines]: Provides Apple's recommendations
  for writing Objective-C code.

[//]: # (links @formatter:off)

[fnd]: foundation.md
[fnd-formatting]: foundation.md#formatting
[fnd-naming]: foundation.md#naming-conventions
[ObjC Guide]: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html
[Apple Coding Guidelines]: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/CodingGuidelines.html

[//]: # (links @formatter:on)
