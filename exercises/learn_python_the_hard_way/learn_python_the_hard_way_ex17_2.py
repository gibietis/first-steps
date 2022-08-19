#Zed Shaw states that it can be one line in lenght. I'm not sure on how to do that and mantain readability, so I'll do the best I can to make it as short as possible.
from sys import argv; from os.path import exists
script, from_file, to_file = argv
in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata)
out_file.close(); in_file.close()
#Okay, this works!