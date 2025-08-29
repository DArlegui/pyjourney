### LIST
# Square brackets ([]) indicate a list, and individual elements in the list are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## Accessing Elements in a List
print(bicycles[0].title())

## Index Positions Start at 0, Not 1
# The reason has to do with how the list operations are implemented at a lower level
print(bicycles[1])
print(bicycles[3])

# Capture last item in the list:
print(bicycles[-1])

## USING INDIVIDUAL VALUES FROM A LIST
message = f"I bought a {bicycles[2].title()} this morning!"
print(message)

#TRY IT YOURSELF
#3-1
names = ['lucas', "george", "noel"]
print(f"Good evening {names[0]}, {names[1]}, and {names[2]}")
#3-2
print(f"Hello {names[1]}!")
#3-3
transporation = ['car', 'bus', 'train']
print(f"I own a mazda {transporation[0]}")

#3-4 Guest List
pokemon = ['pikachu', 'squirtle', 'charmander']
for monster in pokemon:
  print(f"{monster.title()} would you like to battle?")

#3-5
print(pokemon)
pokemon[1] = 'bulbasaur'
print(pokemon)

#3-6
pokemon.insert(0, 'piplup')
pokemon.insert((len(pokemon) // 2), 'chimpchar')
pokemon.append('turtwig')
print(pokemon)

#3-7 Try using random generator
import random
print("I can only invite two pokemons. Sorry!")
while len(pokemon) > 2:
  idx = random.randint(0, len(pokemon) - 1)
  pokemon.pop(idx)

print(pokemon)

#3-8
places = ["japan", "france", "singaphore", "hawaii", "canada"]
print(f"\nBeginning List of Places: {places}\n")
print(f"Sorting List (Original List Unchanged) \n {sorted(places)}")
print(f"Current of Places (Unchanged): {places}\n")
print(f"Sorted Reverse (Original List Unchanged) \n{sorted(places, reverse=True)}") #sorted(iterable, reverse=)
print(f"Current of Places (Unchanged): {places}\n")
places.reverse()
print(f"List has been reversed (un-alphabetical): {places}")
places.reverse()
print(f"List has been un-reversed: {places}")
places.sort()
print(f"List has been sorted: {places}")
places.sort(reverse=True)
print(f"List has been reversed (alphabetical): {places}")

#3-9 Dinner Guests
print(f"\nI am inviting {len(pokemon)} number of pokemon to the party")

#3-10
numbers  = []
for x in range(0, 5):
  numbers.append(random.randint(0, 100))

print(f"Random Number List: \n{numbers}")
print(f"Sorting Number List (List Unchanged): \n{sorted(numbers)}")
print(f"Random Number List: \n{numbers}")
print(f"Reverse Sorting Number List (List Unchanged): \n{sorted(numbers, reverse=True)}")
print(f"Random Number List: \n{numbers}")

idx = random.randint(0, len(numbers) - 1)  # pick a valid index
print(f"Deleting index {idx}, value {numbers[idx]}")

del numbers[idx]
print("Remaining list:", numbers)

final_two = random.sample(numbers, 2)  # no repeats
print(f"Choosing two random numbers{final_two}")

#3-11 Intentional Error
myGuests = []
print(myGuests[-1]) #Gives "IndexError: list index out of range"
