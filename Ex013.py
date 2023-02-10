salario = float(input('Qual o salario do funcionário? R$'))
aum = (salario * 15/100)
nsalario = salario + aum

print('Um funcionario que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario,nsalario))
print('seu aumento foi de R${:.2f}'.format(aum))

