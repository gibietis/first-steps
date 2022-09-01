ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

#call split with the argument ten_things
#stuff = split(ten_things, " ")
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    #next_one = pop(more_stuff) - Call the function pop with the argument more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #call append with the arguments stuff, next one
    #append(stuff, next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
#join command will do the exact opposite of split.
print(" ".join(stuff))
print("#".join(stuff[3:5]))