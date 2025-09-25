""" 10-10 Common Words """
from pathlib import Path

path = Path(__file__).parent / 'gatsby.txt'
content = path.read_text(encoding='utf-8')

words = content.lower().split() # Makes each word its own element
find_word = 'the'
counter = words.count(find_word) #Simpler way

# if words.lower() == find_word: 
#   counter += 1

# for word in words: # "the" will also match words like "there", or "theme"
#     if find_word in word.lower(): counter += 1

print(f"The word '{find_word}' showed up {counter} times!")

""" 10-11, 10-12 Favorite Word
    read_text() → gives you a string.
    json.loads() → turns that string into a real Python object."""
from pathlib import Path
import json

path = Path(__file__).parent / 'fav_num.json'

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"Ah! You're favorite number is {number}")

else:
    while True:
        try:
            u = int(input("Type in your favorite number: "))
        except ValueError:
            print("Please enter a valid number!")
        else:
            break

    contents = json.dumps(u)
    path.write_text(contents)
    print(f"We'll remember your favorite number when you return!")

"""10-13 User Dictionary, 10-4 Verify User """
"""
    path.stat() → asks the operating system for information about the file 
    (like size, last modified time, permissions, etc.).
    .st_size → is one piece of that info: the file size in bytes.
"""
from pathlib import Path
import json

def get_stored_username(path: Path, username):

    if path.exists():
        contents = path.read_text() #string
        users: dict = json.loads(contents) #turns to object

        if username in users:
            return users
        else:
            print(f'{username} does not exist!')
            print(f"Seems like you're new here..")
            return None
    else:
        return None
    
def get_new_username(path: Path, username):
    """ Prompt a new username """
    first = input("What is your name? :")
    last = input("What is your last name? :")
    age = int(input("What is your age? : "))

    if path.exists() and path.stat().st_size > 0:  # make sure file is not empty
        contents = path.read_text()
        try:
            users = json.loads(contents)
        except json.JSONDecodeError:
            users = {}  # fallback if file is corrupted
    else:
        users = {}

    users[username] = { #adds if existing {k:{}} exists
        'first': first,
        'last': last,
        'age': age
    }

    #does not give you a dictionary back; it gives you a string representation of it.
    contents: dict = json.dumps(users, indent=2) 
    path.write_text(contents) #save the JSON string to disk at the given Path

    return username

def greet_user():
    """Greet the user by name."""
    path = Path(__file__).parent / 'username.json'
    u = input("Enter username: ")
    strip_u = u.strip().lower()

    users: dict = get_stored_username(path, strip_u)

    if users:
        print(f"Welcome back, {users[strip_u]['first']} {users[strip_u]['last']}!")
        print(f"You are {users[strip_u]['age']} years old!")
    else:
        username: str = get_new_username(path, strip_u)
        print(f"We'll remember you when you come back, {username}!")

greet_user()