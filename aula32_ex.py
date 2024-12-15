"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
num = input('Digite um número: ')

if num.isdigit():
    num_int = int(num)
    par_impar = num_int % 2 == 0
    txt = "impar"

    if par_impar:
        txt = "par"

    print(f"O número {num} é {txt}")

else:
    print("Você não digitou um número inteiro")
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
time = input("Que horas são? ")

if time.isdigit():
    time_int = int(time)
    manha = 0 <= time_int <= 11
    tarde = 12 <= time_int <= 17
    noite = 17 <= time_int <= 23

    if manha:
        print("Bom dia")
    elif tarde:
        print("Boa tarde")
    elif noite:
        print("Boa Noite")
    else:
        print("Horário inválido")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

"""
pri_nome = input("Digite seu primeiro nome: ")
num_letras = len(pri_nome)
curto = num_letras <= 4
normal = 5 <= num_letras <= 6

if curto:
    print("Seu nome é curto")
elif normal:
    print("Seu nome é normal")
else:
    print("Seu nome é longo")
"""