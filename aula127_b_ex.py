import json

from aula127_a_ex import Pessoa

if __name__ == '__main__':
    with open(Pessoa.file, 'r') as arquivo:
        pessoas = json.load(arquivo)
        p1 = Pessoa(**pessoas[0])
        p2 = Pessoa(**pessoas[1])
        p3 = Pessoa(**pessoas[2])

        print(p1.nome, p1.idade)
        print(p2.nome, p2.idade)
        print(p3.nome, p3.idade)
