
#1
from typing import Counter
class CounterClass:
    def __init__(self):
        self.counter =0
    def increase_one(self): 
        self.counter =self.counter+ 1
        print(self.counter)
    def decrease_one(self):
        self.counter = self.counter- 1
        print(self.counter)
    def get_value(self):
        print(self.counter)

obj = CounterClass()
obj.increase_one()
obj.decrease_one()
obj.get_value()

#2
from datetime import datetime 
todaydate = datetime.now()
now = todaydate.strftime("%m-%d-%y")
print("Today is:",now)

#3
class Person:
    def __init__(self,name,last_name,birth_date):
        self.name = name 
        self.last_name = last_name
        self.birth_date = birth_date
    def get_age(self,age):
        self.age = age
    def can_vote(self):
        if(self.age>18):
            return True
        else:
            return False

    def display(self):
         print(f"Name :{self.name}")
         print(f"Last Name :{self.last_name}")
         print(f"Date of birth :{self.birth_date}")

obj = Person("Bob","Dylan","may 24, 1941")
obj.display()
obj.get_age(34)
print(obj.can_vote())

#4
def maximum(one,two):
    if(one>two):
        return one
    else:
        return two

print(maximum(10,20))

#5
def fizz_buzz(num):
    if(num%3==0):
        return "FizzBuzz"
    elif(num%5==0):
        return "Buzz"
    elif(num%3==0 and num%5 ==0):
        return "FizzBuzz"
    else:
        return num

print(fizz_buzz(7))



















