# Write a program Input a list of elements, create an empty list and add elements divisible by 5 to it. Display the resulting list?

def div5():
    list_1, list_2 = [], []
    n = int(input("Enter the no of inputs: "))
    for i in range(1, n+1):
        element = int(input(f"Enter element {i}: "))
        list_1.append(element)
    print(f"List 1: {list_1}")

    for j in list_1:
        if j % 5 == 0:
            list_2.append(j)
    print(f"List of number divisible by 5: {list_2}")


div5()