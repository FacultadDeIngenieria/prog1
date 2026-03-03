# Introducción a la Programación I
## Configuración para la Práctica

---

# Github

El primer paso es crear una cuenta en GitHub: [https://github.com/](https://github.com/)

Usaremos GitHub para entregar y trabajar en los Trabajos Prácticos (TPs).

---

# Discord

Unite a Discord usando esta URL. Creá una cuenta si no tenés usuario. Descargá la aplicación en tu PC o teléfono.

**¡Necesitás vincular tu cuenta de GitHub con Discord para unirte!**

[https://discord.gg/TvtyCmcPk2](https://discord.gg/9KT3X2a7)

Discord será nuestro centro principal de comunicación para Prog 1. Podés hacer preguntas allí y también recibir notificaciones de los profesores.

---

# GitHub Classroom

Una vez que tengas tu cuenta creada, el paso final es unirte a GitHub Classroom.

**Unirte al TP 1** → [https://classroom.github.com/XXXX](https://classroom.github.com/)

- Encontrá tu nombre y vinculá tu usuario de GitHub
- Si no encontrás tu nombre, avisale al profesor para que te agregue

---

# Trabajos Prácticos

Los trabajos practicos son parte de la materia. Para poder aprobar la cursada de la materia, es necesario tener todos los trabajo prácticos entregados, corregidos y correctos. Que quiere decir que sean correctos? Cada TP tendra un subset de pruebas que evaluán si el código del alumno es correcto. Si todo lo entregado funciona correctamente, dichas pruebas funcionarán y se le tomará como correcta la entrega de dicho TP.

---

# Installing pytest

## Prerequisites

- Python 3.8+ installed
- `pip` package manager

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

## Verify Installation

```bash
pytest --version
```

---

# ¡Comencemos!

¿Preguntas?

Recordá:
- Crear tu cuenta en GitHub
- Unirte al Discord
- Vincular tu cuenta de GitHub con Discord
- Unirte a GitHub Classroom para el TP 1
