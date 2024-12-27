perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for pergunta in perguntas:
    print()
    print("Pergunta:", pergunta["Pergunta"])
    print()
    print("Opções: ")
    cont = 1

    for opcao in pergunta["Opções"]:
        print(f"{cont})", opcao)
        cont += 1

    usuario = int(input("Escolha uma opção: ")) - 1

    if pergunta['Opções'][usuario] == pergunta["Resposta"]:
        print("Acertou!!!")
        acertos += 1
        continue

    print("Errou")

tot_perguntas = len(perguntas)
print(f"Você acertou {acertos} de {tot_perguntas} perguntas")