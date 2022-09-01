
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
game = True
bids = {}

while game:
    name = input("Waht is you name?")
    price = int(input("how much money?"))
    contine = input("print 'yes' or 'no'!")
    bids[name] = price

    if contine == "no":
        game = False
    elif contine == "yes":
        clear()

max_cost = 0
for key in bids:
    if bids[key] > max_cost:
        max_cost = bids[key]
        winner = key

print(f"{winner} : {max_cost}")
