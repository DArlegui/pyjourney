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
