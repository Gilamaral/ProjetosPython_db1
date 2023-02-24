sexo = str(input('informe seu sexo [M/S]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos: ')).strip().upper()[0]
print('sexo {} registrado com sucesso '.format(sexo))






