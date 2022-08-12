#Okay, so the idea is to write mathematical formulas and transform them into functions

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a ,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

#Zed proposes: 24 + 34 / 1000 - 1023 

subtract(add(24, divide(34, 1000)), 1023)