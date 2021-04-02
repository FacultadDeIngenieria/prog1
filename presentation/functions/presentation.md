class: center, middle, inverse

# Introducción a la Programación I
Functions

---

# Agenda

- Functions
- Parameters and arguments
- Returning values

---

# What is a function?

- Named block of code that is designed to perform one specific task
- Any time we want to perform such task, we call / invoke the function by its name
- We can do this as many times as needed, any time we need to perform that action
- Using functions makes our programs easier to
 - write them: reuse
 - read them: naming
 - test them: one test for all usages
 - fix them: one fix for all usages
- *Can you give examples of Python's built-in functions?*

---

# Defining and using a function

```python
➊ def greet_user():
➋	"""Display a simple greeting."""
➌	print("Hello!")

➍ greet_user()
```

- In ➊ we use the keyword *def* to inform Python that we’re defining a function
 - Tells Python the **name** of the function 
 - (Optional) What kind of information the function needs to do its job between parentheses hold that information.
 - Ends in a colon **:**
- All the indented lines that follow *def greet_user():* make up the *body* of the function. 
- In ➋ is a comment called a docstring, which describes what the function does. 
- In ➌ we have the only line of actual code in the body of this function
- Then in ➍, we have a sample of how to call it
- As expected, it prints Hello!:

```
Hello!
```

---

# Passing Information to a Function

- We can modified slightly, the function greet_user() also greet the user by name
- We need to modify it to add *username* in the parentheses of the function’s definition at *def greet_user()* 
 - Now it can accept any value of username we specify
- Defined like this, the function expects we provide a value for *username* to work

```python
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('jesse')
```

- It now prints:

```
Hello, Jesse!
```

---

# Arguments and Parameters

- Let's focus on the previous example
- Variable *username* in function's definition is an example of a *parameter*
 - A parameter is a piece of information the function needs to do its job
- On the other hand, the value *'jesse'* is an example of an *argument*
 - An argument is a piece of information that’s passed from a function call to a function.
- It's important to make this distinction, as often they are used interchangeably
- A function definition can have multiple *parameters*, so a function call may need multiple *arguments* 
- We can pass arguments to our functions in a number of ways
 - **Positional** arguments: they need to be in the same order 
the parameters were written
 - **Keyword** arguments: each argument consists of a variable name and a value

---

# Positional arguments

- When we call a function, Python must match each *argument* in the function call with a *parameter* in the function definition
- The simplest way to do this is based on the order of the arguments provided
- Values matched up this way are called **positional arguments**

```python
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

```
I have a hamster.
My hamster's name is Harry.
```

- Order matters in positional arguments
 - We can get unexpected results if we mix up the order of the arguments in a function call when using positional arguments

---

# Multiple Function Calls

- We can call a function as many times as needed 
- Following last example, describing a second pet requires just one more call to *describe_pet()*

```python
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

- Calling a function multiple times is a very efficient way to work
- The code describing a pet is written once in the function, used many times

---

# Return Values

- A function doesn’t always have to display its output directly
- Instead, it can process some data and then return a value or set of values
- The value the function returns is called a **return value**
- The *return* statement takes a value from inside a function and sends it back to the line that called the function

```python
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
 - Can you tell me the function's name?
 - How many parameters does the function has?
 - Which are their names?
 - What does the function do?

- When we call a function that returns a value, we need to provide a variable that the return value can be assigned to