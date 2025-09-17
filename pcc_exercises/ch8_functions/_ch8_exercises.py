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

""" 8-9 Messages """
txt_unicode = ['UwU', "oWo", ':3']

def print_texts(list_name):
  unicode = list_name.pop()
  print(f"Removing {unicode} from the list.")
  txt = ', '.join(list_name)
  print(f"Texts shows {txt}")

print_texts(txt_unicode[:]) #sending a copy of a list
print(f"Original List {txt_unicode} still intact")
print_texts(txt_unicode) #pop method inside function
print(f"Original List {txt_unicode} last element was removed")

txt_unicode.append('T_T')
txt_unicode.append('QwQ')
print(f"New txt list: {txt_unicode}") 

""" 8-10 Sending Messages """
sent_messages = []

def send_messages(list1, list2):
  while list1:
    temp = list1.pop()
    print(f"Moving {temp} to another list")
    list2.append(temp)

send_messages(txt_unicode, sent_messages)
print(f"\ntxt_unicode list has {txt_unicode}")
print(f"sent_messages list has {sent_messages}")

"""8-11 Archived Messages"""
copy_messages = []
send_messages(sent_messages[:], copy_messages)
print(f"\nsent_messages list has {sent_messages}") #Retained its original values
print(f"copy_messages list has {copy_messages}")

""" 8-12 Sandwiches """
userRequest = ('ham', 'lettuce', 'tomato')
userRequestList = ['patty', 'chili', 'cheese']

def make_sandwiches(*items): #Accepts items in a tuple
    print("User requested the following items: ")
    # for item in items:
    #     print(f"{item}")
    # sandwichList = ", ".join(items)
    print(", ".join(items))

make_sandwiches("pork", 'oil', 'bread')

#use '*' again to unpack a tuple/list when calling *args function
make_sandwiches(*userRequest)
make_sandwiches(*userRequestList)

""" 8-13 """
my_info = build_profile( #from ch8_fn import build_profile
    'dan', 'a', location='america', 
    field='computer science', hobby='piano')

print(my_info)

their_info = fn_bp( #import ch8_fn as fn_bp
    'ellie', 'warner', location='england',
    field='neuro surgeon', hobby='violin'
)

""" 8-14 Cars """
subaru = fn.make_car('subaru', 'forester', color='white', hatchback=True) #import ch8_fn
honda = mc('honda', 'accord', color='blue', hatchback=False) #from ch8_fn import make_car as mc
kia = make_car('kia', 'soul', color='black', hatchback=True) #from ch8_fn import *

print(subaru)
print(honda)
print(kia)

""" 8-15, 16, 17 """
from fn import build_profile
import fn 
import fn as fn_bp
from fn import make_car as mc
from fn import *