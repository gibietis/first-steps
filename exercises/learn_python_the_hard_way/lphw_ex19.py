

#this line defines the function called cheese and crackers, with the arguments cheese count and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #this line prints the cheese count, first argument
    print(f"You have {cheese_count} cheeses!")
    #this line prints the boxes of crackers, the second argument of the function
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #prints a joke :)
    print(f"Man that's enough for a party!")
    #prints another joke :(
    print("Get a blanket!\n")

print("We can just give the function number directly:")
#this line calls/executes/uses the function cheese and crackers, while giving the amounts for the arguments cheese_count and boxes_of_crackers
cheese_and_crackers(20, 30)

#this one sets the quantities as variables, so you don't need to type manually everytime, by binding the function to variables set before.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#shows that you can do math inside functions
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#shows that you can do math AND use variables as arguments.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


