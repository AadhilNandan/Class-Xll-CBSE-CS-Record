# Write a Python program to analyze a sample text file,
# determine the most commonly occurring word, and display its frequency

with open("file.txt", "r") as f:
    data = f.read()
    words = (data.lower()).split()
    max_count = [0, ""]
    for i in words:
        c = words.count(i)
        if c > max_count[0]:
            max_count = [c, i]
    print(f"The most occurring word is '{max_count[1]}' with frequency {max_count[0]}")



