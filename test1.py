str1 = "HARTAJ"


lstWord = list(str1)
print(lstWord)
print(id(lstWord))


print(str1)
y = ""

for x in lstWord:
	y = y + x
	print(x)

print(y)
print(lstWord[3])
