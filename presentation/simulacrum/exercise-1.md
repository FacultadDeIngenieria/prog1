class: center, middle, inverse

# **Ejercicio 1 - Seguimiento de Codigo**

---

## Enunciado

¿Que valor imprime en pantalla al ejecutar el siguiente codigo?

```python
def exam_mystery(text):
    word = "pythonic"
    if len(text) > 5:
        if "a" in text:
            word = text[:3].upper() + word[-2:]
        elif "e" in text:
            word = text[1:4] + "123"
        
        if len(word) > 5:
            result = word[::-1]
        else:
            result = word + "!!!"
    else:
        result = text[::2] + "&" + word[:2]
    
    print("Valor final:", result)

exam_mystery("parcial")
```

---

## Paso 1 - Llamada a la funcion

Se llama a `exam_mystery("parcial")`

```
text = "parcial"
word = "pythonic"
```

---

## Paso 2 - Primera condicion

```python
if len(text) > 5:
```

`len("parcial")` → `7`

`7 > 5` → **True** ✓

Entramos al bloque.

---

## Paso 3 - Condiciones anidadas

```python
if "a" in text:
```

`"a" in "parcial"` → **True** ✓

Se ejecuta:

```python
word = text[:3].upper() + word[-2:]
```

---

## Paso 4 - Evaluacion de la asignacion

```python
word = text[:3].upper() + word[-2:]
```

- `text[:3]` → `"par"`
- `"par".upper()` → `"PAR"`
- `word[-2:]` → `"ic"` (ultimos 2 caracteres de `"pythonic"`)

```
word = "PAR" + "ic" = "PARic"
```

---

## Paso 5 - Segunda condicion interna

```python
if len(word) > 5:
```

`len("PARic")` → `5`

`5 > 5` → **False** ✗

Vamos al `else`:

```python
result = word + "!!!"
```

```
result = "PARic" + "!!!" = "PARic!!!"
```

---

## Paso 6 - Resultado final

```python
print("Valor final:", result)
```

**Imprime:**

```
Valor final: PARic!!!
```

---

class: center, middle, inverse

## Respuesta

# `Valor final: PARic!!!`

[Volver a las respuestas](/simulacrum-answers)
