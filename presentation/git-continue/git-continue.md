class: center, middle, inverse

# Introducción a la Programación I
# Git continue

---

# Agenda
- Branches
- Conflict Resolution
- TP

---

# Branches

![Git Branch]({{site.baseurl}}/presentation/git-continue/git-branch.png)

- Each commit is a depicted as a little box
- The branch `master` points to a commit

---

![Git Branching]({{site.baseurl}}/presentation/git-continue/branching.png)

---

A group of commits that create a single narrative are called a branch

![Git Branches with commits]({{site.baseurl}}/presentation/git-continue/branching-with-commits.png)

---

# Conflicts

- Git is very good at resolving modifications when merging branches and in most cases a git merge runs smooth and automatic.
  - Then a merge commit appears without you even noticing.
- But sometimes the same portion of the code/text is modified on two branches in two different ways and Git issues a conflict. Then you need to tell Git which version to keep (resolve it).

---

# Conflict Resolution

- It is good that Git conflicts exist: Git will not silently overwrite one of two differing modifications.
- Conflicts may look scary, but are not that bad after a little bit of practice. Also they are luckily rare.
- Don’t be afraid of Git because of conflicts. You may not meet some conflicts using other systems because you simply can’t do the kinds of things you do in Git.
- You can take human measures to reduce them.

---

# Trabajo Práctico

- Vamos a ir resolviéndolo juntos
- https://github.com/FacultadDeIngenieria/tallergitprog1/tree/2023
