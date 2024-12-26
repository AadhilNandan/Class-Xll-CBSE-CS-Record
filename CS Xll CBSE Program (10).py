# Write a program to create a binary file with roll number,
# name and mark. Input a roll number and update the marks.

import pickle
with open("file.dat", "wb") as f:
    run = True
    while run:
        roll_no = int(input("Enter the Roll No: "))
        name = input("Enter the Name: ")
        mark = float(input("Enter the Mark: "))
        pickle.dump([roll_no, name, mark], f)
        x = int(input("To continue press 1: "))
        if x != 1:
            run = False

with open("file.dat", "rb+") as g:
    details = []
    try:
        while True:
            details.append(pickle.load(g))
    except EOFError:
        pass

    found = False
    r_no = int(input("Enter the Roll No to Search: "))
    for i, line in enumerate(details):
        if line[0] == r_no:
            mrk = float(input("Enter new mark: "))
            details[i][2] = mrk
            found = True
            print("Marks changed")
            print(f"Roll No: {line[0]} , Name: {line[1]}, Marks: {line[2]}")
            break

    if not found:
        print("No record found with the given Roll No.")
    else:
        g.seek(0)
        g.truncate()
        for record in details:
            pickle.dump(record, g)

