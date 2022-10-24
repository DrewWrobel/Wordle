import random
import string

from words import words

#def split(word):
    #return list(word)

def GRW():
    word = random.choice(words)
    return word.upper()


def Wordle():
    word = GRW(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_word = set()
    letter_in_word = str('*')
    letter_in_place = str('\/')

    tries = 6

    while tries > 0:
        print('You have ', tries, ' left'.join(used_letters))
        print('Current word: ', ' '.join(word_list))

        user_word = input('Guess: ').upper()
        if used_word