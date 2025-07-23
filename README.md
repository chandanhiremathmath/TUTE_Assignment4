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

Place a `sample.txt` file in the same directory, then run:


