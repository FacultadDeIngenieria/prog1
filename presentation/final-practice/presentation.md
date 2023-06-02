class: center, middle, inverse
# Final Practice Exercises
Some practice exercises

---

## Exercise 1: FizzBuzz Function
Write a Python function **fizz_buzz(n: int) -> list** that returns a list with the FizzBuzz sequence from 1 to **n**. In this sequence, multiples of three are replaced by the word "Fizz", multiples of five by the word "Buzz", and multiples of both three and five by "FizzBuzz".

**Example Input/Output:**

Input: **fizz_buzz(5)**

Output: **[1, 2, "Fizz", 4, "Buzz"]**

---

### Solution

```python
def fizz_buzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
```

---

## Exercise 2: Reverse Words in a String
Write a Python function **reverse_words(s: str) -> str** that takes a string **s** as input and returns the string with words reversed. Assume the input string does not contain leading or trailing spaces and the words are always separated by a single space.

**Example Input/Output:**

Input: **reverse_words("Hello world")**

Output: **"world Hello"**

---

### Solution
```python
def reverse_words(s: str) -> str:
    reversed_s = ''

    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]

    return reversed_s
```
---

## Exercise 3: Multiply List Items
Write a Python function **multiply_list(items: list) -> int** that takes a list of integers **items** as input and returns the result of multiplying all the items in the list.

**Example Input/Output:**

Input: **multiply_list([1, 2, 3, 4, 5])**

Output: **120**

---

### Solution
```python
def multiply_list(items: list) -> int:
    result = 1
    for item in items:
        result *= item  
    return result
```

---

## Exercise 4: Factorial Function
Write a Python function **factorial(n: int) -> int** that takes an integer **n** as input and returns the factorial of **n**. Implement this function recursively.

**Example Input/Output:**

Input: **factorial(5)**

Output: **120**

---

### Solution

```python
def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

---

## Exercise 5: Number Guessing Game
Write a Python function **guess_number(guess: int, answer: int) -> str** that takes two integers **guess** and **answer** as inputs, and returns a string "Too high!", "Too low!" or "Congratulations! You've guessed the number!" depending on whether **guess** is too high, too low, or equal to **answer**.

**Example Input/Output:**

Input: **guess_number(7, 10)**

Output: **"Too low!"**

---

### Solution

```python
def guess_number(guess: int, answer: int) -> str:
    if guess > answer:
        return "Too high!"
    elif guess < answer:
        return "Too low!"
    else:
        return "Congratulations! You've guessed the number!"
```
