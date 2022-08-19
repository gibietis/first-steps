#Okay, so the task is rewrite the function using loop and range, while observing the i = i + 1 line, observing if it's still necessary.

#Nope, it's not. It makes sense. Also, the argument for the function becomes useless, since the limit of the function will be given by the range itself.

#The script is not EXACTLY the same, as it runs in a different way. The number at the top and at the bottom was the same when printed (2, 2; 3, 3;).
#Now it shows a different outupt (1, 2; 2, 3). This happens because in the other script, the sum would be made before the second print in the function.
#Ex.: it adds one, and prints the result. Let's say, 2 + 1. it prints three. before adding another number one, it'll print the current
#value of i, which is still 3.
#for the range, it'll print zero three times, one for the top, one for the number and one for the bottom. It won't add anything mid-loop. 
#In fact, the new loop will begin with the number already added. So in the second iteration, it will display 1 at the top, will append 1 to the list,
#print 0 and 1 (given the list numbers) and 1 at the bottom, since nothing was added during mid-loop.

numbers = []
def while_loop():
    i = 0
    for i in range(6):
        print(f"At the top i is {i}")
        numbers.append(i)
        print(f"Numbers now: {numbers}\nAt the bottom i is {i}")

while_loop()

def the_numbers():
    print("The numbers: ")
    for num in numbers:
        print(num)

the_numbers() 