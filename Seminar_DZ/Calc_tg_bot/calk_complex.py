# Работа с комплексными числами

def calc(a:complex, b:complex, operation):
    a = complex(a)
    b = complex(b)
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    if operation == '/':
        return a/b
