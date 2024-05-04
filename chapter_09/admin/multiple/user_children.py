from user import Users


class Privileges(Users):
    """Privileges of users"""

    def __init__(self, first_name, last_name, username, password, gender):
        """
        Initializes info from parents class
        Initializes user info
        """
        super().__init__(first_name, last_name, username, password, gender)
        self.privileges = [
            'can make posts', 
            'can see other users data', 
            'can add/remove users'
            ]

    def show_privileges(self):
        """Display the admins privileges"""
        print(f'{self.username} has the following privileges')
        for privilege in self.privileges:
            print(f'\n-{privilege}')

class Admin(Users):
    """Info specifically on admins"""

    def __init__ (self, first_name, last_name, username, password, gender):
        """
        Initializes info from parent class
        Initializes admin info
        """
        super().__init__ (first_name, last_name, username, password, gender)
        self.privileges = Privileges(first_name, last_name, username, password, gender)
    

daisy = Admin('daisy', 'hardwick', 'slavetomints', '12345678910', 'female')
daisy.privileges.show_privileges()