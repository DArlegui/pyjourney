class Employee:
    """Stores the info of the individual"""

    def __init__(self, first, last, annual=0):
        self.first = first
        self.last = last
        self.salary = annual

    def give_raise(self, money=5000):
        self.salary += money
        print(f"Increased annual pay by {money}, Total: {self.salary:,}")
