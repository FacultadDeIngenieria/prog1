# Introducción a la Programación I
## Configuración para la Práctica

---

# Github

El primer paso es crear una cuenta en GitHub: [https://github.com/](https://github.com/)

Usaremos GitHub para entregar y trabajar en los Trabajos Prácticos (TPs).

---

# Discord

Unite a Discord usando esta URL. Creá una cuenta si no tenés usuario. Descargá la aplicación en tu PC o teléfono.

[https://discord.gg/TvtyCmcPk2](https://discord.gg/9KT3X2a7)

Discord será nuestro centro principal de comunicación para Prog 1. Podés hacer preguntas allí y también recibir notificaciones de los profesores.

---

# GitHub Classroom

Una vez que tengas tu cuenta creada, el paso final es unirte a GitHub Classroom.

**Unirte al TP 1** → [Link al TP 1](https://classroom.github.com/a/c6oH9MFz)

- Encontrá tu nombre y vinculá tu usuario de GitHub
- Si no encontrás tu nombre, avisale al profesor para que te agregue

---

# Trabajos Prácticos

Los trabajos practicos son parte de la materia. Para poder aprobar la cursada de la materia, es necesario tener todos los trabajo prácticos entregados, corregidos y correctos. Que quiere decir que sean correctos? Cada TP tendra un subset de pruebas que evaluán si el código del alumno es correcto. Si todo lo entregado funciona correctamente, dichas pruebas funcionarán y se le tomará como correcta la entrega de dicho TP.


# Instalación de Python

---
## Instalación en Windows

Windows no siempre incluye Python, así que probablemente necesites descargarlo e instalarlo, y luego descargar e instalar un entorno de desarrollo o editor de texto.

Primero, comprueba si Python está instalado en tu sistema.
Abre una terminal de comandos escribiendo `PowerShell` en el menú Inicio.

En la ventana de terminal, escribe `python` en minúsculas. Si aparece un mensaje de error de Python (>>>), significa que Python está instalado en tu sistema. Sin embargo, probablemente verás un mensaje de error indicando que Python no es un comando reconocido o que la aplicación de Microsoft Store no se está cargando.


En ese caso, descarga un instalador de Python para Windows.

Instrucciones en la página siguiente
---
Ve a [http://python.org/downloads/](http://python.org/downloads/). Haz clic en el botón `Descargar Python 3.14.3`; esto debería iniciar automáticamente la descarga del instalador correcto para tu sistema. Después de descargar el archivo, ejecute el instalador. Asegúrese de marcar la opción `"`Añadir Python a PATH`"` para facilitar la configuración correcta del sistema.

![Installation]({{site.baseurl}}/utils/installation/img.png)

---
Abra una ventana de comandos e introduzca `python` en minúsculas. Si aparece el símbolo del sistema de Python (>>>), Windows ha encontrado la versión de Python que acaba de instalar:
```commandline
C:\> python
Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

Cuando haya visto este resultado, presione Ctrl-Z o ingrese `exit` para salir de la terminal de Python y regresar a la terminal.

---
## Instalación en MacOS

### Installing Homebrew
Homebrew es un gestor de paquetes para OS X (y Linux).

Abre una ventana de terminal: Puedes presionar la tecla Command + Barra espaciadora para abrir Spotlight, escribir `Terminal` y presionar Intro. Luego, pega el siguiente comando en la terminal.
```commandline
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
(Ingresa a [https://brew.sh/](https://brew.sh/) para más información sobre Homebrew)


---

Después de descargar e instalar Homebrew con el comando anterior, puedes instalar Python3 escribiendo el comando
```commandline
brew install python3
```

Finalmente, puedes comprobar la versión de Python instalada con el comando `python3`
```commandline
python3
Python 3.9.10 (main, Jan 15 2022, 11:48:00)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Cuando haya visto este resultado, presione Ctrl+D o ingrese `exit` para salir de la terminal de Python y regresar a la terminal.

---
## Instalación en Linux

Abra una ventana de terminal ejecutando la aplicación Terminal en su sistema (en Ubuntu, puede presionar Ctrl+Alt+T). Luego, ejecute los siguientes comandos.
```commandline
sudo apt-get update
sudo apt-get install python3
```

Finalmente, puedes comprobar la versión de Python instalada con el comando `python3`
```commandline
$ python3
Python 3.9.10 (main, Jan 15 2022, 11:48:00)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

Cuando haya visto este resultado, presione Ctrl+D o ingrese `exit` para salir del indicador de Python y regresar al indicador de terminal.

---
# Installing pytest

## Prerequisites

- Python 3.8+ installed
- `pip` package manager

---
## macOS

```bash
# Using pip
pip3 install pytest

# Or with a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

### Add to PATH (if needed)

If `pytest` is not found after install, add the Python scripts directory to your shell profile (`~/.zshrc` or `~/.bash_profile`):

```bash
export PATH="$HOME/Library/Python/3.x/bin:$PATH"
```

Replace `3.x` with your Python version (e.g., `3.11`). Then reload:

```bash
source ~/.zshrc
```
---
## Windows

```powershell
# Using pip
pip install pytest

# Or with a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate
pip install pytest
```

### If pip is not available

```powershell
# Option 1: Ensure pip via Python
python -m ensurepip --upgrade

# Option 2: Download get-pip.py and run it
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
---
## Windows ( cont )
### Add to PATH (if needed)

If `pytest` is not recognized after install, add the Python Scripts directory to your system PATH:

1. Open **Settings > System > About > Advanced system settings**
2. Click **Environment Variables**
3. Under **User variables**, select **Path** and click **Edit**
4. Add the following entry (adjust for your Python version):
   ```
   C:\Users\<YourUser>\AppData\Local\Programs\Python\Python3x\Scripts
   ```
5. Click **OK** and restart your terminal

Or via PowerShell (current session only):

```powershell
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python3x\Scripts"
```
---
## Verify Installation

```bash
pytest --version
```

---

# Solicita la licencia educativa de JetBrains para usar PyCharm Professional.

### Completa el siguiente formulario con tu correo electrónico @edu:

[https://www.jetbrains.com/shop/eform/students](https://www.jetbrains.com/shop/eform/students)

### Crea un usuario de JetBrains con el mismo correo electrónico @edu o inicia sesión con una cuenta existente:

[https://account.jetbrains.com/login](https://account.jetbrains.com/login)

### Descarga e instala PyCharm Professional

[https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download)

### Abre PyCharm y activa tu producto con el mismo usuario.

---

# ¡Comencemos!

¿Preguntas?

Recordá:
- Crear tu cuenta en GitHub
- Unirte al Discord
- Vincular tu cuenta de GitHub con Discord
- Unirte a GitHub Classroom para el TP 1
