import pandas

#processamento dos dados
tabela = pandas.read_excel ('C:\ProjetosPython\ProjetosPython_db1\.idea\BD_Excel\BD_pandas_python.xlsx') 
#processando valores da tabela
tabela['total'] = tabela['preco']*tabela['quantidade'] 
tabela['novo_preco'] = tabela['preco'] * 1.05
#Classificando dados
tabela = tabela.sort_values ('quantidade')
print(tabela)
tabela['teste'] = 0
print (tabela)

for linha in range(len(tabela)):
    if tabela['produto'].iloc[linha] in ['celular']:
        tabela['teste'].iloc[linha] = 'bom'
    else:
        tabela['teste'].iloc[linha] = 'ruim'
    print (linha)
print(tabela)

#atualizar resultado
tabela.to_excel('C:\ProjetosPython\ProjetosPython_db1\.idea\BD_Excel\BD_pandas_python.xlsx')

tabela.append.to_excel