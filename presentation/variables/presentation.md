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
*What ouput will this new program produce?*

--

#### 
The same!

![Hello World Terminal]({{site.baseurl}}/presentation/hello-world/hw-terminal.png)

---

layout: false

# Naming Variables

- There are some conventions to follow, every language has them
- Variable names:
- Can contain only letters, numbers and/or underscores (_)
- Can start with letter or underscore, but **not** a number
  - Valid: *message_1*, invalid: *1_message*
- Spaces are **not** allowed in names (use underscores)
  - Valid: *greeting_message*, invalid: *greeting message*
- Do not use language reserve words in them as they have a particular programatic purpose or meaning
- They should be short, but descriptive
  - *name* better than *n*
  - *student_name* better than *s_n*
  - *name_length* better than *length_of_person_name*
- Avoid starting with upper case letter your names
- Name consistently

```python
# The following program will print a Hello World message to the screen
message = "Hello World!"
print(mesage)
```

---

# So... what is a variable?

- Classic definition, *boxes where you can store values in*
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
speed = 0

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
>>> 3 ** 2
9
```

- What does the ** do?
- All the maths laws apply here: multiple operations in one expressions are valid, and you can alter the expression using parenthesis

```python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

- Spacing has no effect, only enhances the operation's evaluation at first sight

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