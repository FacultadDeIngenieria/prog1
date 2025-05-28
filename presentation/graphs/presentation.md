class: center, middle, inverse

# Python Graphics with Matplotlib

---

# Why Matplotlib?

- Default Python plotting library
- Works out-of-the-box with Python
- Publication-quality figures
- Simple to complex visualizations

---

# Installation

```bash
pip install matplotlib
```

```python
# Basic import
import matplotlib.pyplot as plt
```

```python
# Jupyter magic for notebooks
%matplotlib inline
# Allows not using plt.show()
```

---

# Basic Plot Types

```python
# Line plot
plt.plot([1,2,3,4], [1,4,9,16], 'ro-')

# Bar chart
plt.bar(['A','B','C'], [3,7,2])

# Scatter plot
plt.scatter(x, y, c='blue', marker='x')

# Histogram
plt.hist(data, bins=30)
```

---

# Customizing Plots

```python
plt.title("My Awesome Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.legend(['Data Series'])

# Set axis limits
plt.xlim(0, 10)
plt.ylim(0, 20)

# Add text
plt.text(5, 15, "Important Point")
```

---

# Saving Plots

```python
# Save as PNG (default)
plt.savefig('plot.png')

# High-res PDF
plt.savefig('plot.pdf', dpi=300)

# Transparent background
plt.savefig('plot.png', transparent=True)

# Adjust size (width, height in inches)
plt.figure(figsize=(8,6))
```

---

# Subplots

```python
# Create 2x2 grid of plots
fig, axs = plt.subplots(2, 2)

axs[0,0].plot(x, y)  # Top-left
axs[0,1].scatter(x, y)  # Top-right
axs[1,0].bar(labels, values)  # Bottom-left
axs[1,1].hist(data)  # Bottom-right

plt.tight_layout()  # Prevent overlap
```

---

# NumPy Data Generation Basics

**Why NumPy?**
- Foundation for numerical computing in Python
- 50-100x faster than regular Python lists
- Essential for scientific computing

```python
import numpy as np
```

---

# Using Numpy

## Basic arrays
a = np.array([1, 2, 3])          # 1D array
b = np.array([[1,2], [3,4]])     # 2D array


## Special arrays
zeros = np.zeros(10)             # Array of 0s
ones = np.ones((3,3))           # 3x3 matrix of 1s 
random = np.random.rand(100)     # 100 random numbers (0-1)

---

# Generating data for graphs

```python
# For line plots
x = np.linspace(0, 10, 100)      # 100 pts from 0-10
y = np.sin(x)                    # Sine wave

# For scatter plots
x = np.random.normal(0, 1, 100)  # 100 pts, mean=0, std=1
y = x * 2 + np.random.randn(100) # Linear relationship with noise

# For 3D plots
z = np.linspace(0, 10, 100)
x = np.sin(z)
y = np.cos(z)

# For histograms
data = np.random.gamma(2, 2, 1000) # Gamma distribution

# For images
image = np.random.rand(100, 100)  # 100x100 random pixels
```

--- 

# Combining with matplotlib

```python
plt.plot(np.random.random(100).cumsum())  # Random walk
```
