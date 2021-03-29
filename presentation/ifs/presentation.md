class: center, middle, inverse

# Introducción a la Programación I
if Statements

---

# Agenda

- Conditional 
- if Statements

---

# Introduction

- When we code, we often have a set of conditions, and we have to decide which action to take, based on those conditions
- With *if* statements, we can evaluate the actual state of our program and respond appropriately to that state

---

# A Simple Example

```python
age = int(input("Ingrese su edad: "))

if age >= 18:
	print("Sos mayor de edad :-)")
else:
	print("Sos menor de edad")
```

- This code snippet asks the user for his age and then prints a message stating if he reached the age of majority or not
- First, we are going to see what kind of tests we can examine

---

# Conditional Tests

- At the very center of every *if* statement, we have an expression that can be evaluated as *True* or *False*
 - Called **conditional test**
- If the conditional test:
 - Evaluates to *True*, the code following it gets **executed**
 - Evaluates to *False*, the code following it gets **ignored**
- Equality
```python
>>> city = "Pilar"
>>> city == "Pilar"
True
```
- Inequality
```python
>>> city = "Pilar"
>>> city != "Buenos Aires"
True
```

- Most of our conditional expressions will test for *equality* but sometimes is more efficient to test for *inequality*

---

# Numerical Comparisons

- Testing numerical is pretty simple too

```python
>>> age = 18
>>> age == 18
True
>>> age != 18
False
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

- Every one of them can be used as part of an *if* statement

---

# Checking Multiple Conditions

- Often, we want to check multiple conditions at the same time
 - Depending on the scenario, we have *and* and *or* keywords
- *and* let us check whether two conditions are **both** *True* at the same time
 - It behaves like Boole's *AND* truth table

```python
>>> age_bob = 22
>>> age_alice = 18
>>> age_bob >= 21 and age_alice >= 21
False
>>> age_alice = 22
>>> age_bob >= 21 and age_alice >= 21
True
```

- We can use parenthesis to improve readability

```python
(age_bob >= 21) and (age_alice >= 21)
```

---

# Checking Multiple Conditions

- *or* allows us to check multiple conditions too, but it passes when either or both of the individual tests pass
 - It behaves like Boole's *OR* truth table

```python
>>> age_bob = 22
>>> age_alice = 18
>>> age_bob >= 21 or age_alice >= 21
True
>>> age_bob = 18
>>> age_bob >= 21 or age_alice >= 21
False
```

- Boolean Expressions
 - just another name for conditional tests
- We can have Boolean values too, very useful to save programs state or simplify conditional tests.

```python
game_active = True
can_edit = False
```

---

# Simple if Statements

- The simplest one, and general form of an *if*, has one test and one action

```python
if <conditional_test>:
	<do something>
```

- We can put any conditional test in the first line and just about any action in the **indented** block following it
- If the conditional evalutes to *True* the block gets executed, if not it gets ignored

```python
age = 17
if age >= 16:
	print("Tenés edad para votar!")
```

- The block of actions can have as many as we want (but **indented**):

```python
age = 17
if age >= 16:
	print("¡Tenés edad para votar!")
	print("¿Sabés donde?")
```

---

# if-else Statements

- Often we have to take an action if the conditional passes and another one if not

```python
age = 17
if age >= 16:
	print("¡Tenés edad para votar!")
	print("¿Sabés donde?")
else:
	print("¡Sos muy joven para votar!")
	print("¡Ya vas a poder!")
```

- The *else* keyword is used to mark the block that gets executed if the conditional **not** passes

---

# The if-elif-else Chain

- Often we have to test more than two possible situations, for that Python has the *if-elif-else* syntax
- It runs each conditional test in **order** until one passes
- Suppose this example:
 - Admission for anyone under age 4 is free.
 - Admission for anyone between the ages of 4 and 18 is $25.
 - Admission for anyone age 18 or older is $40.
- How we can determine the admission fee based on the age of a person?

```python
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")
```

```python
"Your admission cost is $25."
```

---

# Using Multiple elif Blocks

- We can use as many *elif* blocks as we want
- Following the example:
 - Let's say that anyone 65 or older pays half the regular admission, or $20

```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost is ${price}.")
```

- Pay attention to the **refactor** in this snippet comparing it to the last one

---

# Omitting the *else* block

- The *else* block is not required at the end of the chain
- Sometimes its useful, and sometimes its clearer to use an additional *elif* statement

```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}.")
```

- The *else* block is a catchall statement
- And sometimes we have a specific final condition, in that case, we can consider using one last *elif* statement

---

# Testing multiple conditions

- The *if-elif-else* is powerful, but only when we need just on test to pass
 - when one passes, the others get skipped
- Sometimes it's important to check **all** the conditions of interest
- Example:
 - We want to know if a number is greater than 10 and if it's an even number


```python
number = int(input("Ingrese un número: "))

if number >= 10:
	print("El número es mayor a 10")
if number % 2 == 0:
	print("El número es par")
```
