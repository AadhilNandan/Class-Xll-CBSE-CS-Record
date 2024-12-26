# Write a Python program to calculate and display the
# size of a file after removing End-Of-Line (EOL) characters,
# leading and trailing whitespace, and blank lines.

with open("file1.txt","r") as f:
    data = f.readlines()
    lines = ''
    for line in data:
        if line != "":
            lines += line.strip()

size = len(lines)
print(f" Size of file is {size}.")

