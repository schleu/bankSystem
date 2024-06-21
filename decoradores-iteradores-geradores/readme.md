
# Desafio: Criando um sistema bancário

 Desafio do bootcamp Coding The Future Vivo - Python AI Backend Developer

## Objetivo Geral

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Desafio

Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores, você foi encarregado de implementar as seguintes funcionalidades no sistema:

* Decorador de log
* Gerador de relatórios
* Iterador personalizado

> [!NOTE]
> Este é o seguimento dos desafios anteriores.

### Decorador de log

* Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc).
* Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

### Gerador de relatórios

* Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas.
* Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

### Iterador personalizado

* Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).
