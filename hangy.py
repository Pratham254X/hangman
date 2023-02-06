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
HANGMAN_PICTURES = ['''
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
wordies = '''ant baboon nice
badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
words = list(wordies)
theSecretWord = random.choice(words).upper()
tries = 6
difficulty = 'X'
def getDifficulty(difficulty):
    while difficulty.upper() not in 'EMH':
        if difficulty.upper() == 'M':
            del HANGMAN_PICTURES[8]
            del HANGMAN_PICTURES[7]
        if difficulty.upper() == 'H':
            del HANGMAN_PICTURES[8]
            del HANGMAN_PICTURES[7]
            del HANGMAN_PICTURES[5]
            del HANGMAN_PICTURES[3]
        else:
            print("Unknown difficulty. Choose again.")
            continue
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayTheBoard(misses, corrects, theSecretWord):
    print(HANGMAN_PICTURES[len(misses)])
    print()
    print('Missed letters: ', end='')
    for letter in misses:
        print(letter, end=' ')
    print()
    blanks = '_' * len(theSecretWord)
    for i in range(len(theSecretWord)):
        if theSecretWord[i] in corrects:
            blanks = blanks[:i] + theSecretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if (len(guess) != 1 and guess != "quit()" and guess != "exit()"):
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif (guess not in 'abcdefghijklmnopqrstuvwxyz' and guess != "quit()" and guess != "exit()"):
            print('Please enter a LETTER.')
        else:
            return guess

def askPlayAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')
    difficulty = input("Choose difficulty: E - Easy, M - Medium, H - Hard: ")
    difficulty = difficulty.upper()
    getDifficulty(difficulty)

print('H A N G M A N')
misses = ''
corrects = ''
theSecretWord = getRandomWord(words)
gameDone = False
difficulty = input("Choose difficulty: E - Easy, M - Medium, H - Hard: ")
difficulty = difficulty.upper()
getDifficulty(difficulty)
while True:
    displayTheBoard(misses, corrects, theSecretWord)
    guess = getGuess(misses + corrects)
    if (guess == "quit()" or guess == "exit()"):
        print("Goodbye!")
        break
    if guess in theSecretWord:
        corrects += guess
        foundAllLetters = True
        for i in range(len(theSecretWord)):
            if theSecretWord[i] not in corrects:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + theSecretWord + '"! You have won!')
            gameDone = True
    else:
        misses += guess
        if len(misses) == tries:
            displayTheBoard(misses, corrects, theSecretWord)
            print('You have run out of guesses!\nAfter ' + str(tries) + ' missed guesses and ' + str(len(corrects)) + ' correct guesses, the word was "' + theSecretWord + '"')
            gameDone = True

    if gameDone:
        if askPlayAgain():
            misses = ''
            corrects = ''
            gameDone = False
            difficulty = input("Choose difficulty: E - Easy, M - Medium, H - Hard: ")
            difficulty = difficulty.upper()
            getDifficulty(difficulty)
            theSecretWord = getRandomWord(words)
        else:
            break