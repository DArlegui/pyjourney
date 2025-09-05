#5-1 Conditional
gpu = "5070"
gpu1 = "5080"
gpu2 = "5090"

if gpu == "5080":
    print("That's not a 5070!")

print("Is the gpu == 5090? I predict false")
print(gpu == "5090")
print(gpu == gpu1)
print(gpu == gpu2)
print(gpu2 == gpu)
print(gpu2 == gpu1)

print(gpu == gpu)
print(gpu1 == gpu1)
print(gpu2 == gpu2)

gpu = "5090"
print(gpu == gpu2)

gpu = "5080"
print(gpu == gpu1)

#5-2 More Conditionals
word = "fish"
word1 = "tuna"

#Using Ternary 
#value_if_true if condition else value_if_false
food = True if word == word1 else False
print(food)

word1 = "Fish"
print(word == word1.lower())

word1 = "Fish"
print(word == word1)

age = 19
drinkingAge = 21
status = "Adult" if age >= 18 else "Minor"
print(status)

print("Can Drink" if age >= drinkingAge else "Nope too young")

age = 22
print("Can Drink" if age >= drinkingAge else "Nope too young")

list = ["mouse", "keyboard", "pen", "paper"]

for item in list: 
	if item == "mouse":
		print("Yes there is! Kill it!")
	else:
		print("Not a rodent")
		
#5-3
alien_color = ['green', 'blue', 'red']

if 'green' in alien_color:
    print("+5 points")

if 'yellow' not in alien_color:
    print("unknown color") #true because yellow isn't in list

#5-4, 5-5

# alien_color = ['yellow', 'blue', 'red']
alien_color = []

if 'green' in alien_color:
    print("+5 Points")
elif "yellow" in alien_color:
    print("+10 Points")
elif "red" in alien_color:
    print("+15 Points")
else:
    print("No points!")

#5-6
age = 2

if age < 13:
    print("baby")
elif 2 <= age < 4:
    print("toddler")
elif 4 <= age < 13:
    print("kid")
elif 13 <= age < 20:
    print("teenager")
elif 20 <= age < 65:
    print('adult')
else: 
    print("elder")

#5-7 Favorite Fruit
favorite_fruits = ['banana', 'grapes', 'strawberry']
if 'grapes' in favorite_fruits:
    print("Do you like it purple or green?")
if "banana" in favorite_fruits:
    print("Donkey Kong")
if "strawberry" in favorite_fruits: 
    print("Collect them all in Celeste")
if 'peach' in favorite_fruits:
    print("Not my favorite")
if 'apple' in favorite_fruits:
    print("Not my favorite")

#5-8
userNames = ['bob', 'john', 'fred', 'matt', 'admin']

for names in userNames:
    if 'admin' in userNames:
        print("Hello admin")
        break
    else:
        print(f"hello {names}")

#5-9 No Users
userNames = ["john", 'matt']

for user in userNames:
    if not userNames:
        print("We need more users!")
        break
    else:
        print(f"Deleting user '{user}'")
        del user

#5-10 Checking Usernames
current_users = ['bob', 'john', 'fred', 'matt', 'admin']
new_users = ['dan', 'JOHN', 'pikachu', 'eevee', 'admin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Please change user name')
    else:
        print(f"The user name {new_user} is available!")
        break 

#5-11 Ordinal Numbers
numbers = []

for i in range(1, 10):
    numbers.append(i)

print(numbers)

for x in numbers:
    if 1 <= x <= 3:
        print(f"{x} is NOT an Ordinal Number!")
    else:
        print(f"{x}th is an Ordinal Number!")

#5-12 Styling Check 

#5-13 IDEAS
# Car List (Insert/Del), Vending Machine Prompt