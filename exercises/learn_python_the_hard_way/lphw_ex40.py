#This is exercise 40 along with the drills proposed by Zed. OOP is pretty challenging at first sight, being very honest.
#I still can't understand much of it.
#Drill one is to add some songs and comprehend that you're actually using a list of strings as the lyrics. The comma at the end of
#each string actually helped me to make this more clear in my head.

#Drill two is to add the lyrics in a separate variable, the pass this variable to the class.
#One observation: I bought the regular version of the book in portuguese. Good old printed book. Yet, they wanted to translate
#absolutely everything written, and it didn't work well in some cases. Once in a while I refer to the english version in PDF to understand something.

#For drill three, the task is to add something, even if you don't know what and how or just break the code
#I've checked a website called "Stacey Learns Code" and found a nice idea for this drill,
#which is to print the song artist. The code is in Python 3.X, looks very different and I wasn't able to replicate it for now.

#PS:
#Okay, the code wasn't in Python, it was in Ruby. It seems that exercise 40 in both books is the same, even the drills are equal.

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

vertigo = Song(["I can't stand the beat, I'm asking for the check",
                "Girl with crimson nails has Jesus around her neck",
                "Swinging to the music, swinging to the music"])

ohne_dich = ["Ohne dich kann ich nicht sein",
            "Ohne dich",
            "Mit dir bin ich auch allein",
            "Ohne dich!",
            "Ohne dich zähl ich die Stunden ohne dich",
            "Mit dir stehen die Sekunden",
            "Lohnen nicht",]

rammstein = Song(ohne_dich)

rammstein.sing_me_a_song()
print("-" * 20)
happy_bday.sing_me_a_song()
print("-" * 20)
bulls_on_parade.sing_me_a_song()
print("-" * 20)
vertigo.sing_me_a_song()