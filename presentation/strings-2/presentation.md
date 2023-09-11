class: center, middle, inverse

# Introducción a la Programación I
Strings ( part 2 )

---


## Multiline Strings

You can assign a multiline string to a variable by using three quotes:

```python
>>> long_text = """Today is a great day!
... I feel like going fishing."""  
>>> print(long_text)
Today is a great day!
I feel like going fishing.
```
Another way to do this is with **\n** (already seen), but it's harder to read.

---
## Check String

To check if a certain phrase or character is present in a string, we can use the keyword  `in`.

```python
>>> txt = "The best things in life are free!"  
>>> print("free" in txt)
True
>>> print("expensive" in txt)
False
```
Similarly we can use `not in`.

```python
>>> print("free" not in txt)
False
>>> print("expensive" not in txt)
True
```

---
# Slicing Strings

You can return a range of characters by using the *slice* syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
Remember that strings start at position **0**.
There are many ways to *slice* a string. We always use **[...]** after the name of the string variable.

---
# Slicing Strings
## Simple character
If we use a simple number, we get the character at that position. The number can't be bigger than the size of the string.
If the number is negative, we start from the end, counting to the left. This is called *Negative indexing*.
```python
>>> txt = 'Python is a great programming language'
>>> txt[0] # character at position 0
'P'
>>> txt[5] # character at position 5
'n'
>>> txt[-1] #  last character
'e'
>>> txt[-2] # second to last character
'g'
>>> txt[45] # character at position 5
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
---
# Slicing Strings
## Contiguous characters
If we use a pair of numbers separated by colons, we get a group of characters. The first number is the start index (and this character is included), and the second one si the end index (which is never included).

```python
>>> txt = 'Python is a great programming language'
>>> txt[12:17] # characters from 13 to 17 (last is not included)
'great'
```
Be careful with these other examples...
```python
>>> alarmist = "Never press this button!"[6:]
>>> hater = "I hate seeing you sad"[:17]
```

---
# Slicing Strings
## Contiguous characters
Skipping a number means getting all the characters from the beginning or to the end, respectively. We can also use negative indexes too.
```python
>>> txt[19:] # from 19 to the end
'programming language'
>>> txt[:9] # from the start to 9 (not included)
'Python is'
>>> txt[-8:] # from -8 to the end
'language'
>>> txt[:-9] # from the start to -9 (not included)
```
---
## Not contiguous characters and reverse order
If we add a third number, it means that we get skipped characters. A **2** means *every two characters*.
If the third number is negative, we get the slice in reverse order. In this case, the first number must refer to a later character than the second one.
```python
>>> txt = 'Python is a great programming language'
>>> txt[7:15:3] # from character 7 to 15 (not included), every 3 characters
'iar'
>>> txt[16:9:-1] # from character 16 to 9 (not included), in reverse order.
'taerg a'
```

What woud this print?
```python
>>> txt[-7:-20:-2]
```
---
## Modifying a String
Strings can't be modified using slices.
```python
>>> txt = 'Python is a great programming language'
>>> txt[0:6] = 'Java  '
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment't
```
To do this, we should rewrite the string variable by assigning it a new value.
```python
>>> txt = 'Java' + txt[7:] + ' too'
>>> txt
'Java is a great programming language too'
```
---
# Other string methods
There are many useful methods for strings. We will see a few.
We always write them after the name of the string variable, conected with a dot, like this: ***string_variable.method(parameters)***


### Replacing characters
**.replace(*old_string*, *new_string*)** returns a string where old_string is replaced by new_string. Let's see how to use it.
```python
>>> txt = 'Python is a great programming language'
>>> print(txt.replace('Python','Java'))
Java is a great programming language
```
But this method doesn't modify the string. It just returns the modified string. To change the original string, we should rewrite it.
```python
>>> txt = txt.replace('Python','Java')
>>> txt
'Java is a great programming language'
```
---
### Counting values in string
**.count(string)** returns counts the number of times a specified value occurs in a string. If the value is not in the string, 0 is returned. For example:
```python
>>> txt = 'Python is a great programming language'
>>> print(txt.count('n'))
2
>>> print(txt.count('gre'))
1
>>> print(txt.count(' '))
5
>>> print(txt.count('!'))
0
```
