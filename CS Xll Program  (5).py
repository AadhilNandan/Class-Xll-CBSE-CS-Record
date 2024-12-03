# Write a program to Create add_client and delete_client methods in Python to add a new client
# and remove a client from a list of client names,
# simulating the insertion and deletion operations of a stack data structure.

def add_client(lst):
    x = input("Enter an client name: ")
    lst.append(x)
    return True


def delete_client(lst):
    print("Deleted Client: ", lst.pop() if lst else "Stack underflow")
    return True


def exit(lst):
    print("Program exited Successfully")
    return False


stack = []
actions = {
    1: add_client,
    2: delete_client,
    3: exit
}

run = True
while run:
    print('''
    1: Add Client
    2: Delete Client
    3: Exit''')
    choice = int(input("Enter your choice (1,2,3): "))
    action = actions.get(choice)
    run = action(stack)

