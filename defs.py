def color(texto, cor):
    if cor == 'red':
        return f'\033[31m{texto}\033[m'
    if cor == 'green':
        return f'\033[32m{texto}\033[m'
    if cor == 'yellow':
        return f'\033[33m{texto}\033[m'


def banco_plvr(texto):
    with open('maste_palavras.txt', 'r+') as arq:
        palavras = arq.read()
        if f'{texto}\n' not in palavras:
            arq.write(f'{texto}\n')
