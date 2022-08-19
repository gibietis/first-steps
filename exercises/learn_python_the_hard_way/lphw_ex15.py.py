#from the system-specific parameters and functions, import argv,
#which establishes the list of command line arguments passed to the script.
from sys import argv
#script refers to the name of the script, so "for this script, filename is the
#assigned parameter to the argv module
script, filename = argv
#the variable txt is assigned the function open, which opens a file
#with the possibility of assigning different parameters, like reading
#or writing to a certain file, in this case, file filename
txt = open(filename)
#prints the name of the file
print(f"Here's your file {filename}:")
#prints the result of the command .read given to the variable txt, which
#opens the filename file given in argv
print(txt.read())
#repeats the process above, but you can insert any other value, like reading
#another file for this process.
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
