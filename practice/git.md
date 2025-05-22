---
title: Trabajo Práctico del Taller
layout: practice
permalink: /practice/git
---

# Git Practice

**Deben juntarse en grupos de 3 alumnos.**

Un alumno del grupo debe crear un repositorio público en su cuenta Github llamado `MarkdownGuideBookProject`.

Todos los alumnos tienen que clonar ese repositorio en su computadora (no es necesario hacer un "fork" del repositorio).

El objetivo del trabajo práctico es armar una guía/libro/documentación del tema que el grupo quiera. La guía tiene que tener una sección por individuo, por ejemplo:

- Se elige el tema Habilidades esenciales para vivir, en un grupo de 3 personas, habrán 3 secciones: Cocinar, Finanzas y Salud. Cada integrante del equipo elige una sección y tiene que crear un archivo markdown narrando sobre el tema de la sección. Cada uno tiene que trabajar en una branch diferente al resto, con un nombre que identifique la sección en la que esta trabajando. (por ejemplo, cooking, finance o health).

Cada archivo de markdown tendrá que tener por lo menos 4 títulos principales (Heading1), 2 listas, 5 links y 4 imágenes o gifs. Las imágenes/gifs tienen que subirse también al repositorio.

Realicen los commits que crean necesarios usando descripciones apropiadas para los mensajes de los commits. Hagan el push a las branches del repositorio que tenían asignados (Cada uno a su repositorio).

Ahí termina la parte individual del trabajo práctico, la siguiente parte necesitan realizarla todos juntos.

Una vez que todas las secciones estén terminadas, tienen que realizar un Pull Request que trate de unificar los cambios de cada sección en main. Habrá un pull request por cada branch de sección.

Antes de unir los cambios, cada alumno deberá revisar el Pull Request de otra sección ajena a la suya, intentando unificar la manera de escribir, donde se guardan las imágenes (si usan una carpeta, que tengan un nombre apropiado, etc) y cualquier otra cosa relacionada a la calidad que crea pertinente. Una vez que cada sección esté ok, quien inició el pull request tiene que integrar los cambios (Merge a Main).

Una vez "mergeados" los cambios, se debe agregar un archivo de carátula e índice de la guía o libro (en un archivo markdown) llamado README.md . Tendrá el Título de la guia, los nombres de los integrantes en orden alfabético y links a cada una de las secciones.

## Pasos a seguir

### Clase 1
1. Crear rama con tu nombre
   - `git checkout -b <nombre-rama>`
   - `git push origin <nombre-rama>`
2. Crear archivo markdown con tu sección
   - `touch <nombre-seccion>.md`
3. Pushear los cambios a tu rama
   - `git add <nombre-seccion>.md`
   - `git commit -m "Agregando archivo markdown"`
   - `git push -u origin <nombre-rama>`
4. Pullear develop
   - `git pull origin develop`
   - `git checkout develop`
5. Mergear tu rama en develop
   - `git merge <nombre-rama>`
6. Resolver conflictos (si los hay)
7. Pushear los cambios a develop
   - `git push origin develop`
8. Crear un pull request desde develop a main

### Clase 2
1. Ir a la rama develop
    - `git checkout develop`
2. Pullear develop
    - `git pull origin develop`
3. Ir a tu rama
    - `git checkout <feature/student-name/theme>`
4. Mergear develop en tu rama
    - `git merge develop`
5. Resolver conflictos (si los hay)
6. Agregar tu contenido al README.md 
    - `git add .`
    - `git commit -m "Add <Theme Name>"`
7. Pushear los cambios a tu rama
    - `git push origin <feature/student-name/theme>`
8. Crear un pull request desde tu rama a develop (desde Github)
9. Pedirle a un compañero que te revise el pull request (desde Github)
10. Mergear los cambios del Pull Request desde Github*

*Si no te deja mergear, es porque no tenes la última versión de develop en tu rama. Para solucionarlo, tenes que volver al paso 1.


**Opcional:**
1. Si tenes cambios ya hechos en otra rama pero no estas en la tuya, podes stashearlos para no perderlos
    - `git stash`
2. Podes verificar que se haya stasheado correctamente
    - `git stash list`
3. Luego podes ir a tu rama
    - `git checkout <feature/student-name/theme>`
4. Y por último, podes aplicar los cambios stasheados
    - `git stash apply`
5. Si no queres aplicar los cambios, podes eliminarlos
  - `git stash drop` (si no lo necesitas más)
6. Si queres aplicar los cambios y eliminarlos al mismo tiempo
  - `git stash pop`