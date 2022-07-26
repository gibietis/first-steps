#The Fibonnaci sequence is a sequence of numbers in which each number of the
#sequence matches the sum of the previous two terms. Given the following recursive
#definition implement (fib(n)).
n = int(input("Insira o número: "))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))