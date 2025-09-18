from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, open, close, number_served=0, *flavors):
        super().__init__(name, cuisine, open, close, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print(f'Flavors Available: {", ".join(self.flavors)}')