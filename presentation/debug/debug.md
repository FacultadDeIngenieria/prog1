class: center, middle, inverse

# Debugging in Python

---

## Introduction to Debugging

- What is Debugging?

Debugging is the process of identifying, analyzing, and fixing errors, or bugs, in a computer program. It helps ensure that the program functions correctly and produces the expected results. Debugging involves systematically troubleshooting to locate the source of the problem and then applying a solution to fix it.

- Key Aspects of Debugging

* `Identifying the Issue`: The first step in debugging is identifying that there is an issue or bug in the program. This can be done by observing incorrect behavior, unexpected output, or error messages.
* `Isolating the Problem`: Once the issue is identified, the next step is to isolate the problem. This involves narrowing down the scope of the issue to understand where exactly the error is occurring in the code.
* `Analyzing the Cause`: After isolating the problem, the cause of the issue needs to be analyzed. This can involve examining the code logic, data flow, and program state to understand why the error is happening.
* `Fixing the Bug`: Once the cause of the issue is understood, a solution or fix can be implemented to correct the error. This may involve modifying the code, adjusting the logic, or applying a patch to address the problem.
* `Testing the Fix`: After applying the fix, it's crucial to test the program to ensure that the issue has been resolved and that the program behaves as expected without introducing new bugs.

---

## Common Errors in Python

- Syntax Errors
- Runtime Errors
- Logical Errors

---

## Common Errors in Python: Syntax Error

A Syntax Error in Python occurs when the code you've written doesn't follow the correct syntax or grammar defined by the Python language. This means Python is unable to understand the code you've written, leading to a syntax error.

Example:

```python
# Incorrect usage of the print function
print "Hello, World!"
```

How does it fail?

```python
  File "<stdin>", line 1
    print "hola"
    ^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

---

## Common Errors in Python: Runtime Errors

A Runtime Error in Python occurs when the code is syntactically correct, but an error occurs while the program is running. These errors are also known as exceptions and can be caused by various reasons such as division by zero, accessing an index out of range, or trying to convert a string to an integer when the string doesn't represent a valid integer.

Example:

```python
# Attempting to divide by zero
result = 10 / 0
```

How does it fail?

```python
>>> result = 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

---

- Logical Errors

A Logical Error occurs when the code is syntactically correct, and it runs without raising any exceptions, but it does not produce the expected or desired output due to flawed logic or incorrect algorithms. Unlike Syntax Errors or Runtime Errors, Logical Errors do not cause the program to terminate abnormally or produce error messages; instead, they cause the program to behave unexpectedly or incorrectly.

Example:
```python
# Program to calculate the average of two numbers
def calculate_average(num1, num2):
    total = num1 + num2
    average = total / 3  # Incorrect calculation
    return average

# Test the function
result = calculate_average(5, 10)
print(f"The average is: {result}") # prints 5. Should be 7.5
```

---

## Python Debugging Tools

- print() Statements
- Logging
- Using an IDE (Integrated Development Environment). Example Pycharm or VSCode for example.

