class Foo(object):
    def __init__(self, *args, **kwargs):
        self.age = 0
        print("Foo __init__")
    def __new__(cls, *args, **kwargs):
        return object.__new__(Stranger, *args, **kwargs)

class Stranger(object):
    def __init__(self,name):
        print("class Stranger's __init__ be called")
        self.name = name

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class SingletonMeta(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        print('__call__')
        if cls.__instance is None:
            cls.__instance == super(SingletonMeta, cls).__call__( *args, **kwargs)
        return cls.__instance

class Test(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    #import pdb;pdb.set_trace()
    #foo = Foo("test")
    #print("ok")
    #s1 = Singleton()
    #s2 = Singleton()
    #print(s1 is s2)
    test1 = Test()
    test2 = Test()
    print(test1 is test2)

