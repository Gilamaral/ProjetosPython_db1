import pandas as pd


tabela = pd.read_excel('C:\ProjetosPython\ProjetosPython_db1\.idea\BD_Excel\BD_pandas_python.xlsx')
tabela = tabela.set_index('produto')

#processa dados na linha da dataFrame (tabela)
tabela.loc[(tabela['teste'] == 'ruim') & (tabela['quantidade'] == 3) , 'quantidade'] = 5
print(tabela)