class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def annoying(self):
        print('annoying')


cat1 = Cat()
cat1.annoying()
dog2 = Dog()
dog2.walk()
