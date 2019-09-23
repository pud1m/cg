from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from random import random
from objects import Bola, bolaDir, Raquete
from core import inicializa_jogo
from pynput.mouse import Button, Controller
import sys


name = b'Thalles Sales - Pong'

#Variáveis globais
x = 20
y = 20
linhas = 3
colunas = 3
orthox = 1200
orthoy = 800
tamanho_bola = 30
tamanho_raquete = {
    'x': 50,
    'y': 150
}
print('iniciando')
# Inicializa as raquetes
raq1 = Raquete(5,0)
raq2 = Raquete(orthox-5-tamanho_raquete['x'],0)

# Inicializa a bola
gamebola = Bola(orthox/2,(orthoy)/2)

# Dict com os botões pressionados
botoes = {
    'w': False,
    's': False,
    '1': False,
    '0': False,
}



def main():
    global orthox
    global orthoy

    mouse = Controller()
    mouse.position = (1200, 400)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(orthox,orthoy)
    glutInitWindowPosition(800, 100)
    glutCreateWindow(name)
    glOrtho(0, orthox, 0, orthoy, -1, 1)
    glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)

    glClearColor(0.,0.,0.,1.)
    glutDisplayFunc(desenha_cena)
    glutKeyboardFunc(key_press)
    glutKeyboardUpFunc(key_up)


    glutMainLoop()
    return
    

#####################################
# Desenhadores
def desenha_cena():
    global x
    global y
    global gamebola
    global raq1
    global raq2
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()

    glColor3f(1, 1, 1)

    #Desenha
    atualiza_pos_raq()
    desenha_bola()

    desenha_raquete(raq1)
    desenha_raquete(raq2)

    glFlush()
    glPopMatrix()
    glutSwapBuffers()
    return


def desenha_bola():
    global tamanho_bola
    global gamebola

    px = gamebola.x
    py = gamebola.y

    glBegin(GL_POLYGON)
    glVertex3f(px, py, 0)
    glVertex3f(px, py+tamanho_bola, 0)
    glVertex3f(px+tamanho_bola, py+tamanho_bola, 0)
    glVertex3f(px+tamanho_bola, py, 0)
    glEnd()
    return


def desenha_raquete(raq):
    global tamanho_raquete

    px = raq.x
    py = raq.y

    print('render raquete')
    print(px)
    print(py)

    glBegin(GL_POLYGON)
    glVertex3f(px, py, 0)
    glVertex3f(px, py+tamanho_raquete['y'], 0)
    glVertex3f(px+tamanho_raquete['x'], py+tamanho_raquete['y'], 0)
    glVertex3f(px+tamanho_raquete['x'], py, 0)
    glEnd()
    return

#####################################
# Controles
ESC = as_8_bit( '\033' )
W = as_8_bit('\167')
S = as_8_bit('\163')
zero = as_8_bit('\060')
um = as_8_bit('\061')
def key_press(bkey, x, y):
    global botoes

    key = bkey.decode('UTF-8')

    if key == chr(27):  # Sair
        exit()

    if key == 'w':    # P1 up
        print('w')
        botoes['w'] = True
    if key == 's':    # P1 down
        print('s') 
        botoes['s'] = True

    if key == '1': # P2 up
        print('1') 
        botoes['1'] = True  
    if key == '0':   # P2 down
        print('0')
        botoes['0'] = True
    sys.stdout.flush()

    mouse = Controller()
    mouse.position = (1200, 400)


    return

def key_up(bkey, x, y):
    global botoes

    key = bkey.decode('UTF-8')

    if key == 'w':   # P1 up
        print('w up')
        botoes['w'] = False
    if key == 's':     # P1 down
        print('s up') 
        botoes['s'] = False

    if key == '1': # P2 up
        print('1 up') 
        botoes['1'] = False  
    if key == '0':   # P2 down
        print('0 up')
        botoes['0'] = False
    sys.stdout.flush()
    return


#####################################
# Handler para as raquetes

def atualiza_pos_raq():
    global raq1
    global raq2
    global botoes

    print('atualizando pos')

    if botoes['w']:
        raq1.moverCima()
    if botoes['s']:
        raq1.moverBaixo()
    if botoes['1']:
        raq2.moverCima()
    if botoes['0']:
        raq2.moverBaixo()
    
    mouse = Controller()
    mouse.position = (1200, 400)
    mouse.click(Button.left, 1)

    return


#####################################
# Handler para a bola

def atualiza_pos_bola(valor):
    global gamebola

    if gamebola.direcao == 0:
        gamebola.direcao = 4
    gamebola.mover()

if __name__ == '__main__': main()