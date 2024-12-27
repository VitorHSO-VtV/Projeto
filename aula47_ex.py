"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "tradutor"
letras_acertadas = ""
numero_tentativas = 0

while True:
    palavra = ""
    usuario = input("Digite uma letra: ")
    
    if len(usuario) > 1:
        print("Digite apenas uma letra")
        continue

    numero_tentativas += 1

    if usuario in palavra_secreta:
        letras_acertadas += usuario

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra += letra
        else:
            palavra += "*"

    os.system("cls")

    if palavra == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

    print(palavra)