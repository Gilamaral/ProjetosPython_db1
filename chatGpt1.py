import pandas as pd

# Cria um DataFrame de exemplo
df = pd.DataFrame({
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [25, 30, 40],
    "Sexo": ["M", "F", "M"]
})

# Transforma o DataFrame em uma lista de dicionários
lista = df.to_dict("records")

print(lista)
