# Write your code below this line 👇
# def prime_checker(number):
#     if number == 2 or number == 3 or number == 5:
#         print("It's a prime number.")
#     elif number %2 != 0 and number % 3 != 0 and number %5:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
