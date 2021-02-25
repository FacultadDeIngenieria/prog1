class: center, middle, inverse

# Introducción a la Programación I
Variables

---

# Agenda

- Variables
- Primitive data types
- Operators (Cast)

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




