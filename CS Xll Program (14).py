# Write a Python program that Accept employee details
# (Emp_NO, Name, Salary) from the use and Save the
# collected data into a binary file using the pickle module.
# Read the data from the binary file and display it.

import pickle

with open("Employee.dat", "ab") as f:
    while True:
        print()
        emp_no = int(input("Enter Employee No: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        emp_data = [emp_no, name, salary]
        pickle.dump(emp_data, f)
        x = int(input("To add another data, press 1: "))
        if x != 1:
            break

with open("Employee.dat", "rb") as g:
    print("\nEmployee Details:")
    print("-" * 40)

    try:
        while True:
            emp = pickle.load(g)
            print("-" * 40)
            print(f''' 
Employee No    : {emp[0]}
Employee Name  : {emp[1]}
Employee Salary: {emp[2]}\n''')
            print("-" * 40)

    except EOFError:
        print("End Of Data")

