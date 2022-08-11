from sys import argv
script, input_file = argv

#This defines print_all as a function, with the argument f.
def print_all(f):
    #This prints the function read of the argument f.
    print(f.read())

#This rewinds the file
def rewind(f):
    #I don't know what this does
    f.seek(0)

#This defines print_a_line as a function, with the arguments line_count and f
def print_a_line(line_count, f):
    #this prints the value for line_count and reads the line for the argument f
    print(line_count, f.readline())

#This sets the current file to opening the input file determined in the commandline (argv)
current_file = open(input_file)

print("First let's print the whole file:\n")

#calls the function print_all with the argument current_file, which opens the file set by input_file argv given by the commandline
print_all(current_file)
print("Now let's rewind, kind of like a tape.")

#rewinds files. After the readline() function is executed, the script will move towards the end of the file. When you rewind the file, the program
#goes back to the beginning, like an actual tape.
rewind(current_file)

print("Let's print three lines:")

#Okay, so this sets a variable current line, which amounts to one. The idea here is to add one number at each interation, for each line. So this will return
#the number of the current line. The script doesn't really show the current line. Instead, it counts how many lines have passed, which amounts to
#the current line.
current_line = 1
#okay, so you run the function print_a_line with the argument current line, which equals to one. This will display the current line. The second argument, current_file
#will open input_file, which was defined by the command line when the program was executed. Input file will be read by the function .readline().
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)