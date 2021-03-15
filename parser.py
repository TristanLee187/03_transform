from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname,'r')
    commands = list(map(str.split,file.readlines()))
    file.close()
    i=0
    while i<len(commands):
        command=commands[i][0]
        if command=='line':
            i+=1
            add_edge(points,*list(map(int,commands[i])))
        elif command=='ident':
            ident(transform)
        elif command=='scale':
            i+=1
            scale=make_scale(*list(map(int,commands[i])))
            matrix_mult(scale,transform)
        elif command=='move':
            i+=1
            translate=make_translate(*list(map(int,commands[i])))
            matrix_mult(translate,transform)
        elif command=='rotate':
            i+=1
            axis,theta=commands[i]
            theta=int(theta)
            if axis=='x':
                rotate=make_rotX(theta)
                matrix_mult(rotate,transform)
            elif axis=='y':
                rotate=make_rotY(theta)
                matrix_mult(rotate,transform)
            else:
                rotate=make_rotZ(theta)
                matrix_mult(rotate,transform)
        elif command=='apply':
            matrix_mult(transform,points)
        elif command=='display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif command=='save':
            i+=1
            save_extension(screen,commands[i][0])
        else:
            print('Goodbye')
            break
        i+=1
