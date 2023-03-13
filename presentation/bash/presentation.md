class: center, middle, inverse

## Bash
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

Interactive: allows running commands through a prompt one command at a time.

Non-interactive: run bash commands through a scripts, automating certain logic. A script is a list of commands (same as the ones that can be typed in a command line), stores in a file. It executes commands sequentially.

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

In aN UNIX OS, to leave the manual page use q and press enter
---
## Navigating directories

mkdir - Creates a directory

cd - Change directory

ls - List directory's contents

touch

---
## Manipulating Files

cat - Read file and write it to the standard output

cp - Copy

mv - Renaming Files

rm - Removing Files

echo - Writes arguments to the standard output
---
## Piping

'|' allows connecting UNIX programs to each other.

`ls | grep hi`

ls lists the files in the working directory, this output is checked by the grep command for the word `hi`.

---
## Trabajo Práctico

Capture the Flag!

https://github.com/krother/bash_tutorial
---