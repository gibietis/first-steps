#okay, so this sets a varible i with the number zero assigned as value.
i = 0
#this sets an empty list to a variable called numbers
numbers = []
#while the variable i is less than 6, in other words, while i < 6 == true
while i < 6:
    #this prints the value of i. At first, its zero. So it'll print "At the top i is 0"
    print(f"At the top i is {i}")
    #this function will append i to the numbers list. Meaning the empty list now holds 0 as a value.
    numbers.append(i)

    #this states that i = i (0) has the value of i (0) + 1. It'll do this each pass of the loop, while the condition set in line 6 is true.
    #Oddly enough, Zed didn't use i += 1, neither asked to do so at the script. Probably because i = i + 1 makes the code easier to understand for beginners.
    i = i + 1
    #Same questioning: why didin't he use fstrings here? Anyways, this prints the list of numbers
    print("Numbers now: ", numbers)
    #this prints the value of i at the end of the while loop
    print(f"At the bottom i is {i}")

#prints the numbers once the condition breaks the loop
print("The numbers: ")
#prints the variable numbers.
for num in numbers:
   print(num)