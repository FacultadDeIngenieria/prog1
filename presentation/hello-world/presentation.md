class: center, middle, inverse

# Introducción a la Programación I
Hello World

---

# What you'll need

- Reference book **Python Crash Course** [site](https://ehmatthes.github.io/pcc_2e/regular_index/)
- To write your first programs, you'll need:
 - The Python interpreter for your operating system
  - Download it for your OS [here](https://www.python.org/downloads/)
  - Consult the [installation instructions](https://ehmatthes.github.io/pcc_2e/setup_instructions/setup_instructions/) by reference book
- A text editor
 - Any text editor will suit you fine. (Recommended [Sublime Text](http://www.sublimetext.com))
- Terminal

.center[![Python Book]({{site.baseurl}}/presentation/hello-world/python-book.png)]

---

# Walkthrough

Your first program will be the classic introduction to any language the HelloWorld! 
- It will simply display the greeting "Hello world!"
- To create this program, you will:
- Create a source file (.py file). A source file contains code, written in the Python programming language, that you and other programmers can understand
- Run the program using the Python interpreter

---

# Create Source File: hello_world.py

- Open Sublime Text editor
- It would be a great idea to create a folder, called **prog1-python** in a known location of your computer
- Save the empty file with the name *hello_world.py* in the previously created folder
- Type the following:

```python
# The following line will print a Hello World message to the screen
print("Hello World!")
```

---

layout: true

# Let's run it!

---

- Open your Terminal or Shell 
- Change current directory to the one you have created using the **cd** command
- Once there, type the following:

```bash
python3 hello_world.py #or the Python 3 interpreter command on your system
```

--

- You should see something like this:

![Hello World Terminal]({{site.baseurl}}/presentation/hello-world/hw-terminal.png)

---

layout: false

# What happened when you run hello_world.py?

```python
# The following program will print a Hello World message to the screen
print("Hello World!")
```

- The **Python interpreter** reads the file to determine what's in it
- In this case:
 - It sees the **print** followed by parentheses
 - So it prints to the screen what is **inside** them
 - What happened to the text after the **#**?
- Your editor also does things:
 - It highlights different parts of the code
 - It recognizes **print()** as the name of a function showing it in a different color
 - It knows that **"Hello World!"** is not Python code and displays it in another color
 - This feature is called *syntax highlighting*

---

# Comments

 - What happened to this line?

```python
# The following program will print a Hello World message to the screen
```

- The hash mark indicates a comment, so anything after it is ignored by the interpreter
- What comments should you write?
  - Main reason: explain what your code does
  - In the middle of your work, you know what it does, but after some time, if you go back to the project, would you remember?
  - Others can contribute to your code
