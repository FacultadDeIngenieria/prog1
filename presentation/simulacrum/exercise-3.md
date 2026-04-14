class: center, middle, inverse

# **Ejercicio 3 - Validacion de Strings**

---

## Enunciado

Escribir una funcion `validate_token` que reciba un string y devuelva `True` si cumple:

1. Empieza y termina con la misma letra (ignorando mayusculas/minusculas).
2. Longitud de al menos 8 caracteres.
3. Contiene al menos un digito numerico (0-9).
4. No tiene espacios en blanco al principio ni al final.

**Sin usar loops.**

---

## Analisis de cada condicion

**Condicion 1** - Misma letra al inicio y fin:

```python
token[0].lower() == token[-1].lower()
```

**Condicion 2** - Longitud minima 8:

```python
len(token) >= 8
```

---

## Analisis de cada condicion (cont.)

**Condicion 3** - Al menos un digito (sin loops):

```python
("0" in token or "1" in token or "2" in token or
 "3" in token or "4" in token or "5" in token or
 "6" in token or "7" in token or "8" in token or
 "9" in token)
```

**Condicion 4** - Sin espacios al principio ni al final:

```python
token == token.strip()
```

---

## Solucion

```python
def validate_token(token):
    if token != token.strip():
        return False
    if len(token) < 8:
        return False
    if token[0].lower() != token[-1].lower():
        return False
    has_digit = ("0" in token or "1" in token or
                 "2" in token or "3" in token or
                 "4" in token or "5" in token or
                 "6" in token or "7" in token or
                 "8" in token or "9" in token)
    return has_digit
```

---

## Ejemplo 1

```python
validate_token("  a123456a")
```

- `"  a123456a" != "  a123456a".strip()` → `"  a123456a" != "a123456a"` → **True**
- Retorna **False** (tiene espacios al principio)

---

## Ejemplo 2

```python
validate_token("A_token_9A")
```

- `"A_token_9A" == "A_token_9A".strip()` → **True** ✓
- `len("A_token_9A")` → `10 >= 8` → **True** ✓
- `"A".lower() == "A".lower()` → `"a" == "a"` → **True** ✓
- `"9" in "A_token_9A"` → **True** ✓

Retorna **True**

---

## Ejemplo 3

```python
validate_token("abc123de")
```

- Sin espacios → ✓
- `len("abc123de")` → `8 >= 8` → ✓
- `"a".lower() == "e".lower()` → `"a" == "e"` → **False** ✗

Retorna **False** (no empieza y termina con la misma letra)

---

class: center, middle, inverse

[Volver a las respuestas](/simulacrum-answers)
