class: center, middle, inverse

# Introducción a la Programación I
Strings

---

# Agenda

- Strings
- Capture user input

---

# Strings

- A *string* is a sequence or series of characters inside quotes
  - Many languages have the same definition
  - Python: single quoted **'** or double quoted **"** are the same
  - In Java only double quoted

```python
message = "This is a string."
also_message = 'This is also a string.'
```

- Simplest operation with a String: 
  - concatenate it with another one using the **+** operator

```python
hello_world = "Hello," + " world" + "!"
print(hello_world)
```

- Similar to printing it's content, we can know how many characters a String has

```python
hello_world = "Hello," + " world" + "!"
print(len(hello_world)) #13
```

---

# Methods and Strings

- Another simple thing to do with a String is change the case of it

```python
name = "ada lovelace"
print(name.title())

#Save this file as name.py, and then run it. You should see this output:
Ada Lovelace
```

- Variable *name* refers to the lowercase *"ada lovelace"* string.
- The method *title()* appears after the variable
- A *method* is an action that the language (Python) can perform over a piece of data.
- The dot **.** here implies that the action *title()* is performed over the variable *name*
- Any method is followed by parentheses because often they need more data to perform the action (not in this case)
- Finally, as you may guessed, changes each word to title case, where each words starts with a capital letter
- We are going to study many methods in the following slides

---

# String methods: upper() & lower()

- Other useful methods that deal with cases: *upper()* and *lower()*

```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# This will display the following:
ADA LOVELACE
ada lovelace
```

- *lower()* is particularly useful when you want to store data independently of how the user entered it in the first place

---