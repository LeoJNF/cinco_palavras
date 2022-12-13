from random import choice
from defs import color, banco_plvr

arq = open('maste_palavras.txt')

#ESCOLHENDO A PALAVRA DO BANCO
palesc = str(choice(list(arq))).upper().strip()

arq.close()

for plv in range(6):
    if plv == 5:
        print(f'\nPerdeu.\nA palavra era {palesc}')
        break
    plvr = str(input(f'\n{plv+1}º Tentativa: ')).upper()
    if len(plvr) != 5:
        print('Palavra escolhida precisa ter 5 letras')
        while True:
            plvr = str(input(f'\n{plv + 1}º Tentativa: ')).upper()
            if len(plvr) == 5:
                break
    #Adicionando a palavra no banco caso ela não faça parte ainda
    banco_plvr(plvr.lower())
    #Comparando as palavras
    for ten in range(5):
        temoun = palesc.count(plvr[ten])
        if temoun > 0:
            p1 = plvr.find(plvr[ten])
            p2 = palesc.find(plvr[ten])
            p3 = plvr.rfind(plvr[ten])
            p4 = palesc.rfind(plvr[ten])
            if p1 == p2 and plvr[ten] == palesc[ten] or p4 == p3 and \
                    plvr[ten] == palesc[ten]:
                print(color(plvr[ten], 'green'), end=' ')
            else:
                print(color(plvr[ten], 'yellow'), end=' ')
        else:
            print(color(plvr[ten], 'red'), end=' ')
    if plvr == palesc:
        print('\nParabens!! Você acertou!!')
        break
