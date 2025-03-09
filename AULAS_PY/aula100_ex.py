from dados import produtos

import copy

produtos = [
	{**produto, "preco": round(produto["preco"] * 1.1, 2)}
	for produto in produtos
]

novos_produtos = copy.deepcopy(produtos)

print(*novos_produtos, sep="\n")
print()

produtos.sort(key=lambda produtos: produtos["nome"])

produtos_ordenados_por_nome = copy.deepcopy(produtos)

print(*produtos_ordenados_por_nome, sep="\n")
print()

produtos.sort(key=lambda produtos: produtos['preco'])

produtos_ordenados_por_preco = copy.deepcopy(produtos)

print(*produtos_ordenados_por_preco, sep="\n")
print()