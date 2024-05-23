class: center, middle, inverse

# Introducción a la Programación I
Tuples

---

# Agenda  

- What is a tuple?
- How does a tuple look like in Python?

---

# What is a tuple?

A tuple is a data structure that stores an ordered collection of values.
Tuples are similar to lists, but they are immutable, meaning that the values
inside a tuple cannot be changed.


---

# Tuples in python

Python represents tuples using parentheses ().

### Examples of tuples

```python
empty_tuple = () # empty tuple

fruits = ("apple", "banana", "cherry")

coordinates = (3, 4)
```

---

# Accessing values 

You can access the value at a specific index using the square bracket notation.

```python
fruits = ("apple", "banana", "cherry")

print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[-1]) # cherry
```

---

# Updating values

Tuples are immutable, so you cannot add or update values once the tuple is created.
```python
fruits = ("apple", "banana", "cherry")
fruits[0] = "orange" # TypeError: 'tuple' object does not support item assignment
```
--- 

# Removing Entries

You cannot remove individual elements from a tuple, but you can delete the entire tuple.

```python
fruits = ("apple", "banana", "cherry")
del fruits[0] # TypeError: 'tuple' object doesn't support item deletion
```

---

# Tuple Methods

Tuples have only two methods: count() and index().

```python
fruits = ("apple", "banana", "cherry")
fruits.count("apple") # 1, as the amount of "apple" in the tuple is 1
fruits.index("banana") # 1, as the index of "banana" in the tuple is 1

names = ("Alice", "Bob", "Alice")
names.count("Alice") # 2, as the amount of "Alice" in the tuple is 2
names.index("Bob") # 1, as the index of "Bob" in the tuple is 1
```

---


# Iterating Through a Tuple

You can iterate through a tuple using a for loop, a for in range loop and a while.
You can also use enumerate with tuples

```python
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
    
for i in range(len(fruits)):
    print(fruits[i])
    
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

for index, fruit in enumerate(fruits):
    print(index, fruit)

```

---

# Tuple Unpacking

You can unpack a tuple into multiple variables.

```python
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a) # apple
print(b) # banana
print(c) # cherry
```

---

# Tuple Packing

You can pack multiple values into a tuple.

```python
fruits = "apple", "banana", "cherry"
print(fruits) # ('apple', 'banana', 'cherry')
```

---

# Tuple Concatenation

You can concatenate two or more tuples using the + operator.

```python
fruits = ("apple", "banana", "cherry")
colors = ("red", "yellow", "pink")
fruits_colors = fruits + colors
print(fruits_colors) # ('apple', 'banana', 'cherry', 'red', 'yellow', 'pink')
```

---

# Tuple Slicing

You can slice a tuple using the colon operator.

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits[1:3]) # ('banana', 'cherry')
print(fruits[:3]) # ('apple', 'banana', 'cherry')
print(fruits[3:]) # ('date', 'elderberry')
```

---

# Use Cases

- Tuples are used to store multiple values in a single variable.

```python
coordinates = (3, 4)
```

- Tuples are used to return multiple values from a function.

```python
def get_coordinates():
    return 3, 4

x, y = get_coordinates()
```

---

- Tuples are used to store fixed-size data, such as days of the week, months of the year, etc.

```python
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
```
