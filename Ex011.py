larg = float(input('Qual a largura da sua parede em metros? '))
alt = float(input('Qual a altura da sua parede em metros? '))
area = larg * alt
material = area / 2
print('sua parede tem as dimensões de {}x{} e a ára de {}mt² ' .format(larg,alt,area))
print('Para pintar sua parede vc precisará de {}lt de tinta ' .format(material))
