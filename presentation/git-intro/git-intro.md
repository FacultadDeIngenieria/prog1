class: center, middle, inverse

# Introducción a la Programación I
Git intro

---

# Agenda

- What is a Version Control System?
- What is Git?
- Git Basics
- Github

---

![Copias]({{site.baseurl}}/presentation/git-intro/copias.png)

---

# What is a Version Control System?

- Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.
- It allows you to:
  - revert selected files back to a previous state
  - revert the entire project back to a previous state
  - compare changes over time
  - see who last modified something that might be causing a problem, who introduced an issue and when
  - Recover and more

---

# What is Git?

- Git (2005) is a free and open source distributed version control system.

---

# Other Version Control Systems

Other Version Control Systems (CVS, Subversion, and Perforce), they store information on a list of file-based changes. This is called **delta-based** version control.

![Other Version Control]({{site.baseurl}}/presentation/git-intro/other-version-control.png)

---

# Git Benefits

With Git every time you save the state of the project, Git takes a picture of what all your files look like at that moment and stores a reference to that snapshot.
To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored.

![Git Benefits]({{site.baseurl}}/presentation/git-intro/git-benefits.png)

---

# Git can work locally

- **Local Operation**: Most operations in Git need only local files and resources to operate. This allows you to work offline and travel with your repository.
- **Tracking Changes**: it’s impossible to change the contents of any file or directory without Git knowing about it.

---

# Three states: modified, staged, and committed

- **Modified** means that you have changed the file but have not committed it to your database yet.
- **Staged** means that you have marked a modified file in its current version to go into your next commit snapshot.
- **Committed** means that the data is safely stored in your local database.

---

# Common Git workflow

- You modify files in your working tree.
- You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area.
- You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
![Three states]({{site.baseurl}}/presentation/git-intro/three-states.png)

---

# GitHub

GitHub is a for-profit company that offers a cloud-based Git repository hosting service. Essentially, it makes it a lot easier for individuals and teams to use Git for version control and collaboration.

https://github.com

![Github]({{site.baseurl}}/presentation/git-intro/github.png)


---

# Putting into practice

https://ohmygit.org/

Oh My Git! is a game that teaches you how to use Git. Follow the instructions to download it and run it.
