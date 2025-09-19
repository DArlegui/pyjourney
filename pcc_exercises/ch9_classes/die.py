from random import randint

class Die:
  def __init__(self, sides=6):
    self.sides = sides
  
  def roll_die(self):
    return randint(1, self.sides)
  
  def print_x_rolls(self, x_amount):
    rand_list = []
    for _ in range(0, x_amount):
      rand_list.append(f"{self.roll_die()}")
    print(f"Rolling a {self.sides}-sided die {x_amount} times: {', '.join(rand_list)}")