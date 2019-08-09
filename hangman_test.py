import random

#print(random.randrange(1,20))
str1 = "CROWN"
l = len(str1)
#print(l)
m = int(l / 2) + 1
print(m)
i = 1
#alreadyGen = str(9)

while i <= m:
	r = random.randrange(0,l-1)
	print(str(r) + " Random Num")
	if i > 1:
		finR = alreadyGen.find(str(r))
		print(alreadyGen)
		print(finR)
		if finR != -1:
			continue
		else:
			alreadyGen = alreadyGen + str(r)
			sChar = str1[r]
			str1 = str1.replace(sChar, "_")
			print(str1)
	else:
		#str1[r] = "_"
		sChar = str1[r]
		str1 = str1.replace(sChar, "_")
		print(str1)
		alreadyGen = str(r)
	i += 1
	print(alreadyGen)
	#print(str1)
