# Exploring Abstract Base Class collection
# in particular the Container class

from collections.abc import Container

# a class which determines if a data member is an odd number
class OddContainer(Container): # works without inheriting from 'Container'
    def __contains__(self, __x): # overriding the built-in 'contains' method
        # we need to check if it's an odd number
        if not isinstance(__x, int) or not __x%2: 
            return False
        return True # yes, it is an odd integer

if __name__ == '__main__':
    odd_c = OddContainer()
    print( Container.__abstractmethods__)
    print( issubclass(OddContainer, Container) ) # True
    print( 1 in odd_c) # assert True (the in operator invokes __contains__)
    print(2 in odd_c) # False
    print('1' in odd_c)