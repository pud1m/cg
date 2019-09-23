from objects import Bola, bolaDir, Raquete




def colidiu_com_raquete(raq, gamebola, tamanho_raq):
    if raq.y < gamebola.y < raq.y + tamanho_raq['y']:
        return True
    else:
        return False


def handle_colisao(raq, gamebola, tamanho_raq, orthox, orthoy, tamanho_bola, call):
    print('=============================================================')
    ############
    # bola na esquerda
    if call == 'side':
        if gamebola.direcao == 1 or gamebola.direcao == 2 or gamebola.direcao == 3:
            if gamebola.y - tamanho_bola > raq.y - tamanho_raq['y']/2: # bateu na metade superior da raquete

                pos_rel = raq.y - gamebola.y
                if pos_rel <= 0:
                    coeficiente_relativo = 1
                else:
                    coeficiente_relativo = 1/pos_rel

                vy = 1/coeficiente_relativo

                gamebola.direcao = 5
                gamebola.coeficiente['y'] = vy
                return

            if gamebola.y - tamanho_bola == raq.y - tamanho_raq['y']/2: # bateu no meio exato da raquete
                gamebola.direcao = 4
                return

            if gamebola.y - tamanho_bola < raq.y - tamanho_raq['y']/2: # bateu na metade inferior da raquete

                pos_rel = (gamebola.y - raq.y)*(-1)
                if pos_rel <= 0:
                    coeficiente_relativo = 1
                else:
                    coeficiente_relativo = 1/pos_rel

                vy = 1/coeficiente_relativo

                gamebola.direcao = 6
                gamebola.coeficiente['y'] = vy
                return


    ############
    # bola na direita
        elif gamebola.direcao == 4 or gamebola.direcao == 5 or gamebola.direcao == 6:
            if gamebola.y + tamanho_bola > raq.y + tamanho_raq['y']/2: # bateu na metade superior da raquete

                pos_rel = raq.y - gamebola.y
                if pos_rel <= 0:
                    coeficiente_relativo = 1
                else:
                    coeficiente_relativo = 1/pos_rel

                vy = 1/coeficiente_relativo

                gamebola.direcao = 2
                gamebola.coeficiente['y'] = vy
                return

            if gamebola.y + tamanho_bola == raq.y + tamanho_raq['y']/2: # bateu no meio exato da raquete
                gamebola.direcao = 1
                return

            if gamebola.y + tamanho_bola < raq.y + tamanho_raq['y']/2: # bateu na metade inferior da raquete

                pos_rel = (gamebola.y - raq.y)*(-1)
                if pos_rel <= 0:
                    coeficiente_relativo = 1
                else:
                    coeficiente_relativo = 1/pos_rel

                vy = 1/coeficiente_relativo

                gamebola.direcao = 3
                gamebola.coeficiente['y'] = vy
                return
    
    ############
    # bola no topo
    if call == 'top':
        if gamebola.direcao == 2:
            gamebola.direcao = 3
            return
        if gamebola.direcao == 5:
            gamebola.direcao = 6
            return    
    
    ############
    # bola em baixo
    if call == 'bottom':
        if gamebola.direcao == 3:
            gamebola.direcao = 2
            return
        if gamebola.direcao == 6:
            gamebola.direcao = 5
            return
