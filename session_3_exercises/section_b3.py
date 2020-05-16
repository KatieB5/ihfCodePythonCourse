#1
apple = {"Type":"Bramley", "Price":"0.39", "Colour":"Green"}

#2
apple["best_before"] = "03/05/2021"

#3
apple["Price"] = "0.41"

#4
apple["is_on_sale"] = True
print(apple)

#5
for key in apple:
    print(str(key) + " = " + str(apple[key]))

#6
del (apple["is_on_sale"])