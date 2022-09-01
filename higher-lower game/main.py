from game_data import data
from random import randint
from art import logo, vs
from replit import clear


def random_num():
    ramdom_num = randint(0, 49)
    return ramdom_num


def check_answer(answer, person_A, person_B):
    if answer == "A" and data[person_A]['follower_count'] > data[person_B]['follower_count'] or answer == "B" and data[person_B]['follower_count'] > data[person_A]['follower_count']:
        return True
    else:
        return False


def game():
    game_over = False
    score = 0
    print(logo)
    while not game_over:
        person_a = random_num()
        person_b = random_num()

        # For testing
        # print( f"person A = {data[person_a]['follower_count']} ")
        # print( f"person B = {data[person_b]['follower_count']} ")
        print(f"Compare A: {data[person_a]['name']}, a {data[person_a]['description']}, from {data[person_a]['country']}.")
        print(vs)
        print(f"Against B: {data[person_b]['name']}, a {data[person_b]['description']}, from {data[person_b]['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ")

        clear()
        print(logo)
        if check_answer(answer, person_a, person_b):
            score +=1
            print(f"You're right! Current score: {score}.")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()