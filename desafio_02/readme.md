
# Desafio: Criando um sistema bancário

 Desafio do bootcamp Coding The Future Vivo - Python AI Backend Developer

## Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária.

## Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário(cliente de banco) e criar conta corrente (vincular com usuário).

### Operação de depósito

> v1

* Deve ser possível depositar valores positivos para a minha conta bancária.
* Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

> v2

* A função depósito deve receber os argumentos apenas por posição (positional only).
  * Sugestão de argumentos:  `saldo, valor, extrato`
  * Sugestão de retorno: `saldo, extrato`

### Operação de saque

> v1

* O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
* Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

> v2

* A função saque deve receber os argumentos apenas por nome (keyword only).
  * Sugestão de argumentos: `saldo, valor, extrato, limite, numero_saques, limite_saques`
  * Sugestão de retorno: `saldo, extrato`

### Operação de extrato

> v1

* Essa operação deve listar todos os depósitos e saques realizados na conta.  
* No fim da listagem deve ser exibido o saldo atual da conta.
* Se o extrato estiver em branco, exibir a mensagem: `Não foram realizadas movimentações.`
* Os valores devem ser exibidos utilizando o formato R$ xxx.xx, `exemplo: 1500.45 = R$ 1500.45`

> v2

* A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
  * Argumentos posicionais: `saldo`
  * Argumentos nomeados: `extrato`

### Criar Usuários

> v1

* Não possui

> v2

* O programa deve armazenar os usuários em uma lista, um usuário é composto por:
  * nome
  * data de nascimento
  * cpf
  * endereço
* O Endereço é uma string com o formato: `"logradouro, nro - bairro - cidade/sigla estado"`
* Deve ser armazenado somente os números do CPF.
* Não podemos cadastrar 2 usuários com o mesmo CPF.

### Criar Conta Corrente

> v1

* Não possui

> v2

* O programa deve armazenar contas em uma lista
* Uma conta é composta por:
  * agencia
  * número da conta
  * usuário
* O numero da conta é sequencial, iniciando em 1.
* O número da agência é fixo: `"0001"`.
* O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário
