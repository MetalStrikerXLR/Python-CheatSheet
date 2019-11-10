class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')

john = Person('john smith')
john.talk()

bob = Person('Bob smith')
bob.talk()