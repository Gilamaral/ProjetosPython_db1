valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: \n")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei: {v}")
print("Cheguei no final da lista.")