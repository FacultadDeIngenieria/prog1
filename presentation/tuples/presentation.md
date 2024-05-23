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

