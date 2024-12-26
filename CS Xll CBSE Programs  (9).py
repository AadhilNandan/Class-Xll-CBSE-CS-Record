# Write a program to create a binary file with name and roll number.
# Search for a given roll number and display the name,
# if not found display appropriate message.

import pickle
with open("file.dat", "wb") as f:
    run = True
    while run:
        roll_no = int(input("Enter the Roll No: "))
        name = input("Enter the Name: ")
        pickle.dump([roll_no, name], f)
        x = int(input("To continue press 1: "))
        if x != 1:
            run = False

with open("file.dat", "rb") as g:
    details = []
    try:
        while True:
            details.append(pickle.load(g))
    except EOFError:
        found = False
        r_no = int(input("Enter the Roll No to Search: "))
        for line in details:
            if line[0] == r_no:
                print(f"Roll No: {line[0]} , Name: {line[1]}")
                found = True
        if not found:
            print("No record found with the given Roll No.")

