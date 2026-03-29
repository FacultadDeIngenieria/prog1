# TP4 - Soluciones

## Ejercicio 1 — `maximums.py`

```python
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        return x
    return y


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return max_of_two(max_of_two(x, y), z)
```

## Ejercicio 2 — `number_to_month.py`

```python
def number_to_month(month):
    if month == 1:
        return "enero"
    elif month == 2:
        return "febrero"
    elif month == 3:
        return "marzo"
    elif month == 4:
        return "abril"
    elif month == 5:
        return "mayo"
    elif month == 6:
        return "junio"
    elif month == 7:
        return "julio"
    elif month == 8:
        return "agosto"
    elif month == 9:
        return "septiembre"
    elif month == 10:
        return "octubre"
    elif month == 11:
        return "noviembre"
    elif month == 12:
        return "diciembre"
    else:
        return "error"
```

## Ejercicio 3 — `quadratic.py`

```python
import math


def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a * x ** 2 + b * x + c


def to_string(a, b, c):
    parts = []
    if a != 0:
        parts.append(f"{a} * X^2")
    if b != 0:
        parts.append(f"{b} * X")
    if c != 0 or (a == 0 and b == 0):
        parts.append(f"{c}")
    return "f(x) = " + " + ".join(parts)


def derivation(a, b, c):
    da = 2 * a
    db = b
    parts = []
    if da != 0:
        parts.append(f"{da} * X")
    if db != 0:
        parts.append(f"{db}")
    if not parts:
        parts.append("0")
    return "f'(x) = " + " + ".join(parts)
```

## Ejercicio 4 — `classify_number.py`

```python
def classify_number(n):
    if n == 0:
        return "zero"
    elif is_positive(n) and is_even(n):
        return "positive even"
    elif is_positive(n) and not is_even(n):
        return "positive odd"
    elif not is_positive(n) and is_even(n):
        return "negative even"
    else:
        return "negative odd"
```

## Ejercicio 5 — `price_calculator.py`

```python
def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    discounted = apply_discount(subtotal, discount_pct)
    total = apply_tax(discounted, tax_pct)
    return round(total, 2)


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    total_a = final_price(price_a, qty_a, disc_a, tax_pct)
    total_b = final_price(price_b, qty_b, disc_b, tax_pct)
    if total_a <= total_b:
        return "A"
    return "B"
```

## Ejercicio 6 — `text_analyzer.py`

```python
def total_letters(text):
    return count_vowels(text) + count_consonants(text)


def vowel_percentage(text):
    t = total_letters(text)
    if t == 0:
        return 0.0
    return round(count_vowels(text) / t * 100, 1)


def analyze_text(text):
    v = count_vowels(text)
    c = count_consonants(text)
    t = total_letters(text)
    p = vowel_percentage(text)
    return f"V:{v} C:{c} T:{t} P:{p}%"
```
