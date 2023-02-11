import pandas as pd

# busca arquivo em excel
tabela = pd.read_excel('C:\ProjetosPython\ProjetosPython_db1\.idea\BD_Excel\Vendas.xlsx')
tabela = tabela.set_index('SKU')
print(tabela)
#seleciona linhas de uma tabela
tabela = tabela.loc[(tabela['Produto'] == 'Tablet')]
print(tabela)
#inclui e calcula dados dentro das colunas 
tabela ['valor_vendido'] = tabela ['Quantidade Vendida'] * tabela ['Preco Unitario'] 
print (tabela)
