#Python hangman
# 1. accept a character
# 2. make a words list
# 3. take a random word from list
# 4. make a limit eg. 6
# 5. check if char is in word
# 6. if not try += 1
# Add char in missed words list
# 7. if yes, show CORRECT!
# 8.if tries == try, user failed
# 9.  if all words guessed,user wins!
# 10. Terminate game
import random, time
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''',
 '''
    +---+
   [O   |
   /|\  |
   / \  |
       ===''',
       '''
    +---+
   [O]  |
   /|\  |
   / \  |
       ==='''  ]
print("NICE TO MEET YOU")
print("Howdy!")
time.sleep(1)
print("Hangman with Indian Theme")
print("Starting game....")
time.sleep(1)
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
tries = 6
difficulty = 'X'
def getDifficulty(difficulty):
    while difficulty not in 'EMH':
        if difficulty == 'M':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
        if difficulty == 'H':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[5]
            del HANGMAN_PICS[3]
        else:
            print("Unknown difficulty. Choose again.")
            continue
def getGetRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')
    difficulty = input("Choose difficulty: E - Easy, M - Medium, H - Hard: ")
    getDifficulty(difficulty)

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getGetRandomWord(words)
gameIsDone = False
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) == tries:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(tries) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getGetRandomWord(words)
        else:
            break