# 1
f = open("jabberwocky.txt", "r")

for x in f:
    print(x)


# 2
f = open("austen.txt", "r")

total_num_of_lines = 0

for lines in f:
    total_num_of_lines += 1

print("There are " + total_num_of_lines + " lines in this file")


# 3
f = open("numbers.txt", "r")

total = 0

for x in f:
    total += int(x)

print(total)
