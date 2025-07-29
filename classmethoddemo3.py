class User:
    _default_role = "member"
    _user_count = 0

    def __init__(self,username,role=None):
        self.username = username
        self.role = role or User._default_role
        self.__class__._user_count +=1

    @classmethod
    def set_default_role(cls,role):
        cls._default_role = role

    @classmethod
    def get_user_count(cls):
        return cls._user_count
    
class AdminUser(User):
    _user_count = 0

u1 = User("Alice")
u2 = User("Bob")

a1 = AdminUser("admin1")
a2 = AdminUser("admin2")
a3 = AdminUser("admin3")

print(User.get_user_count())
print(AdminUser.get_user_count())