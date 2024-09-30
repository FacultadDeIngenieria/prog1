class: center, middle, inverse

# Files

---

# Understanding Files

Definition of a file:

- A file is a collection of data stored in a computer system.
- Files can store different types of data like text, numbers, images, videos, or binary information.
- They are stored on a device’s storage (hard drive, SSD, etc.) and can be accessed by programs to read, write, or manipulate data.

---

# Slide: Why Do We Need Files?

- ***Persistent Storage***: Files allow data to be stored permanently on a device. Without files, all data would be lost when a program closes or the computer shuts down.
- ***Data Sharing:*** Files can be shared across different programs or systems (e.g., sending an image or document by email).
- ***Organizing Information:*** Files help organize and categorize data in a system, such as saving documents in folders, logging information, or managing large datasets.

---

# Key Characteristics

**File Name:** Every file has a unique name that identifies it on the system. A file name is usually divided into two parts: **name** and **extension**.
  - Name: Describes the file (e.g., document, data).
  - Extension: Indicates the type of file (e.g., .txt, .csv, .jpg).

```
Example:
	•	notes.txt is a file where “notes” is the name, and .txt is the extension that tells us it’s a text file.
```

**File Path:** The file path describes where a file is located on your computer. A file can be in different directories or folders. The path tells the system where to look.

```
Example:
	•	C:/Documents/notes.txt indicates the file is located in the “Documents” folder on the C: drive.
```

---

# Types of Files: txt

***Text Files (.txt):***

- Plain text files contain human-readable data. 
- Used to store notes, logs, or configuration settings. 

```
Example: A shopping list saved in groceries.txt:

Apples
Bananas
Bread
```

---

# Working with Text Files in Python

```python
# read
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# write
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample text.")
```

- 'r': Read mode, opens an existing file.
- 'w': Write mode, creates a new file or overwrites the existing one.
- 'a': Append mode, adds to the end of the file without overwriting.

---

# Types of Files: csv

***CSV (Comma-Separated Values)*** files are used for structured data like spreadsheets. Each row represents a record, and columns are separated by commas.

```
Example: A table saved as data.csv:
Name, Age, Grade
Alice, 20, B
Bob, 19, A
```

---

# Working with CSV files in Python

```python
import csv
# read
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# write
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 20, 'B'])
```

- csv.reader(): Reads a CSV file row by row.
- csv.writer(): Writes to a CSV file.

---

# Types of Files: binary

***Binary Files:*** These files store data in a binary (0s and 1s) format and are not human-readable.

```
Examples: Images (.jpg), audio (.mp3), and executable files (.exe).
```


---

# Types of Files: zip

***Zip***: These files contain one or more compressed files or folders. They reduce the file size and are convenient for sharing multiple files together.

```
Example: project.zip might contain several text, CSV, and image files compressed together.
```

---

# Working with zip files in Python

```python
import zipfile

# compressing files
with zipfile.ZipFile('archive.zip', 'w') as archive:
    archive.write('example.txt')
    archive.write('data.csv')
    
# extracting files from a zip
with zipfile.ZipFile('archive.zip', 'r') as archive:
    archive.extractall('extracted_files/')
    
# listing files in a zip
with zipfile.ZipFile('archive.zip', 'r') as archive:
    print(archive.namelist())    
```

---

# Common file handling operations:

```python
# reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line)

# checking that a file exists
import os
if os.path.exists('example.txt'):
    print("File exists")
else:
    print("File not found")
```
