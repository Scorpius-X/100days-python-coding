import sys
sys.path.append("C:\\Users\\HP\\Documents\\GitHub\\100days-python-coding")
from Clears_vscode_terminal.clear_terminal import clear_terminal

#adds
def add(n1, n2):
    return n1 + n2

#subtracts
def subtract(n1, n2):
    return n1 - n2

#multipies
def muliply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*": muliply,
    "/" : divide,
}
def calculator():
    should_continue = True
    num1 = float(input("Input your first number: "))
    for symbols in operations:
        print(symbols)

    while should_continue:
        operation_symbol = input("Pick an operation symbol: ")
        num2 = float(input("Input your next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1 = num1 , n2 = num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y"
        if not should_continue:
            clear_terminal()
            calculator()
        else:
            num1 = answer
calculator()