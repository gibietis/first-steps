#The idea is to replace "6" with a variable and converting the while loop in a function I can call.
v = 6
numbers = []
def while_loop():
    #okay, so this is interesting. I've let the variable "i" outside the function and Python returned me "Local variable referenced before assignment"
    #I didn't understand at first, but now it makes sense. Two options: bring the variable inside the function, or make 
    #the variable global with "global variable_name"
    i = 0
    while i < v:
        print(f"At the top i is {i}")
        numbers.append(i)
        #changed this
        i += 1
        #shortened the script
        print(f"Numbers now: {numbers}\nAt the bottom i is {i}")

while_loop()
#I'll convert this to a function just for fun

def the_numbers():
    #Okay, now I see why Zed did this. If he directly printed the variable, he'd print the list. It's not what we want, we want the numbers, one by one.
    print("The numbers: ")
    for num in numbers:
        print(num)

the_numbers()