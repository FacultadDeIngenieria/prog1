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

- Similar to printing it's content, we can know how many characters a String has:

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

# Strings: ==, !=, <, >, <=, >= operators

- We can use these operators to know if two Strings are equal or not.
- If they are equal, **==** comparison returns *True* and if not, the **==** returns *False*
- Viceversa with **!=**

```python
print("Buenos Aires" == "Pilar") #False
print("Pilar" == "Pilar") #True

print("Buenos Aires" != "Pilar") #True
print("Pilar" != "Pilar") #False
```

- Comparing two Strings with this **<, >, <=, >=** operators will help us determine which comes first in a dictionary

```python
print("Buenos Aires" > "Pilar") #False
print("Buenos Aires" < "Pilar") #True
```

---

# Stripping Whitespace

- Extra whitespaces can be confusing in your programs and lead to bugs
- To ensure that no whitespace exists at the right end of a string use *rstrip()* method

```python
➊ >>> favorite_language = 'python '
➋ >>> favorite_language
	'python '
➌ >>> favorite_language.rstrip()
	'python'
➍ >>> favorite_language
	'python '
```

- In ➊ we have an extra right whitespace
- Asking Python its value evidence this (➋)
- When the rstrip() method acts on the variable favorite_language at ➌, this extra space is removed
- But asking for *favorite_language* value in (➍) shows the original value
- To remove it permanently, we have to associate the modified value to the variable

```python
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
	'python'
```

---

# Stripping Whitespace

- Similar to *rstrip()*, we have *lstrip()* and *strip()* methods
- *lstrip()* ensures us that no whitespace exists at the beginning of the string
- *strip()* combines *lstrip()* and *rstrip()*

```python
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
	' python'
>>> favorite_language.lstrip()
	'python '
>>> favorite_language.strip()
	'python'
```

---

# Formatting Strings with other variables values

- Many times we want to use a variable's value inside a string

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"Hello, {first_name} {last_name}!"
print(full_name) #Hello, ada lovelace!
```

- You do that by inserting an *f* befor opening a string
- f is for format, so these strings are called *f-strings*
- Constant string content can be mixed with variables
- You can modify the string variable using any of the seen methods first

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"Hello, {first_name.title()} {last_name.title()}!"
print(full_name) #Hello, Ada Lovelace!
```

---

# Python Library: String

- Python language, as any language, is fully documented
- One of the first thing you should seek when learning a new language
- For example, Strings methods in Python documentation:
  - https://docs.python.org/3/library/stdtypes.html#string-methods

---

# User input

- Many times, to make your programs interactive, you want to ask your user to enter a value
- For that, we use the built-in *input()* method

```python
>>> number = input('Ingrese un numero: ')
Ingrese un numero: 4
>>> number
'4'
```

- If we want to parse the input as a number, we have *int()* or *float()* built-in methods

```python
>>> int(number)
4
```