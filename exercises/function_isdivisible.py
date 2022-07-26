#Implement a function named “is_divisible” that receives two parameters (named “a”
#and “b”) and returns true if “a” can be divided by “b” or false otherwise. A number
#is divisible by another when the remainder of the division is zero. Use the modulo
#operator (“%”).
a = int(input("Define the 'a' value: "))
b = int(input("Define the 'b' value: "))
def is_divisible (a, b):
    if a % b == 0:
        return True
    else:
        return False