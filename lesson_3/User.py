class User:
    def __init__(self, firstname, lastname):
        print("Меня зовут", firstname)
        print("Моя фамилия", lastname)
        self.username = firstname
        self.userlastname = lastname
    def sayName(self):
        print("Меня зовут", self.username)
    def seyLastname(self):
        print("Моя Фамилия", self.userlastname)