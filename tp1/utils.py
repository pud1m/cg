


def centraliza_tela(screen, orthox, orthoy):
    
    padding_x = (screen['x'] - orthox)/2
    padding_y = (screen['y'] - orthoy)/2

    padding = {
        'x': int(padding_x),
        'y': int(padding_y)
    }
    return padding