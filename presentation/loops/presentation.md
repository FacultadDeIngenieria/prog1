class: center, middle, inverse

# Introducción a la Programación I
Loops

---

# Agenda

- For
- While

---

# For

- We already learned how to create Lists and how to work with specific elements in a List.
- Example:

```python
magicians = ['alice', 'david']

print(magicians[0])
print(magicians[1])
```

- *What if the length of the List changes?*

---

# For

- Looping allows you to take the same action, or set of actions, with every item in a list.
- Work efficiently with lists of any length, including those with thousands or even millions of items.
- Here, **indentation** is extremely important.

---

# For - Example

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

- First line: we define a List of elements.
- Second line: we define a **for** loop.
    - This line tells Python to pull a name from the list *magicians*, and associate it with the variable *magician*.
- Third line: print the name that’s just been assigned to the variable *magician*.

- Python then **repeats** the second and third line, once for each name in the list
- How we read this: For every magician in the list of magicians, print the magician’s name.
- Output is:

```python
alice
david
carolina
```

---

# For - Another example

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

This will print:

```python
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

- A *for* loop can have as many lines as you want, **indentation** is important.

---

# For with range()

The **range()** function creates a sequence of numbers.
The syntax is **range (start, stop, step)**, or **range (start, stop)** or simply **range (stop)**



```python
print("Let's see the square of the first 10 pair numbers.")
for pair_number in range (0, 20, 2):
    print(f"The square of {pair_number} is {pair_number**2}")
```

This will print:
```python
Let's see the square of the first 10 pair numbers.
The square of 0 is 0
The square of 2 is 4
The square of 4 is 16
The square of 6 is 36
...
```
As usual, the "stop" index is not included.

---

# For with range()

You can also use a negative step. For example:

```python
print("An inversed list of numbers")
for number in range (10, 0, -1):
    print(number)
```
This will print:
```python
10
9
8...
```
**range()** is frequently combined with lists. For example:
```python
magicians = ['alice', 'david', 'carolina']
for index in range(len(magicians)):
    print(f'{index}. {magicians[index].title()}')
```
This will print:
```python
1. Alice
2. David
3. Carolina
```
---

# Looping a multi array

- *How would we print all elements in a multi array?*

---

# Looping a multi array

- *How would we print all elements in a multi array?*

```python
magician_groups = [['alice', 'david'], ['carolina']]
for magician_group in magician_groups:
    for magician in magician_group:
        print(magician)
```

---

# While

- The for loop takes a collection of items and executes a block of code once for each item in the collection.
- In contrast, the while loop runs as long as a certain condition is true.

---

# While - Example

- The following while loop counts from 1 to 5:

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1
```

- The while loop is set to keep running as long as the value of current_number is less than or equal to 5.

---

# While - Complex example

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = prompt + "\nEnter 'quit' to end the program.\n"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message) 
```

- *What does this example do? Try it!*
---

# While - Complex example

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = prompt + "\nEnter 'quit' to end the program.\n"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message) 
```

- *What does this example do? Try it!*
- *What if we don't want to care about the case?*

---
# Warning!

Although **while** may seem similar to **if**, they are essentially different!
**while** is always for **loops** (repetitive structures), and **if** only for simple decisions (conditional structures).

Try the next excercise:

Ask the user for positive numbers, and store them in a list. To terminate the list, the user should enter '0'. Afterward, display the numbers in reverse order.

---

# Exiting a loop

 - It is possible to exit a loop anytime, with the **break** statement.
 - Suppose you want to terminate a loop and skip to the next code after the loop; **break** will help you do that.
 - A typical scenario of using the **break** in Python is when an external condition triggers the loop's termination.

For example:
```python
sum = 0
for i in range(10):
    n = int(input('Insert a positive number: ')
    if n<0:
        break
    sum = sum + n
print(f'The sum of yur numbers is {sum}')

```

