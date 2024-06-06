class User:
    def __init__(self, first_name, last_name):
        print(first_name)
        print(last_name)
        self.user_name = first_name
        self.user_last_name = last_name
    def say_name(self):
        print(self.user_name)
    def say_lastname(self):
        print(self.user_last_name)
    def say_fullname(self):
        print(f"{self.user_name}, {self.user_last_name}")