#Add another variable to the function arguments that you can pass in that lets you change
#the + 1 on line 8, so you can change how much it increments by.
#Okay, this was harder to read than it was to execute.
numbers = []
def while_loop(tops):
    i = 0
    while i < tops:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 3
        print(f"Numbers now: {numbers}\nAt the bottom i is {i}")

while_loop(60)

def the_numbers():
    print("The numbers: ")
    for num in numbers:
        print(num)

the_numbers() 