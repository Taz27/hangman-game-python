import random

#print(random.randrange(1,20))
str1 = "CROWN"
word_lst = list(str1)
l = len(str1)
#print(l)
m = int(l / 2) + 1
print(m)
i = 1
maskedLetters = ""
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
			maskedLetters = maskedLetters + sChar
			print(str1)
	else:
		#str1[r] = "_"
		sChar = str1[r]
		str1 = str1.replace(sChar, "_")
		maskedLetters = maskedLetters + sChar
		print(str1)
		alreadyGen = str(r)
	i += 1

print(alreadyGen)
print(str1)
print("Masked Letters are: " + maskedLetters)
maskedLetters = maskedLetters.upper()
#print(str1)

#print(userInput)
#if userInput in maskedLetters:
while True:
	print("Make a guess. Enter Alphabet: ")
	print("-----------------------------")
	userInput = str(input())
	userInput = userInput.strip()
	userInput = userInput.upper()
	if userInput.isalpha() and len(userInput) == 1:
		print("Input is Valid")
		break
	else:
		print("Please only enter a single Alphabet:")
		continue

print(">>>>>>>>>>>")
