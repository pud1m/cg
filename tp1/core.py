from objects import Raquete, Bola, bolaDir



class GameCore:
    def __init__(self):
        self.score = {
            '1': 0,
            '2': 0,
        }
        self.sets = {
            '1': 0,
            '2': 0,
        }
        self.deuce = False
        self.pausado = False
        self.numOfSets = 5
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
    
    def score(self, playerFor, playerAgainst):
        if int(self.score[str(playerFor)]) == 9 and int(self.score[str(playerAgainst)]) == 10:
            self.deuce = True
            add_score(playerFor)
            return

        if self.deuce:
            


    def add_score(self, player):
        self.score[str(player)] = int(self.score[str(player)]) + 1
        return

    def add_set(self, player):
        self.sets[str(player)] = int(self.sets[str(player)]) + 1
        return
