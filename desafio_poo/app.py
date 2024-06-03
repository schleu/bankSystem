from datetime import date, datetime
from typing import List
from abc import ABC, abstractmethod, abstractproperty


class Cliente:
    def __init__(self, endereco:str) -> None:
        self._endereco = endereco
        self._contas = []
    def realizar_transacao(self, conta:'Conta', transacao:'Transacao') -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:date, endereco:str) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Conta:
    def __init__(self, numero:str, cliente:Cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico:Historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int):
        return cls(cliente, numero)

    def sacar(self, valor:float)->bool:
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            return True
        return False
    
    def depositar(self, valor:float)->bool:
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            return True
        return False

class Conta_Corrente(Conta):
    def __init__(self, numero: str, cliente: Cliente, limite:float=500, limite_saques:int=3) -> None:
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques


    def sacar(self, valor):
        numero_saques = 0

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques


        if excedeu_limite or excedeu_limite:
            return False
        else:
            super().sacar(valor)
            return True
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Transacao(ABC):
    @abstractmethod
    def registrar(conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self,valor:float) -> None:
        self._valor = valor
    
    def registrar(self, conta:Conta):
        conta.depositar(self._valor)

class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        self._valor = valor
    
    def registrar(self, conta: Conta):
        conta.sacar(self._valor)



class Historico:
    def __init__(self) -> None:
        super().__init__()
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao:Transacao ):
        self._transacoes.append({
            "tipo":transacao.__class__.__name__,
            "valor":transacao.valor,
            "data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })
        pass
    
pf = Pessoa_Fisica('123.456.789-00','Danilo Scleu',date(1993,2,18),'Rua Exeplo, 123')

print(f'Pessoa Fisica {pf}')
print('-----')

cc = Conta_Corrente(0,'0001','0001',pf)

print(f'Conta corrente {cc}')
print(f'Saldo {cc.saldo()}')
print(f'Depotar {cc.depositar(200)}')
print(f'Saldo {cc.saldo()}')
print(f'Sacar {cc.sacar(200)}')
print(f'Saldo {cc.saldo()}')