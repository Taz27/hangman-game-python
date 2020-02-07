# hangman-game-python
**Hangman Game**

I coded this app in ***Python***. It is my own version of the popular **Hangman Game** in which a word (name of an animal) with missing letters is displayed on the screen and you get 7 chances to guess the missing letters. On every wrong guess, an ASCII art image of *'hangman'* is displayed, getting closer to being hanged and a 'fail' sound is played. On every correct guess, the half guessed word is shown and a 'cheering' sound is played. When you correctly guess all the missing letters, a 'clapping' sound is played and when you lose all your 7 chances to guess, a 'loser' sound is played and the full word is displayed along with the *'Hanged Man'* ASCII art image.

I used an algorithm which reads the list of words from a text file and randomly hides the letters before showing the word to guess depending on its length on every loop. I used the *winsound* Python library for playing sounds.
