from objects import Raquete, Bola, bolaDir



class GameCore:
    def __init__(self, tw, th):
        self.telaWidth = tw
        self.telaHeight = th
        self.score = {
            '1': 0,
            '2': 0,
        }
        self.teclas = {
            '1': {
                'cima': 0,
                'baixo': 0
            },
            '2': {
                'cima': 0,
                'baixo': 0
            }
        }
        self.sair = False
    
    def comeca_jogo(self, bola, p1, p2):
        bola.x = self.telaWidth/2
        bola.y = self.telaHeight/2

        p1.x = 1
        p1.y = self.telaHeight/2

        p2.x = self.telaWidth - 1
        p2.y = self.telaHeight/2


def inicializa_jogo():
    global gamebola
    global raq1
    global raq2

    # Inicializa as raquetes
    raq1 = Raquete(0,0)
    raq2 = Raquete(0,0)

    # Inicializa a bola
    gamebola = Bola(0,0)
    return



