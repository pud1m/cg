from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from objects import Bola, bolaDir, Raquete
from core import GameCore
from colisao import colidiu_com_raquete, handle_colisao
from utils import centraliza_tela, set_field_size, ReadTexture, marca_placar, ReadTextureTile
from pynput.mouse import Button, Controller
from math import *


##################################################
name = b'Thalles Sales - Pong'

#Variáveis globais
tamanho_bola = 25
vel_bola = 40
vel_raquete = 30
tamanho_raquete = {
    'x': 50,
    'y': 150
}
tamanho_topbar = 100

# Tela
screen = { # Resolução do dispositivo
    'x': 1920,
    'y': 1080
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
gamebola = Bola(orthox/2,(orthoy)/2, vel_bola)

# Inicializa o GameCore
core = GameCore()

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
    global orthox
    global orthoy
    global tamanho_topbar
    
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()

    

    ############# Desenha

    # Campo
    glColor3f(1, 1, 1)
    desenha_campo()

    # Linhas no campo
    glColor3f(1, 1, 1)
    desenha_linhas()

    # Posiciona raquetes
    glColor3f(1, 1, 1)
    atualiza_pos_raq()

    # Bola
    glColor3f(1, 1, 1)
    desenha_bola()

    # Raquetes
    glColor3f(1, 1, 1)
    desenha_raquete(raq1)
    desenha_raquete(raq2)

    # Placar
    desenha_placar()

    # Texto com título dos jogadores
    if not core.switchSet:
        marca_placar(orthox*0.01, orthoy+tamanho_topbar-30, str('Jogador 1'))
        marca_placar(orthox*0.9, orthoy+tamanho_topbar-30, str('Jogador 2'))
    else:
        marca_placar(orthox*0.01, orthoy+tamanho_topbar-30, str('Jogador 2'))
        marca_placar(orthox*0.9, orthoy+tamanho_topbar-30, str('Jogador 1'))


    # Pontuação dos jogadores no set
    marca_placar(orthox*0.01, orthoy+tamanho_topbar-60, str('Pontos: ' + str(core.score['1'])))
    marca_placar(orthox*0.9, orthoy+tamanho_topbar-60, str('Pontos: ' + str(core.score['2'])))

    # Contador de sets
    marca_placar(orthox*0.01, orthoy+tamanho_topbar-90, str('Sets: ' + str(core.sets['1'])))
    marca_placar(orthox*0.9, orthoy+tamanho_topbar-90, str('Sets: ' + str(core.sets['2'])))

    # Máximo de set
    marca_placar(orthox*0.5, orthoy+tamanho_topbar-60, str('Melhor de ' + str(core.numOfSets)))

    # Indicador de deuce
    if core.deuce:
        marca_placar(orthox*0.5, orthoy+tamanho_topbar-90, str('Deuce'))
    

    glFlush()
    glPopMatrix()
    glutSwapBuffers()
    return


def desenha_bola():
    global tamanho_bola
    global gamebola
    global orthox
    global orthoy

    px = gamebola.x
    py = gamebola.y

    print('render bola')
    print(px)
    print(py)


    if px > orthox /2:
        ortho_prop = px/orthox
        tamanho_custom = tamanho_bola*ortho_prop
    else:
        ortho_prop = (orthox-px)/orthox
        tamanho_custom = tamanho_bola*ortho_prop



    tid = ReadTexture(None, 'bola.jpg')

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    lados = 32    
    glBegin(GL_POLYGON)    
    for i in range(200):    
        va = tamanho_custom * cos(i*2*pi/lados) + px    
        vb = tamanho_custom * sin(i*2*pi/lados) + py    
        glVertex3f(va,vb,0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    return


def desenha_placar():
    global orthox
    global orthoy
    global tamanho_topbar

    tid = ReadTextureTile(None, 'wood_low.jpg')
    
    
    glBindTexture(GL_TEXTURE_2D, tid)
    #glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)


    glBegin(GL_POLYGON)
    glVertex3f(0, orthoy+tamanho_topbar, 0)
    glVertex3f(orthox, orthoy+tamanho_topbar, 0)
    glVertex3f(orthox, orthoy, 0)
    glVertex3f(0, orthoy, 0)
    glEnd()

    #glDisable(GL_TEXTURE_2D)
    return


def desenha_campo():
    global orthox
    global orthoy
    global tamanho_topbar

    
    tid = ReadTexture(None, 'grass2.jpg')

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)


    glBegin(GL_POLYGON)

    glVertex3f(0, orthoy, 0)
    glVertex3f(orthox, orthoy, 0)
    glVertex3f(orthox, 0, 0)
    glVertex3f(0, 0, 0)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    return


def desenha_linhas():
    global orthox
    global orthoy

    # Topo
    glBegin(GL_POLYGON)
    glVertex3f(100, orthoy-100, 0)
    glVertex3f(orthox-100, orthoy-100, 0)
    glVertex3f(orthox-100, orthoy-110, 0)
    glVertex3f(100, orthoy-110, 0)
    glEnd()

    # Baixo
    glBegin(GL_POLYGON)
    glVertex3f(100, 100, 0)
    glVertex3f(orthox-100, 100, 0)
    glVertex3f(orthox-100, 110, 0)
    glVertex3f(100, 110, 0)
    glEnd()

    # Esquerda
    glBegin(GL_POLYGON)
    glVertex3f(100, orthoy-100, 0)
    glVertex3f(110, orthoy-100, 0)
    glVertex3f(110, 100, 0)
    glVertex3f(100, 100, 0)
    glEnd()

    # Direita
    glBegin(GL_POLYGON)
    glVertex3f(orthox-110, orthoy-100, 0)
    glVertex3f(orthox-100, orthoy-100, 0)
    glVertex3f(orthox-100, 100, 0)
    glVertex3f(orthox-110, 100, 0)
    glEnd()

    # Esquerda centro
    glBegin(GL_POLYGON)
    glVertex3f(orthox/2-orthox/4, orthoy-100, 0)
    glVertex3f(orthox/2-orthox/4+10, orthoy-100, 0)
    glVertex3f(orthox/2-orthox/4+10, 100, 0)
    glVertex3f(orthox/2-orthox/4, 100, 0)
    glEnd()

    # Direita centro
    glBegin(GL_POLYGON)
    glVertex3f(orthox/2+orthox/4, orthoy-100, 0)
    glVertex3f(orthox/2+orthox/4+10, orthoy-100, 0)
    glVertex3f(orthox/2+orthox/4+10, 100, 0)
    glVertex3f(orthox/2+orthox/4, 100, 0)
    glEnd()

    # Linha do meio
    glBegin(GL_POLYGON)
    glVertex3f(orthox/2-orthox/4, orthoy/2-5, 0)
    glVertex3f(orthox/2+orthox/4, orthoy/2-5, 0)
    glVertex3f(orthox/2+orthox/4, orthoy/2+5, 0)
    glVertex3f(orthox/2-orthox/4, orthoy/2+5, 0)
    glEnd()

    return


def desenha_raquete(raq):
    global tamanho_raquete

    px = raq.x
    py = raq.y

    tid = ReadTexture(None, 'wood_low.jpg')

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    
    glBegin(GL_POLYGON)
    glVertex3f(px, py, 0)
    glVertex3f(px, py+tamanho_raquete['y'], 0)
    glVertex3f(px+tamanho_raquete['x'], py+tamanho_raquete['y'], 0)
    glVertex3f(px+tamanho_raquete['x'], py, 0)
    glEnd()


    glDisable(GL_TEXTURE_2D)
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
    global core
    
    ################################################
    ####### Colisão com a raquete
    # Esquerda/direita
    if 0 < gamebola.x <= tamanho_raquete['x']*1.2: # bola na esquerda
        if colidiu_com_raquete(raq1, gamebola, tamanho_raquete):
            if gamebola.direcao == 1 or gamebola.direcao == 2 or gamebola.direcao == 3:
                handle_colisao(raq1, gamebola, tamanho_raquete, orthox, orthoy, tamanho_bola, 'side')
                return
        
    if orthox - tamanho_raquete['x']*1.2 - tamanho_bola < gamebola.x + tamanho_bola >= orthox - tamanho_raquete['x']*1.2: # bola na direita
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
        core.playerScored(2,1)

    
    if gamebola.x >= orthox: # Bola na direita
        gamebola.resetar()
        gamebola.direcao = 1
        core.playerScored(1,2)

    return










# Força o loop    
if __name__ == '__main__': main()