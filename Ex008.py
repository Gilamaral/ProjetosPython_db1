m = float(input('Digite um numero em metros: '))
print('A medida de {}m corresponde a ')
km = m/1000
hm = m/100
dm = m*10
cm = m*100
mm = m*1000
print('{}Km \n{}hm \n{:.0f}dam \n{:.0f}cm \n{:.0f}mm'.format(km,hm,dm,cm,mm))