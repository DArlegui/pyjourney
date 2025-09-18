class Restaurant:
    def __init__(self, name, cuisine, open, close, number_served=0):
        self.name = name
        self.cuisine = cuisine
        self.open = open
        self.close = close
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.name.title()}, Cuisine type: {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"Opens {self.open}am - {self.close}pm. Served {self.number_served} customers.")

    def set_number_served(self, served):
        if served > self.number_served:
            self.number_served = served
        else:
            print("Number less than number_served")
    
    def increment_number_served(self):
        self.number_served += 1
