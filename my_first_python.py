#! python
print("Hello, This program is coded by Taran Mand in PYTHON 3")
print("Please enter your name?")
x = str(input())
print()
print("Hello " + x + ", Please enter how many times you want to say WAHEGURU?")
try:
 numTimes = int(input())
 print("OK. Your wish is granted! ....Press any key to continue.")
 a = input()
 i = 1
 while i <= numTimes:
   if i == 1:
    print(x + " says SATNAM WAHEGURU " + str(i) + " time.")
   else:
    print(x + " says SATNAM WAHEGURU " + str(i) + " times.")
    #if i == 250000:
    #print("Enter WAHEGURU...!")
    #x = input()
   i += 1
 print(" ")
 print("Thank you for using my program. Regards, TARAN MAND :)")
 y = input()
except ValueError:
   print("That's not an Number!")
   print("Please Re-Execute the program and enter a number.")
   y = input()

   print(y)
