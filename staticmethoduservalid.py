# Example 2: Validation Helper
class User:
    def __init__(self,username):
        if not User.is_valid_username(username):
            print("Invalid username!")
            return
        self.username = username
        print(f"User '{self.username}' created.")

    @staticmethod
    def is_valid_username(name):
        #must be at least 3 characters and all alphabetic
        return len(name) >=3 and name.isalpha()

print(User.is_valid_username('abc'))

u1 = User("Bob")
u2 = User("Jo")
u3 = User("123")