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

alreadyGuessed = ""
isGuessComplete = False
numOfGuessesLeft = 7


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


while numOfGuessesLeft > 0 and isGuessComplete == False:
	while True:
		print("Already Guessed: " + alreadyGuessed)
		print("Make a guess. Enter Alphabet: ")
		print("-----------------------------")
		userInput = str(input())
		userInput = userInput.strip()
		userInput = userInput.upper()
		if userInput.isalpha() and len(userInput) == 1:
			print("Input is Valid")
			if userInput in alreadyGuessed:
				print("You already guessed this Alphabet earlier...")
				continue
			else:
				alreadyGuessed = alreadyGuessed + userInput
				break
		else:
			print("Please only enter a single Alphabet:")
			continue

	print(">>>>>>>>>>>")

	if userInput in maskedLetters:
		print("Good Guess.")
		i = 0
		for a in maskedWord_lst:
			if word_lst[i] == userInput:
				maskedWord_lst[i] = userInput
			i = i + 1
		print(maskedWord_lst)
		for x in maskedWord_lst:
			newWord = newWord + x
		print("New Word After Guess: " + newWord)
		if newWord == str1:
			print("You fully guessed the word. You WIN *****")
			isGuessComplete = True
		else:
			newWord = ""

	else:
		numOfGuessesLeft = numOfGuessesLeft - 1
		print("Wrong guess. Chances remaining: " + str(numOfGuessesLeft))
		if numOfGuessesLeft == 0:
			print("GAME OVER ###### ----- You are a LOSER")
