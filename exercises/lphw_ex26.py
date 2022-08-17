#Okay, so we're supposed to correct all problems with this code. The corrupted code is available @ https://learnpythonthehardway.org/python3/exercise26.txt
#We can find syntax and logic errors in the code. Zed said this would take quite some time to get right, but it seems that I've been able to fix every
#major problem in about 25 minutes. 
# This can only mean two things: I'm getting the hang of it or I'm completely clueless.
# I didn't run this through VSCode the first time, I've opened the Text Editor. VSCode makes finding
#errors way too easy, which is not a problem in itself, but it defeats the purpose of the exercise. To be fair, I found a problem with line 61
#with VSCode (missing 'f' from fstring)
from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())

print("Let's practice everything.")
print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6 
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.".format(*formula))


people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

