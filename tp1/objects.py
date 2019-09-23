
from enum import Enum
import random


bolaDir = {
    'stop': 0,

    'esq': 1,
    'esq_cima': 2,
    'esq_baixo': 3,

    'dir': 4,
    'dir_cima': 5,
    'dir_baixo': 6
}



# Classe da bola
class Bola:
    # Construtor
    def __init__(self, xr, yr, vel):
        self.xInicial = xr
        self.yInicial = yr
        self.x = xr
        self.y = yr
        self.direcao = bolaDir['stop']
        self.velocidade = vel
        self.coeficiente = {
            'x': 1,
            'y': 0
        }

    # Reseta a bola
    def resetar(self):
        self.x = self.xInicial
        self.y = self.yInicial
        self.direcao = bolaDir['stop']
        return

    def mover(self):
        if self.direcao == bolaDir['stop']:
            return
        if self.direcao == bolaDir['esq']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x - vel['x']
            return
        if self.direcao == bolaDir['dir']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x + vel['x']
            return

        if self.direcao == bolaDir['esq_cima']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x - vel['x']
            self.y = self.y - vel['y']
            return
        if self.direcao == bolaDir['esq_baixo']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x - vel['x']
            self.y = self.y + vel['y']
            return

        if self.direcao == bolaDir['dir_cima']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x + vel['x']
            self.y = self.y - vel['y']
            return
        if self.direcao == bolaDir['dir_baixo']:
            vel = getVel2d(self.velocidade, self.coeficiente)
            self.x = self.x + vel['x']
            self.y = self.y + vel['y']
            return
        return
    


        

# Classe da raquete
class Raquete:
    # Construtor
    def __init__(self, xr, yr, vel):
        self.xInicial = xr
        self.yInicial = yr
        self.x = xr
        self.y = yr
        self.velocidade = vel

    def resetar(self):
        self.x = self.xInicial
        self.y = self.yInicial
        return

    def moverCima(self):

        if self.y + 12 > 650:
            self.y = self.y
            return
        else:
            self.y = self.y + self.velocidade
            print(self.y)
            return

    def moverBaixo(self):

        if self.y - 12 < 0:
            self.y = self.y
            return
        else:
            self.y = self.y - self.velocidade
            return


def getVel2d(velocidade, coeficiente):
    resposta = {
        'x': velocidade * coeficiente['x'],
        'y': velocidade * coeficiente['y']
    }
    return resposta