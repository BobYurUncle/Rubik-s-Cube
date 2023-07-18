"""
RubiksCube

- A program that implements a rubiks cube through the Pieces object and the Cube object
- Directions of positive rotation are defined by applying the right hand rule on an axis of rotation
- Converting Coordinate System to Index Values
    x coordinate value + 1 = x index value
    y coordinate value * -1 + 1 = y index value
- References:
    Helpful guideline - https://github.com/pglass/cube
    Rubiks cube layout - https://ruwix.com/the-rubiks-cube/japanese-western-color-schemes/
    Using Matplotlib to draw - https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python/#

"""

from math import pi
from Matrix import matrix_mul
from RotationMatrices import rotate_x_matrix, rotate_y_matrix, rotate_z_matrix

"""
Piece Class

"""

class Piece:

    def __init__(self, pos, colors):
        self.pos = pos
        self.colors = colors

    # rotates a piece by multiplying the position matrix by a rotation matrix and swapping the color values that are NOT on the axis of rotation
    def rotate(self, axis, angle):
        
        # swapping colors is only necessary when the angle of rotation is not a multiple of an 180 degree or pi radians rotation 
        swap = not (angle / pi).is_integer()  

        if axis == "x":
            self.pos = matrix_mul(self.pos, rotate_x_matrix(angle))

            if swap:
                self.colors = [self.x_color(), self.z_color(), self.y_color()]

        elif axis == "y":
            self.pos = matrix_mul(self.pos, rotate_y_matrix(angle))

            if swap:
                self.colors = [self.z_color(), self.y_color(), self.x_color()]

        elif axis == "z":
            self.pos = matrix_mul(self.pos, rotate_z_matrix(angle))

            if swap:
                self.colors = [self.y_color(), self.x_color(), self.z_color()]

        else:
            Exception("Inputted an invalid axis") 

    # needs to be indexed twice as the self.pos is a matrix, which is implemented by a two-dimensional list
    def x(self):
        return self.pos[0][0]
    
    def y(self):
        return self.pos[1][0]
    
    def z(self):
        return self.pos[2][0]
    
    def x_color(self):
        return self.colors[0]
    
    def y_color(self):
        return self.colors[1]
    
    def z_color(self):
        return self.colors[2]
    
    # lists out important information of a piece
    def print_info(self):

        print("Position: (" + str(self.x()) + ", " + str(self.y()) + ", " + str(self.z()) + ")")
        print("Colors: (" + str(self.x_color()) + ", " + str(self.y_color()) + ", " + str(self.z_color()) + ")")


# a rubiks cube has 6 faces, 8 corner pieces, 12 side pieces, and 6 faces pieces
class Cube:

    def __init__(self):
        self.pieces = []
        self.init_cube()

    # manually adding all the pieces of the cube
    def init_cube(self):

        # corner pieces
        self.pieces.append(Piece([[1],[1],[1]], ["red","white","blue"]))
        self.pieces.append(Piece([[1],[1],[-1]], ["red","white","green"]))
        self.pieces.append(Piece([[1],[-1],[1]], ["red","yellow","blue"]))
        self.pieces.append(Piece([[1],[-1],[-1]], ["red","yellow","green"]))
        self.pieces.append(Piece([[-1],[1],[1]], ["orange","white","blue"]))
        self.pieces.append(Piece([[-1],[1],[-1]], ["orange","white","green"]))
        self.pieces.append(Piece([[-1],[-1],[1]], ["orange","yellow","blue"]))
        self.pieces.append(Piece([[-1],[-1],[-1]], ["orange","yellow","green"]))

        # side pieces
        self.pieces.append(Piece([[0],[1],[-1]], ["empty","white","green"]))
        self.pieces.append(Piece([[0],[-1],[-1]], ["empty","yellow","green"]))
        self.pieces.append(Piece([[0],[1],[1]], ["empty","white","blue"]))
        self.pieces.append(Piece([[0],[-1],[1]], ["empty","yellow","blue"]))
        self.pieces.append(Piece([[1],[0],[-1]], ["red","empty","green"]))
        self.pieces.append(Piece([[-1],[0],[-1]], ["orange","empty","green"]))
        self.pieces.append(Piece([[1],[0],[1]], ["red","empty","blue"]))
        self.pieces.append(Piece([[-1],[0],[1]], ["orange","empty","blue"]))
        self.pieces.append(Piece([[1],[1],[0]], ["red","white","empty"]))
        self.pieces.append(Piece([[1],[-1],[0]], ["red","yellow","empty"]))
        self.pieces.append(Piece([[-1],[1],[0]], ["orange","white","empty"]))
        self.pieces.append(Piece([[-1],[-1],[0]], ["orange","yellow","empty"]))

        # face pieces
        self.pieces.append(Piece([[0],[0],[1]], ["empty","empty","blue"]))
        self.pieces.append(Piece([[0],[0],[-1]], ["empty","empty","green"]))
        self.pieces.append(Piece([[1],[0],[0]], ["red","empty","empty"]))
        self.pieces.append(Piece([[-1],[0],[0]], ["orange","empty","empty"]))
        self.pieces.append(Piece([[0],[1],[0]], ["empty","white","empty"]))
        self.pieces.append(Piece([[0],[-1],[0]], ["empty","yellow","empty"]))

    # prints the face of the cube that is at z = -1
    def print_face(self):

        # ordering the pieces into their proper positions as self.pieces is unordered
        face = [[0,0,0],[0,0,0],[0,0,0]]
        index = 0
        n = 0

        while n != 9:
            curr_piece = self.pieces[index]

            if curr_piece.z() == -1:
                col_index = curr_piece.x() + 1
                row_index = curr_piece.y() * -1 + 1
                face[col_index][row_index] = curr_piece.z_color()
                n += 1
 
            index += 1

        # prints out the "front" face of a rubiks cube in a formatted way
        print("Rubik's Cube:")

        for r in range(3):
            print("----------------------------")
            print("|        |        |        |")
            line = "|"

            for c in range(3):
                curr_piece_color = face[c][r]
                num_spaces = 7 - len(curr_piece_color)
                line += " " + curr_piece_color

                for n in range(num_spaces):
                    line += " "

                line += "|"

            print(line)
            print("|        |        |        |")
            
        print("----------------------------")

    # prints out all faces of the rubix cube in a format that is simpler than print_face()
    def print_cube(self):
            
        # gets all faces of the rubiks cube by saving the front state of the cube and rotating it to access all sides
        front = self.get_face()
        self.turn("x", 90, "degrees")
        top = self.get_face()
        self.turn("x", 90, "degrees")
        back = self.get_face()
        self.turn("x", 90, "degrees")
        bottom = self.get_face()
        self.turn("x", 90, "degrees")
        self.turn("y", 90, "degrees")
        left = self.get_face()
        self.turn("y", 180, "degrees")
        right = self.get_face()
        self.turn("y", 90, "degrees")

        # printing the top row (includes a space and the top face)
        print("Rubik's Cube:")
        line = ""
        print("        ---------")

        for r in range(3):

            line += "        "
            line += "| "

            for c in range(3):
                line += top[c][r] + " " 

            line += "| "
            print(line)
            line = ""

        print("---------------------------------")
        line = ""
        
        # printing the middle row (includes the left, front, right, and back faces)
        for r in range(3):
            line += "| "

            for c in range(3):
                line += left[c][r] + " "

            line += "| "
            
            for c in range(3):
                line += front[c][r] + " "

            line += "| "

            for c in range(3):
                line += right[c][r] + " "

            line += "| "

            for c in range(3):
                line += back[c][r] + " "
                
            line += "| "
            print(line)
            line = ""

        print("---------------------------------")
        
        # printing the last row (includes a space and the bottom face)
        line = ""
        for r in range(3):
            line += "        "
            line += "| "

            for c in range(3):
                line += bottom[c][r] + " " 

            line += "| "   
            print(line)    
            line = "" 

        print("        ---------")

    # returns the front face of the cube as a two dimensional list
    def get_face(self):

        face = [[],[],[]]
        index = 1

        for r in range(3):

            for c in range(3):
                face[c].append(self.get_face_piece(index).z_color()[0])
                index += 1

        return face

    # used to retrieve pieces from the front face based on number between 1 through 9
    def get_face_piece(self, piece_num):

        if piece_num == 1:

            pos = (-1, 1)

        elif piece_num == 2:
            pos = (0, 1)

        elif piece_num == 3:
            pos = (1, 1)

        elif piece_num == 4:
            pos = (-1, 0)
            
        elif piece_num == 5:
            pos = (0, 0)

        elif piece_num == 6:
            pos = (1, 0)

        elif piece_num == 7:
            pos = (-1, -1)

        elif piece_num == 8:
            pos = (0, -1)

        elif piece_num == 9:
            pos = (1, -1)

        for p in self.pieces:

            p_pos = (p.x(), p.y())

            if p_pos == pos and p.z() == -1:
                return p    

    # rotates a 3 x 3 portion of the cube
    def rotate(self, piece, axis, angle, units = "radians"):

        # converting degrees to radians
        if units != "radians":
            angle = angle / 180 * pi

        # rotating only the pieces that share the same axis value (based on the axis of rotation) as the chosen piece
        for p in self.pieces:   
            
            if (axis == "x" and piece.x() == p.x()) or (axis == "y" and piece.y() == p.y()) or (axis == "z" and piece.z() == p.z()):
                p.rotate(axis, angle)

    # rotates all pieces in the cube
    def turn(self, axis, angle, units = "radians"):

        # converting degrees to radians
        if units != "radians":
            angle = angle / 180 * pi

        # rotating every single piece of the cube
        for x in self.pieces:
            x.rotate(axis, angle)
