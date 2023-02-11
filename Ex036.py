# Calculo de aprovação para financiamento.
vimovel = float(input('Qual o valor do imóvel desejado? R$'))
salario = float(input('Digite seu salário atual: R$'))
prazo = float(input('Qual o prazo para pagamento em anos: '))
limite_s = salario * 30/100
prestacao = vimovel / (prazo * 12) 
if prestacao < limite_s:
    print('Parabens! seu financiamento foi aprovado!')
    print('sua prestação mensal será de R${:.2f} '.format(prestacao))
else:
    print('Financiamento recusado.')
    