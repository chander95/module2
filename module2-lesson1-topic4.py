#1 if one cake requires 250 grams of flour and you only have 2.5kg of flour, how many cakes can you make using the arithmatic operations
gram = 1
kilogram = gram * 1000

current_flour = kilogram * 2.5
#print(current_flour)

cake = gram * 250

cakes = current_flour // cake
print(cakes)
print("----------------------------------------------")

#2 Use the assignment operator to claim a variable "kingdom" with a value of "Pythonland"
kingdom = "Pythonland"
print(kingdom)
print("----------------------------------------------")

#3 Given two prices, "shirt1 = 45" and "shirt2 = 50", use a comparison operator to check if shirt1 is cheaper than shirt2
shirt1 = 45
shirt2 = 50
print(shirt1 < shirt2)
print("----------------------------------------------")

#4 write a logical operation to determine if you should take an umbrella if its either going to rain or going to rain heavily
weather = "rain"
if weather == "rain":
    print("It will rain today. Good idea to take your umbrella.")
elif weather == "heavy rain":
    print("There will be heavy rain today! Take an umbrella and a coat and cap!")

print("----------------------------------------------")

#5 Evaluate the expression 3 + 5 * 2 - 8. What would be the order of operations?
#first would be 5 * 2 for 10. then 10 + 3 = 13 - 8 = 5.
print(3 + 5 * 2 - 8)
print("----------------------------------------------")
#6 You have 10 pastries and you want to divide them equally among 3 friends. How many does each friend get and how many are left over?
pastries = 10
friends = 3
each_gets = pastries // friends
leftover = pastries % friends
print("Each friend will get " + str(each_gets) + " pasteries")
print("There will be " + str(leftover) + " pastry leftover.") 
print("----------------------------------------------")

#7 You already have a kingdom named "Pythonland". Use the assignment operator to add "is wonderful!" to it.
kingdom = "Pythonland"
print(kingdom + " is wonderful!")
print("----------------------------------------------")

#8 Two knights have strength values of knight1 = 45 and knight2 = 50. Use a comparison operator to determine if knight1 has the same strength as knight2.
knight1 = 45
knight2 = 50
print(knight1 == knight2)
print("----------------------------------------------")

#9 A chef has 2 ingredients, eggs = True and flour = False. He can only make pancakes if he has both. Detemine if the chef can make pancakes.
eggs = True
flour = False
if eggs == True and flour == True:
    print("Pancakes are being made as we speak!")
else:
    print("Sorry, we can't make pancakes today.")
print("----------------------------------------------")

#10 A castle's height is 100 units and its moat's width is 50 units. If you double the castle's height and halve the moat's width, what would be the new dimentions?
castle_height = 100
moat_width = 50
dimensions1 = castle_height * moat_width
print(dimensions1)

castle_height = castle_height * 2
moat_width = moat_width / 2
dimensions2 = castle_height * moat_width
print(dimensions2)
print("----------------------------------------------")

#additional exercises

num = 7

if num % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

print("----------------------------------------------")

color = "pinkred"
if color == "red":
    print("Hello red!")
else:
    print("You're not red!")