class: center, middle, inverse

# Publishing with GitHub Pages


---

## What is GitHub Pages?

- **Free** static site hosting from GitHub repositories  
- Built directly from your repo's files  
- Supports:  
  - HTML/CSS/JS websites  
  - Jekyll-powered blogs  
  - Project documentation  
  - Personal/portfolio sites  

---

## Why Use GitHub Pages?

✅ **Free hosting** (no server costs)  
✅ **Simple workflow** (just git push)  
✅ **Custom domains** (yourname.com)  
✅ **Built-in CI/CD** (automatic builds)  
✅ **Version controlled** (full history)  

---

# Core Technologies

### HTML Basics
```html
<!DOCTYPE html>
<html>
<head>
  <title>My Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Welcome</h1>
  <p>Edit this to build your site!</p>
</body>
</html>
```

---

# CSS Basics

```css
/* styles.css */
body {
  font-family: Arial;
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  color: #2e86ab;
}
```

---

# Jekyll: Static Site Generator
## Why Jekyll?

- Built into GitHub Pages
- Blog-aware with Markdown support
- Front Matter for metadata

Basic Structure
```
.
├── _config.yml
├── _posts/
│   └── 2024-05-15-welcome.md
├── _layouts/
│   └── default.html
└── index.md
```

---

# Publishing Methods

1. Branch Method

```bash
git checkout -b gh-pages
git push origin gh-pages
```

2. Docs Folder Method
- Enable in repo Settings → Pages
- Select main branch /docs folder

3. Actions Method: Use GitHub Actions for custom builds

---

# Step-by-Step: User Site

1. Create new repo: username.github.io
2. Add index.html:

```html
<!DOCTYPE html>
<html>
<body>
  <h1>Hello World!</h1>
</body>
</html>
```

3. Push to GitHub:

```bash
git add .
git commit -m "Initial site"
git push
```

---

# Setting up Jekyll

- Guide: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll
- Themes: https://jamstackthemes.dev/ssg/jekyll/


