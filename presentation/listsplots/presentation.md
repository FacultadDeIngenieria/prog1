class: center, middle, inverse

# Introducción a la Programación I
List Comprehension & Plots

---

# Agenda

- Ranges
- List Comprehensions
- Plots

---

# Numerical lists

- Up until now we discussed and talk about *lists of Strings*, but there are many use cases where storing a *set of numbers* makes a lot of sense:
 - Keep track of positions of a each character in a game
 - Player's high scores
 - Data visualization
- Lists are ideal for this
- Python has many tools to work efficiently with lists of numbers

---

layout: true

# The *range()* function

---

- This function makes it easy to generate a series of numbers. For example:

```python
for value in range(1, 5):
	print(value)
```

- What does the above code print?

--

- Although this code looks like it should print the numbers from 1 to 5, it doesn’t print the number 5:

```python
1
2
3
4
```

- Why?
 - Remember slicing?
 - Off-by-one behavior

---

layout: false

# Using *range()* to make a list of numbers

- There is a simple way of converting the output of the previous function directly into a list
- We use another built-in function:
 - *list()*

```python
numbers = list(range(1, 6))
print(numbers)
```

- With the desirable result:

```python
[1, 2, 3, 4, 5]
```

- It even has a third *step* argument to do things like:

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)

[2, 4, 6, 8, 10]
```

---

# Using *range()* to make a list of numbers

- And we can even make this more complex:

```python
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)
```

- Where we can get the first 10 square numbers:

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

# List Comprehension

- The previous approach for generating the list squares consisted of using three or four lines of code
- A list comprehension allows you to generate this same list in just one line of code
- A list comprehension combines the *for* loop and the creation of new elements into one line, and automatically appends each new element
- Let's see how the previous example is don using list comprehension:

```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

- And that function part can be as complex as you want it to be

```python
list = [x**2+2*x+3 for x in range(1, 11)]
print(list)
```

- Which leads to a question... can we easily plot this function/list?

---

# Data visualization: generating data

- *Data visualization* involves exploring data through visual representations

- *Data analysis* uses code to explore the patterns and connections in a data set

- A *data set* can be made up of a small list of numbers that fits in one line of code or it can be many gigabytes of data
- We already know the basics of generating a data set on a list using a function
- Python is an easily extensible language, so let's reuse someones previous effort and plot that data in beautiful charts.

---

# Installing a library: Matplotlib

- One of the most popular tools is Matplotlib, a mathematical plotting library
- To install it:

```python
python -m pip install --user matplotlib
or
python3 -m pip install --user matplotlib
```

.center[![Installation output]({{site.baseurl}}/presentation/listsplots/installation_output.png)]

---

# Now let's use it!

- Let's use it to plot the previous lists of squares
- Once installed, using it is as simple as follows:

```python
import matplotlib.pyplot as plt

#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [x**2 for x in range(1, 11)] 

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
```

.center[![Simple]({{site.baseurl}}/presentation/listsplots/simple.png)]

---

# Now let's use it!

- Another one, plotting a sine function:

```python
import math
import matplotlib.pyplot as plt

squares = [math.sin(x / 10.0) for x in range(1, 100)] 

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
```

.center[![Sine]({{site.baseurl}}/presentation/listsplots/sine.png)]
