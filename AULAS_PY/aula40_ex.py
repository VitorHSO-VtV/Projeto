while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except:
        print("Um dos dados digitados não é um número, Tente novamente")
        continue

    operador = input("Digite um operador matemático | + | - | / | x |: ")
    operador_unico = len(operador) > 1
    operador_valido = operador not in "+-/x"

    if operador_valido
        print("Operador inválido")
    elif operador_unico:
        print("Digite apenas um operador")
        continue
    
    if operador == "+":
        result = num1 + num2
    elif operador == "-":
        result = num1 - num2
    elif operador == "/":
        result = num1 / num2
    elif operador == "x":
        result = num1 * num2
    else:
        result = f'Operador "{operador}" Inválido'

    print(f"O resultado de {num1} {operador} {num2} é {result}")
    sair = input("Digite [S] para sair: ").lower().startswith("s")

    if sair:
        break