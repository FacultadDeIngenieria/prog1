class: center, middle, inverse

# Introducción a la Programación I
Recursion

---

# Agenda

- Recursion

---

# Recursion

- Programming technique in which a method calls itself to solve a problem.
- Such methods are called recursive methods.
- Many problems can be solved only with recursion.
- Others can be solved better with it.

---

# Recursion - Example

- Example: integer factorial calculation.
    - 0! = 1
    - 1! = 1 \* 0!
    - 2! = 2 \* 1! \* 0!
    - 3! = 3 \* 2 \* 1! \* 0!
    - ...

---

# Recursion - Example

```python
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3  # We could use an input here too!
print(f"The factorial of {num} is {factorial(num)}")
```

---

# Recursion - Example

- To show it graphically:

.center[![Factorial]({{site.baseurl}}/presentation/recursion/factorial.png)]