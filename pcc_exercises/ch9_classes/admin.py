from user import User

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        #Taken off '{self.first_name} {self.last_name}' since Privileges class cannot track it
        print(f"Admin's Privileges: {", ".join(self.privileges)}")

class Admin(User):
    def __init__(self, first_name, last_name, location, age, username=None, password=None):
        super().__init__(first_name, last_name, location, age, username, password)
        self.privileges = Privileges() #Instances as Attributes
    
    def show_name_privileges(self):
        #self.(instance of privileges).(attribute of pivileges)
        print(f"{self.first_name} {self.last_name}'s Privileges: {", ".join(self.privileges.privileges)}")