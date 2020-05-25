#1
def is_odd(num):
    if num % 2 == 0:
        return True
    return False
# test
is_odd(2)

#2
def reverse_word(word):
    reversed_word = ""
    word_length = len(word) 
    while word_length > 0: 
        reversed_word += word[word_length - 1]
        word_length -= 1 
    # print(reversed_word)
    return reversed_word

# test
reverse_word("Umbrella")

#3
def falling_stars(num):
    stars = ""
    for x in range(0, num):
        stars += "*"
    print(stars)
    
    if num > 1:
        falling_stars(num - 1)

# test
falling_stars(5)

#4
def padlock(code):
    if code == "S3cr3tC0d3":
        return "Unlock"
    else:
        return "Locked"

padlock("S3cr3tC0d3")
padlock("SecretCode")

#5
def sum_of_multiples(max_num):
    total_sum = 0
    for x in range(0, max_num + 1):
        if x % 3 == 0:
            total_sum += x
        elif x % 5 == 0:
            total_sum += x
    return total_sum

# tests
sum_of_multiples(20)
sum_of_multiples(50)

#6
def is_prime(num):
    if num == 1:
        print("1 is not a prime number")
    if num != 1:
        for x in range(2, num):
            if num % x == 0:
                print(str(num) + " is not a prime number")
           
        print(str(num) + " is a prime number")

# tests
is_prime(1)
is_prime(2)
is_prime(3)
is_prime(11)
is_prime(29)

#7
def is_string_pallindrome(string):
    string_length = len(string)
    last_letter = string_length - 1
    i = 0
    while i < last_letter:
        if string[i] == string[last_letter]:
            i += 1
            last_letter -= 1
            if i == last_letter:
                print("String is a palindrome")
        else:
            print("String is not a palindrome")
            break

# tests 
is_string_pallindrome("radar")
is_string_pallindrome("sentence")

#7 alt version
def alt_is_string_pallindrome(string):
    reversed_string = reverse_word(string)
    if reversed_string.lower() == string.lower():
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

# test
alt_is_string_pallindrome("mAdam")

#8
def is_sentence_pallindrome(string):
    new_string = string.replace(" ", "").lower()
    reversed_string = reverse_word(new_string)
    if reversed_string == new_string:
        print("Sentence is a palindrome")
    else:
        print("Sentence is not a palindrome")

# test
is_sentence_pallindrome("a nut for a jar of Tuna")