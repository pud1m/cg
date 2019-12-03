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
        self.switchSet = False
        self.storedRaqSpeed = 0
        self.storedDirection = 0
        self.winner = 0

    
    def playerScored(self, playerFor, playerAgainst):
        if int(self.score[str(playerFor)]) == 9 and int(self.score[str(playerAgainst)]) == 10:
            self.deuce = True
            self.score = {
                '1': 0,
                '2': 0
            }
            self.add_score(playerFor)
            return

        if self.deuce:
            self.add_score(playerFor)
            if int(self.score[str(playerFor)]) - int(self.score[str(playerAgainst)]) == 2:
                self.fecha_set(playerFor, playerAgainst)
            return
        

        if int(self.score[str(playerFor)]) == 10:
            self.fecha_set(playerFor, playerAgainst)
            return

        self.add_score(playerFor)
        return

            
            


    def add_score(self, player):
        self.score[str(player)] = int(self.score[str(player)]) + 1
        return

    def add_set(self, player):
        self.sets[str(player)] = int(self.sets[str(player)]) + 1
        return

    def fecha_set(self, playerFor, playerAgainst):
        self.add_set(playerFor)
        self.score = {
            '1': 0,
            '2': 0
        }
        self.deuce = False

        self.troca_lados()

        if int(self.sets[str(playerFor)]) + int(self.sets[str(playerAgainst)]) == self.numOfSets:
            self.winner = playerFor
            self.pausado = True
            return
        else:
            return

    
    def troca_lados(self):
        sets_a = self.sets['1']
        sets_b = self.sets['2']

        self.sets = {
            '1': sets_b,
            '2': sets_a
        }

        if self.switchSet:
            self.switchSet = False
        else:
            self.switchSet = True

        return

    def reset_game(self):
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
        self.switchSet = False
        self.storedRaqSpeed = 0
        self.storedDirection = 0
        self.winner = 0
        return
