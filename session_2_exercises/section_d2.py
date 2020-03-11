list_of_fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]

for fruit in list_of_fruit:
    print(fruit)

for numbers in range(1, 101, 1):
    print(numbers)

for numbers in range(1, 101, 2):
    print(numbers)

for years in range(1896, 2020, 4):
    print(years)

for number in range(1, 101, 1):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
