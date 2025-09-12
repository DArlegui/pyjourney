""" 8-1 Message """
def display_message(): 
  print("Hey everyone, right now I'm learning how to write functions and arguments in python!")

display_message()

""" 8-2 Favorite Book """
def favorite_book(title):
  print(f"One of my fav books are {title.title()}.")

favorite_book("ready player one")

""" 8-3 T-Shirts """
def make_shirt(size, text):
  print(f"Your shirt size shall be {size} with the text {text}.")

make_shirt(8, "Hewwo")
make_shirt(14, "Kitty")

""" 8-4 Large Shirts """
def make_shirt(size='Large', text='I Love Python'):
  print(f"Your shirt size shall be {size} with the text {text}.")

make_shirt()
make_shirt(size='Medium')

""" 8-5 Cities """
def describe_city(name, country):
  print(f"{name.title()} is in {country.title()}")

describe_city('los angeles', 'america')

""" 8-6 City Name """
def city_country(city, country):
  return f'"{city.title()}, {country.title()}"'

print(city_country('san francisco', 'america'))
print(city_country('tokyo', 'japan'))
print(city_country('honolulu', 'america'))

""" 8-7, 8-8 Album/User Albums """
def make_album(artist, title, number=None):
  album = {"artist": artist, "title": title}

  if number:
    album['songs'] = number

  return album

def num_of_songs(album_dict):
  return album_dict.get('songs', 0)

def print_albums(albums): #takes a list of dictionary and loops it
  for album in albums:
    if 'songs' in album:
      print(f"{album['artist'].title()} by {album['title'].title()}, {album['songs']} song(s)")
    else:
      print(f"{album['artist'].title()} by {album['title'].title()}")

albums = [] #a list of album dictionaries

nirvana = make_album('nirvana', 'nevermind', 3)
albums.append(nirvana)

beatles = make_album('abbey road', 'the beatles')
albums.append(beatles)

albums.append(make_album('sheer heart attack', 'queen', 5))

print_albums(albums)

#calling num_of_songs function
print(num_of_songs(nirvana))
print(num_of_songs(beatles))

#User Input
print("Add album (press 'q' to quit)")
while True:
  artist = input("Artist name : ")
  if artist.lower() == 'q':
    break

  title = input("Title of the album: ")
  if title.lower() == 'q':
    break

  album = make_album(artist, title)
  albums.append(album)

print_albums(albums)