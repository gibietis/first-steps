people = 30
cars = 40
trucks = 15

#Okay, so this is pretty straight up. If and elif arguments are pretty simple to understand.
#if condition = true, the execute
#else, but if this other condition is true, then execute this instead.
#if none of the is fulfilled, execute this.

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We shoult not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")