# Soluciones TP8 - Archivos y Excepciones

Este archivo contiene las soluciones de referencia para todos los ejercicios del TP8.

Cada ejercicio vive en su propio archivo `exercise_NN_*.py` y tiene su `test_tp8_NN_*.py` correspondiente.

Temas evaluados:

- Lectura y escritura de archivos de texto (`open`, `read`, `readlines`, `write`).
- Manejo de excepciones (`try/except`, propagación de `FileNotFoundError`, lanzamiento de `ValueError`).
- Estructuras ya conocidas: listas, diccionarios, tuplas, strings y bucles.

---

## Ejercicio 1 — `read_lines`

**Objetivo:** Leer un archivo y retornar una lista de líneas sin saltos de línea ni espacios al principio/final, ignorando líneas vacías.

**Solución:**
```python
def read_lines(filename):
    resultado = []
    with open(filename, "r") as f:
        for linea in f:
            limpia = linea.strip()
            if limpia:
                resultado.append(limpia)
    return resultado
```

**Conceptos:**
- `with open(...) as f:` abre el archivo y lo cierra automáticamente.
- Iterar un `file` con `for linea in f:` recorre línea por línea sin cargar todo en memoria.
- `strip()` saca espacios y saltos de línea al principio/final.
- El `if limpia:` filtra líneas vacías (un string vacío es falsy).
- Si el archivo no existe, `open` ya lanza `FileNotFoundError` — no hace falta hacer nada especial.

**Alternativa con list comprehension:**
```python
def read_lines(filename):
    with open(filename, "r") as f:
        return [linea.strip() for linea in f if linea.strip()]
```

---

## Ejercicio 2 — `count_words`

**Objetivo:** Contar la frecuencia de cada palabra en un archivo, sin distinguir mayúsculas/minúsculas.

**Solución:**
```python
def count_words(filename):
    frecuencia = {}
    with open(filename, "r") as f:
        contenido = f.read()
    for palabra in contenido.split():
        clave = palabra.lower()
        frecuencia[clave] = frecuencia.get(clave, 0) + 1
    return frecuencia
```

**Conceptos:**
- `f.read()` devuelve todo el contenido como un único string.
- `str.split()` sin argumentos separa por cualquier whitespace (espacios, tabs, saltos de línea) y descarta los vacíos.
- `dict.get(clave, 0)` devuelve 0 si la clave no existe, muy útil para contadores.
- `lower()` normaliza para hacer el conteo case-insensitive.

**Alternativa con `collections.Counter`:**
```python
from collections import Counter

def count_words(filename):
    with open(filename, "r") as f:
        return dict(Counter(f.read().lower().split()))
```

---

## Ejercicio 3 — `read_sales` y `process_sales`

**Objetivo:** Parsear un archivo con ventas en formato `producto:valor;...` y luego imprimir totales/promedios por producto.

**Solución parte 1 — `read_sales`:**
```python
def read_sales(filename):
    ventas = {}
    with open(filename, "r") as f:
        contenido = f.read()
    for registro in contenido.split(";"):
        registro = registro.strip()
        if not registro:
            continue
        producto, valor = registro.split(":")
        ventas.setdefault(producto, []).append(float(valor))
    return ventas
```

**Conceptos:**
- `split(";")` separa todos los registros. Si el archivo termina con `;`, queda un string vacío al final que hay que saltear.
- `dict.setdefault(clave, [])` crea la lista si no existe y la devuelve; así podemos hacer `.append(...)` directamente.
- `split(":")` devuelve dos partes: nombre y valor. Desempaquetado directo en `producto, valor`.

**Solución parte 2 — `process_sales`:**
```python
def process_sales(data):
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
```

**Conceptos:**
- Iterar `dict.items()` respeta el orden de inserción (garantizado desde Python 3.7).
- Formato `f"{x:.2f}"` fuerza siempre dos decimales (`125.00`, no `125.0`).
- `sum(lista) / len(lista)` es el promedio estándar.

---

## Ejercicio 4 — `safe_average`

**Objetivo:** Promediar solo las líneas que se puedan convertir a float; lanzar `ValueError` si no hay ninguna válida.

**Solución:**
```python
def safe_average(filename):
    total = 0.0
    cantidad = 0
    with open(filename, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            try:
                total += float(linea)
                cantidad += 1
            except ValueError:
                continue
    if cantidad == 0:
        raise ValueError("no valid numbers")
    return total / cantidad
```

**Conceptos:**
- `try/except ValueError` captura el error cuando `float(linea)` falla, y el `continue` ignora esa línea.
- Guardar `total` y `cantidad` por separado evita hacer dos pasadas por el archivo.
- Validación final: si no hubo ninguna línea válida, lanzar `ValueError("no valid numbers")`.

**Alternativa con lista intermedia:**
```python
def safe_average(filename):
    numeros = []
    with open(filename, "r") as f:
        for linea in f:
            try:
                numeros.append(float(linea.strip()))
            except ValueError:
                pass
    if not numeros:
        raise ValueError("no valid numbers")
    return sum(numeros) / len(numeros)
```

---

## Ejercicio 5 — `csv_to_dict`

**Objetivo:** Leer un CSV con header `name,age,city` y retornar una lista de diccionarios; `age` como `int`.

**Solución:**
```python
def csv_to_dict(filename):
    with open(filename, "r") as f:
        lineas = f.readlines()
    if not lineas:
        return []
    header = [campo.strip() for campo in lineas[0].strip().split(",")]
    resultado = []
    for linea in lineas[1:]:
        linea = linea.strip()
        if not linea:
            continue
        valores = [campo.strip() for campo in linea.split(",")]
        registro = {}
        for clave, valor in zip(header, valores):
            if clave == "age":
                registro[clave] = int(valor)
            else:
                registro[clave] = valor
        resultado.append(registro)
    return resultado
```

**Conceptos:**
- `f.readlines()` devuelve una lista con todas las líneas (cada una incluye `\n`).
- `zip(header, valores)` empareja cada nombre de columna con su valor.
- Convertir `age` a `int` es un caso especial — el resto queda como string.
- Archivo vacío o solo header → `[]`.

**Alternativa con dict comprehension:**
```python
def csv_to_dict(filename):
    with open(filename, "r") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]
    if len(lineas) < 2:
        return []
    header = lineas[0].split(",")
    return [
        {k: int(v) if k == "age" else v
         for k, v in zip(header, fila.split(","))}
        for fila in lineas[1:]
    ]
```

---

## Ejercicio 6 — `grades_stats`

**Objetivo:** Para cada línea `estudiante:nota1,nota2,...`, retornar `(promedio, max, min)` como tupla de floats.

**Solución:**
```python
def grades_stats(filename):
    stats = {}
    with open(filename, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            estudiante, notas_str = linea.split(":")
            notas = [float(n) for n in notas_str.split(",")]
            promedio = sum(notas) / len(notas)
            stats[estudiante] = (promedio, max(notas), min(notas))
    return stats
```

**Conceptos:**
- Desempaquetado con `split(":")` porque sabemos que la línea tiene exactamente un `:`.
- List comprehension para convertir todas las notas a `float` en una sola línea.
- `max()` y `min()` funcionan directamente sobre listas.
- La tupla `(promedio, max, min)` se construye con paréntesis (aunque son opcionales).

---

## Ejercicio 7 — `write_inventory`

**Objetivo:** Escribir un diccionario `item → cantidad` al archivo, en orden alfabético.

**Solución:**
```python
def write_inventory(filename, inventory):
    with open(filename, "w") as f:
        for item in sorted(inventory):
            f.write(f"{item}:{inventory[item]}\n")
```

**Conceptos:**
- `open(..., "w")` abre en modo escritura: **sobreescribe** el archivo si existe, o lo crea si no.
- `sorted(dict)` ordena las **claves** alfabéticamente.
- Si el diccionario está vacío, el `for` no itera y el archivo queda vacío (pero sí se crea).
- La función no retorna nada → implícitamente `None`.

**Alternativa iterando `items()` ordenados:**
```python
def write_inventory(filename, inventory):
    with open(filename, "w") as f:
        for item, cantidad in sorted(inventory.items()):
            f.write(f"{item}:{cantidad}\n")
```

---

## Ejercicio 8 — `find_longest_word`

**Objetivo:** Retornar la palabra más larga del archivo; en empate, la primera que aparece.

**Solución:**
```python
def find_longest_word(filename):
    with open(filename, "r") as f:
        palabras = f.read().split()
    if not palabras:
        raise ValueError("file has no words")
    mas_larga = palabras[0]
    for palabra in palabras[1:]:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga
```

**Conceptos:**
- `split()` sin argumentos ya maneja espacios, tabs y saltos de línea como separadores.
- La comparación `>` (estricto, no `>=`) asegura que en empate se queda con la **primera** aparición.
- Si la lista está vacía, lanzamos `ValueError`.

**Alternativa con `max(... , key=len)`:**
```python
def find_longest_word(filename):
    with open(filename, "r") as f:
        palabras = f.read().split()
    if not palabras:
        raise ValueError("file has no words")
    return max(palabras, key=len)
```

**Nota:** `max` también respeta la primera aparición en caso de empate, así que esta versión también cumple la consigna.

---

## Ejercicio 9 — `merge_files`

**Objetivo:** Concatenar dos archivos en un tercero; si alguno de los inputs no existe, no crear el output.

**Solución:**
```python
def merge_files(file1, file2, output):
    with open(file1, "r") as f1:
        contenido1 = f1.read()
    with open(file2, "r") as f2:
        contenido2 = f2.read()
    with open(output, "w") as f_out:
        f_out.write(contenido1)
        f_out.write(contenido2)
```

**Conceptos:**
- **Orden importa:** leer ambos archivos ANTES de abrir el output en modo `"w"`. Si `open(output, "w")` se ejecuta primero, el archivo se crea aunque después falle la lectura.
- Si `file1` o `file2` no existe, `open` lanza `FileNotFoundError` antes de tocar el output.
- Modo `"w"` sobreescribe el output si ya existía.

---

## Ejercicio 10 — `parse_log`

**Objetivo:** Parsear líneas `NIVEL: mensaje` en un diccionario `{nivel: [mensajes...]}`. Líneas sin `:` → `ValueError`.

**Solución:**
```python
def parse_log(filename):
    logs = {}
    with open(filename, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            if ":" not in linea:
                raise ValueError("invalid log line")
            nivel, mensaje = linea.split(":", 1)
            nivel = nivel.strip()
            mensaje = mensaje.strip()
            logs.setdefault(nivel, []).append(mensaje)
    return logs
```

**Conceptos:**
- `split(":", 1)` divide **solo en el primer** `:`. Esto permite que el mensaje contenga `:` (por ejemplo `"hora 10:30"`).
- Validación `if ":" not in linea:` **antes** del split — si no hay dos puntos, es una línea inválida.
- Las líneas vacías se ignoran sin validar.
- `setdefault(nivel, [])` inicializa la lista si el nivel es nuevo.

**Alternativa con `defaultdict`:**
```python
from collections import defaultdict

def parse_log(filename):
    logs = defaultdict(list)
    with open(filename, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            if ":" not in linea:
                raise ValueError("invalid log line")
            nivel, mensaje = linea.split(":", 1)
            logs[nivel.strip()].append(mensaje.strip())
    return dict(logs)
```

---

## Tabla resumen

### Modos de apertura de archivos
| Modo | Lectura | Escritura | Crea si no existe | Sobreescribe | Append |
| ---- | ------- | --------- | ----------------- | ------------ | ------ |
| `"r"` | sí | no | no (error) | — | — |
| `"w"` | no | sí | sí | sí | no |
| `"a"` | no | sí | sí | no | sí |
| `"r+"` | sí | sí | no (error) | no | no |

### Métodos comunes de archivo
| Método | Devuelve | Cuándo usarlo |
| ------ | -------- | ------------- |
| `f.read()` | string completo | archivos chicos, contenido como una unidad |
| `f.readlines()` | lista de líneas | necesitás acceder por índice |
| `for linea in f:` | iterador de líneas | archivos grandes, una línea a la vez |
| `f.write(s)` | `None` | escribir un string (hay que poner `\n` a mano) |

### Excepciones típicas
| Excepción | Cuándo se lanza | Cómo manejarla |
| --------- | --------------- | -------------- |
| `FileNotFoundError` | `open("x", "r")` con archivo inexistente | Propagar o `try/except FileNotFoundError:` |
| `ValueError` | `int("abc")`, `float("x")` | `try/except ValueError:` |
| `KeyError` | Acceso `d["k"]` si no existe | `d.get("k")` o validar con `in` |
| `PermissionError` | No tenés permisos sobre el archivo | Normalmente se propaga |

---

## Tips y buenas prácticas

1. **Siempre usar `with open(...)`:**
   ```python
   # Correcto — el archivo se cierra solo al salir del bloque
   with open("datos.txt") as f:
       contenido = f.read()

   # Evitar — hay que acordarse de f.close()
   f = open("datos.txt")
   contenido = f.read()
   f.close()
   ```

2. **Propagar vs capturar excepciones:**
   - Si no podés hacer nada útil con el error, propagalo (no lo captures).
   - Solo captura si vas a dar una respuesta alternativa o transformar el error.
   ```python
   # Correcto: transformamos el error
   try:
       valor = float(linea)
   except ValueError:
       continue  # ignoramos la línea
   ```

3. **No abrir el output antes de leer los inputs:**
   Si leés primero y escribís después, un `FileNotFoundError` en la lectura no deja un archivo vacío detrás (importante en el Ejercicio 9).

4. **Formatear con f-strings y `:.2f`:**
   ```python
   total = 100
   print(f"${total:.2f}")   # "$100.00"
   ```

5. **`split(sep, 1)` para respetar separadores dentro del valor:**
   ```python
   "INFO: hora 10:30".split(":", 1)
   # → ["INFO", " hora 10:30"]
   ```

6. **Acumuladores en diccionarios de listas:**
   ```python
   # Con setdefault
   d.setdefault(clave, []).append(valor)

   # Con defaultdict
   from collections import defaultdict
   d = defaultdict(list)
   d[clave].append(valor)
   ```
