class: center, middle, inverse

# Introducción a la Programación I
Lists

---

# Agenda

- Lists
- Strings as Lists

---

# What is a List?

- A list is a collection of items in a particular order.
- They are mutable, which means values can be changed.
- In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
- Example:

```python
empty_list = []   # define an empty list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']   # define a list with elements
print(bicycles)   # print the list!
```

- If you ask Python to print a list, Python returns its representation of the list, including the square brackets:

```python
['trek', 'cannondale', 'redline', 'specialized']
```

---

# Lists - Indexes

- Python considers the first item in a list to be at position 0, not position 1, which is true for almost all programming languages.

.center[![List Index]({{site.baseurl}}/presentation/lists/list_index.png)]

---

# Accessing Elements in a List

- As lists are ordered, you can access any element in a list by telling Python the position, or index, of the item desired.
- To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
- Example:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']   # define a list with elements
one_item = bicycles[0]   # get the item in the index 0 of the list type variable called 'bicycles'
print(one_item)   # print the item
```
- When we ask for a single item from a list, Python returns just that item without square brackets, which means the item is not inside a list, it's just the item.

---

# Length of a List

- You can quickly find the length of a list by using the len() function.
- The same function as the one used in Strings is used here.
- Example:

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']   # define a list with elements in the shell interpreter
>>> len(cars)   # use the len() function with 'cars' as argument, which will return the amount of items it has
4
```

---

# Modifying elements in a List

- The syntax for modifying an element is similar to the syntax for accessing an element in a list.
- To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']   # define a list with elements
print(motorcycles)   # print the list

motorcycles[0] = 'ducati'   # replace item in index 0 with a new value
print(motorcycles)   # print the modified list
```

- The code above will print:

```python
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

---

# Adding Elements to a List - Append

- To add an element at the end of a list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')   # this method appends the element at the end of the list
print(motorcycles)
```

- Which prints the original list, and the list with the appended element:

```python
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

---

# Adding Elements to a List - Insert

- You can add a new element at any position in your list by using the insert() method.
- You do this by specifying the index of the new element and the value of the new item.
- Example:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')   # insert the value 'ducati' at index 0 (the beginning of the list)
print(motorcycles)
```

- This operation shifts every value from the given index to the end of the list one position to the right, resulting in:

```python
['ducati', 'honda', 'yamaha', 'suzuki']
```

---

# Removing Elements from a List

- To remove an element from a specific index:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # delete item in index 0
print(motorcycles)
```

- The 'del' statement before a List removes the element at said index, printing:

```python
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

---

# Working with Part of a List - Slice

- We learned how to access single elements in a list, and we can also work with a specific group of items in a list, which we call a slice.
- To make a slice, specify the index of the first and last elements you want to work with between brackets, separated by colon.
- First index is included, second index is excluded.
- It returns a **new** list, which means you should keep it in a new variable.
- Example:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
sliced_players = players[1:4]   # slice List 'players' from index 1 to 4
print(sliced_players) 
```

- *What does this code print?*

---

# Working with Part of a List - Slice

- We learned how to access single elements in a list, and we can also work with a specific group of items in a list, which we call a slice.
- To make a slice, specify the index of the first and last elements you want to work with between brackets, separated by colon.
- First index is included, second index is excluded.
- It returns a **new** list, which means you should keep it in a new variable.
- Example:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
sliced_players = players[1:4]   # slice List 'players' from index 1 to 4
print(sliced_players) 
```

- *What does this code print?*

- It prints indexes 1, 2, and 3 (as the second index is excluded):

```python
['martina', 'michael', 'florence']
```

---

# Working with Part of a List - Slice

- To show it graphically:

.center[![Sublist Substring]({{site.baseurl}}/presentation/lists/sublist_substring.png)]

---

# Working with Part of a List - Slice

- If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.
- Example:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])   # slice the List 'players' from index 0 to 4, and print it
```

- Which prints:

```python
['charles', 'martina', 'michael', 'florence']
```

---

# Working with Part of a List - Slice

- A similar syntax works if you want a slice from an index to the end of a list.
- Example:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])   # slice the List 'players' from index 2 to 5 (the end), and print it
```

- Which prints:

```python
['michael', 'florence', 'eli']
```

---

# Working with Part of a List - Slice

- The last two syntax can be merged to generate a list that goes from the beginning to the end.
- We use this to create a copy of a list (because it returns a new one!).
- It is called shallow copy.
- Example:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])   # slice the List 'players' from index 0 to 5 (the end), and print it
```

- Which prints:

```python
['charles', 'martina', 'michael', 'florence', 'eli']
```

---

# Strings as Lists

- As stated in the Strings presentation, a String is a sequence of characters.
- In Python, **a String is a List**.
- Go back to the first image in this presentation and see that list represents a String: List of characters.
- The most clear example is the `len()` function.
- Another example could be getting a character in an index of a String, or slicing the string to obtain only a part of it (called substring in other languages)
- But remember that Strings are not mutable. To modify a String, you need to create a new one from an existing one.

---


# List of lists

- It's a list whose components are themselves lists.
- Also known as multidimensional lists.
- Example:

```python
multi_list = [['a', 'b', 'c'], ['d', 'e']]
```

- This is a list where the index 0 has a list of length 3, and index 1 has a list of length 2.
- *How would we access element 'c' of a multidimensional list?*

---

# List of lists

- It's a list whose components are themselves lists.
- Also known as multidimensional lists.
- Example:

```python
multi_list = [['a', 'b', 'c'], ['d', 'e']]
```

- This is a list where the index 0 has a list of length 3, and index 1 has a list of length 2.
- *How would we access element 'c' of a multidimensional list?*

```python
multi_list[0][2]
```
