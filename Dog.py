class Animal:
    def __int__(self):
        self.number_of_nose = 1

    def eat(self):
        print("eating")


class Dog(Animal):
    def walk(self):
        print("walking")
        super().number_of_legs = 4


class Fish(Animal):

    def swim(self):
        print("swimming")
