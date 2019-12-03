from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from objects import Bola, bolaDir, Raquete
from core import GameCore
from utils import ReadTexture, ReadTextureTile, notice_center
from math import cos, sin, pi

####################
# Funções de desenho



def desenha_notice(texto, w, orthox, orthoy):

    y = orthoy/2
    x = orthox/2
    bx = w
    by = 20

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3f(x-bx, y+2*by, 0.2)
    glVertex3f(x+2*bx, y+2*by, 0.2)
    glVertex3f(x+2*bx, y-by, 0.2)
    glVertex3f(x-bx, y-by, 0.2)
    glEnd()

    notice_center(orthox, orthoy, texto)
    return



def desenha_bola(tamanho_bola, gamebola, orthox, orthoy):

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
        glVertex3f(va,vb,0.5)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    return


def desenha_placar(orthox, orthoy, tamanho_topbar):

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


def desenha_campo(orthox, orthoy, tamanho_topbar):
    
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


def desenha_linhas(orthox, orthoy):

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


def desenha_raquete(raq, tamanho_raquete):

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