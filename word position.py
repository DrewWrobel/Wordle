
def split(word):
    return [char for char in word]

def game():
    word = str('farce')
    uword = str('fancy')

    while word is not uword:
        if uword[0] == word[0]:
            #print('$')
            if uword[1] == word[1]:
                #print('$$')
                if uword[2] == word[2]:
                    print('$$$')

                for
                    if uword[3] == word[3]:

                        if uword[4] in word[4]:
                            print('$$$$%')

                        elif uword[4] != word[4]:
                            print('$$$$-')
                            break


        elif uword[0] in split(word):
            print('#')

        elif uword[0] not in split(word):
            print('-')


if __name__ == '__main__':
    game()