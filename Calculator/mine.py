def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculation():
    num_1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol= input("Pick an operation ")
        num_2 = float(input("What's the next number"))


        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} '=' {answer}")

        continue_quesion  = input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation\n"
                                  f"type 'exit' to exit ")

        if continue_quesion == "y":
            num_1 = answer
        elif continue_quesion == "exit":
            break
        else:
            should_continue = False
            calculation()

calculation()