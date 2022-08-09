#Okay, so I'm supposed to write a function on my own and execute it 10 times in different ways.
import math
def ten_times(arg1, arg2):
    print(f"So this will print {arg1}, which is arg1, and {arg2}, which is arg2.")
    print(f"Let's say that this function counts the ammount of soy sacks yielded per hectare.")
    print(f"The plantation yielded {arg1} sacks of soy, harvested in {arg2} hectares of land.")
    print("\n")

ten_times(100, 2)

#I can also assign variables to the arguments.

sacks_of_soy = 300
hectares = 6

ten_times(sacks_of_soy, hectares)

ten_times(10/2, 3*6)

ten_times(10 ** 3, math.sqrt(30))

ten_times(math.sin(3), math.tan(30))

ten_times (1,2)

def tentimes_istoomuch(diesel, time):
    print(f"This will calculate how many liters of diesel an engine drains in total, given how much diesel it takes per hour ran")
    consumption = diesel * time
    print(f"Diesel consumption is {consumption} liters")
    print("\n")

tentimes_istoomuch(12, 25)

liters_hour = 16.1
time_spent = 97.5

tentimes_istoomuch(liters_hour, time_spent)