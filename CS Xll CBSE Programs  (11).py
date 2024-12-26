# Write a program to create a random number generator
# that generates random numbers between 1 to 6 simulating a die.

import random
run = True
while run:
    print("="*15, " Welcome to Die Simulator ", "="*15 )
    x = int(input("To Play Press 1: "))
    if x == 1:
        print(f"You got {random.randint(1, 6)}")
    else:
        run = False
    print("="*25, " Thank You ", "="*25, "\n")


