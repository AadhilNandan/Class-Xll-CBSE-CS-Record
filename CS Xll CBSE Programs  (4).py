# Write a program to implement all the basic operations of a stack.
def push(lst):
    x = input("Enter an element: ")
    lst.append(x)
    return True


def pop(lst):
    print("Deleted element: ", lst.pop() if lst else "Stack underflow")
    return True


def peek(lst):
    print("Top element: ", lst[-1] if lst else "Stack underflow")
    return True


def display(lst):
    print("Stack elements: ", lst[::-1] if lst else "Stack underflow")
    return True


def exit(lst):
    print("Program exited Successfully")
    return False


stack = []
actions = {
    1: push,
    2: pop,
    3: display,
    4: peek,
    5: exit
}

run = True
while run:
    print('''
    1: Push
    2: Pop
    3: Display
    4: Peek
    5: Exit''')
    choice = int(input("Enter your choice (1,2,3,4,5): "))
    action = actions.get(choice)
    run = action(stack)

