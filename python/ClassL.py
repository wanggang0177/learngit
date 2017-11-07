#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

def run_twice(animal):
    animal.run()

dog = Dog()
cat = Cat()
# run_twice(dog)
# run_twice(cat)
# print(type(dog))
# print (dir(dog))

class Student(object):
    __slots__ = ('name', 'age')
    pass

student = Student()
student.name = 'wangg'
student.age = 28
# student.sex = 'm'
print(student.name)
print(student.age)
