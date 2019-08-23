import datetime
import json
import re

class MyClass:
	x = 5

obj1 = MyClass()
print(obj1.x)


class Person:
	  def __init__(self, name, age):
		  self.name = name
		  self.age = age

	  def myfuncIntro(self):
		  print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

p1 = Person("Honey Singh", 35)
p2 = Person("Taran Mand", 38)

print("My friends are " + p1.name + " and " + p2.name)
p2.myfuncIntro()

class Student(Person):
	def __init__(self, name, age, sex, place_of_birth):
		super().__init__(name, age)
		self.sex = sex
		self.place_of_birth = place_of_birth
	def myfuncWelcome(self):
		print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old. I am a " + self.sex + " and from " + self.place_of_birth)

x = Student("Lund Singh", 36, "male", "Chandigarh")
x.myfuncIntro()
x.myfuncWelcome()

import platform

x = platform.system()
print(x)
x = platform.machine()
print(x)
x = platform.node()
print(x)
x = platform.processor()
print(x)
x = platform.uname()
print(x)
x = platform.win32_ver()
print(x)

#s1 = list(["ABCDEF", "ZZZZZ", "YYYYY"])
#myIt = iter(s1)
#print(next(myIt))
#for x in myIt:
#	print(x)
x = dir(platform)
y = 0
#for i in x:
#	print(i)
#	y = y + 1
print("\nTotal functions in platform are: " + str(y))

x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))

#print(p1)
#print(id(p1))
#print(p2)
#print(id(x))
#print(x)
# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(x)
print(y)

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print(x.start())
print(x.span())
print(x.string)
print(x.group())

if (x):
  print("YES! We have a match!")
else:
  print("No match")

str = "HARTAJ"
x = re.split("z", str)
print(x)

try:
	print(z)
except Exception as err:
	print(err)
else:
	print("Nothing went wrong.")
finally:
	print("The 'try except' is finished")

age = 36
name = "John"
txt = "His name is {0}. {0} is {1} years old."
print(txt.format(name, age))

#f = open("IMG_5400.jpg", "rb")
#print(f.readline())
#for x in f:
#	print(x)
#print(f.readline())
#f.write("penguin elephant parrot albatross tortoise leopard tiger anteater antelope rabbit peacock zebra giraffe sheep baboon camel eagle badger beaver #rhino vulture bear crocodile kangaroo buffalo kingfisher ostrich koala dinosaur meerkat wolf")
#f.close()
#print(x)
#f_cnts = f.read()
#f.close()

#f = open("new_IMG_file.jpg", "wb")
#f.write(f_cnts)
#f.close()
