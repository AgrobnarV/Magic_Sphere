import random


def load_word_list(file_path='word_list.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def get_word_rus(word_list):
    return random.choice(word_list).upper()


def get_category(word):
    categories = {
        'human': 'Object',
        'work': 'Activity',
        'question': 'Task'
    }
    return categories.get(word, 'Unknown category of word')


def print_word(word_, list_):
    result = [c if i == 0 or i == len(word_) - 1 or c in list_ else '_' for i, c in enumerate(word_)]
    print(' '.join(result))


def display_hangman(tries):
    stages = [  # Final state: head, body, both arms, both legs
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ ⎞
           |    
           -
        ''',
        # Head, body, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ 
           |
           -
        ''',
        # Head, body, both arms
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |
           |
           -
        ''',
        # Head, body, and one arm
        '''
           --------
           |      |
           |      O
           |     ⎛▼
           |
           |
           -
        ''',
        # head and body
        '''
           --------
           |      |
           |      O
           |      ▼
           |
           |
           -
        ''',
        # only head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # Initial state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word_list, max_parts=6):
    word = get_word_rus(word_list)
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    tries = max_parts
    print(f"Let's play the word guessing game! Category: {get_category(word)}")
    print(display_hangman(tries))
    print(word_completion)

    while tries > 0:
        word_input = input('Enter a letter or a word: ').upper()

        if not word_input.isalpha():
            print('You were wrong, try again')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print("That's already been used")
            continue

        if len(word_input) > 1:
            if word_input == word:
                print('Congratulations, you guessed the word! You won!')
                break
            else:
                guessed_words.append(word_input)
        else:
            if word_input in word:
                guessed_letters.append(word_input)
            else:
                tries -= 1

        print(f"That's not it, you have {tries} tries left")
        print(display_hangman(tries))
        print_word(word, guessed_letters)

    if tries == 0:
        print(f"You couldn't guess the word: {word}")


play(load_word_list())
# play(load_word_list(), max_parts=8)
