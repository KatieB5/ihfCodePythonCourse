# 1
f = open("register.txt", "a")

name = True
while name:
    name = input("What is your name? ")
    f.write(name + "\n")
f.close()


# 2
def is_odd(num):
    if num % 2 == 0:
        return True
    return False

g = open("even.txt", "w")
for x in open("numbers.txt", "r"):
    if is_odd(int(x)):
        g.write(x)
g.close()


# 3
cipher = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "10": "J",
    "11": "K",
    "12": "L",
    "13": "M",
    "14": "N",
    "15": "O",
    "16": "P",
    "17": "Q",
    "18": "R",
    "19": "S",
    "20": "T",
    "21": "U",
    "22": "V",
    "23": "W",
    "24": "X",
    "25": "Y",
    "26": "Z"
}

decoded_message = ""

f = open("secret.txt", "r")
for x in f:
    cipher_key = x.strip()
    # decoded_message += cipher[x]
    print(cipher[cipher_key])
print(decoded_message)


# 4 (original version only based on frequency of 1 as leading digit)
def fake_data_calculator(file):
    f = open(file, "r")
    
    total_nums_in_file = 0
    total_nums_starting_with_1 = 0

    for x in f:
        if x:
            total_nums_in_file += 1
            if x[0] == "1":
                total_nums_starting_with_1 += 1
    
    leading_digit_probability = ((total_nums_starting_with_1/total_nums_in_file) * 100)

    if int(leading_digit_probability) >= 30:
        print("For " + file + " leading digit probablity is " + str(leading_digit_probability) + ", so this file probably does not contain fake data")
    else:
        print("For " + file + " leading digit probablity is " + str(leading_digit_probability) + ", so this file probably contains fake data")

data = ["accounts_1.txt", "accounts_2.txt", "accounts_3.txt"]

for file in data:
    fake_data_calculator(file)


# 4 (alternative version)

def fake_data_calculator2(file):
    f = open(file, "r")

    leading_dig_count = {}
        
    for i in range(1, 10):
        leading_dig_count[str(i)] = 0
    

    for x in f:
        if x:
            leading_dig_count[x[0]] += 1

    print("Results for: " + file)

    for y in range(1, 10):
        print(str(y) + "=" + str(leading_dig_count[str(y)]/100) + "%")

data = ["accounts_1.txt", "accounts_2.txt", "accounts_3.txt"]

for file in data:
    fake_data_calculator2(file)