class: center, middle, inverse

# Understanding LLM Code Generation Pitfalls & Hallucinations

---

## What Are LLM "Hallucinations"?

**Definition**: When AI generates false or fabricated information with high confidence.

### Why It Happens:

Pattern recognition without true understanding
Training on unverified internet data
Over-optimization for plausible-sounding responses

--- 

# Code-Specific Hallucinations:
```python
# Ask: "Write Python code to connect to PostgreSQL with SSL"
# Hallucinated response might include:
import postgresql  # Non-existent library
conn = postgresql.connect(ssl="fake_parameter")  # Wrong syntax
```

--- 

# Major LLM Shortcomings for Coders
## 1. Wrong Library Versions
```python
# Ask: "Use TensorFlow for image classification"
# LLM might give:
tf.keras.layers.Conv2D(32, (3, 3), activation='relu')  # Old API format
New Version: tf.keras.layers.Conv2D(32, kernel_size=3, activation='relu')
```

---

## 2. Imaginary Features
```javascript
// Ask: "React hook to cache API calls"
// Hallucinated response:
import { useCache } from 'react';  // Not a real hook!
```

---

# Hallucination Case Studies
## Case 1: Fake Documentation
```text
"Write code using pandas.read_xml()"
Reality: read_xml() didn't exist until pandas 1.3.0 - LLM might invent parameters.
```

---

## Case 2: Nonexistent Error Handling
```python
# Claimed to handle all exceptions:
try:
    risky_operation()
except:  # Actually hides KeyboardInterrupt (Ctrl+C)!
    pass
```

---

# Testing for Hallucinations
## Library Verification:

```bash
pip show <library>  # Check if package exists
```

---
# API Cross-Checking:

```python
import inspect
print(inspect.getsource(function))  # View real implementation
```

---

# Sandbox Testing:

```python
from unittest.mock import Mock
test_db = Mock()  # Safe environment to test DB code
```

---

# Best Practices for Safe Coding
Do:
```python
# Ask for explanations:
"Explain this regex: ^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$"

# Request alternatives:
"Show 3 ways to iterate a dictionary in Python"
```
Don't:
```python
# Blindly trust:
"Write secure authentication for my app"  # Never!

# Use without testing:
deploy(ai_generated_code)  # Always review first!
```

---

# When Hallucinations Are Dangerous
## Security Code:

1. Fake "secure encryption" implementations
2. Imaginary OAuth2 parameters
3. Medical/Financial Systems:

```python
# Hallucinated formula:
def calculate_dosage(weight):
    return weight * 0.2  # No medical basis!
```
4. Legal Documents: Fabricated contract clauses

---

# Student Exercise: Spot the Bug
```python
# LLM-generated code:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```
## Tasks:
1. Find the syntax error
2. Improve efficiency (test only up to √n)
3. Write test cases

---

# Key Takeaways
1. Always verify LLM output against official docs
2. Test thoroughly - especially edge cases
3. Understand before copy-pasting
4. Use AI for:
   - Boilerplate generation
   - Documentation lookup
   - Error explanation

"Trust, but verify"

