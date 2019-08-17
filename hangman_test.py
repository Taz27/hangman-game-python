import random

#print(random.randrange(1,20))
str1 = "HARTAJ"
word_lst = list(str1)
l = len(str1)
#print(l)
m = int(l / 2) + 1
print(m)
i = 1
maskedLetters = ""
maskedWord = ""
newWord = ""
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
			maskedWord = maskedWord.replace(sChar, "_")
			maskedLetters = maskedLetters + sChar
			print(maskedWord)
	else:
		#str1[r] = "_"
		sChar = str1[r]
		maskedWord = str1.replace(sChar, "_")
		maskedLetters = maskedLetters + sChar
		print(maskedWord)
		alreadyGen = str(r)
	i += 1

print(alreadyGen)
print("Original word is: " + str1)
print("Masked word is: " + maskedWord)
print("Masked Letters are: " + maskedLetters)
maskedLetters = maskedLetters.upper()
maskedWord_lst = list(maskedWord)
print(maskedWord_lst)
#subWord = word_lst[1 + 1:]
#print("Subword: " + str(subWord))

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
if userInput in maskedLetters:
	print("Good Guess.")
	alphaNum = word_lst.count(userInput)
	#print("Num times exists: " + str(alphaNum))
	if alphaNum == 1:
		xIndex = word_lst.index(userInput)
		maskedWord_lst[xIndex] = word_lst[xIndex]
		print(maskedWord_lst)
		for x in maskedWord_lst:
			newWord = newWord + x
		print("New Word After Guess: " + newWord)
	else:
		'''rInd = 0
		while alphaNum != 0:
			xIndex = word_lst.index(userInput)
			maskedWord_lst[xIndex] = word_lst[xIndex]
			#make a sub word after that position of that alphabet.
			subWord = word_lst[xIndex + 1:]
			rInd = subWord.index(userInput)
			alphaNum = alphaNum - 1'''
		i = 0
		for a in maskedWord_lst:
			if word_lst[i] == userInput:
				maskedWord_lst[i] = userInput
			i = i + 1
		print(maskedWord_lst)
		for x in maskedWord_lst:
			newWord = newWord + x
		print("New Word After Guess: " + newWord)

else:
	print("Wrong guess")
