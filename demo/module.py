#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog like eat meat')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_go(o):
    o.run()


dog = Dog()

cat = Cat()
run_go(cat)
run_go(dog)


# 还可以这样
class MyTimer(object):
    def run(self):
        print("time running...")


timer = MyTimer()
run_go(timer)

print(isinstance(dog, Animal))
print(isinstance(cat, Dog))

# types
import types

print('===============')
print(type('1234'))  # <class 'str'>
print(type(run_go))  # <class 'function'>

print(type(abs) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x:x) == types.LambdaType)

print(type(x for x in range(10)) == types.GeneratorType)

print("=========== 多个")
print( isinstance([1,2,3], (list, tuple)) )
print( isinstance((1,2,3), (list, tuple)) )

print('====dir=')
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

print('======= len')

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog)) 

