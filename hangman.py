import random
from words import word_list


# get the word
# check for inpropriate input 
# check for letter and word input
# check for lose

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play_game(word):
    
    tries = 0
    guessed = False
    guessed_word = []
    guessed_letter = []
    word_completion = '-' * len(word)

    print('Let\'s play HANGMAN!')
    print(display_hangman(tries))
    print(word_completion)
    print('\n')

    while tries < 6 and not guessed:
        guess = input('Enter a letter or a word ?: ').upper()

        if len(guess) == 1 and guess.isalpha():

            if guess in guessed_letter:
                print('You already guess that letter !')

            elif guess not in word:
                print('Sorry you got a wrong answer !')
                guessed_letter.append(guess)
                tries += 1
                
            else:
                print('You guess the right letter !')
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if '-' not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print('You already guess the word!')

            elif guess != word:
                guessed_word.append(guess)
                tries += 1
                print('You guess the wrong answer !')

            else:
                print('You win the game !')
                guessed_word.append(guess)
                guessed = True
                word_completion = word


        else:
            print('Invalid Input')
        
        print(display_hangman(tries))
        print(word_completion)
        print('\n')


    if guessed:
        print('Yay ! you\'ve won the game !')
    
    else:
        print('You run out of try, the word is '+ word + '. Maybe next time')



def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play_game(word)

    while input('Play Again? (Y/N): ').upper() == 'Y':
        word = get_word()
        play_game(word)

if __name__ == '__main__':
    main()
