#Step 1
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display_word =[]
for _ in range(len(chosen_word)):
    display_word.append("_")

print(display_word)
end_of_game = False
lives = 6

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display_word[i] = guess

    print(display_word)
    if "_" not in display_word:
        end_of_game = True
        print("You Win!")
    if guess not in display_word:
        lives -= 1
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print ("You Lose!")



