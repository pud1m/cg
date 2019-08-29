from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from random import random

name = b'Thalles Sales'

#Variáveis globais
x = 20
y = 20
linhas = 3
colunas = 3
orthox = 800
orthoy = 800

def main():
    global orthox
    global orthoy

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutInitWindowPosition(800, 200)
    glutCreateWindow(name)
    glOrtho(0, orthox, 0, orthoy, -1, 1)

    glClearColor(0.,0.,0.,1.)
    glutDisplayFunc(display)
    glutKeyboardFunc(esc_press)

    glutMainLoop()
    return

def display():
    global x
    global y
    global linhas
    global colunas
    glClear(GL_COLOR_BUFFER_BIT)


    glPushMatrix()
    i = 1
    j = 1
    size = 150
    while i <= linhas:
        x_init = x
        while j <= colunas:
            glColor3f(random(),random(),random())
            glBegin(GL_POLYGON)
            glVertex3f(x,y,0)
            glVertex3f(x+size,y,0)
            glVertex3f(x+size,y+size,0)
            glVertex3f(x,y+size,0)
            glEnd()
            j = j + 1
            x = x + 200
        
        y = y + 200
        x = x_init
        i = i + 1
        j = 1


    glFlush()
    glPopMatrix()
    glutSwapBuffers()
    return
ESC = as_8_bit( '\033' )
def esc_press(*args):
    if args[0] == ESC:
        exit()

if __name__ == '__main__': main()