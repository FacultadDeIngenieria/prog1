class: center, middle, inverse

# Introducción a la Programación I
# Git continue

---

# ¿Qué es el Control de Versiones?

Un **VCS (Version Control System)** permite:

- Registrar cambios en archivos a lo largo del tiempo
- Recuperar versiones anteriores
- Saber quién hizo cada cambio
- Comparar modificaciones
- Trabajar en equipo sin perder trabajo

---

# ¿Por Qué lo Necesitamos?

Sin versionado, muchos proyectos terminan así:

```plaintext
proyecto_final.doc
proyecto_final_v2.doc
proyecto_final_v3_ahora_si.doc
proyecto_final_definitivo_FINAL.doc
```

## Problemas

- No sabés cuál es la última versión
- Podés perder trabajo fácilmente
- No podés volver atrás
- Colaborar en equipo se vuelve caótico

---

# Evolución de los Sistemas de Versionado

## Local Version Control

```plaintext
Mi PC
├── version1
├── version2
└── version3
```

## Centralized Version Control

```plaintext
Developers → Servidor Central
```

## Distributed Version Control

```plaintext
Dev ↔ Repo Central ↔ Dev
```

---

# ¿Qué es Git?

> Git es un sistema de control de versiones distribuido.

Creado por **Linus Torvalds** en 2005.

## Características

- Muy rápido
- Distribuido / offline-first
- Seguro (hashes)
- Escalable

---

# ¿Cómo Piensa Git?

## Otros Sistemas

Guardan diferencias entre versiones.

## Git

Guarda **snapshots completos** del proyecto.

```plaintext
Commit A → Foto completa
Commit B → Foto completa
Commit C → Foto completa
```

---

# ¿Por Qué Git es Potente?

- Cada clon es un backup completo
- Casi todas las operaciones son locales
- Historial completo disponible offline
- Cada commit tiene hash único

```plaintext
e83c5163316f89bfbde7d9ab23ca2e25604af290
```

---

# Modelo Mental de Git

```plaintext
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Repository
```

## Componentes

- **Working Directory:** tus archivos actuales
- **Staging Area:** cambios preparados
- **Repository:** historial guardado

---

# Crear / Obtener un Repositorio

## Proyecto Nuevo

```bash
git init
```

## Proyecto Existente

```bash
git clone <url>
```

## Ver Estado

```bash
git status
```

---

# Commits

Un **commit** es una foto del proyecto en un momento dado.

```bash
git add .
git commit -m "Agrego autenticación"
```

## Buenas Prácticas

- Un commit = un cambio lógico
- Commits pequeños y frecuentes
- Mensajes claros y descriptivos

---

# Ejemplos de Commit Messages

## Buenos

```plaintext
Add login endpoint with JWT authentication
Fix validation bug on signup form
Refactor payment service to use strategy pattern
Remove deprecated customer endpoint
```

## Malos

```plaintext
Cambios
Fix
Update stuff
Arreglo varias cosas
asdf
```

---

# Ignorar Archivos con .gitignore

```gitignore
node_modules/
.env
.idea/
target/
```

## Usar Para

- Dependencias
- Variables sensibles
- Configuración local
- Archivos generados automáticamente

---

# Branches

Una **branch** es una línea paralela de desarrollo.

```bash
git checkout -b feature-auth
```

## Permiten

- Desarrollar features aisladas
- Experimentar sin romper main
- Trabajar en paralelo

---

# Merge

Combina cambios de una branch en otra.

```bash
git merge feature-auth
```

## Uso Típico

- Integrar una feature terminada a `main`

---

# Merge Conflicts

Ocurren cuando dos ramas modifican la misma parte.

```java
<<<<<<< HEAD
return user.getName();
=======
return user.getFullName();
>>>>>>> feature-auth
```

---

# Resolver Merge Conflicts Paso a Paso

## 1. Git marca conflicto al mergear

```bash
git merge feature-auth
```

```plaintext
CONFLICT (content): Merge conflict in UserService.java
Automatic merge failed
```

## 2. Ver archivos conflictuados

```bash
git status
```

---

# Resolver Merge Conflicts Paso a Paso (cont.)

## 3. Abrir archivo y editar manualmente

```java
<<<<<<< HEAD
return user.getName();
=======
return user.getFullName();
>>>>>>> feature-auth
```

↓

```java
return user.getFullName();
```

## 4. Marcar como resuelto

```bash
git add UserService.java
```

## 5. Finalizar merge

```bash
git commit
```

---

# Git vs GitHub

## Git

Herramienta de versionado local

## GitHub

Hosting online para repositorios Git

### Alternativas

- GitLab
- Bitbucket

---

# Sincronización con Remoto

## Subir Cambios

```bash
git push
git push -u origin feature-auth
```

## Traer Cambios

```bash
git pull
git pull origin main
```

---

# Workflow Profesional con GitHub

```plaintext
main
 ├── feature/123-login
 ├── feature/245-payment-retry-flow
 ├── feature/381-user-profile-settings
 └── hotfix/912-navbar-mobile-overflow
```

---

# Proceso de Trabajo en GitHub

1. Pull de `main`
2. Crear branch de feature
3. Desarrollar
4. Commit frecuente
5. Push branch remota
6. Abrir Pull Request
7. Code Review
8. Merge a `main`

---

# Pull Requests

Permiten:

- Revisar código antes de mergear
- Discutir implementación
- Aprobar cambios
- Mantener calidad técnica

---

# Flujo Completo Real

```plaintext
git checkout main
git pull
git checkout -b feature/245-payment-retry-flow
git add .
git commit -m "Implement retry logic for failed payments"
git push -u origin feature/245-payment-retry-flow
→ Abrir Pull Request
→ Merge
```

---

# Resumen de Comandos

```bash
git init        → Inicializar repo nuevo
git clone URL   → Clonar repo existente
git status      → Ver estado actual
git add .       → Stagear cambios
git commit -m "Add login endpoint" → Crear commit
git log         → Ver historial
git branch      → Listar branches
git checkout -b feature/123-login → Crear/cambiar branch
git merge feature/123-login → Mergear branch
git pull        → Traer cambios remotos
git push        → Subir cambios remotos
```

---

# Resumen Final

Git permite:

- Versionar código profesionalmente
- Colaborar en equipo sin caos
- Recuperar cambios fácilmente
- Trabajar en paralelo con branches
- Escalar desarrollo de software real

## Frase para Recordar

> Git no guarda archivos.  
> **Git guarda la historia de tu proyecto.**

## Recurso Oficial

https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control