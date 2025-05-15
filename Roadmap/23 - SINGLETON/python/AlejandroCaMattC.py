"""Design patterns in Python: Singleton
   - A singleton is a design pattern that restricts the instantiation of
   a class to one single instance."""


class Singleton:
    """A singleton class that ensures only one instance of the class is created."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1)  # Output: <__main__.Singleton object at 0x...>
print(singleton2)  # Output: <__main__.Singleton object at 0x...>


"""Exercise"""


class UserSession:

    _instance = None

    id: None
    username: None
    name: None
    email: None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, id: int, username: str, name: str, email: str):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email
        }

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
session1.set_user(1, "johndoe", "John Doe", "jadoe@gmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())  # Should be the same as session1

session3 = UserSession()
session3.clear_user()
print(session3.get_user())  # Should be None
