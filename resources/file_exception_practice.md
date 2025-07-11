# Ejercicios de práctica sobre archivos y excepciones


(Se focalizan en archivos de texto txt y csv)


## Ejercicio 1

Leer un archivo de texto y contar cuántas palabras hay en cada línea siguiendo las siguientes instrucciones:

1. Implementá la función `count_words_per_line(filename)`.
2. Si el archivo no existe, mostrará un mensaje de error: `"Archivo no encontrado"`.
3. Si existe, por cada línea del archivo imprimirá:
   `Línea 1: 4 palabras`
   `Línea 2: 3 palabras`, etc.

**Ejemplo de entrada:**
Archivo `texto.txt`:

```
Hola mundo desde Python
Archivos de texto simples
Excepciones también se manejan
```

**Salida esperada:**

```
Línea 1: 4 palabras
Línea 2: 3 palabras
Línea 3: 4 palabras
```


## Ejercicio 2

Leer un archivo `.csv` con datos de temperaturas y calcular promedio por ciudad siguiendo las siguientes instrucciones:

1. Implementá la función `promedio_temperaturas(filename)` que lea el archivo y agrupe las temperaturas por ciudad.
2. Hacer un archivo csv `promedios.csv` que muestre el promedio por ciudad, redondeado a 2 decimales.
3. Usá `try/except` para manejar el caso en que el archivo no exista.

**Formato del archivo:**
`temperaturas.csv`

```
Ciudad,Temperatura
Buenos Aires,20
Córdoba,25
Rosario,23
Buenos Aires,22
Córdoba,24
```

**Salida esperada:**

```
Ciudad,Promedio
Buenos Aires,21.00
Córdoba,24.50
Rosario,23.00
```


## Ejercicio 3

Verificar si los usuarios que iniciaron sesión están registrados siguiendo las siguientes instrucciones:

1. Implementá `verificar_sesiones(archivo_usuarios, archivo_sesiones)`.
2. Mostrar:

   * "Usuario válido: ..." si figura en la lista de usuarios.
   * "Usuario no registrado: ..." si no está en la lista.
3. Usá `try/except` para manejar archivos faltantes.


**Archivos:**

* `usuarios.txt`: lista con un usuario por línea.
* `sesiones.txt`: cada línea tiene un usuario que inició sesión.

**Ejemplo:**
`usuarios.txt`

```
Alice
Bob
Charlie
```

`sesiones.txt`

```
Bob
Dave
Alice
Eve
```

**Salida esperada:**

```
Usuario válido: Bob
Usuario no registrado: Dave
Usuario válido: Alice
Usuario no registrado: Eve
```


## Ejercicio 4

Leer un archivo de texto donde cada línea tiene un gasto con el formato `categoría:monto`, y calcular el total por categoría. Las instrucciones son:

1. Implementá la función `gastos_por_categoria(nombre_archivo)`.
2. Agrupar los montos en un diccionario.
3. Hacer un archivo de texto `totales.txt` que muestre el total gastado por categoría.
4. Manejar `FileNotFoundError`.


**Ejemplo de archivo `gastos.txt`:**

```
comida:150.50
transporte:50.00
comida:75.25
ocio:100.00
transporte:60.00
```

**Archivo `totales.txt`:**

```
comida: $225.75
transporte: $110.00
ocio: $100.00
```


## Ejercicio 5


Leer un archivo CSV con calificaciones de estudiantes y calcular estadísticas. Instrucciones:

1. Crear la función `estadisticas_notas(archivo_csv)` que:

   * Agrupe las notas por estudiante.
   * Calcule y muestre el promedio de cada uno.
2. Usá `csv.reader()` y excepciones para archivo inexistente.


**Ejemplo de archivo:** `notas.csv`

```
Nombre,Nota
Juan,7
Ana,9
Carlos,8
Ana,6
Juan,10
```

**Salida esperada:**

```
Juan: promedio 8.50
Ana: promedio 7.50
Carlos: promedio 8.00
```
