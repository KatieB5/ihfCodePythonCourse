#1

def print_name(name):
    print(name)

print_name("Katie")

#2

def hello(name):
    print("Hello, " + name)

hello("Katie")

#3

names = ["Alice", "Bob", "Charlie"]

for name in names:
    hello(name)

#4

def area_calculator(x, y):
    print(str(x * y))

area_calculator(4, 6)

#5

def print_list(list):
    for item in list:
        print(item)

print_list(["book", "textbook", "magazine", "newspaper", "journal article"])

#6

def school_decider(age):
    if (age in range (1, 11)):
        print("You're too young to go to this school")
    elif (age in range(11, 17)):
        print("You can can come to this school")
    elif (age > 16):
        print("You're too old for school")
    elif (age == 0):
        print("You're not born yet!")

school_decider(1)