import random

#6-1 Person
sponge = {
    'first_name': 'spongebob',
    'last_name': 'squarepants',
    'age': 22,
    'city': "bikini bottom"
}

print(sponge)
print(sponge['first_name'])
print(sponge['last_name'])
print(sponge['age'])
print(sponge['city'])

fav_numbers = {
    'bob': 4,
    'matt': 9,
    'sally': 7
}

#6-2 Favorite Number
for k,v in fav_numbers.items(): 
    print(f"Person {k}'s favorite number is {v}")

exists = fav_numbers.get('dan', "no value")
exists_0 = fav_numbers.get('matt', "no value")
print(exists)
print(exists_0)

#6-3 Glossary, 6-4 continue
python_dict = {
    'word1': 'dynamic',
    'word2': 'argument',
    'word3': 'syntax',
    'word4': 'dictionary',
    'word5': 'list',
    'word6': 'set',
    'word7': 'languages',
    'word8': 'elif',
    'word9': 'key-values',
    'word10': '.items()'
}

print('Words that I learned from python are: ')
for v in python_dict.values():
    print(f"{v}")

#6-5 Rivers
rivers = {
    'yangtze river': 'china',
    'nile river': 'egypt',
    'amazon river': 'brazil'
}

for k, v in rivers.items():
    print(f"The {k} runs through {v}.")

#6-6. Polling
favorite_languages = {
    'jen': 'python', #name, fav_lang
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['eric', 'maddie'] #people that didn't take the poll
all_people = list(favorite_languages.keys()) + people #combining everyone
random.shuffle(all_people) #shuffing the indexes positions
print(all_people)

for person in all_people:
    if person not in favorite_languages.keys():
        print(f"{person} haven't taken the poll!")
    else:
        print(f"Hi {person} your favorite language is {favorite_languages[person].title()}")

#6-7
sponge = {
    'first_name': 'spongebob',
    'last_name': 'squarepants',
    'age': 22,
    'city': "bikini bottom"
}

starfish = {
    'first_name': 'patrick',
    'last_name': 'star',
    'age': 20,
    'city': "under a rock"
}

squid = {
    'first_name': 'squidward',
    'last_name': 'tenticles',
    'age': 18,
    'city': "bikini bottom"
}

sea_creatures = [sponge, starfish, squid]
print(sea_creatures)

for creatures in sea_creatures:
    print(f"{creatures['first_name'].title()} {creatures['last_name'].title()}, age {creatures['age']} lives in {creatures['city']}")

#6-8
sam = {
    'owner': 'cousin',
    'pet': 'dog',
    'age': 19,
}

pedro = {
    'owner': 'distance friend',
    'pet': 'cat',
    'age': 20,
}

pets = [sam, pedro]

shelly = {
    'owner': 'friend',
    'pet': 'hamster',
    'age': 2
}

pets.append(shelly)
for pet in pets:
    print(f"My {pet['owner']} own a {pet['pet']} their age is {pet['age']}")

#6-9 Favorite Places
favorite_places = {
    'matt': ['pier 39', 'circus circus'],
    'paul': ['england', 'france'],
    'lilly': ['disneyland', 'mall']
}
##Conditional Expession (one-line) : results = "yes" if condition else "no"
for k, v in favorite_places.items():
    print(f"Hi {k.title()}, your favorite {'places' if k != 'matt' else 'countries'} are:")
    for places in v:
        print(f"\t{places.title()}")

#6-10 Favorite Numbers
fav_numbers = {
    'bob': ['4','5','9'],
    'matt': ['7','8','9'],
    'sally': ['23','0']
}

for k,v in fav_numbers.items():
    print(f"{k} favorite number are")
    format = ', '.join(v) #list of strings concatenate
    print(format)

# format = '' #f-string concatenate
# for n in v:
#     format = f'{format} {n}'

#6-11/12 List of Cities + Added a (nested) list inside a dictionary of a dictionary
cities = {
    'san francisco': {
        'places': ['golden gate bridge', 'peir 39'],
        'population': 827_526,
        'country': 'USA'
    },
    'tokyo': {
        'places': ['tokyo disneyland', 'senso-ji', 'akihabara'],
        'population': 14_000_000,
        'country': 'japan'
    },
    'shanghai': {
        'places': ['oriental pearl tower', 'the bund'],
        'population': 30_000_000,
        'country': "china"
    }
}

for city, info in cities.items():
    format = ', '.join(info['places']).title()
    print(f'{city.title()} has amazing places such as {format}.')
    print(f'They have a population of {info['population']:,}.')
    print(f'This city is located in {info['country'].title()}')