import functools


def now():
    print('2018-09-17')


f = now
f()
print(f.__name__)
print(now.__name__)

print("====== decorator ====")


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now2():
    print('2009')


now2()
print(now2.__name__)
print()


# 3层嵌套 def
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)  # 执行func

        return wrapper

    return decorator


@log2('execute')
def now3():
    print("2018-09-199")


now3()
print(now3.__name__)  # wrapper

# 修改 __name__
# 使用 @functools.wraps(func)

# 偏函数
print()
print(int("12345"))
print(int("12345", base=8))
print(int("12345", base=16))


#def int2(x, base=2):
 #   return int(x, base)

#print(int2('1000000'))

int2 = functools.partial(int, base=2)
print(int2('1000000'))



