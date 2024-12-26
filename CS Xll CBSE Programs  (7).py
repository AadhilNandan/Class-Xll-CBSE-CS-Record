# Write a program to read a text file and display the number of vowels,
# consonants, upper case, lower case characters in file.

with open("file.txt","r") as f:
    text = f.read()
    count_vowels = 0
    count_consonants = 0
    count_upper = 0
    count_lower = 0

    for ch in text:
        if ch.isupper():
            count_upper += 1
        if ch.islower():
            count_lower += 1
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                count_vowels += 1
            else:
                count_consonants += 1

print(f"Vowels: {count_vowels}")
print(f"Consonants: {count_consonants}")
print(f"Uppercase Characters: {count_upper}")
print(f"Lowercase Characters: {count_lower}")

