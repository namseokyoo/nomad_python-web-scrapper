#Data Types of Python
a_string = 'like this'
a_number = 3
a_float = 3.14
a_boolean = False
a_none = None
print(type(a_float))

#List inpython
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(type(days))
print("Mon" in days)
print(days[3])
print(len(days))

days.append("Sat") #mutable
print(days)

days.reverse()
print(days)


#Tuples and Dicts
# Tuple is immutable

days2 = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(days2))

namseok = {
  "name" :  "namseok",
  "age" : 36,
  "korean" : True,
  "fav_food" : ["kimchi", "pizza"]
}

print(namseok)
print(namseok["fav_food"])

namseok["hobby"] = "woodwork"

print(namseok)


#Built in Functions
print(len("alskdjflasjdflka"))

age = "18"
print(age)
print(type(age))

n_age = int(age)
print(n_age)
print(type(n_age))


#Creating a Your First python Function

def say_hello(who):
  print("hello", who)
  print("bye")

say_hello("namseok")

def plus(a,b=0):
  print(a+b)

plus(5,6)



#Returns

def p_plus(a,b):
  print(a+b)

def r_plus(a,b):
  return a+b


p_result = p_plus(2,3)
r_result = r_plus(2,3)

print(p_result, r_result)


#Keyworded Arguments

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello(age="36",name="namseok")
print(hello)


#Code Chanllenge!

def plus(a,b):
  return float(a)+float(b)

def minus(a,b):
  return float(a)-float(b)

def times(a,b):
  return float(a)*float(b)

def division(a,b):
  return float(a)/float(b)

def negation(a):
  return -float(a)

def power(a,b):
  return float(a)**float(b)

def reminder(a,b):
  return float(a)%float(b)


#Conditionals part open

def plus(a,b):
  if type(b) is int or type(b) is float:
    return a+b
  else:
    return None

print(plus(12,12))


#if else and ord

def age_check(age):
  print(f"you are {age}")
  if age <18:
    print("you cant drink")
  elif age == 18 or age ==19:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("engjoy your drink")

age_check(19)


# for in

days=("Mon", "Tue","Wed", "Thu", "Fri")

for day in days:
  if day is "Wed":
    break
  else:
    print(day)


#Module


import math

from math import ceil
from math import fsum as sexy_sum
# 

print(math.ceil(1.2))
print(math.fabs(-1.2))
print(sexy_sum([1,2,3,4,5,6,7]))

from calculator import plus

print(plus(1,2))