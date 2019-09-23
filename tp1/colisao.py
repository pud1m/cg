from objects import Bola, bolaDir, Raquete




def colidiu_com_raquete(raq, gamebola, tamanho_raq):
    if raq.y < gamebola.y < raq.y + tamanho_raq['y']:
        return True
    else:
        return False


def handle_colisao(raq, gamebola, tamanho_raq, orthox, orthoy, tamanho_bola):
    print('=============================================================')
    ############
    # bola na esquerda
    if gamebola.direcao == 1: 
        if gamebola.y - tamanho_bola/2 > raq.y - tamanho_raq['y']/2: # bateu na metade superior da raquete

            pos_rel = raq.y - gamebola.y
            if pos_rel <= 0:
                coeficiente_relativo = 1
            else:
                coeficiente_relativo = 1/pos_rel

            vy = 1/coeficiente_relativo

            raq.direcao = 5
            gamebola.coeficiente['y'] = vy
            return

        if gamebola.y - tamanho_bola/2 == raq.y - tamanho_raq['y']/2: # bateu no meio exato da raquete
            raq.direcao = 4
            return

        if gamebola.y - tamanho_bola/2 < raq.y - tamanho_raq['y']/2: # bateu na metade inferior da raquete

            pos_rel = (gamebola.y - raq.y)*(-1)
            if pos_rel <= 0:
                coeficiente_relativo = 1
            else:
                coeficiente_relativo = 1/pos_rel

            vy = 1/coeficiente_relativo

            raq.direcao = 6
            gamebola.coeficiente['y'] = vy
            return


    ############
    # bola na direita
    if gamebola.direcao == 4:
        if gamebola.y - tamanho_bola/2 > raq.y - tamanho_raq['y']/2: # bateu na metade superior da raquete
            print('=============================================================Metade superior')

            pos_rel = raq.y - gamebola.y
            if pos_rel <= 0:
                coeficiente_relativo = 1
            else:
                coeficiente_relativo = 1/pos_rel

            vy = 1/coeficiente_relativo

            raq.direcao = 2
            gamebola.coeficiente['y'] = vy
            return

        if gamebola.y - tamanho_bola/2 == raq.y - tamanho_raq['y']/2: # bateu no meio exato da raquete
            print('=============================================================meio exato')
            raq.direcao = 1
            return

        if gamebola.y - tamanho_bola/2 < raq.y - tamanho_raq['y']/2: # bateu na metade inferior da raquete
            print('=============================================================Metade inferior')

            pos_rel = (gamebola.y - raq.y)*(-1)
            if pos_rel <= 0:
                coeficiente_relativo = 1
            else:
                coeficiente_relativo = 1/pos_rel

            vy = 1/coeficiente_relativo

            raq.direcao = 3
            gamebola.coeficiente['y'] = vy
            return
    
    