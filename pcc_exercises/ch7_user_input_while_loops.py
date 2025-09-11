#7-1 Rental Car
userInput = input("What kind of rental car would you like? : ")
print(type(userInput))
print(f"{"BMW" if "bmw" == userInput.lower() else userInput.title()} coming right up!")

#7-2 Restaurant Seating
prompt = "Welcome to McDonalds' 5 star fancy restaurant!"
prompt += "\nHow many people? : "
numPeople = int(input(prompt))
print(f"{"Please wait for the next available table" if numPeople > 8 else "Your table is ready"}.")

#7-3 Multiples of Ten
userInput = int(input("Enter a number: "))
print("This number is a multiple of 10!" if userInput % 10 == 0 else "Not a multiple of 10!")

#7-4 Pizza Toppings
toppings = ['pepperoni', 'onions', 'bacon']
tempToppings = []

while True:
  prompt = "What kind of pizza topping?"
  prompt += "\nEnter 'q' when finished: "
  userInput = input(prompt)

  if userInput == 'q':
    break
  if userInput not in toppings:
    print("Sorry we don't have that!")
  else:
    tempToppings.append(userInput)
    print("Adding that in now!")

userTopping = ", ".join(tempToppings)
print(f"Your pizza order with toppings of {userTopping} coming right up.")

#7-5 Movie Tickets 
prompt = "Welcome to McDonalds' 5 star fancy restaurant!"
prompt += "\nHow many people? : "

active = True
while active:
  prompt = "What is your age?"
  userAge = (input(prompt + "\npress 'q' to exit : "))

  if userAge == 'q':
    break

  if userAge < 3:
    print("Your ticket is free!")
  elif 3 <= userAge <= 12:
    print("Ticket will cost you $10.")
  else:
    print("Ticket will cost you $15.")

#7-6 Three Exits
x = 0

while x < 5:
    x += 1
    print(x)

print(f"Final value is {x}")

active = True
age = 13
while active:
    age = int(input("How old are you: "))
    if age >= 21:
        print("Welcome to the club!")
        active = False
    else:
        print("Come back when you're older! Next!")

userInput = ''
listFood = []
print("What's your favorite food?")

while userInput != 'q':
    prompt = ("(press 'q' to quit) : ")
    userInput = input(prompt)

    if userInput.lower() != 'q': 
        listFood.append(userInput)

if listFood:
    userFood = ", ".join(listFood)
    print(f"I like {userFood} too!")
else:
    print("Guess you don't eat huh.")

#7-7 Infinity While Loop
restock = 0
while restock < 1:
    print("Out of business!")

#7-8,9 Deli
sandwich_orders = ['terriyaki sandwich', 'ham sandwich', 'pastrami', 'cheese sandwich', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
  current_order = sandwich_orders.pop()
  if current_order == 'pastrami':
    print("Deli has ran our of pastrami.")
  else:
    print(f"{current_order.title()} coming right up!")
    finished_sandwiches.append(current_order)

final_stats = ", ".join(finished_sandwiches)
print(f"All orders of {final_stats} are finished.")

#7-10 Dream Vacation w/ Input Validation
user_polls = { 
  #user, vacation_dream
}
active = True

while active:
  user = input("What is your name? : ")
  vacation_dream = input("If you could visit one place in the world, where would you go? : ")

  user_polls[user] = vacation_dream

  cont = input("Next person? (y/n) : ").lower()
  while cont != 'y' and cont != 'n':
    cont = input("(y/n) ONLY! : ").lower()

  if cont.lower() == 'n':
    active = False

for k, v in user_polls.items():
  print(f"{k.title()} would like to go to {v.title()}")

# ✅ Truth Table for AND (and)
# Rule: A and B is True only if BOTH are True.

# | A | B | A and B |
# | - | - | ------- |
# | T | T | T       |
# | T | F | F       |
# | F | T | F       |
# | F | F | F       |

# ✅ Truth Table for OR (or)
# Rule: A or B is True if AT LEAST one is True.

# | A | B | A or B |
# | - | - | ------ |
# | T | T | T      |
# | T | F | T      |
# | F | T | T      |
# | F | F | F      |