"""
PlayRubiksCube

- A program that implements player manipulation of the state of a rubiks cube through the PlayCube class

"""

from RubiksCube import Cube
from random import randint
from copy import deepcopy
import os

"""
PlayCube Class

- A class that implements the UI for interacting with a rubiks cube
- self.cube is an instance of the Cube class that is the rubiks cube a player interacts with
- self.print_type is a field that indicates the format the rubiks cube is printed in the UI
    either is the value "face" or "cube", respectively meaning only the front face is printed or all faces of the cube are printed

"""

class PlayCube:

    def __init__(self):
        self.cube = Cube()
        self.print_type = "face"

    # helper function to ask for the user's input and to keep doing so until a valid input is given
    def get_input(self, question, valid_responses):

        print(question)
        valid = False

        # denies inputs that aren't on the list of valid responses and asks until it gets an acceptable answer
        while not valid:
            my_input = str(input(""))

            for v in valid_responses:

                if my_input == v:
                    valid = True
                    break
                
                # to escape any current text prompt, a new PlayCube class is created that's identical to the current one 
                elif my_input == "cancel":
                    new_play(self)
                    break

            if not valid:
                print("Not a valid input. Please try again: ")

        return my_input

    # presents all the commands
    def commands(self):

        os.system("cls")
        print("All commands:")
        print("cancel - cancels any current text prompt and returns to the main screen")
        print("commands - presents all commands")
        print("cube - changes the format of the displayed cube to print all faces")
        print("face - changes the format of the displayed cube to print only the front face")
        print("quit - quits the program")
        print("references - lists various information necessary for interacting with the cube through the UI")
        print("rotate - rotates a 3 x 3 portion of the cube")
        print("scramble - randomly scrambles the cube")
        print("turn - rotates the entire cube")
        input("\n(enter anything to exit the commands screen)\n")

    # lists various information necessary for interacting with the cube through the UI
    def references(self):

        os.system("cls")
        print("References:")
        possible_responses = ["directioning", "numbering"]
        choice = self.get_input("Would you like information on how rotation directioning works or how the front face of the cube is numbered? \n(enter either \'directioning\' or \'numbering\')", possible_responses)
        os.system("cls")

        # prints a cartesian plane for reference
        if choice == "directioning":
            print("Directioning - Positive direction of rotation is defined by the right hand rule applied on any particular axis of rotation:\n")
            print("y")
            print("^")
            print("| z")
            print("| ^")
            print("|/")
            print("O----------> x")

        # prints the front face of a rubiks cube and labels each piece with its related number
        elif choice == "numbering":
            print("\nFront face numbering - This numbering system is used to refer to the front pieces when rotating the cube:")
            print("----------------------------")
            print("|        |        |        |")
            print("|   1    |    2   |    3   |")
            print("|        |        |        |")
            print("----------------------------")
            print("|        |        |        |")
            print("|   4    |    5   |    6   |")
            print("|        |        |        |")
            print("----------------------------")
            print("|        |        |        |")
            print("|   7    |    8   |    9   |")
            print("|        |        |        |")
            print("----------------------------")

        input("\n(enter anything to exit the references screen)\n")

    # rotates a 3 x 3 portion of the cube
    def rotate(self):

        # asks for the piece that's to be rotated
        possible_responses = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        piece_num = int(self.get_input("What piece do you want to rotate? \n(enter either \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', or \'9\')", possible_responses))
        piece = self.cube.get_face_piece(piece_num)

        # asks for the axis of rotation
        possible_responses = ["x", "y", "z"]
        axis = self.get_input("What axis do you want to rotate about? \n(enter either \'x\', \'y\', or \'z\')", possible_responses)

        # asks for the angle of rotation
        possible_responses = ["90", "180", "270"]
        angle = int(self.get_input("How many degrees do you want to rotate? \n(enter either \'90\', \'180\', or \'270\')", possible_responses))

        # asks whether it's a positive or negative rotation
        possible_responses = ["positive", "negative"]
        sign = self.get_input("In the positive or negative direction? \n(enter either \'positive\' or \'negative\')", possible_responses)

        if sign == "negative":
            angle = angle * -1 

        self.cube.rotate(piece, axis, angle, "degrees")

    # rotates the entire cube
    def turn(self):

        # asks for the axis of rotation
        possible_responses = ["x", "y", "z"]
        axis = self.get_input("What axis do you want to rotate about? \n(enter either \'x\', \'y\', or \'z\')", possible_responses)

        # asks for the angle of rotation
        possible_responses = ["90", "180", "270"]
        angle = int(self.get_input("How many degrees do you want to rotate? \n(enter either \'90\', \'180\', or \'270\')", possible_responses))

        # asks whether it's a positive or negative rotation
        possible_responses = ["positive", "negative"]
        sign = self.get_input("In the positive or negative direction? \n(enter either \'positive\' or \'negative\')", possible_responses)

        if sign == "negative":
            angle = angle * -1 

        self.cube.turn(axis, angle, "degrees")

    # randomly scrambles the cube
    def scramble(self):

        # completes 100 random moves
        for x in range(100):

            piece_num = randint(1,9)
            axis = randint(1,3)
            angle = randint(1,3)
            sign = randint(1,2)

            piece = self.cube.get_face_piece(piece_num)

            # random axis of rotation of either x, y, or z
            if axis == 1:
                axis = "x"

            elif axis == 2:
                axis = "y"

            elif axis == 3:
                axis = "z"
            
            # random angle of rotation of either 90, 180, or 270 degrees
            if angle == 1:
                angle = 90

            elif angle == 2:
                angle = 180

            elif angle == 3:
                angle = 270

            # random positive or negative rotation
            if sign == 2:
                angle = angle * -1

            self.cube.rotate(piece, axis, angle, "degrees")

        os.system("cls")
        print("Cube randomized!")
        input("\n(enter anything to proceed)\n")

    # the base of the UI
    def interact_cube(self):

        possible_responses = ["cancel", "commands", "cube", "face", "quit", "references", "rotate", "scramble", "turn"]
        quit = False

        while not quit:
            os.system("cls")
            
            # controls the format of the cube that is displayed
            if self.print_type == "face":
                self.cube.print_face()

            else:
                self.cube.print_cube()

            my_input = self.get_input("What do you want to do? \n(enter \'commands\' for a list of commands)", possible_responses)
            
            # where all the various commands are called
            if my_input == "cancel":
                new_play(self)

            elif my_input == "commands":
                self.commands()

            elif my_input == "cube":
                self.print_type = "cube"

            elif my_input == "face":
                self.print_type = "face"

            elif my_input == "quit":
                quit = True

            elif my_input == "references":
                self.references()

            elif my_input == "rotate":
                self.rotate()

            elif my_input == "scramble":
                self.scramble()

            elif my_input == "turn":
                self.turn()

# driver function
def new_play(old_game):

    new_game = deepcopy(old_game)
    del old_game
    new_game.interact_cube()

new_play(PlayCube())