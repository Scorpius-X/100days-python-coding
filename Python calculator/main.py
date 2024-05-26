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
    '+' : add,
    '-' : subtract,
    '*' : muliply,
    '/' : divide,
}