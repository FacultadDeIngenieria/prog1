class: center, middle, inverse

# Introducción a la Programación I
Variables

---

# Agenda

- Variables
- Numeric data types
  - Integers
  - Floats

---

layout: true

# Variables

---

- Let's modify our **hello_world.py** to use one variable named **message**
- Every variable is connected to a **value**

*Can you guess how that modification will look like?*

--

```python
# The following program will print a Hello World message to the screen
message = "Hello World!"
print(message)
```
*What output will this new program produce?*

--

#### 
The same!

![Hello World Terminal]({{site.baseurl}}/presentation/hello-world/hw-terminal.png)

---

layout: false

# Naming Variables

- There are some conventions to follow, every language has them
- Variable Names:
	- Are case sensitive: x != X
	- Can contain only letters, numbers and underscores (_)
	 - This method of writing is known as **snake_case**
	- Can start with letter or underscore, but **not** a number
	  - Valid: *message_1*, invalid: *1_message*
	- Spaces are **not** allowed in names (use underscores)
	  - Valid: *greeting_message*, invalid: *greeting message*
	- Do not use language reserved words, as they have a particular programatic purpose or meaning
	- They should be short, but descriptive:
	  - *name* better than *n*
	  - *student_name* better than *s_n*
	  - *name_length* better than *length_of_person_name*
	- Avoid starting with upper case letter your names
	- Name consistently

```python
# Will the following program print a Hello World message to the screen?
message = "Hello World!"
print(mesage)
```

---

# So... what is a variable?

- Classic definition: *boxes where you can store values in*
- Super helpful idea
- We often draw the concept that way
- Not an **accurate** way to describe how languages (Python, Java) **represent them internally**
- Better to think them as *labels that you can assign to values*
- Much better *a variable references a certain value*

---

# Numbers

- Most programs define and gather some sort of data to do something useful with it
- It helps to classify different types of data, lets start with numbers
- Numbers are used quite often in programming
  - Scores, data, information
- Divided in:
  - Integers
  - Floats
- *Can you guess their main difference?*

---

# Creating an Integer variable

- Integers represents the numbers that can be written without a fractional component
- To create an integer variable, you simply use the *assignment* operator **=**

```python
# Some samples
actual_speed = 100
low_speed = 10
average_speed = actual_speed - low_speed

local_score = 2
away_score = 1
```

---

# Other operations with Integers

- You can add (+), subtract (-), multiply (*), and divide (/) integers in Python:

```python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

- All the maths laws apply here: multiple operations in one expressions are valid, and you can alter the expression using parenthesis (we will see precedence rules later)

```python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

- Spacing has no effect, only enhances the operation's evaluation at first sight

---

# Other operations with Integers

- You can alse use power (**), integer division (//) and module (%) in Python:

```python
>>> 2 ** 3
8
>>> 7 // 3
2
>>> 7 % 3
1
>>> 3 / 2
1.5
>>> 3 % 2
1
```
---

# Precedence rules

- Precedence follows the PEMDAS rules: *Parentheses, Exponents, Multiplication - Division, Addition - Subtraction*

*1st* Parentheses:
```python
>>> (5 + 1) / 3 = 2
>>> 5 + 1 / 3 = 5.333333
```
 
*2nd* Exponents:
```python
>>> 5 ** 2 - 2 = 23
>>> 2 * 5 ** 2 = 100
```
 
*3rd* Multiplication - Division (- Integer Division - Module):
```python
>>> 1 + 2 * 3 = 7
```

*4th* Addition - Substraction
```python
>>> 3 + 8 / 2 = 7
```

---

# Floats

- They are used to represent any number with a decimal point (same as many programming languages)
  - Refers to the fact that a decimal point can appear at any position in a number (floating)
- Their use is straighforward, things will likely happend as expected

```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

- **Likely... :-)**

```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

???

This happens in all languages and is of little concern. Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally. Just ignore the extra decimal places for now

---

# Integers and Floats

- Operations, as in math, are the same and valid for both
- Dividing two numbers, even integers, produce always a float
- The mix also produce a float

```python
#Two integers
>>> 4 / 2
2.0

#Mixing
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

- What if we want to convert a float into an integer?
  - We use the built-in function *int()*

```python
>>> int(5.6)
5
```

---

# Underscores and multiples

- When writing long numbers, digits can be grouped using **_** (NOTE: what happens when you print it?)

```python
>>> universe_age = 14_000_000_000

>>> print(universe_age)
14000000000
```

- You can assign values to more than one variable in a single line

```python
>>> x, y, z = 0, 0, 0
```

- We can assign the same value to multiple variables

```python
>>> x = y = z = 0
```