class: center, middle, inverse

## Bash Continued
---
## Recap

Enter the link, do not copy or run any code, we will do it step by step together

[https://sebiglesias.com.ar/bash-test](https://sebiglesias.com.ar/bash-test)


---
## New Commands

pwd - Writes the absolute pathname of the current working directory

curl - Downloads files from the internet
- `curl https://sebiglesias.com.ar/bash-test` # downloads the file `bash-test` from the internet

grep - Searches for a pattern
- `ls | grep *.txt` # Searches for any file that ends with .txt

history - Shows the history of commands


---
## Finding files and writing files

find - Searches for files in a directory hierarchy

`find . -name "*.txt"` searches for all files that end with .txt in the current directory

nano - Creates a file and opens it in a text editor
- `nano resumen_de_la_mejor_materia.txt`# creates a file called `resumen_de_la_mejor_materia.txt` and opens it in a text editor

diff - Compares files line by line
- `diff resumen_de_la_mejor_materia.txt resumen_prog1.txt` # compares the files `resumen_de_la_mejor_materia.txt` and `resumen_prog1.txt` 


---
## Environment variables

Environment variables are special variables that contain information about your login session. They're stored for the system shell to use when executing commands. They exist whether you're using Linux, Mac, or Windows. Many of these variables are set by default during installation or user creation

`echo $HOME` # prints the value of the environment variable `HOME`

`HELLO="Hello World"` # creates an environment variable called `HELLO` with the value `Hello World`

`echo $HELLO` # prints the value of the environment variable `HELLO`


---
## Aliases

Aliases are a way to create shortcuts for commands. They are useful for commands that you use frequently, or commands that are long and difficult to type.

`alias ll='ls -l'` # creates an alias called `ll` for the command `ls -l`

`ll` # lists all the files in the working directory

`unalias ll` # removes the alias `ll`

`aliases` # lists all the aliases


---
## Hands on

https://github.com/krother/bash_tutorial

---