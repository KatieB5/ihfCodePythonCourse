#1
import random
number = random.randint(1, 10)
print(number)

#2
number = int(input("Provide a number between 1 and 10: "))
while number != 7:
   number = int(input("Provide a number between 1 and 10: "))
if number == 7:
    print("Wow lucky number 7!")

#2
import random
rand_num = random.randint(1, 10)
while rand_num != 7:
   rand_num = random.randint(1, 10)
if rand_num == 7:
    print("Wow lucky number 7!")

#3
from math import floor, ceil

width = int(input("Please provide a rectangle width: "))
height = int(input("Please provide a rectangle height: "))

area = floor(width * height)

print("The area of your rectangle is: " + str(area))

#4
user_input = input("What is your password? ")
password = "qwerty123"

user_guesses = 0

while user_guesses < 2:
    if user_input == password:
        print("You have successfully logged in.")
        break
    else:
        print("PASSWORD FAILURE")
        user_input = input("What is your password? ")
        user_guesses += 1
print("System Failure")

#5
import random

computer_score = 0
user_score = 0
while computer_score < 2 and user_score < 2:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = input("Do you choose rock, paper or scissors? ")
    print("You chose: " + user_choice)
    print("The computer chose: " + computer_choice)
    
    if user_choice == computer_choice:
        print("Its a draw!")
        computer_score += 1
        user_score += 1
    elif user_choice == "rock" and computer_choice == "paper":
        print("Sorry, you lose!")
        computer_score += 1
    elif computer_choice == "rock" and user_choice == "paper":
        print("Great stuff - you win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Sorry, you lose!")
        computer_score += 1
    elif computer_choice == "paper" and user_choice == "scissors":
        print("Great stuff - you win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Sorry, you lose!")
        computer_score += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        print("Great stuff - you win!")
        user_score += 1
    else:
        print("Please choose rock, paper, or scissors? ")
print("Game over! You scored: " + str(user_score) + " and the computer scored: " + str(computer_score))


