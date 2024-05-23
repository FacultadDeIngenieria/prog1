class: center, middle, inverse

# Introducción a la Programación I
Maps

---

# Agenda  

- What is a map?
- How does a map look like in Python?

---

# What is a map?

A map is a data structure is a data structure that stores key-value pairs. Each key is unique,
and it maps to a specific value. Maps are used to quickly retrieve, update, and delete values
based on their keys.

- Keys on a map can be of any type that can be compared with others of its kind. We could have
strings, numbers, booleans and even complex types as keys, as long as we can compare two
values of that kind.

- Values on a map can be of any type at all

---

# Maps in Python

Python calls its maps dictionaries, and the type it gives to them is `dict`

### Examples of maps

```python
student_ages = dict() # empty dict

students_ages = {
  "Micaela": 18,
  "Francisco": 19,
  "Mirtha": 22,
  "José": 27
}

full_airport_name = {
  "AEP": "Aeroparque Jorge Newbery",
  "EZE": "Aeropuerto Internacional Minisitro Pistarini",
  "CPC": "Chapelco - Aviador Carlos Campos"
}

```
---

# Accessing values 

You can access the value associated with a specific key using the square bracket notation.

```python
print(full_airport_name["AEP"]) # Aeroparque Jorge Newbery
```

---

# Adding and Updating Entries

To add a new key-value pair or update the value for an existing key, use the assignment operator =.

```python
# Adding a new entry
student_scores["David"] = 88

# Updating an existing entry
student_scores["Alice"] = 95
```

If the key exists, it will be updated. If the key was not present, it will be created.

--- 

# Removing Entries

### Using del

```python
del student_scores["Bob"]
```

### Using pop
```python
student_scores.pop("Charlie")
```

---

# Dictionary Methods

Dictionaries come with several useful methods:

	•	keys(): Returns a view object that displays a list of all the keys 
            in the dictionary.
	•	values(): Returns a view object that displays a list of all the values 
            in the dictionary.
	•	items(): Returns a view object that displays a list of dictionary’s 
            key-value tuple pairs.


---

# Keys

```python
student_scores = {
  "Alice": 85,
  "Bob": 70,
  "Charlie": 60
}

print(student_scores.keys()) # dict_keys(['Alice', 'Bob', 'Charlie'])
```

---

# Values

```python
student_scores = {
  "Alice": 85,
  "Bob": 70,
  "Charlie": 70
}
print(student_scores.values()) # dict_values([85, 70, 70])
```


---

# Items

```python
student_scores = {
  "Alice": 85,
  "Bob": 70,
  "Charlie": 60
}
print(student_scores.items()) # dict_items([('Alice', 85), ('Bob', 70), ('Charlie', 60)])
```

---

# Iterating Through a Dictionary

You can loop through a dictionary using a for loop to access keys, values, or key-value pairs.

```python
# Iterating through keys
for key in student_scores:
    print(key)

# Iterating through values
for value in student_scores.values():
    print(value)

# Iterating through key-value pairs
for key, value in student_scores.items():
    print(key, value)
```

