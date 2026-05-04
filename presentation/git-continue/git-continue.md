class: center, middle, inverse

# Introducción a la Programación I
# Git continue

---

# ¿Qué es el Control de Versiones?

Un **Sistema de Control de Versiones (VCS)** permite registrar cambios en archivos a lo largo del tiempo para poder:

- Recuperar versiones anteriores
- Comparar modificaciones
- Saber quién hizo cada cambio
- Colaborar con otros desarrolladores
- Mantener un historial completo del proyecto

---

# ¿Por Qué Necesitamos Versionado?

Sin control de versiones, muchos proyectos terminan así:

```plaintext
proyecto_final.doc
proyecto_final_v2.doc
proyecto_final_v3_ahora_si.doc
proyecto_final_v3_ahora_si_bueno.doc
proyecto_final_defINITIVO_FINAL.doc
```

---

# Problemas de Trabajar Sin Versionado

- No sabés cuál es la última versión
- Podés perder trabajo fácilmente
- No podés volver atrás con seguridad
- Es muy difícil trabajar en equipo
- No queda trazabilidad de cambios

---

# Tipos de Sistemas de Control de Versiones

1. Local Version Control
2. Centralized Version Control
3. Distributed Version Control

---

# 1. Local Version Control

Cada usuario guarda versiones manualmente en su máquina.

```plaintext
Mi PC
├── version1
├── version2
└── version3
```

### Ventajas
- Simple

### Desventajas
- No colaborativo
- Sin backups reales
- Fácil perder historial

---

# 2. Centralized Version Control (CVCS)

Todos trabajan contra un servidor central.

```plaintext
Desarrolladores
      ↓
Servidor Central
```

### Ejemplos
- SVN
- Perforce

---

# Problemas de CVCS

- Punto único de falla
- Si el servidor cae, nadie trabaja
- Si el servidor se corrompe, se pierde todo

---

# 3. Distributed Version Control (DVCS)

Cada desarrollador tiene una copia completa del repositorio.

```plaintext
Dev A ↔ Repo Central ↔ Dev B
 ↑
Backup local completo
```

### Ejemplos
- Git
- Mercurial

---

# ¿Qué es Git?

> Git es un sistema de control de versiones distribuido.

Creado por Linus Torvalds en 2005.

---

# ¿Cómo Almacena Datos Git?

Git guarda snapshots completos del proyecto en cada commit.

```plaintext
Commit A → Snapshot completo
Commit B → Snapshot completo
Commit C → Snapshot completo
```

---

# Conceptos Fundamentales

- Repository
- Working Directory
- Staging Area
- Commit
- Branch
- Merge
- Remote Repository

---

# Repositorio

Carpeta versionada por Git.

```bash
git init
```

---

# Working Directory

Tu carpeta de trabajo actual donde modificás archivos.

---

# Staging Area

Zona intermedia antes del commit.

```bash
git add archivo.java
```

---

# Repository (.git)

Base de datos donde Git almacena historial y metadata.

---

# Flujo Interno de Git

```plaintext
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Repository
```

---

# Commits

Un commit representa una foto del proyecto en un momento dado.

```bash
git commit -m "Agrego autenticación"
```

---

# Buenas Prácticas de Commit

- Un commit = un cambio lógico
- Mensajes claros y descriptivos
- Frecuencia alta, tamaño pequeño

---

# Branches

Una branch es una línea paralela de desarrollo.

```bash
git branch feature-login
```

---

# ¿Para Qué Sirven las Branches?

- Desarrollar features aisladas
- Probar ideas sin romper main
- Trabajar en paralelo

---

# Merge

Combina ramas.

```bash
git merge feature-login
```

---

# Git vs GitHub

---

# Git

Herramienta de versionado.

---

# GitHub

Plataforma online para alojar repositorios Git.

---

# Comandos Básicos

```bash
git init
git clone
git status
git add
git commit
git log
git branch
git checkout
git merge
git pull
git push
```

---

# Crear Repositorios Reales

---

# Inicializar Proyecto Nuevo

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
```

---

# Clonar Proyecto Existente

```bash
git clone https://github.com/user/proyecto.git
```

---

# Verificar Estado Inicial

```bash
git status
```

---

# Primer Commit de un Proyecto

```bash
git add .
git commit -m "Initial commit"
```

---

# Crear Archivo .gitignore

Permite excluir archivos de Git.

Ejemplo:

```gitignore
node_modules/
.env
.idea/
target/
```

---

# Commits en Profundidad

---

# ¿Qué Debe Tener un Buen Commit?

- Un propósito claro
- Cambios relacionados entre sí
- Mensaje entendible para terceros

---

# Ejemplos de Buenos Commits

```plaintext
Add login endpoint
Fix validation bug on signup
Refactor payment service
```

---

# Ejemplos de Malos Commits

```plaintext
Cambios
Update
Fix stuff
asdf
```

---

# Historial de Commits

```bash
git log
```

---

# Ver Historial Simplificado

```bash
git log --oneline --graph
```

---

# Branches en Profundidad

---

# Crear Branch

```bash
git branch feature-auth
```

---

# Cambiar de Branch

```bash
git checkout feature-auth
```

---

# Crear + Cambiar en Un Paso

```bash
git checkout -b feature-auth
```

---

# Listar Branches

```bash
git branch
```

---

# Borrar Branch

```bash
git branch -d feature-auth
```

---

# Merge Conflicts

---

# ¿Qué Es un Merge Conflict?

Sucede cuando:

> Dos ramas modifican la misma línea o bloque de código.

---

# Ejemplo de Conflicto

```java
<<<<<<< HEAD
return user.getName();
=======
return user.getFullName();
>>>>>>> feature-auth
```

---

# Cómo Resolver un Conflicto

1. Revisar ambas versiones
2. Elegir qué conservar
3. Editar manualmente
4. Guardar archivo
5. Hacer commit del merge

---

# GitHub Workflow

---

# Flujo Profesional Estándar

```plaintext
main
 ├── feature/login
 ├── feature/payments
 └── hotfix/navbar
```

---

# Workflow Recomendado

1. Pull de main actualizado
2. Crear branch feature
3. Desarrollar
4. Commit frecuente
5. Push branch remota
6. Abrir Pull Request
7. Code Review
8. Merge a main

---

# Push de Nueva Branch

```bash
git push -u origin feature-auth
```

---

# Pull Antes de Trabajar

```bash
git pull origin main
```

---

# Pull Request

Un Pull Request permite:

- Revisar cambios antes del merge
- Discutir implementación
- Aprobar código
- Mantener calidad técnica

---

# Buenas Prácticas de GitHub Workflow

- Nunca trabajar directo en main
- PRs pequeños y frecuentes
- Review obligatorio
- Merge solo código aprobado

---

# Flujo Completo de Trabajo Real

```plaintext
1. git checkout main
2. git pull
3. git checkout -b feature/nueva-funcionalidad
4. Programar
5. git add .
6. git commit -m "Implement nueva funcionalidad"
7. git push -u origin feature/nueva-funcionalidad
8. Abrir Pull Request
9. Merge
```

---

# Resumen Final

Git permite:

- Versionar código profesionalmente
- Trabajar en equipo
- Mantener historial completo
- Resolver conflictos ordenadamente
- Escalar desarrollo de software real

---

# Frase para Recordar

> Git no guarda archivos.  
> Git guarda la historia de tu proyecto.

---

# Recurso Oficial

https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control