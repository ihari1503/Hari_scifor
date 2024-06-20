# -*- coding: utf-8 -*-
"""OOPS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yQKiJhV_q62AOUUlGq6H00Dpir8uGes1
"""

class Father:
  def skills(self):
    print("sh")

class Mother:
  def skills(self):
    print("wd")

class child(Father,Mother):
  def skills(self):

    print("Child ")

ch = child()
ch.skills()

#Method Overwriting

class Animal:
  def make(self):
    print("xyz")
class Dog(Animal):
  def make(self):
    print("tyh")
class cat(Animal):
  def make(self):
    print("ki")

d = Dog()
c = cat()
a = Animal()

print(d.make())
print(c.make())
print(a.make())

class Dog():

     def animal_kingdom(self):

       print("Mammal")

     def legs(self):

       print("Four")

class Lizard():

     def animal_kingdom(self):

       print("Mammal lizard")

     def legs(self):

       print("Four")

def function1(obj):

       obj.animal_kingdom()

       obj.legs()

obj_dog = Dog()

obj_lizard = Lizard()

function1(obj_dog)

function1(obj_lizard)

class Car:
  def __init__(self,brand,model,year):
    self.__brand = brand
    self.model = model
    self.year = year

  def get_brand(self):
    return self.__brand

  def accelerate(self):
    print(f"The {self.model} is accelerating!")

my_car = Car("Tesla","Model 5",2023)
print(my_car.model)

print(my_car.get_brand())
print(my_car.accelerate())

class student:
  def __init__(self,name,studentid,present_days):
    self.name = name
    self.__studentid = studentid
    self.present_days = present_days

  def getstdid(self):
    return self.__studentid

  def attend(self):

    print(self.present_days)

stt = student("Aayush","SD1256",57)
print(stt.attend())