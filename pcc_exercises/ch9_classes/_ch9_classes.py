""" 9-1, 9-2, 9-4, 9-10 Restaurant/Three Restaurants/Number Served/Imported Restaurant """
from restaurant import Restaurant

restaurant = Restaurant('food_place', 'fries', 6, 11, 10)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(15)
restaurant.open_restaurant()
restaurant.increment_number_served()
restaurant.open_restaurant()

my_restaurant = Restaurant('mcdonalds', 'borgors', 6, 11)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

their_restaurant = Restaurant('chick-fil-a', 'chicken borgers', 11, 9)
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()

their_restaurant1 = Restaurant('chipotle', 'mexican grill', 9, 10)
their_restaurant1.describe_restaurant()
their_restaurant1.open_restaurant()

their_restaurant2 = Restaurant('ichiran ramen', 'noodles', 11, 10)
their_restaurant2.describe_restaurant()
their_restaurant2.open_restaurant()

""" 9-6 Ice Cream Stand""" # Needs 9-1 Restaurant Class
from icecreamstand import IceCreamStand as ICS

flavors = ['Cookies and Cream', 'Chocomint', 'Strawberry']
my_stand = ICS('Baskin Robins', 'dessert', 9, 11, 10, *flavors)
my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.display_flavors()

""" 9-3 Users, 9-5 Login Attempts """ #Added while loop input attempts
from user import User

she = User('Lizzy', 'Mckurthy', 'London', 31)
she.describe_user()
she.greet_user()

me = User('Dan', 'Carter', 'America', 35, 'dan', 'qwerty')
me.describe_user()
me.release_sens()
me.greet_user()

print("Login Credentials")

while(True):
    u = input('Username: ')
    p = input('Password: ')
    if me.credential_check(u, p):
        me.reset_login_attempts()
        print("You're in champ!")
        break
    else:
        me.increment_login_attempts()
        print(f"Incorrect Credentials. Try Again... Login Attempts {me.login_attempts}")
        if me.login_attempts >= 3:
            print("Too many login attempts! You are blocked!")
            break

print("Imagine User Dashboard Here/Login Screen")

""" 9-7 Admin, 9-8 Privileges, 9-11,12 Imported Admin/Multiple Modules  """
from admin import Admin

myself = Admin('Dan', 'Carter', 'America', 20)
myself.privileges.show_privileges()
myself.show_name_privileges()

""" 9-9 Battery Upgrade """
from car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()