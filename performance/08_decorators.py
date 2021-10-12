# Python includes a decorator to make things thread-safe
from threading import Lock

# here is a function which can be used to make a class thread-safef using locks
def lock_class(methodnames, lockfactory):
    return lambda cls:make_thread_safe(cls, methodnames, lockfactory)

def lock_method(method): # this will return a locked version of a method
    if getattr(method, '__is_locked', False):
        raise TypeError('Method {} is already locked'.format(method))
    def locked_method(self, *args, **kwargs):
        with self._lock: # remember, this lock will be released at teh end of 'with'
            return method(self, *args, **kwargs) # call the method!!
    lock_method.__name__ = '{}({})'.format('locked method', method.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, methodnames, lockfactory):
    init = cls.__init__ # take a copy of the existing __init__ of this cls
    def newinit(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lockfactory
    cls.__init__ = newinit # override the original __init__ with this new one
    # now we iterate over all the class methods, making them thread safe
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod) # repalce the old methods with these new lockable versions
    return cls # has a new init and new version of every method

@lock_class(['add', 'remove'], Lock) # Lock is a lock factory
class DecoratorLockSet(set): # we extend the 'set' data-type using our decorator
    # the 'add' and 'remove' methods of the 'set' have now been made thread-safe with locks
    # we can lock specific methods like this
    @lock_method
    def methodToLock(self):
        print('this method will be explicitly locked (and therefore thread safe)')

if __name__ == '__main__':
    my_set = (4,3,2)
    my_inst = DecoratorLockSet(my_set)
    # is it locked?
    print(my_inst.add.__is_locked) # True
    print(my_inst.remove.__is_locked) # True
    print(my_inst.methodToLock.__is_locked) # True
    
