import random

fruits = ['orange', 'apple', 'mango', 'banana', 'kiwi', 'strawberry', 'lemon', 'avacado', 'apricot', 'cherry', 'coconut', 'papaya', 'date', 'guava', 'blueberry', 'lime', 'peach', 'pear', 'watermelon', 'pomegranate', 'rasberry', 'plum', 'pineapple', 'grape', 'grapefruit', 'cranberry', 'fig', 'dragonfruit', 'tamarind', 'jackfruit', 'nectarine', 'raisin']

while True:

    computer = random.choice(fruits)

    lives = 6
    guessed_letters = []
    display = ['_'] * len(computer)

    print('Welcome to Hangman!')
    print(f"The word has {len(computer)} letters.")

    while lives > 0 and '_' in display:

        print('Current word: ', ' '.join(display))
        print('Guessed letters: ', guessed_letters)
        print('Lives remaining: ', lives)

        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print('You already guessed that letter!')
            continue

        guessed_letters.append(guess)

        if guess in computer:
            for i, letter in enumerate(computer):
                if letter == guess:
                    display[i] = guess
            print('Good guess!')
        else:
            lives -= 1
            print('Wrong guess!')

    if '_' not in display:
        print('======================================================================')
        print(f'Congratulations!\nYou guessed the word: {computer} in {lives} lives.')
        print('======================================================================')
    else:
        print(f'Game Over! The word was: {computer}')

    replay = input('Wanna play again? (y/n): ').lower()
    if replay != 'y':
        print('Thanks for playing Hangman!')
        break