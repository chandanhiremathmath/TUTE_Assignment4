# TUTE_Assignment4

#TASK 1

# Read a File and Handle Errors in Python

This Python script reads a file named `sample.txt` and prints its contents line by line.  
It also handles errors gracefully in case the file does not exist.

## 📌 Features

- Opens a text file named `sample.txt`
- Reads and prints each line with line numbers
- Handles `FileNotFoundError` using a `try-except` block
- Manually closes the file after reading

## 🧠 How It Works

- Tries to open the file using `open('sample.txt', 'r')`
- If successful, it reads the file line by line and prints the content
- If the file does not exist, it prints an error message:  
  `"Error: The file 'sample.txt' does not exist."`

## 🚀 How to Run

Place a `sample.txt` file in the same directory, then run


#TASK2

# 📝 File Handling in Python: Write, Append, and Read

## 📌 Overview

This Python program demonstrates how to perform **file operations** — writing, appending, and reading — using the built-in `open()` function. It interacts with a file named `output.txt`.

---

## 📂 Features

✅ Write user input to `output.txt`  
✅ Append additional input to the same file  
✅ Read and display the complete content of the file  

---

## 🛠 How the Program Works

1. **Write Mode (`'w'`)**
   - Prompts the user to input text.
   - Writes the input to `output.txt`, replacing any existing content.

2. **Append Mode (`'a'`)**
   - Prompts the user to input additional text.
   - Appends the input to the same file without removing existing content.

3. **Read Mode (`'r'`)**
   - Reads and displays the entire content of the file after write and append operations.






