# Write a program to read a number and check whether it is a prime number.
def prime(no):
    chk = 0
    for i in range(2, (no//2) + 1):
        if no % i == 0:
            chk += 1
    return chk


while True:
    x = int(input("Enter a number: "))
    is_prime = prime(x)

    if is_prime != 0:
        print("It is not a prime number!")
    else:
        print("It is a prime number")

