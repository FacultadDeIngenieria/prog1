class: center, middle, inverse

# Introducción a la Programación I
Algoritmos

---

# ¿Qué son los algoritmos? 

Un algoritmo es una secuencia de pasos para resolver un problema o realizar una tarea específica. Estos pasos deben ser definidos y ordenados de manera clara para que se puedan seguir correctamente.

---
# ¿Lavarse los dientes es un algoritmo? 

---
# Lavarse los dientes es también un algoritmo

 1. Agarrar la pasta dental
 2. Revisar si le queda
 3. ¿Si no tiene? Busco una nueva
 4. Busco el cepillo y lo coloco en los dientes
 5. Muevo de lado a lado
 6.  ¿Pasaron 2 minutos?  Volver a 5.
 7.  Enjuagarse
 8. Terminé

---

# Ejemplos de algoritmos en la vida cotidiana
Los algoritmos  pueden usar para:
* Encontrar la mejor ruta para llegar a un lugar en GPS.
* Mostrar los resultados más relevantes en una búsqueda en Google.
* Recomendar contenido basado en las preferencias de los usuarios.
* Hacer realidad el siguiente videojuego
* Diagnosticar enfermedades
* Enviar paquetes a tu casa
* Mucho más...

---

# Tipos diferentes de algoritmos

* Algoritmo de búsqueda: 
	* Buscar elementos dentro de un conjunto de datos. 
* Algoritmo de ordenación: 
	* Organizar elementos dentro de un conjunto de datos. 
* Algoritmo de optimización: 
	* Encontrar la mejor solución a un problema dado.
* Algoritmos recursivos: 
	* Resolver un problema a través de la repetición de una tarea. 

---

# Beneficios de Aprender Algoritmos

* Desarrollar habilidades de pensamiento crítico. 
* Comprender mejor el mundo digital. 
* Mejorar la capacidad de resolver problemas.
* Mejorar la habilidad de diseñar sistemas y programas.

---

# Conclusión 

Los algoritmos son una parte importante de nuestra vida moderna, y aprender sobre ellos puede ayudarnos a desarrollar nuestra capacidad de resolver problemas.

---
class: center, middle, inverse

# Introducción a la Programación I
Lenguajes

---

# ¿Por qué Python?

- La **curva de aprendizaje** del lenguaje para el que nunca programó, es mas **suave**
- **Eficiente**: mas con menos
- Su sintaxis lo lleva a producir **código más limpio**
- Fácil de leer, fácil de depurar
- Extensamente usado en trabajos académicos y de aplicación real
- **RECORDAR:** el lenguaje que nos acompaña en esta materia, es una herramienta para aplicar los conocimientos generales

---

# ¿Por qué NO Java?

- La **curva de aprendizaje** del lenguaje para el que nunca programó, es mas **empinada**
- Mucha **magia** cuando recién se está empezando
- Arrastra **vicios** de larga data que lo hacen complicado como primer lenguaje
- Luego de aprendido un lenguaje como Python, el pasaje a Java será mas rápido y transparente

---

# Language Trends (Stack Overflow)


.center[![Language Rank Trends]({{site.baseurl}}/presentation/introduction/stackoverflow-languages.png)]

---

# Language Trends (GitHub)


.center[![Language Rank Trends]({{site.baseurl}}/presentation/introduction/github-languages.png)]

---

# Language Trends (RedMonk)


.center[![Language Rank Trends]({{site.baseurl}}/presentation/introduction/redmonk-languages.png)]

---


# Primera enseñanza

Programamos en un mundo globalizado, y nos entendemos entre todos programando en __inglés.__

---

# Python

- Wikipedia: Python is an **interpreted**, **high-level** and **general-purpose** programming language. It is **dynamically typed** and **garbage-collected**.
- Multi paradigm: functional, object oriented, structured
- Portable: runs on Windows, Linux, macOS (a little less portable than Java)
- Designed by Guido van Rossum. First version in 1991.

???

https://en.wikipedia.org/wiki/Python_(programming_language)


---

# Why interpreted?

- As opposed to **compiled languages**
- **Compilation:** involves translating your human understandable code to machine understandable code, or **Machine Code**
- **Machine code** is the base level form of instructions that can be directly executed by the CPU.
- **Interpreted:** Python code is translated to **bytecode**
- This **bytecode** is a low-level set of instructions that can be executed by an **interpreter.** 
- Instead of executing the instructions on CPU, bytecode instructions are executed on a Virtual Machine.

???

https://towardsdatascience.com/how-does-python-work-6f21fd197888#:~:text=For%20the%20most%20part%2C%20Python,pyc%20or%20

---

# Portable - Platform independent

- As long as the **Python bytecode** and 
- **the Virtual Machine** have the **same version**
- **Python bytecode** can be executed on **any platform** where an interpreter exists (Windows, macOS, Linux).

---

# What exactly is Garbage Collection?

- In older programming languages, memory allocation was quite **manual**.
- Many times when you use variables that are no longer in use or referenced anywhere else in the program, they need to be cleaned from the memory.
- **Garbage Collector** does that for you. It **automatically** frees up space without you doing anything.

---

# How Python Interpreter Works?

.center[![Python Interpreter]({{site.baseurl}}/presentation/introduction/python-interpreter.jpeg)]

