'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação da trabalhos dos alunos. Faça um programa
que leia o nome dos quatros alunos e mostre a ordem sorteada. até a aula 8
'''
import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
nomes = [n1,n2,n3,n4]
random.shuffle(nomes)
print(nomes)