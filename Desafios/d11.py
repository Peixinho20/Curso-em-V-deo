'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta
 necessária para pintá-la, sabendo que cada litro de tinta, pinta uam áreaa de 2m^2. até a aula 7
'''
l = float(input('Qual a largura da sua parede em metros? '))
h = float(input('Qual a altura da sua parede em metros? '))
a = l*h
t = a/2
print('Baseado nas medidas da sua parede a área dela é {:.2f}m² e quantidade de tinta necessária será {:.2f}l'.format(a,t))