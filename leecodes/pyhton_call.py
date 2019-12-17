class Counter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    for i in range(10):
        foo()
    print(foo.count)
