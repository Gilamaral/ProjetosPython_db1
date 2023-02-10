distancia = float(input('Digite a diatancia do seu destino em km: '))
'''if distancia > 200:
    print(' O valor da sua passagem e R${:.2f}'.format (distancia*0.50))
else:
    print(' O valor da sua passagem e R${:.2f}'.format(distancia * 0.45))'''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('o preço da sua passagem será R${:.2f}'.format(preco))