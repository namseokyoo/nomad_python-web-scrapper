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

def plus():

def minus
