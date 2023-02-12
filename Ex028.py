# Jogo da advinhação com o computador

from time import sleep
from random import randint
print('-=-'* 20)
print('vou pensar em um numero entre 0 e 5 tente advinhar...!')
print('-=-'* 20)
while True:
    computador = randint(0, 5)  # faz o computador pensar e sortear um numero!
    print('-'* 60)
    jogador = int(input('Em que numero pensei? ')) #Jogador tentaadvinhar
    print('processando...')
    sleep(3)
    print ('Meu numero é... {}'.format(computador))
    
    if jogador == computador:
        print('Parabens vc conseguiu me vencer!!')
    else:
        print('Ganhei! eu pensei no numero {} e voce digitou {} '.format(computador, jogador))
    print('-' * 60)
    sair = str(input('Quer jogar mais uma? s ou n? '))
    if sair == 'n':
        break


