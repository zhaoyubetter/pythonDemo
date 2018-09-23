# 函数

# 可变参数  - 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(1, 2, 3, 4, 5))


# 关键字参数 dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30, city='Beijing', job='Java')

person('Michael', 30, **{'city': 'Beijing', 'job': 'Java'})

# 命名关键字参数  限制关键字参数的名字，就可以用命名关键字参数
# 特殊分隔符*，*后面的参数被视为命名关键字参数
print('========= >>>>>><<<<<<<< =============')


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('better', 30, city='Beijing', job='Java')


def person3(name, age, *like, city, job):  # *like 为可变参数
    print(name, age, like, city, job)


person3('chelsea', 30, 'Android', 'Kotlin', city='Beijing', job='Java')
