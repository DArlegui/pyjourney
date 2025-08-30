## Chapter 2

# Strings
# .title() method | changes each word to title case
# .upper() | converts string to uppercase
# .lower() | converts string to lowercase
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# f-strings
first = "dan"
second = "a"
full_name = f"{first} {second}"
print(f"Hello there, {full_name.title()}")

# \t \n
print("Languages:\n\tPython\n\t") 

# Stripping Whitespace
# rstrip() | removes any whitespace on the right side of a string
# lstrip() | removes any whitespace on the left side of a string
# strip() | removes any whitespace from both sides at once of a string
favorite_language = ' python '
favorite_language.rstrip()
' python'
favorite_language.lstrip()
'python '
favorite_language.strip()
'python'

# Removing Prefixes
# .removeprefix() | removes the prefix and returns the rest of the string
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# Try it yourself pg.25
# 2-3
name = "Dan"
print(f"Hello {name}, are you getting enough sleep lately?")
#2-4
print(name.upper())
print(name.lower())
print(name.title())
#2-5
quote = "Don't believe everything you read on the internet"
author = "Abraham Lincoln"
print(f"{author} once said, {quote}")
#2-6
famous_person = "Gandhi"
message = "You must be the change you wish to see in the world"
print(f"{famous_person} said {message}")
#2-7
name = "  Dan \n"
print(name.rstrip())
print(name.lstrip())
print(name.strip())
#2-8
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))