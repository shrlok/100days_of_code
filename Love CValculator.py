# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.lower() + name2.lower()
true_score = 0
love_score = 0
true_score += names.count("t")
true_score += names.count("r")
true_score += names.count("u")
true_score += names.count("e")

love_score += names.count("l")
love_score += names.count("o")
love_score += names.count("v")
love_score += names.count("e")

result = int(str(true_score)+str(love_score))

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
