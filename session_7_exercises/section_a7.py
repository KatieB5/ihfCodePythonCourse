# 1


# 2
def radius_and_area(circumference, pi = 3.14):
    radius = int((circumference/pi)/2)
    area = int(radius ** 2)
    return radius, area

print(radius_and_area(234))

# 3

def first_word_finder(filename):
    f = open(filename, "r")

    total_lines = 0
    num_of_lines = 0
    lines = []

    for line in f:
        total_lines += 1
        
        if line.startswith("Mr"):
            num_of_lines += 1
            lines.append(line)

    return num_of_lines, lines

print(first_word_finder("../session_6_exercises/austen.txt"))

# 4
def new_file_of_params(*args):
    f = open("new_params_file.text", "w")
    f.write(str(args))

new_file_of_params(
    "Katie",
    "Bickford",
    "31031992",
    "O negative"
)

