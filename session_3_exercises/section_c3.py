#1
contacts = []

name = None

while name != " ":
    name = input("Enter a name: ")
    age = int(input("Enter age: "))
    contacts.append({"name":name, "age":age})
    print(contacts)

#2
import random

beetles = []
scores = []
winner = None

dice_number = random.randint(1, 6)

parts = {
    "1": "Eye",
    "2": "Mouth",
    "3": "Antennae",
    "4": "Leg",
    "5": "Head",
    "6": "Body"
}

players = input(int("How many players are playing this game? "))

for n in range(players):
    beetles.append({
        "1": 2,
        "2": 1,
        "3": 2,
        "4": 6,
        "5": 1,
        "6": 1
    })
    scores.append(0)

while not winner:
    for current_player in range(players):

        x = input("Player " + str(current_player) + ": Please roll the dice...")
        if x == "q":
            break
        dice_roll = str(random.randint(1, 6))
        scores[current_player] += 1
        print("You've rolled a: " + dice_roll)
        if beetles[current_player][dice_roll] > 0:
            if dice_roll == "1" and beetles[current_player]["5"]:
                print("You can't have an eye without a head")
            elif dice_roll == "2" and beetles[current_player]["5"]:
                print("You can't have a mouth without a head")
            elif dice_roll == "3" and beetles[current_player]["5"]:
                print("You can't have an antenna without a head")
            elif dice_roll == "4" and beetles[current_player]["6"]:
                print("You can't have a leg without a body")
            else:
                print("You've got a " + parts[dice_roll])
                beetles[current_player][dice_roll] -= 1
                for body_part in beetles[current_player]:
                    if beetles[current_player][body_part]:
                        print("You need the following bits to make a full beetle: " +
                              str(beetles[current_player][body_part]) + " " + parts[body_part])
                if sum(beetles[current_player].values()) == 0:
                    winner = current_player

print("The winner is: " + str(winner))

print(scores)