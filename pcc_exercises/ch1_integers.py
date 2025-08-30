# Python uses two multiplication symbols to represent exponents:
print(3 ** 2)

# Python supports the order of operations too, so you can use multiple operations in one expression.
print(2 + 3*4)
print((2 + 3) * 4)

## FLOATS
# For the most part, you can use floats without worrying about how they behave.
print(0.2  + 0.1) #Gives an arbitrary number
print(round(0.2  + 0.1343, 2)) #Gives an arbitrary number
from decimal import Decimal
print(Decimal('0.2') + Decimal('0.1'))
print(round(0.2 + 0.1), 1)
print(4 * 0.1)

## INTEGERS AND FLOATS
# When you divide any two numbers, mix an integer and a float in any other operation, you’ll get a float:
print(4/2) #2.0
print(3.0 ** 2) #9.0

## UNDERSCORES IN NUMBERS
# You can group digits using underscores to make large numbers more readable:
universe_age = 14_000_000_000
print(universe_age)

## MULTIPLE ASSIGNMENTS
# You can assign values to more than one variable using just a single line of code
x, y, z = 0, 0, 0

## CONSTANTS
# A constant is a variable whose value stays the same throughout the life of a program
MAX_CONNECTIONS = 10
print(MAX_CONNECTIONS)

## TRY IT YOURSELF
#2-9
print(5+3, 9-1, 4*2, 2**3)

#2-10
fav_num = 7
actual_fav_num = 2
print(f"My favorite number is {fav_num}, but it's actually {actual_fav_num}")

## TRY IT YOURSELF
# 2-11
# TypeScript - Strict type of JavaScript
# Python - Perty simple and straight to the point


### THE ZEN OF PYTHON
# import this
# print(this)