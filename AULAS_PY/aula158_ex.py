"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, account_number):
        self.agency = agency
        self.account_number = account_number
        self.balance = 0
    
    @abstractmethod
    def deposit(self, value): ...

    @abstractmethod
    def withdrawal(self, value): ...

class CurrentAccount(Account):
    def deposit(self, value):
        self.balance += value
    
    def withdrawal(self, value):
        self.balance -= value

class SavingAccount(Account):
    def deposit(self, value):
        self.balance += value
    
    def withdrawal(self, value):
        if self.balance >= 0:
            self.balance -= value

class People():
    @property
    def name(name):
        return _name
    
    @name.setter
    def name(name):
        _name = name

    @property
    def age(age):
        return _age
    
    @age.setter
    def age(age):
        _age = age

class Client(People):
    def __init__(self, account: CurrentAccount | SavingAccount):
        self.account = account

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
    
    def add_client(self, client: Client):
        self.clients.append(client)
    
    def deposit(self, value, agency, account_number, costumer: Client):
        for client in self.clients:
            if agency == client.account.agency:
                if client == costumer:
                    if account_number == client.account.account_number:
                        client.account.deposit(value)
                        break

    def withdrawal(self, value, agency, account_number, costumer: Client):
        for client in self.clients:
            if agency == client.account.agency:
                if client == costumer:
                    if account_number == client.account.account_number:
                        client.account.withdrawal(value)
                        break

marcos = Client(SavingAccount(1, 14251))

ana = Client(CurrentAccount(4, 14561))

brasil = Bank("banco do brasil")
brasil.add_client(marcos)
brasil.add_client(ana)

brasil.deposit(300, 1, 14251, marcos)
brasil.withdrawal(150, 1, 14251, marcos)
print(marcos.account.balance)