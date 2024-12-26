# Write a program to remove all the lines that contain the
# character “a” in a file and write it to another file.

with open('file.txt', 'r') as f:
    with open('file2.txt', 'w') as g:
        data = f.readlines()
        for line in data:
            c_a, c_A = line.count("a"), line.count("A")
            if c_a == 0 and c_A == 0:
                g.write(line)

