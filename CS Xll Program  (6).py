# Write a program to read a text file by line and
# display each word separated by a "#"
with open("file.txt", "r") as f:
    for line in f:
        new_line = "#".join(line.split())
        print(new_line + "#")

