while True:
    cpf_input = input("Digite seu CPF apaixo:\n ")
    cpf_trat = cpf_input \
        .replace(".", "") \
        .replace("-", "") \
        .replace(" ", "")
    
    val1 = False
    som1 = 0
    cont1 = 10

    val2 = False
    som2 = 0
    cont2 = 11

    cpf_curto = len(cpf_trat) != 11
    
    if cpf_curto:
        print("O CPF possui falta de caractéres")
        continue

    try:
        int(cpf_trat)
    except TypeError:
        print("O CPF contém caractéres inesperados")
        continue

    # calculo primeiro digito

    for i in range(9):
        num1 = cpf_trat[i]
        som1 += (int(num1) * cont1)
        cont1 -= 1

    tot1 = (som1 * 10) % 11
    tot1 = 0 if tot1 > 9 else tot1
    val1_int = int(cpf_trat[9])

    if val1_int == tot1:
        val1 = True

    print("Validação 1:", val1 if val1 else val1, tot1)

    if not val1:
        continue

    # calculo segundo digito

    for i in range(10):
        num2 = cpf_trat[i]
        som2 += (int(num2) * cont2)
        cont2 -= 1

    tot2 = (som2 * 10) % 11
    tot2 = 0 if tot2 > 9 else tot2
    val2_int = int(cpf_trat[10])

    if val2_int == tot2:
        val2 = True

    print("Validação 2:", val2 if val2 else val2, tot2)

    if val1 and val2:
        print(f"O CPF {cpf_input} é válido")