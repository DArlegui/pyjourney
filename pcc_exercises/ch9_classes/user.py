class User:
    def __init__(self, first_name, last_name, location, age, 
                 username=None, password=None):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.age = age
        self.username = username
        self._password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, Location: {self.location}, Age: {self.age}")

    def release_sens(self):
        print(f"Username: {self.username} Password: {self._password}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def credential_check(self, userInput, passInput):
        if self.username == userInput and self._password == passInput:
            return True
        return False

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
