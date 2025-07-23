try:
    file = open('sample.txt', 'r')  # Try to open the file
    print("The file exists. Contents are:")

    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1

    file.close()  # Manually close the file
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

