def break_words(stuff):
    """This function will break words for us."""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """Sort words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after removing it from the total"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes a sentence and returns each word"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Takes a sentence and returns the first and last words."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Takes a sentence and returns the first and last words sorted"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Okay, so it makes sense to have the "words" variable in each function, so that you don't mess with the variable "sentence" in a permanent way.
#This means every iteration of a function will have the full sentence. If you popped words directly, you'd have problems with functions in line 20, 25 and 31.
#Also, I had no idea the triple quotes would create a documentation for my code. That's pretty clever tbh.

#NAME
#    test17
#
#FUNCTIONS
#    break_words(stuff)
#        This function will break words for us.
#    
#    print_first_and_last(sentence)
#        Takes a sentence and returns the first and last words.
#    
#    print_first_and_last_sorted(sentence)
#        Takes a sentence and returns the first and last words sorted
#    
#    print_first_word(words)
#        Prints the first word after removing it from the total
#    
#    print_last_word(words)
#        Prints the last word
#    
#    sort_sentence(sentence)
#        Takes a sentence and returns each word
