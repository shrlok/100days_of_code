import random,
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_chose_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.]\n>>>"))
computer_choos_num = random.randint(0, 2)
list_of_values = (rock, paper, scissors)

user_chose = list_of_values[user_chose_num]
computer_chose = list_of_values[computer_choos_num]

print(user_chose)
print(f"Computer chose:|\n{computer_chose}")

# 0>2 2>0 3<2
if user_chose == computer_chose:
    print("It's a Draw!")
elif user_chose_num == 0 and computer_choos_num == 2:
    print("You Win!")
elif user_chose_num == 1 and computer_choos_num == 0:
    print("You Win!")
elif user_chose_num == 2 and computer_choos_num == 1:
    print("You Win!")
else:
    print("You Loose!")