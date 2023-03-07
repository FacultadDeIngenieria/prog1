class: center, middle, inverse

# Introducción a la Programación I
Introduction

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

