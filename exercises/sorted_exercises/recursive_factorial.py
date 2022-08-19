#Implement the factorial function and test it with several different values. Cross-check
#with a calculator.
x = int(input("Insert the number you with to factor: "))
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(x))

#Cross-check okay!