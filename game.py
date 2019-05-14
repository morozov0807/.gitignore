import random
import sys

# picture of gallows
gallows = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
       "_______\n|     |\n|\n|\n|\n|\n|\n=======",
      ]

# Lists of words for the game
five_letters = ['ankle', 'apple', 'birds', 'aunts', 'blood',
         'bones', 'forty', 'glitz', 'gnome', 'goats',
          'fairy', 'gator', 'glass', 'kneel', 'laces',
          'patio', 'party', 'taffy', 'zones', 'wages'
         ]
ten_letters = ['jackrabbit', 'maximizers', 'abnormally', 'abolishers', 'adrenaline',
        'california', 'basketball', 'friendship', 'renovation', 'skateboard',
        'understand', 'leadership', 'restaurant', 'generation', 'girlfriend',
        'vegetables', 'protection', 'trampoline', 'rainforest', 'instrument']
fifteen_letters = ['maneuverability', 'insubordination', 'excommunication', 'acclimatization',
             'rationalisation', 'mischievousness', 'kindheartedness', 'procrastinating',
            'confidentiality', 'instrumentation', 'inaccessibility', 'marginalization']

#my amazing functions
def pick_diff():
    prompt = "Pick a difficulty, please. (Easy, Medium, Hard)\n>"
    choice = ""
    while choice not in ['easy', 'medium', 'hard']:
        choice = input(prompt)
        choice = choice.lower()
    change_diff(choice)

def change_diff(level):
    message = "\nYou picked " + level + ". Do you want to change it? [Y/N]\n>"
    answer = ""
    while answer not in ['y', 'n']:
        answer = input(message)
        answer = answer.lower()
    if answer == 'y':
        pick_diff()
    if answer == 'n':
        print("\nLET'S PLAY!\n")
        choose_word(level)

def choose_word(choice):
    if choice == 'easy':
        word = random.choice(five_letters)
    elif choice == 'medium':
        word = random.choice(ten_letters)
    elif choice == 'hard':
        word = random.choice(fifteen_letters)
    play_game(word)

def play_game(this_word):
    word = list(this_word)
    blanks = "_" * len(word)
    blanks = list(blanks)
    guessed = []
    incorrect = 6
    while incorrect > 0:
        print("\n" + gallows[incorrect]
              + "\nYou have {} chances.".format(incorrect)
              + "\nYour word: " + "".join(blanks)
              + "\nGuessed letters: " + ", ".join(guessed)
             )
        letter = input("Your guess: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("\n\nYou already guessed that!")
            elif letter in word:
                for index,character in enumerate(word):
                    blanks = list(blanks)
                    if character == letter:
                        blanks[index] = letter
                        current = "".join(blanks)
                        if blanks == word:
                            print("\n\nCONGRATULATIONS, YOU WON!!\nYour word was " + ''.join(word) + ".\n")
                            play_again()
            elif letter not in word:
                incorrect -= 1
                guessed.append(letter)
        else:
            print("\n\n!Only single letters allowed!\n\n")
    else:
        print(gallows[0])
        print("\nSorry " + player + ", your game is over!\nYour word was " + ''.join(word) + ".")
        play_again()

def play_again():
    """Offer the player a chance to play again."""
    repeat = input("Would you like to play again " + player + "? [Y/N]\n>").lower()
    if repeat == 'y':
        print("Let's play!")
        pick_difficulty()
    else:
        print("Thanks for playing! Have a great day!")
        sys.exit()

# Let's play, "welcome" 
player = input("Let's play hangman! Please type your name.\n>").lower()
player = player.title()
print("\nHey, " + player + "!\nYou get six incorrect guesses before you lose.\nWhich difficulty would you like?\n  Easy - Five letter word\n  Medium - Ten letter word\n  Hard - Fifteen letter word")

# Selecting the difficulty
difficulty = pick_diff()