nome = "Vitor h"
num_letras = len(nome)
indice = 0
novo_nome = ""

while indice < num_letras:
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1

novo_nome += "*"
print(f"{novo_nome}")