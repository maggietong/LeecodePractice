import time
from threading import Thread, Lock

class SingletonMeta(type):
    lock = Lock()
    singletons = {}
    
    def __call__(cls, *args, **kwargs):
        if cls in cls.singletons:
            return cls.singletons[cls]

        with SingletonMeta.lock:
            if cls not in cls.singletons:
                time.sleep(1)
                cls.singletons[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls.singletons[cls]


class Singleton(object):
    __metaclass__=SingletonMeta
    pass

class A(Singleton):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__name__, id(self), self.name)

def print_singleton_a(idx):
    print('A singleton', idx, A('singleton'))

class B(A):
    pass

def print_singleton_b(idx):
    print('B singleton', idx, B('singleton'))


if __name__ == "__main__":
    import pdb; pdb.set_trace()
    print_singleton_a(1)
