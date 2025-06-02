class: center, middle, inverse

# Exceptions

---

# What Is an Exception?

- An **exception** is an event that disrupts the normal flow of program execution.
- It occurs when a runtime error happens (e.g., division by zero or accessing an out-of-range index).
- Exception handling allows you to:
    - Detect and respond to errors in a controlled way.
    - Prevent the program from terminating abruptly.
    - Separate main program logic from error-handling logic.

---

# Why Do We Need Exception Handling?

- **Robustness:** Enables the program to continue running even if an unexpected error occurs.
- **Clarity:** Error-handling code (`except` block) is kept separate from “happy path” code (`try` block).
- **Error Propagation:** If a function cannot handle a certain exception, it can let it “bubble up” to the caller for handling.
- **Maintainability:** Simplifies error detection and correction by centralizing error handling.

---

# Basic Syntax: try / except

```python
try:
    # Protected block: code that might raise an exception
    result = 10 / divisor
    print("The result is:", result)
except ZeroDivisionError:
    # Executes if a ZeroDivisionError occurred
    print("Error: Division by zero is not allowed.")
```

---

# else and finally Blocks

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
else:
    # Executes only if NO exception occurred
    print("File content:")
    print(content)
finally:
    # Executes always, whether an exception occurred or not
    print("Closing the file (if it is open).")
    try:
        file.close()
    except NameError:
        pass
```

- **else:**  
  - Runs only if the `try` block did not raise an exception.  
  - Useful for logic that should execute only when there are no errors.
- **finally:**  
  - Always runs, regardless of whether an exception was raised.  
  - Ideal for releasing resources (closing files, connections, etc.).

---

# Catching Multiple Exceptions and the Generic Block

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("Error: You must enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    # Catches any other unexpected exception
    print("An unexpected error occurred:", e)
else:
    print("Successful calculation. Result:", result)
```

- You can list multiple exceptions in a single `except`:
  ```python
  except (ValueError, TypeError):
      print("Type or value error.")
  ```
- `except Exception as e:`  
  - Catches any exception derived from `Exception` (most common ones).  
  - The variable `e` holds the exception instance, useful to view the error message.

---

# Raising Exceptions with raise

- Sometimes we want to explicitly generate an exception when a special condition is detected.  
- We use the `raise` statement.

```python
def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return x ** 0.5

try:
    result = calculate_square_root(-4)
    print("Result:", result)
except ValueError as ve:
    print("Error in calculate_square_root function!", ve)
```

- `raise ErrorType("Explanatory message")` throws the exception.  
- Allows **argument validation** or **internal condition checks** in functions and classes.

---

# Built-In Exceptions

- **ArithmeticError**: base class for arithmetic errors.  
  - `ZeroDivisionError`  
  - `OverflowError`  
- **ValueError**: invalid value error (e.g., converting "abc" to integer).  
- **TypeError**: operation or function applied to an inappropriate type (e.g., adding integer and string).  
- **IndexError**: index out of range in list, tuple, or string.  
- **KeyError**: key does not exist in dictionary.  
- **FileNotFoundError**: file or directory not found.  
- **IOError / OSError**: input/output or system-related errors.

```python
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index is out of range!")
```

---

# Inspecting Exception Information

When you catch with `as`, you can inspect the exception object:

```python
try:
    number = int("twenty")
except ValueError as error:
    print("Caught ValueError:", error)        # Shows internal message
    print("Exception type:", type(error).__name__)  # Name of the exception
```

- `error.args` contains a tuple with the arguments passed when raising the exception.  
- The `traceback` shows the call sequence that led to the exception.  
  You can obtain it using the `traceback` module:
  ```python
  import traceback

  try:
      1 / 0
  except ZeroDivisionError:
      traceback.print_exc()
  ```

---

# Best Practices for Handling Exceptions

1. **Do not use exceptions for normal flow**  
   • Only for unexpected situations or errors.  
2. **Catch the most specific exception possible**  
   • Avoid generic `except Exception:` unless absolutely necessary.  
3. **Never “silence” exceptions without reason**  
   • An empty `except:` block hinders debugging.  
   ```python
   try:
       # …
   except:
       pass  # Avoid this! Better to at least log or print the error.
   ```
4. **Release resources in `finally` or use context managers**  
   • Files, connections, sockets, etc.  
   ```python
   with open("file.txt", "r") as f:
       content = f.read()
   # No need for finally to close the file.
   ```
5. **Document exceptions a function can raise**  
   • In the docstring, indicate possible errors.

---

# Practical Examples

## Example 1: Read an Integer from User

```python
def request_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

age = request_integer("Enter your age: ")
print("Entered age:", age)
```

- Repeats the prompt until the user enters a valid integer.  
- Prevents the program from crashing with a `ValueError`.

---

# Summary and Conclusions

- **Exception:** mechanism to handle runtime errors.  
- **Main blocks:**  
  - `try`: code that might fail.  
  - `except`: error handling.  
  - `else`: optional, runs if no exception occurred.  
  - `finally`: always runs.  
- **Exception types:** built‐in (ValueError, TypeError, etc.) and custom.  
- **Best practices:**  
  1. Catch specific exceptions.  
  2. Do not use exceptions for normal logic.  
  3. Release resources with `finally` or `with`.  
  4. Document possible errors in docstrings.