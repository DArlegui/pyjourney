#4-1
pizzas = ["hawaiian", 'pepperoni', "cheese"]
for pizza in pizzas:
  print(f"I like {pizza.title()} pizza")

print("In all honesty, I prefer hamburgers and ramen.")

#4-2
animals = ['dog', 'cat', 'horse']
for animal in animals:
  print(f"{animal.title()} would make a great pet!")

print("I prefer cats.")

#4-3 Counting to Twenty
for x in range(1, 21):
  print(x)

#4-4 One Million
million = [value for value in range(1, 1_000_000)]
# for x in million:
#   print(x)
print(million[-1])
print(million[:10])  

#4-5 Summing Million
print(f"Min of Mil: {min(million):,}")
print(f"Max of Mil: {max(million):,}")
print(f"Sum of Mil: {sum(million):,}")

#4-6 Odd Numbers
numbers = []
for x in range(1, 21, 2):
  numbers.append(x)
print(f"Odd Numbers: {numbers}")

#4-7 Threes
numbers = [x * 3 for x in range(3, 30)]
print(f"Multiples of 3: {numbers}")

#4-8 Cubes
numbers = [value ** 3 for value in range(1, 10)]
c = 0
for x in numbers:
  c += 1
  print(f"Cube of {c}: {x}")

#4-9 Cube Comprehension 
print(min(numbers))
print(max(numbers))
print(sum(numbers))