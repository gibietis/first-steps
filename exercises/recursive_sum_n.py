#Implement a recursive function to compute the sum of the (n) first integer numbers
#(where (n) is a function parameter). Start by thinking about the base case (the sum
#of the first 0 integers is?) and then think about the recursive case.
n = int(input("Insert the value for 'a': "))
def integers(n):
    if n == 0:
        return 0
    else:
        return n + integers(n-1)
print(integers(n))