#My first python program
import platform
print("Hello Taran Mand")
x = "FUCK"
print(x[2])
print(len(x))
print(x.lower())
a = "Hello, World!"
b = a.split(",")
print(b[0])
"""docstring la la la """
print("Enter your name:")
#x = input()
#print("Hello, ", x)
thislist = ["apple", "banana", "cherry"]
print(thislist[2])
print(a[5:13])

for x in thislist:
	print(x)
i = 1
"""while i < 1300:
  print(str(i) + " WAHEGURU JI is the BEST !!!...SATNAM WAHEGURU")
  if i == 25:
   print("Enter WAHEGURU...!")
   x = input()
  i += 1
# work with files

#open file for write

f=open('e:/workpy2_file.txt','w')

print(f)

f.write("aaaaaaaaaaaaaaaaaaa\n")
f.write("bbbbbbbbbbbbbb");"""
for x in range(10, 51, 5):
  print(x)

def my_function(f_name = "Lund Singh"):
  print("Hello, my name is " + f_name)

my_function()
my_function("Honey Singh")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(4)

func_x = lambda a, b: a * b
print("\n" + str(func_x(4, 5)) + "\n")

def myfunc(n):
  return lambda a : a * n

mydoubler = lambda a: a * 2

print(mydoubler(5))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mand", 36)
p2 = Person("Chutiya", 42)

print(p1.name)
print(p1.age)
p2.myfunc()
p1.myfunc()
print(p2)
print(p1)
print(Person)

class Student(Person):
  pass

s1 = Student("Lund", 29)
s1.myfunc()

s2 = Student("Guchie", 44)
s2.myfunc()

x = dir(platform)
print(x)
y = platform.system()
print(y)

import datetime

x = datetime.datetime.now()

print(x)
print(x.strftime("%c"))
print("New Patch1")
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(x)

print("This is the new change.")
print("This is 2nd change.")
print("")
print("Honey Singh")
print("New PAtch2")
print("New PAtch3")

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

filename = 'fail-trombone-03.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)
