numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')

continuar = 's'


while True:
    num = int(
        input('digite um numero entre 0 e 5 e descubra o valor por extenso : '))
    if 0 <= num <= 5 and continuar == 's':
        print(f'o numero é {numero[num]}')
        continuar = input('deseja continuar digite [s/n]: ')
    else:
        print('Numero errado, ', end='')
    if continuar == 'n':
        break


print('fim do programa!')
