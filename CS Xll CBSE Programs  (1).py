# Write a program to accept string as an input and to count and display the total number of times a character is present.

def countchar(sentence, character):
    sentence = sentence.lower()
    character = character.lower()
    count = 0
    for char in sentence:
        if character == char:
            count += 1
        else:
            continue
    if count == 0:
        print(f"{character} is not found")
    else:
        print(f"The no of occurrence of {character} is {count}")


input_sentence = input("Enter a sentence: ")
input_character = input("Enter a character to count: ")
countchar(input_sentence, input_character)

