def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2: {arg2}")

#args is unnecessary

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg: {arg2}")

#this receives only one argumet

def print_one(arg1):
    print(f"arg1: {arg1}")

#this receives no arguments

def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()