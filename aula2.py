# Aula sobre a função print()
# A função print deve receber um ou mais argumentos dentro dos parenteses separados por vírgola

print(12, 34) # print(argumento1, argumento2)

# Por padrão o print mostrará no terminal os argumentos separádos por um espaço
# isso pode ser mudádo trocando a chave sep padrão do print por outra coisa

print(56, 78, sep="-") # print(argumento1, argumento2, sep='texto usado na separação dos argumentos' ou sep="texto usado na separação dos argumentos")

# A quabra de linha do print no Windows vem pelo comando \r\n que é o padrão CRLF
# Em outros sistemas baseados em unix usá-se \n que é o padrão LF

# A chave end no print muda oque é mostrado ao acabar uma linha (depois do último argumento)
# Por padrão a chave end vem como "\r\n", assim quebrando a linha
# isso pode ser mudádo trocando a chave end padrão do print por outra coisa

print(9, 10, end="-") # print(argumento1, argumento2, end='texto usado após o último argumento' ou end="texto usado após o último argumento")
print(11, 12) # print(argumento1, argumento2)