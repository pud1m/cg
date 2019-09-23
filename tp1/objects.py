
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
    def __init__(self, xr, yr):
        self.xInicial = xr
        self.yInicial = yr
        self.x = xr
        self.y = yr
        self.direcao = bolaDir['stop']

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
            self.x = self.x - 1
            return
        if self.direcao == bolaDir['dir']:
            self.x = self.x + 1
            return

        if self.direcao == bolaDir['esq_cima']:
            self.x = self.x - 1
            self.y = self.y - 1
            return
        if self.direcao == bolaDir['esq_baixo']:
            self.x = self.x - 1
            self.y = self.y + 1
            return

        if self.direcao == bolaDir['dir_cima']:
            self.x = self.x + 1
            self.y = self.y - 1
            return
        if self.direcao == bolaDir['dir_baixo']:
            self.x = self.x + 1
            self.y = self.y + 1
            return
        return
        

# Classe da raquete
class Raquete:
    # Construtor
    def __init__(self, xr, yr):
        self.xInicial = xr
        self.yInicial = yr
        self.x = xr
        self.y = yr

    def resetar(self):
        self.x = self.xInicial
        self.y = self.yInicial
        return

    def moverCima(self):

        if self.y + 12 > 650:
            self.y = self.y
            return
        else:
            self.y = self.y + 10
            print(self.y)
            return

    def moverBaixo(self):

        if self.y - 12 < 0:
            self.y = self.y
            return
        else:
            self.y = self.y - 10
            return