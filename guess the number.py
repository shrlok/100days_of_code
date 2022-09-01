import random
level = input("turn the level 'hard' or 'easy'")
number = random.randint(0,101)
if level == "hard":
    guess = 5
elif level == "easy":
    guess = 10

for i in range(guess ):
    print(f"you have a {guess} attempts remaining to guess nubmer !")
    guess -= 1
    player_number = int(input("pick a number >> "))
    if player_number == number:
        print("Win!")
        break
    elif player_number > number:
        print("So Hight!")
    else:
        print("So Low!")
