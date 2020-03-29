#1
contacts = []

name = None

while name != " ":
    name = input("Enter a name: ")
    age = int(input("Enter age: "))
    contacts.append({"name":name, "age":age})
    print(contacts)