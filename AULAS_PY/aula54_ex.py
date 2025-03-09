import os
lista = []

while True:
    edit = input("Digite [I] para inserir [R] para remover e [L] para listar: ").lower()

    if len(edit) > 1:
        print("Digite apenas um digito")
        continue
    elif edit == "i":
        os.system("cls")
        inserir = input("Item: ")
        lista.append(inserir)
    elif edit == "r":
        
        try:
            remover = int(input("indice: "))
            removido = lista.pop(remover)
        except:
            print("Indice inválido")

    elif edit == "l":
        os.system("cls")

        if len(lista) == 0:
            print("Nem um produto cadastrado")

        for indice, produto in enumerate(lista):
            print(indice, produto)
    else:
        print("Valor Inválido")