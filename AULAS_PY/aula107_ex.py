# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def zip(l1, l2):
	if len(l1) > len(l2):
		zipped = [(l1[i], l2[i]) for i in range(len(l2))]
		return zipped
	zipped = [(l1[i], l2[i]) for i in range(len(l1))]
	return zipped

file = zip(lista_1, lista_2)

print(*file, sep="\n")