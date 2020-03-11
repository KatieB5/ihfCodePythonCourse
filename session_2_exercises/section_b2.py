name = input("What is your name? ")
if name == "Alice":
    print("Hello, Alice")
elif name == "Bob":
    print("You're not Bob! I'm Bob")
else:
    print("You must be Charlie")


age = int(input("Enter your age "))
if age < 11 and age > 0:
    print("You're too young to go to this school")
elif age >= 11 and age < 16:
    print("You can come to this school")
elif age > 16:
    print("You're too old for school")
else:
    print("You're not born yet!")


month = str(input("Name a month of the year "))
if (month == "March") or (month == "April") or (month == "May"):
    print(month + " is in Spring")
elif (month == "June") or (month == "July") or (month == "August"):
    print(month + " is in Summer")
elif (month == "September") or (month == "October") or (month == "November"):
    print(month + " is in Autumn")
elif (month == "December") or (month == "January") or (month == "February"):
    print(month + " is in Winter")
else:
    print("I don't know")
    

x, y = input("Please provide two numbers ").split()
x = int(x)
y = int(y)
if (x%2 == 0) and (y%2 == 0):
    print("Even")
elif (x%2 == 1) and (y%2 ==1):
    print("Odd")
else:
    print(x * y)

