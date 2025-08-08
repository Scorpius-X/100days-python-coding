def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2


operators ={
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}
def calculator():
    should_accummulate = True

    num1 = float(input("what is the first number that you want to add?: "))

    while should_accummulate:

        for symbol in operators:
            print(symbol)

        operator_symbol = input("Please input your operator symbol: ")
        num2 = float(input("what is the second number that you would like to add?: "))
        answer = operators[operator_symbol](num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        choice = input(f"Type Y to continue calculating with {answer} or X to start afresh: ").lower()
        if choice == 'y':
            num1 = answer
            print(answer)
        else:
            should_accummulate = False
            print("\n" * 20)
            calculator()

calculator()




