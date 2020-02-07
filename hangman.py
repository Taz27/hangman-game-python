import random
import winsound #for playing sounds

banner = '''
#     #    #    #     #  #####  #     #    #    #     #
#     #   # #   ##    # #     # ##   ##   # #   ##    #
#     #  #   #  # #   # #       # # # #  #   #  # #   #
####### #     # #  #  # #  #### #  #  # #     # #  #  #
#     # ####### #   # # #     # #     # ####### #   # #
#     # #     # #    ## #     # #     # #     # #    ##
#     # #     # #     #  #####  #     # #     # #     #
'''

codedBy = '''\
********************************************************
GAME PROGRAMMED BY: (T | A | R | A | N - M | A | N | D )
********************************************************
'''
hanger = [
"""
________
|      |
|
|
|
|             """,
"""
________
|      |
|      0
|
|
|             """,
"""
________
|      |
|      0
|     /
|
|             """,
"""
________
|      |
|      0
|     /|
|
|             """,
"""
________
|      |
|      0
|     /|\\
|
|             """,
"""
________
|      |
|      0
|     /|\\
|     /
|             """,
"""
________
|      |
|      0
|     /|\\
|     / \\
|
~~ YOU GOT ME HANGED :( LOSER !!!"""]

winPic = """
   0
~~ | ~~
  / \\
************
~~ WINNER ~~
************"""

#Define functions here
def format_Word(wd):
	fWord = ""
	for x in wd:
		  fWord = fWord + x + " "
	return fWord

def convert_wordList_to_string(w_list):
	nWord = ""
	for x in w_list:
		nWord = nWord + x
	return nWord

print(banner)
print(codedBy)

f = open("list_of_animals.txt", "r")
words = f.read()
f.close()
#words = "penguin elephant parrot albatross tortoise leopard tiger anteater antelope rabbit peacock zebra giraffe sheep baboon camel eagle badger beaver #rhino vulture bear crocodile kangaroo buffalo kingfisher ostrich koala dinosaur meerkat wolf"

words_list = words.split()
random.shuffle(words_list)
#print(words_list)

for wrdz in words_list:

	#print(random.randrange(1,20))
	str1 = str(wrdz)
	str1 = str1.upper()
	#convert string word to list.
	word_lst = list(str1)
	l = len(str1)
	#Divide the lenth of word in half and add 1 to get the number of letters to mask.
	letters_to_mask_num = int(l / 2) + 1
	#Initialize the variables to be used.
	i = 1
	maskedLetters = ""
	maskedWord = ""
	newWord = ""
	alreadyGuessed = ""
	isGuessComplete = False
	numOfGuessesLeft = 7
	hangerCount = 0

	while i <= letters_to_mask_num:
		#generate a random number upto the length of the word.
		r = random.randrange(0,l-1)
		#print(str(r) + " Random Num") show random number generated.
		if i > 1: # If first random number has been generated, check if the random numbers generated after that are unique.
			finR = alreadyGen.find(str(r)) #check if this random num has been already generated.
			#print(alreadyGen)
			#print(finR)
			if finR != -1: #if the random number is NOT new, then continue.
				continue
			else: #if random number is unique, record it, get the character at that index in word, replace it with "_"
				alreadyGen = alreadyGen + str(r) #Keep the record of random numbers renerated.
				sChar = str1[r]
				maskedWord = maskedWord.replace(sChar, "_")
				maskedLetters = maskedLetters + sChar #Keep a record of letters that are masked.
				#print(maskedWord)
		else:
			#if random number is being generated first time, no need to check if it is unique.
			#Replace the character at the random index with "_"
			sChar = str1[r]
			maskedWord = str1.replace(sChar, "_")
			maskedLetters = maskedLetters + sChar #Keep a record of masked letter.
			#print(maskedWord)
			alreadyGen = str(r) #Keep a record of random number generated.
		i += 1

	#print(alreadyGen)
	#print("Original word is: " + str1)
	print("\nYou will be shown a Word. You have to guess the missing alphabets. \nYou have only 7 chances. (*HINT: The word is the name of a Bird or an Animal.)")
	input("\nPress ENTER to continue...")
	print("\nGuess the Alphabets in this Word: " + format_Word(maskedWord))

	#print("Masked Letters are: " + maskedLetters)

	#Convert masked letters into Upper case and cast into a list.
	maskedLetters = maskedLetters.upper()
	maskedWord_lst = list(maskedWord)
	#print(maskedWord_lst)
	#print(word_lst)

	#Give 7 chances to the user to Keep guessing the letters in the word and until the full word is NOT guessed.
	#Run the loop 7 times and until full word is not guessed completely.
	while numOfGuessesLeft > 0 and isGuessComplete == False:
		while True: #indefinte loop to get valid input from user.
			#print("Already Guessed: " + alreadyGuessed)
			print("\nMake a Guess. Enter an Alphabet: 						(Enter 'quit' to quit the game.)")
			print("------------------------------")
			userInput = str(input())
			userInput = userInput.strip() #Strip input of any white spaces.
			userInput = userInput.upper() #Convert input into upper case.
			if userInput.isalpha() and len(userInput) == 1: #Check if input is only Alphabets amd only single character.
				#print("Input is Valid")
				if userInput in alreadyGuessed: #If the alphabet entered has already been guessed, let the user know, and continue the loop.
					print("\nYou have already Guessed this Alphabet earlier...")
					print("\nGuessed Word So Far: " + format_Word(convert_wordList_to_string(maskedWord_lst)))
					continue
				else:
					alreadyGuessed = alreadyGuessed + userInput #Update the guessed letters record and break indefinte loop.
					break
			elif userInput == "QUIT":
				exit()
			else:
				print("\nPlease only enter a single Alphabet (Between A to Z).")
				print("\nGuessed Word So Far: " + format_Word(convert_wordList_to_string(maskedWord_lst)))
				continue

		#print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

		if userInput in maskedLetters: #Check if the alphabet entered is present in masked letters string.
			print("Amazing...!!! That is a Good Guess :)")
			i = 0
			for a in maskedWord_lst: #loop through every character in the word and replace the one matching the user input in the masked word.
				if word_lst[i] == userInput:
					maskedWord_lst[i] = userInput
				i = i + 1
			#print(maskedWord_lst)
			newWord = convert_wordList_to_string(maskedWord_lst)
			print("\nGuessed Word So Far: " + format_Word(newWord))
			if newWord == str1: #Check if the new word after guess is equal to the original word.
				print("\nAWESOME...!!! You fully Guessed the Word. You WIN ********* :)")
				print(winPic)
				filename = './sounds/Winning_Sound.wav'
				winsound.PlaySound(filename, winsound.SND_FILENAME)
				isGuessComplete = True #flag that full word is guessed.
				print("\n>>>>>>>>Press ENTER to continue...(Enter 'q' to Quit the game)")
				usrInp = str(input())
				usrInp = usrInp.upper()
				usrInp = usrInp.strip()
				if usrInp == "Q":
					#print("QUITING....")
					exit()
			else: #If word is not fully guessed yet.
				newWord = ""
				filename = './sounds/Cheering_Sound.wav'
				winsound.PlaySound(filename, winsound.SND_FILENAME)

		else:
			numOfGuessesLeft = numOfGuessesLeft - 1 #If it is a wrong guess, let the user know chances remaining.
			print("OOPS ..! Wrong Guess :(")
			print("Chances Remaining: " + str(numOfGuessesLeft))
			print(hanger[hangerCount]) #Show related HANGMAN graphic
			hangerCount = hangerCount + 1 #Increment the hangman graphic counter.
			if numOfGuessesLeft == 0: #If all chances are used, Let the user know.
				filename = './sounds/game_over.wav'#play game over sound.
				winsound.PlaySound(filename, winsound.SND_FILENAME)
				#print("")
				print("\nGAME OVER ****** You are a LOSER")
				print("\nThe word you were trying to guess was: " + format_Word(str1))
				print("\n>>>>>>>>Press ENTER to continue...(Enter 'q' to Quit the game)")
				usrInp = str(input())
				usrInp = usrInp.upper()
				usrInp = usrInp.strip()
				if usrInp == "Q":
					#print("QUITING....")
					exit()
			else:
				filename = './sounds/Loser_Sound.wav' #play wrong guess sound if still guesses are remaining.
				winsound.PlaySound(filename, winsound.SND_FILENAME)
				#newWord = convert_wordList_to_string(maskedWord_lst)
				print("\nGuessed Word So Far: " + format_Word(convert_wordList_to_string(maskedWord_lst)))
