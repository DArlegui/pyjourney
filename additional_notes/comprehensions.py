import random


nums = [random.randint(0, 100) for _ in range(10)]
print("Ten random ints:", nums)

squares = [value**2 for value in range(1, 10)]
print(f"Squaring numbers 1–9: {squares}")

age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

words = ["apple", "banana", "cherry"]
print(", ".join(words))
print(" - ".join(words))
