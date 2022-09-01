# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

hight_score = 0
for score in student_scores:
    if score > hight_score:
        hight_score = score

print(f"The highest score in the class is: {hight_score}")
