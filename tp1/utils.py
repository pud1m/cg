from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy
from PIL import Image
import os

def centraliza_tela(screen, orthox, orthoy):
    
    padding_x = (screen['x'] - orthox)/2
    padding_y = (screen['y'] - orthoy)/2

    padding = {
        'x': int(padding_x),
        'y': int(padding_y)
    }
    return padding



def set_field_size(screen, topbar):

    x = screen['x']*0.9
    y = screen['y']*0.9

    orthox = x
    orthoy = y - topbar

    retorno = {
        'x': int(orthox),
        'y': int(orthoy)
    }

    return retorno

###############################
# Leitor de texturas retirado de: http://www.magikcode.com/?p=122
def ReadTexture(self, filename):
    # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
    # and other file types.  We convert into a texture using GL.
    print('trying to open', filename)
    try:
        caminho = os.path.join(os.getcwd(), 'tp1', filename)
        #caminho = 'C:/Users/thalles.sales/cefet/cg/tp1/stone.png'
        image = Image.open(caminho)
    except IOError as ex:
        print('IOError: failed to open texture file')
        message = 'erro'
        print(ex)
        print(message)
        return -1
    print('opened file: size=', image.size, 'format=', image.format)
    imageData = numpy.array(list(image.getdata()), numpy.uint8)

    textureID = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
        0, GL_RGB, GL_UNSIGNED_BYTE, imageData)

    image.close()
    return textureID