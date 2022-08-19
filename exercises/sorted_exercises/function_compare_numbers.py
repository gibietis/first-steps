def add2():
    x = int(input("Insert the first number: "))
    y = int(input("Insert the second number: "))
    if x > y:
        print("The first number is greater than the second number")
    elif x == y:
        print("Both numbers are equal")
    else:
        print("The second number is greater than the first number")
