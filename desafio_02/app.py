menu ="""
Bem vindo ao seu banco

Select a option:
----------------------
|   [d] Depositar    |
|   [w] Sacar        |
|   [e] Extrato      |
|   [u] Usuario      |
|   [c] Criar Conta  |
|   [q] Quit         |
----------------------
=> """



def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"= Deposito: +R$ {valor:.2f}  =\n"
    else:
        print("Valor inválido. Por favor, insira um valor positivo.")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor <= limite:
            if saldo > valor:
                saldo -= valor
                extrato += f"= Retirada: -R$ {valor:.2f} = \n"
                numero_saques += 1
            else:
                print("Saldo insuficiente.")
        else:
            print(f"Saque deve ser menor que R$ {limite:.2f}")
    else:
        print("Limite de {LIMITE_SAQUES} saques diarios atingido.")
    return saldo, extrato
    
def exibir_extrato(saldo,/,*,extrato):
    if(extrato == ''):
        print(f"============EXTRATO============")
        print(f" Você não possui movimentações ")
        print(f"===============================")
    else:
        print(f"=========EXTRATO==========")
        print(f"=                        =")
        print(f"= {extrato}              =")
        print(f"=                        =")
        print(f"= Saldo: {saldo}         =")
        print(f"==========================")


def find_user(cpf, users):
    user_found = [user for user in users if user['cpf'] == cpf]
    return user_found[0] if user_found else None

def criar_usuario(users):
    cpf = input(f'Insira seu cpf\n=>')
    user_found = find_user(cpf, users)
    
    if(user_found):
        print('Usuario já existente.')
        return

    nome = input(f'Insira seu nome\n=>')
    nascimento = input(f'Insira sua data de nascimento\n=>')
    endereco = input(f'Insira seu endereço (logradouro, nro - bairro - cidade/sigla estado)\n=>')

    users.append({
        "nome":nome,
        "data_nascimento":nascimento,
        "cpf":cpf,
        "endereco":endereco
    })
    print('Usuario criado.')


def criar_conta_corrent(agencia, numero_conta, users):
    cpf = input('Digite seu CPF\n=>')
    user_found = find_user(cpf, users)
    
    if(user_found):
        print('Conta corrente criada com sucesso.')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": user_found}
    else:
        print('Usuario não encontrado')


def main():
    balance = 0
    extract = ""
    limit_amount_withdraw = 500
    quantity_withdraws = 0
    LIMIT_WITHDRAW = 3
    users = []
    accounts = []
    AGENCY = "0001"
    
    while True:
        opcao = input(menu)

        if opcao == "d":
            value = float(input("Informe o valor:\n=>"))
            balance, extract  = depositar(balance, value, extract)
        elif opcao == "w":
            value = float(input("Informe o valor:\n=>"))
            balance, extract = sacar(
                saldo=balance,
                valor=value,
                extrato=extract,
                limite=limit_amount_withdraw,
                numero_saques=quantity_withdraws,
                limite_saques=LIMIT_WITHDRAW,
            )

        elif opcao == "e":
           exibir_extrato(balance, extrato=extract)

        elif opcao == "u":
           criar_usuario(users)

        elif opcao == "c":
           cc = criar_conta_corrent(AGENCY, len(accounts)+1, users)
           accounts.append(cc)
            
        elif opcao == "q":
            print("Até logo.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")




main()