""" 10-1 Learning Python """
from pathlib import Path
contents = 'In Python you can use the standard library. \n'
contents += 'A set of tools included in Python\'s standard installation. \n'
contents += 'Library includes data structures and tools for your work.'

# Makes file inside the it's parent folder no matter which dir you're in (terminal)
path = Path(__file__).parent / "learning_python.txt"
# path = Path('learning_python.txt') # creates on current dir terminal folder

path.write_text(contents)

""" 10-2 Learning C,  10-3 Simpler Code"""
contents = path.read_text()
print(contents)
# lines = contents.splitlines() # temp variable
# print(lines)

c_lang = ''
for line in contents.splitlines():
  c_lang += line.replace('Python', 'C++')

print(c_lang)

""" 10-4 Guest, 10-5 Guest Book """
list_names = []

while True:
  f = input("First Name (q to quit): ")
  l = input("Last Name (q to quit): ")
  if f == 'q' or l == 'q':
    print("You decided to quit... \n")
    print("Appending listed name(s) on a txt file...")
    break

  list_names.append(f"{f.title()} {l.title()}")

newlined = '\n'.join(list_names)
print(newlined)
path = Path(__file__).parent / "guest_book.txt"
path.write_text(newlined)
