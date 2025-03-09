# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Pessoa:
    file = 'aula127_ex.json'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def save(self):
        try:
            with open(self.file, 'r', encoding="utf-8") as arquivo:
                data = json.load(arquivo)
            if not isinstance(data, list):
                data = [data]
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(self.__dict__)

        with open(self.file, 'w', encoding="utf-8") as arquivo:
            json.dump(data, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    pessoa1 = Pessoa('João', 33)
    pessoa1.save()
    pessoa2 = Pessoa('Maria', 47)
    pessoa2.save()
    pessoa3 = Pessoa('Vitor', 17)
    pessoa3.save()