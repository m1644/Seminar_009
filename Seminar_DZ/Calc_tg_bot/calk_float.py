# Работа с рациональными числами

def calc(a:float, b:float, operation):
    a = float(a)
    b = float(b)
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    if operation == '/':
        return a/b
