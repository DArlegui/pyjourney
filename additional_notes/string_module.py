import string
import random

print("Lowercase:", string.ascii_lowercase)
print("Uppercase:", string.ascii_uppercase)
print("Letters  :", string.ascii_letters)

alphabet_list = list(string.ascii_lowercase)
print("Alphabet list:", alphabet_list)

print("Random letter:", random.choice(string.ascii_lowercase))
