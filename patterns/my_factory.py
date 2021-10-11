# using the Factory design patterns
from abc import ABCMeta, abstractmethod

class Animal(): # Abstract Base Class
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print('woof')

class Cat(Animal):
    def do_say(self):
        print('miaow')

class Bat(Animal):
    def do_say(self):
        print('_____')

# factory to create animals
class CreatureFactory():
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == '__main__':
    cf = CreatureFactory()
    animal = input('which creature? ')
    cf.make_sound(animal)
    
