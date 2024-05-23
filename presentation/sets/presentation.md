class: center, middle, inverse

# Introducción a la Programación I
sets

---

# Agenda  

- What is a set?
- How does a set look like in Python?

---

# What is a set?

A set is a data structure that stores an unordered collection of unique values.
Sets are similar to lists, but they do not allow duplicate values.


---

# Tuples in python

Python represents sets using curly braces {}.


### Examples of sets

```python
empty_set = set() # empty set

fruits = {"apple", "banana", "cherry"}

numbers = {1, 2, 3, 4, 5}

```

---

# Accessing values


You cannot access values in a set using an index, as sets are unordered collections of values.


```python
fruit[0] # TypeError: 'set' object is not subscriptable

```

---

# Updating values

Sets are mutable, so you can add and remove values from a set.

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("date")
print(fruits) # {'apple', 'banana', 'cherry', 'date'}
```
--- 

# Removing Entries

You can remove values from a set using the remove() or discard() methods.

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # {'apple', 'cherry'}

fruits.discard("apple")
print(fruits) # {'cherry'}

fruits.remove("banana") # KeyError: 'banana'
fruits.discard("banana") # No error
```

---

# Tuple Methods


Sets have several methods that you can use to manipulate them. Some of the most common methods are:

- add(): Adds an element to the set.
- remove(): Removes an element from the set. If the element is not present, it raises a KeyError.
- discard(): Removes an element from the set. If the element is not present, it does not raise an error.
- pop(): Removes and returns an arbitrary element from the set.
- clear(): Removes all elements from the set.
- copy(): Returns a shallow copy of the set.
- union(): Returns a new set containing all the elements from the original set and another set.
- intersection(): Returns a new set containing only the elements that are present in both sets.
- difference(): Returns a new set containing only the elements that are present in the original set but not in the other set.

---

# Set union

You can combine two sets using the union() method or the | operator.

```python
fruits = {"apple", "banana", "cherry"}
colors = {"red", "yellow", "pink"}
fruits_colors = fruits.union(colors)
print(fruits_colors) # {'apple', 'banana', 'cherry', 'red', 'yellow', 'pink'}
```

---

# Set intersection

You can find the common elements between two sets using the intersection() method or the & operator.

```python
fruits = {"apple", "banana", "cherry", "orange"}
colors = {"red", "yellow", "pink", "orange"}
common = fruits.intersection(colors)
print(common) # {'orange'}
```

---

# Set difference


You can find the elements that are present in the first set but not in the second set using the difference() method or the - operator.

```python
fruits = {"apple", "banana", "cherry", "orange"}
colors = {"red", "yellow", "pink", "orange"}
diff = fruits.difference(colors)

print(diff) # {'apple', 'banana', 'cherry'}
```

---
# Iterating Through a Set

You can iterate through a set using a for loop.

```python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```