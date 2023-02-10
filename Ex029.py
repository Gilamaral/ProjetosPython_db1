velocidade = float(input('Qual a velocidade do veículo? '))
if velocidade > 80:
    print('\033[1;31mvoce foi multado, excedeu o limite de segurança que é de \033[30;41m80km/h\033[m.') # \033[m é o comando para incluir cores no inicio e no fim de onde vc quer colorir
    multa = (velocidade-80)*7
    print('\033[1;31mVoce deve pagar uma multa de {:.2f}\033[m'.format(multa))
print('bom dia! dirija com segurança.')
