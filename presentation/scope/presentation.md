class: center, middle, inverse

# Introducción a la Programación I

Scope
---
# Python scope

 - The scope of a name defines the area of a program in which you can unambiguously access that name, such as variables, functions, objects, and so on.
 - A **name** will only be visible to and accessible by the code in its scope. It is importan to avoid name collisions and unpredictable behaviors.
 - Most commonly, you’ll distinguish two general scopes:
   - **Global scope**: The names that you define in this scope are available to all your code.
   - **Local scope**: The names that you define in this scope are only available or visible to the code within the scope.


> The term **name** refers to the identifiers of variables, constants, functions, classes, or any other object that can be assigned a name.
---
## Global Scope

 - This is the top-most scope in a Python program.
 - This  scope contains all of the names that you define at the top level of a program.
 - Names in this Python scope are visible from everywhere in your code.

```python
>>> def any_function():
>>>		print(my_var)
>>> my_var = 10
>>> print(my_var)
>>> any_function()
10
10
```
---
## Functions: Local Scope
 - This is the scope created at function calls.
 - Every time you call a function, you’re also creating a new local scope.
 - Parameters and variables that you assign inside a function exist only within the local scope associated with the function call
 - When the function returns, the local scope is destroyed and the names are forgotten.
---
## Functions: Local Scope
```python
>>> def square(base):
...     result = base ** 2
...     print(f'The square of {base} is: {result}')
...
>>> square(10)
The square of 10 is: 100
```
This is a normal usage of a function
```python
>>> result
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    result
NameError: name 'result' is not defined
```
We can see that *result* exists exclusively within the local scope of a function call.
```python
>>> base
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    base
NameError: name 'base' is not defined
```
The same happens with *base*. It is not accessible from outside the function.

---
# Global scope inside a function
 - However, we can force a variable to be **global**, even when it is defined inside a function, using the **global** keyword before the name.
```python
>>> def square(base):
...     global result
...     result = base ** 2
...     print(f'The square of {base} is: {result}')
...
>>> square(10)
The square of 10 is: 100
>>> result
100
```
 - Beware that if you don't call the function before, *result* won't exist.
