import itertools

ns = itertools.repeat('Better', 3)
for n in ns:
    print(n)

print("=====contextlib=====")


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Better') as q:
    q.query()

# @contextmanager

print('=====@contextmanager========')
from contextlib import contextmanager


class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin....')
    q = Query2(name)
    yield q
    print('End...')


with create_query('Chelsea') as q2:
    q2.query()

print('==== 前后执行代码 ==')


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('\tHello')
    print('\tBetter')
