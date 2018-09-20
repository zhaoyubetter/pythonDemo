class MyObject(object):
    def __init__(self):
        self._x = 8

    def power(self):
        return self._x * self._x


obj = MyObject()
print(hasattr(obj, '_x'))

print(obj._x)

print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))

print( hasattr(obj, 'power') )

print(getattr(obj, 'power'))