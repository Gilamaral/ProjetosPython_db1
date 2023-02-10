produto = float(input('Qual o preço d produto? '))
desc = 0.95
vfinal = produto * desc
desconto = (produto * 5/100)
print('O valo do priduto custava R${:.2f} na promoção com desconto de 5% vai custar R${:.2f} '.format(produto,vfinal))
print('O valor do desconto é R${:.2f} '.format (desconto))
