class: center, middle, inverse

## Linux and Bash
---
## Bash is in the top 10 most popular programming languages

https://survey.stackoverflow.co/2023/#most-popular-technologies-language
![stackoverflow]({{site.baseurl}}/presentation/bash-intro/stackoverflow-2023.png)

---
## Linux is up there as well
https://sueldos.openqube.io/encuesta-sueldos-2023.01/
![openqube]({{site.baseurl}}/presentation/bash-intro/openqube-2023.png)

---
## Installation

**Windows**: Download Cygwin (https://www.cygwin.com/install.html)
**Mac**: use the Terminal app
**Linux**: Open a terminal

We will be using the terminal to run bash commands, make sure you have it installed.

---
## Shells and Terminals

A shell is a command interpreter. It takes commands from the user, and delivers them to the operating system to perform.

A terminal is a program that lets you interact with the shell.

- Available on any OS
- Flexible & Efficient
- Great for prototyping and automating simple tasks

---
## Bash (1989)

Bourne Again Shell

Bash is an enhanced version of the Bourne Shell, or sh (1977)

Default shell on most UNIX operating systems

---
## Bash interactive and non-interactive mode

Interactive: allows running commands through a prompt, one command at a time.

Non-interactive: run bash commands through scripts, automating certain logic. A script is a list of commands (same as the ones that can be typed in a command line), stored in a file. It executes commands sequentially.

---
## Hands on

**Bashcrawl**: https://gitlab.com/slackermedia/bashcrawl

Bashcrawl is a game that teaches you how to use the command line.

Follow the instructions to download it and run it.

---
## Interactive mode: Commands

BASH reads commands from its input (either a terminal or a file)

Each "line" is treated as a command: an instruction to be carried out

Bash divides each line into words separated by a whitespace character (space or tab)

The first word of the line is the name of the command to be executed, all other words are arguments.

`$ man man`

`$` Usually indicates that the shell is Bash compatible

`man` "manual", displays manual documentation pages

Each command on your system is likely to have a man page

In a UNIX OS, to leave the manual page use q and press enter

---
## Navigating directories

mkdir - Creates a directory
- `mkdir facultad` creates a directory called `facultad`
- `mkdir facultad/programacion1` creates a directory called `programacion` inside `facultad/programacion1`

cd - Change directory
- `cd facultad/programacion1` changes the current directory to `facultad`

touch - Create a file
- `touch resumen_de_la_mejor_materia.txt` creates a file called `resumen_de_la_mejor_materia.txt`

ls - List directory's contents
- `ls` lists the files in the working directory

---
## Piping

'|' allows connecting UNIX programs to each other.

`ls | grep hi`

ls lists the files in the working directory, this output is checked by the grep command for the word `hi`

---
## Manipulating Files

cat - Read file and write it to the standard output
- `cat resumen_de_la_mejor_materia.txt` prints the contents of the file `resumen_de_la_mejor_materia.txt`

cp - Copy File(s)
- `cp resumen_de_la_mejor_materia.txt resumen_de_la_mejor_materia_2.txt` copies the file `resumen_de_la_mejor_materia.txt` to `resumen_de_la_mejor_materia_2.txt`

mv - Move File(s)
- `mv resumen_de_la_mejor_materia_2.txt facultad/programacion1.txt` moves the file `resumen_de_la_mejor_materia_2.txt` to `facultad/programacion1.txt

rm - Remove File(s) and directories
- `rm facultad/programacion1.txt` removes the file `facultad/programacion1.txt`

echo - Writes arguments to the standard output
- `echo rm *.txt` prints all the options to be removed to make sure we are deleteing what we want to delete.

---
## Other comands

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

https://forms.gle/ra2P5qd2qozHpNGQ6