# Write a Python program to create a CSV file storing student information
# (Roll_No, Name, Marks). Collect data for 5 students from the user
# and Save the collected data into the CSV file.
# Read the content of the CSV file and display it.

import csv

with open("Students.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll_No", "Name", "Marks"])
    print("*" * 20, "Enter Details", "*" * 20)
    for i in range(1, 6):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        mark = float(input("Enter Mark: "))
        details = [roll_no, name, mark]
        writer.writerow(details)
        print("*" * 40)

with open("Students.csv", "r") as g:
    data = csv.reader(g)
    for row in data:
        if row:
            print(row)

