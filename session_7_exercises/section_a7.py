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

# 5

import json 

def new_file_of_kwargs(**kwargs):
    f = open("new_kwargs_file.text", "w")
    f.write(json.dumps(kwargs))

new_file_of_kwargs(
    fname = "Katie",
    lname = "Bickford",
    dob = "31031992",
    blood_type = "O negative"
)

# 6
from functools import reduce
import operator 

def calculator_func(*nums, operand):
    if operand == "multiply":
        # print(reduce(operator.mul, nums, 1))
        return reduce(operator.mul, nums, 1)
    if operand == "add":
        # print(sum(nums))
        return sum(nums)

calculator_func(1, 2, 3, 4, operand = "multiply")
calculator_func(65, 200, 84, 12, operand = "add")

# 7 a
import csv 

def new_contacts(contacts):
    new_file = csv.writer(open("new_contacts_file.csv", "w"))
    for key, value in contacts.items():
        new_file.writerow([key, value])

new_contacts({
    "fname": "Katie",
    "lname": "Bickford",
    "phone_number": "01615478893"
})

# 7 b

prompt = input("Would you like to add some contects? (Y/N)")

if prompt == "Y":
    new_file_2 = open("new_contacts_file_2.csv", "a")
    fieldnames = ['fname', 'lname', 'phone_number']
    writer = csv.DictWriter(new_file_2, fieldnames=fieldnames)
    writer.writeheader()
    
    fname = True

    while fname:
        fname = input("First name: ")
        lname = input("Last name: ")
        phone_number = input("Phone number: ")
        writer.writerow({'fname': fname, 'lname': lname, 'phone_number': phone_number})
    new_file_2.close()
    exit()
