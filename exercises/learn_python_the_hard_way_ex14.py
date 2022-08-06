from sys import argv

script, user_name, mood, age = argv
x = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

likes = input(x)

print(f"I heard you are {mood}.")
print(f"Is that related to your age? {age}, right?")
print(f"Anyways, where do you live {user_name}?")
lives = input(x)

print("What kind of computer do you have?")
computer = input(x)

print(f"""
Alright, so you said {likes} about liking me.
You indeed look like a {mood} dude, probably because you are {age}
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

