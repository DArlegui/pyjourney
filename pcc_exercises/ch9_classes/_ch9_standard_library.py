""" Python Standard Library"""
from random import shuffle, sample, choice
from string import ascii_lowercase

""" 9-13 Dice """
from die import Die

six_sided = Die(6)
six_sided.print_x_rolls(10)

ten_sided = Die(10)
ten_sided.print_x_rolls(20)

twenty_sided = Die(20)
twenty_sided.print_x_rolls(20)

""" 9-14 Lottery, 9-15 Lottery Analysis 
    choice() → can repeat.
    sample() → no repeats.
    shuffle() → just rearranges the list after you've built it. 
    set() → It doesn’t care about order. It doesn’t allow duplicates. my_set = {1, 2, 3, 3, 2}
    frozenset() → immutable version. a set that cannot be changed after it’s made 
"""

pool = list(range(1,100)) + list(ascii_lowercase) #125 unique symbols
winning_list = []
lottery_ticket = []
money = 0
tries = 0

def draw_ticket(pool_list):
  shuffle(pool_list)
  return frozenset(sample(pool_list, 2)) # 4 unique symbols, order doesn’t matter

winning_list = draw_ticket(pool)

print(f"Winning Ticket: {winning_list}")
print("Simulating Lottery Gambling")

while True:
  lottery_ticket = draw_ticket(pool)
  money += 10 # How much customer has spent
  tries += 1 # How many times this gambler has bought

  if tries % 100_000 == 0:
    print(f"Bought {tries:,} tickets...")

  if lottery_ticket == winning_list:
    print("You've Won 50 Million Dollars!!!")
    print(f"Lottery Ticket: {lottery_ticket}")
    break

print(f"Winning Ticket: {winning_list}")
print(f"Winning ticket matched after {tries:,} buys. Money spent: ${money:,}. Percentage: {1/tries:.7%}")

""" 9-16 Python Module of the Week 
    # https://pymotw.com
"""
# https://pymotw.com/3/decimal/index.html
import decimal

fmt = '{0:<25} {1:<25}'

print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# Integer
print(fmt.format(5, decimal.Decimal(5)))

# String
print(fmt.format('3.14', decimal.Decimal('3.14')))

# Float
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print('{:<0.23g} {:<25}'.format(
    f,
    str(decimal.Decimal.from_float(f))[:25])
)