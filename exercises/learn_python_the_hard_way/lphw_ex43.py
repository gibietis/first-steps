#The idea behind this project is to make your own game from Zed's instructions on how to start a code from scratch.
#I won't do this for now. I want to finish all the basic concepts given by the book and start working on Project Farm.
#Being very honest, I don't find coding text-based games amusing at all.
#Yet, I'll still type the game made by Zed, since copying and reading code, did help me a lot to understand coding better.

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("Finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud... if she were smarter.",
            "Such a loser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
        

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. Yand your
            Last mission is to get the neutron destruct bomb from the Weapons ARmory, put it in the bridge, and blow
            The ship p after getting into an escape pod.

            You're running down the central corridor to the Weapons Armory when
            a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume flowing around
            his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.
            """))

        action = input("> ")

        #Sorry, no time to type any more stories. It looks cool, but it consumes quite a lot of time.
        if action == "shoot!":
            print(dedent("""
            You try to kill the Gothon and he kills you
            """))
            return "death"

        elif action == "dodge!":
            print(dedent("""
            You try to dodge and he eats you
            """))

        elif action == "tell a joke":
            print(dedent("""
            You distract him and you are able to get through the Armory door
            """))
            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You get to a code lock. If you get it wront 10 times, it'll lock forever
        """))

        code = f"{randing(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
        print("BZEEEDZD!")
        guesses += 1
        guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            You get the bomb and run away
            """))

            return "the bridge"

        else:
            print(dedent("""
            You get blown up
            """))

            return "death"

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You jump into a room with 5 enemies who are about to kill you
            """))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                You get shot and die
                """))

            return "death"
        
        elif action == "slowly place the bomb":
            print(dedent("""
                You plant the bomb and rush to the escape pod
                """))

            return "escape_pod"
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You run to the pods and find five of them
        """))
    
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You board a terrible pod and die a terrible death
            """))
            return "death"

        else:
            print(dedent("""
            You board the good pod and survive
        """))
            return "finished"

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return "finished"

class Map(object):

    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death(),
        "fnished": Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()