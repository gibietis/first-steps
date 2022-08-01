#Go through the string below and if the length of a word is even print 'even!'

#Personal note: I've decided to add something related to f-strings here, so it would make the exercise a little bit more interesting.
#The code worked on the first try :D 
string = 'Print every word in this sentence that has an even number of letters'

for palavra in string.split():
    x = len(palavra)
    if len(palavra) % 2 == 0:
            print(palavra)
            print(f'O cumprimento da palavra acima é de {x} caracteres\n')