# from hangy import getRandomWord, words

import pygame
import os
import math
import random

pygame.init()

WIDTH, HEIGHT = 1366, 768


win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Hangman Game!")

center = win.get_rect().center

# load images

images = []

for i in range(7):

    image = pygame.image.load(os.path.join(
        "images", "hangman" + str(i) + ".png"))
    images.append(image)

print(images)

# game variables

# Names of states and cities of India

wordies = '''jharkhand mumbai delhi srinagar kerala assam karnataka maharashtra mizoram nagaland rajasthan meghalaya sikkim odisha kashmir  dehradun panji dispur kota  bihar chandigarh amritsar lucknow ladakh telangana shimla gangtok lakshadweep jamshedpur  jaipur indore assam chennai patna haryana punjab bhopal kolkata uttarakhand '''.split()
words = list(wordies)
done_guessed_word = []
word = random.choice(words).upper()
# print(word)

hangman_status = 0

OFF_WHITE = (245, 245, 245)
# OFF_WHITE = (245, 245, 245)

guessed = []


# button variables

RADIUS = 20

GAP = 15

letters = []

startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)

starty = 400

A = 65

for i in range(26):

    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))

    y = starty + ((i // 13) * (GAP + RADIUS * 2))

    letters.append([x, y, chr(A + i), True])


# fonts

LETTER_FONT = pygame.font.SysFont('open sans', 40)

WORD_FONT = pygame.font.SysFont('open sans', 60)

TITLE_FONT = pygame.font.SysFont('open sans', 70)


FPS = 200

clock = pygame.time.Clock()

run = True

# 
def drawFunc():
    OFF_WHITE = (245, 245, 245)
    win.fill(OFF_WHITE)

    # draw title

    text = TITLE_FONT.render("HANGMAN", 1, (0, 0, 0))

    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word

    display_word = ""

    for letter in word:

        if letter in guessed:

            display_word += letter + " "

        else:

            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, (0, 0, 0))

    win.blit(text, (400, 200))

    # draw buttons

    for letter in letters:

        x, y, ltr, visible = letter

        if visible:

            pygame.draw.circle(win, (0, 0, 0), (x, y), RADIUS, 3)

            text = LETTER_FONT.render(ltr, 1, (0, 0, 0))

            win.blit(text, (x - text.get_width() /
                     2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    # pygame.time.delay(500)
    OFF_WHITE = (245, 245, 245)
    win.fill(OFF_WHITE)
    text = WORD_FONT.render(message, 1, (0, 0, 0))
    win.blit(text, (text.get_rect(center=win.get_rect().center)))
    pygame.display.update()
    pygame.time.delay(2000)

while run:
    if (word not in done_guessed_word):
        drawFunc()
        clock.tick(FPS)
        drawFunc()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                m_x, m_ypos = pygame.mouse.get_pos()

                for letter in letters:

                    x, y, ltr, visible = letter

                    dis = math.sqrt((x - m_x) ** 2 + (y - m_ypos) ** 2)

                    if visible:

                        if dis < RADIUS:

                            letter[3] = False
                            guessed.append(ltr)

                            if ltr not in word:
                                hangman_status += 1

        drawFunc()
    # Give a hint to the user if he/she fails to guess the correct letter in 3 attempts
        # if hangman_status == 3:
        #     # hint = random.choice(list(word))
        #     hints = 1
        #     while hints == 1:
        #         for i in word:
        #             if i not in guessed:
        #                 print(i)
        #                 text = LETTER_FONT.render(i, 1, (0, 0, 0))
        #                 guessed.append(i)
        #                 hints += 1
        #     win.blit(text, (400, 200))
        #     pygame.display.update()

        won = True

        for letter in word:

            if letter not in guessed:

                won = False

                break
        if won:
            display_message("You WON!")
            break
        if hangman_status == 6:
            display_message("You LOST!")
            print("The word was: " + word)
            display_message("The word was: " + word)
            break
        
    # main()
done_guessed_word.append(word)
pygame.quit()