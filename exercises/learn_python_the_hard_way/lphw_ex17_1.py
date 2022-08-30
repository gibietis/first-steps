#Okay, so the idea is to take the same code, remove whatever I find irrelevant and try to make it shorter and better. 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}\n")
in_file = open(from_file); indata = in_file.read()

print("\nReady, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w'); out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()