name = str(input("What is your name? "))
if name == "Bob":
    print("Hello, Bob!")

name = str(input("What is your name? "))
if name != "Alice":
    print("You're not Alice!")

password = str(input("What is the password? "))
if password == "querty123":
    print("You have successfully logged in")
else:
    print("Password failure")

even_or_odd = int(input("Enter a number "))
if even_or_odd%2 == 0:
    print("Even")
else:
    print("Odd")

x, y = input("Enter two values: ").split()
total = int(x+y)
if total > 21:
    print("Bust")
else:
    print("Safe")