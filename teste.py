import funcoes
import sys

erroadicionar = False

agenda = open("telefonica.csv")
nome = 'Diogo'
telefone = '11987654321'

adicionar = funcoes.adicionar(agenda,nome,telefone)

if adicionar:
	erroadicionar = True

if erroadicionar:
	sys.exit(1)
else:
	sys.exit(0)
