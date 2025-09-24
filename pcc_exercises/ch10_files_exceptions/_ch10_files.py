""" 10-1 Learning Python """
from pathlib import Path
contents = 'In Python you can use the standard library. \n'
contents += 'A set of tools included in Python\'s standard installation. \n'
contents += 'Library includes data structures and tools for your work.'

# Makes file inside the it's parent folder no matter which dir you're in (terminal)
path = Path(__file__).parent / "learning_python.txt"
# path = Path('learning_python.txt') 

path.write_text(contents) # creates on current path dir folder

""" 10-2 Learning C,  10-3 Simpler Code
    lines = contents.splitlines() # temp variable
    print(lines) """
contents = path.read_text()
print(contents)

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

""" 10-6 Addition, 10-7 Addition Calculator """
while True:
    n1 = input("Enter Value (q to quit): ")
    if n1.lower() == 'q': break

    n2 = input("Enter Value (q to quit): ")
    if n2.lower() == 'q': break

    try:    answer = int(n1) + int(n2)
    except  ValueError: print("Invalid Input! Try Again")
    else:   print(answer)

""" 10-8 Cats and Dogs, 10-9 Silent Cats and Dogs 
# splitlines() makes it into a list ['Sammy', 'John Doe', 'Vanny']
# split() Doesn't include the whitespace ['Sammy', 'John', 'Doe', 'Vanny'] 
# write_text() auto creates a new file, try-except won't work. """

dog_names = ['Sammy', 'John Doe', 'Vanny']
cat_names = ['Pedro', 'Ace', 'Muffin']

def read_file(path_name, title="Name", list_name=[]):
    path_temp = Path(__file__).parent / f"{path_name}"
    
    if not path_temp.exists():
        path_temp.write_text('\n'.join(list_name))
    
    try:
        list_contents = path_temp.read_text(encoding='utf-8').splitlines()
    except FileNotFoundError:
        print(f"File '{path_name}' is missing")
    else:
        print(f"{title} List: {', '.join(list_contents)}")

read_file('dogs.txt', "Dog", dog_names)
read_file('cats.txt', "Cat", cat_names)