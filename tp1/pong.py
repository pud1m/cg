from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from objects import Bola, bolaDir, Raquete
from core import inicializa_jogo
from colisao import colidiu_com_raquete, handle_colisao
from utils import centraliza_tela, set_field_size, ReadTexture
from pynput.mouse import Button, Controller
from math import *


##################################################
name = b'Thalles Sales - Pong'

#Variáveis globais
tamanho_bola = 15
vel_bola = 1
vel_raquete = 8
tamanho_raquete = {
    'x': 50,
    'y': 150
}
tamanho_topbar = 100

# Tela
screen = { # Resolução do dispositivo
    'x': 1366,
    'y': 768
}

# Campo
orthox = 10
orthoy = 10

orthos = set_field_size(screen, tamanho_topbar)
orthox = orthos['x']
orthoy = orthos['y']

print('iniciando')
# Inicializa as raquetes
raq1 = Raquete(5,0, vel_raquete)
raq2 = Raquete(orthox-5-tamanho_raquete['x'],0, vel_raquete)

# Inicializa a bola
gamebola = Bola(orthox/2,(orthoy)/2, 5)

# Dict com os botões pressionados
botoes = {
    'w': False,
    's': False,
    '1': False,
    '0': False,
}
##################################################


def main():
    global orthox
    global orthoy
    global screen
    global tamanho_topbar

    mouse = Controller()
    mouse.position = (1200, 400)
    sc = centraliza_tela(screen, orthox, orthoy+tamanho_topbar)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(orthox,orthoy+tamanho_topbar)
    glutInitWindowPosition(sc['x'], 0)
    glutCreateWindow(name)
    glOrtho(0, orthox, 0, orthoy+tamanho_topbar, -1, 1)
    glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)

    glClearColor(0.,0.,0.,1.)
    glutDisplayFunc(desenha_cena)
    glutKeyboardFunc(key_press)
    glutKeyboardUpFunc(key_up)
    glutTimerFunc(10,atualiza_pos_bola, 1)

    glutMainLoop()
    return
    

#####################################
# Desenhadores
def desenha_cena():
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
    desenha_placar()

    glFlush()
    glPopMatrix()
    glutSwapBuffers()
    return


def desenha_bola():
    global tamanho_bola
    global gamebola

    px = gamebola.x
    py = gamebola.y

    print('render bola')
    print(px)
    print(py)


    lados = 32    
    glBegin(GL_POLYGON)    
    for i in range(100):    
        va = tamanho_bola * cos(i*2*pi/lados) + px    
        vb = tamanho_bola * sin(i*2*pi/lados) + py    
        glVertex3f(va,vb,0)
    glEnd()

    return


def desenha_placar():
    global orthox
    global orthoy
    global tamanho_topbar

    tid = ReadTexture(None, 'stone.png')

    glBindTexture(GL_TEXTURE_2D, tid)
    glBegin(GL_POLYGON)
    glVertex3f(0, orthoy+tamanho_topbar, 0)
    glVertex3f(orthox, orthoy+tamanho_topbar, 0)
    glVertex3f(orthox, orthoy, 0)
    glVertex3f(0, orthoy, 0)
    glEnd()
    return


def desenha_raquete(raq):
    global tamanho_raquete

    px = raq.x
    py = raq.y

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
    global orthoy
    global tamanho_topbar
    global tamanho_raquete
    global botoes

    print('atualizando pos')

    if botoes['w']:
        raq1.moverCima(orthoy-tamanho_topbar, tamanho_raquete['y'])
    if botoes['s']:
        raq1.moverBaixo(0, tamanho_raquete['y'])
    if botoes['1']:
        raq2.moverCima(orthoy-tamanho_topbar, tamanho_raquete['y'])
    if botoes['0']:
        raq2.moverBaixo(0, tamanho_raquete['y'])
    
    mouse = Controller()
    mouse.position = (1200, 400)
    mouse.click(Button.left, 1)

    return


#####################################
# Handler para a bola

def atualiza_pos_bola(valor):
    global gamebola
    global orthox
    global orthoy

    print('***************************************************')
    print(orthox)
    print(orthoy)

    if gamebola.direcao == 0:
        gamebola.direcao = 4
    gamebola.mover()
    checa_colisao()
    glutTimerFunc(10,atualiza_pos_bola, 1)

    
#####################################
# Detecção de colisão

def checa_colisao():
    global gamebola
    global raq1
    global raq2
    global tamanho_raquete
    global tamanho_bola
    global orthox
    global orthoy
    
    ################################################
    ####### Colisão com a raquete
    # Esquerda/direita
    if 0 < gamebola.x <= tamanho_raquete['x']: # bola na esquerda
        if colidiu_com_raquete(raq1, gamebola, tamanho_raquete):
            if gamebola.direcao == 1 or gamebola.direcao == 2 or gamebola.direcao == 3:
                handle_colisao(raq1, gamebola, tamanho_raquete, orthox, orthoy, tamanho_bola, 'side')
                return
        
    if orthox - tamanho_raquete['x'] - tamanho_bola < gamebola.x + tamanho_bola >= orthox - tamanho_raquete['x']: # bola na direita
        if colidiu_com_raquete(raq2, gamebola, tamanho_raquete):
            if gamebola.direcao == 4 or gamebola.direcao == 5 or gamebola.direcao == 6:
                handle_colisao(raq2, gamebola, tamanho_raquete, orthox, orthoy, tamanho_bola, 'side')
                return

    # Topo/baixo
    if gamebola.y >= orthoy - 10:
        handle_colisao(raq1, gamebola, tamanho_raquete, orthox, orthoy, tamanho_bola, 'bottom')
        return

    if gamebola.y - 2*tamanho_bola <= 0:
        handle_colisao(raq1, gamebola, tamanho_raquete, orthox, orthoy, tamanho_bola, 'top')
        return

    ################################################
    ####### Score   
    if gamebola.x <= 0: # Bola na esquerda
        gamebola.resetar()
        gamebola.direcao = 4
    
    if gamebola.x >= orthox: # Bola na direita
        gamebola.resetar()
        gamebola.direcao = 1

    return










# Força o loop    
if __name__ == '__main__': main()