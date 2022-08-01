#Use for, .split(), and if to create a statement that will print out words that start with 's':

string = 'Print only the words that Start with "s" in this sentence'

for palavra in string.split():
    if palavra [0].lower() == 's':
        print(palavra)

