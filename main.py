menu ="""

   [d] Depositar    
   [w] Sacar        
   [e] Extrato      
   [q] Quit         

=> """

balance = 0
extract = ""
limit_amount_withdraw = 500
quantity_withdraws = 0
LIMIT_WITHDRAW = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito".upper())
        value = float(input("Informe o valor:\n=>"))
        if value > 0:
            balance += value
            extract += f"Deposito: +R$ {value:.2f} \n"
        else:
            print("Valor inválido. Por favor, insira um valor positivo.")
    elif opcao == "w":
         print("\nSaque".upper())
        if quantity_withdraws < 3:
            value = float(input("Informe o valor:\n=>"))
            if value <= limit_amount_withdraw:
                if balance > value:
                    balance -= value
                    extract += f"Retirada: -R$ {value:.2f} \n"
                    quantity_withdraws += 1
                else:
                    print("Saldo insuficiente.")
            else:
                print(f"Saque deve ser menor que R$ {limit_amount_withdraw:.2f}")
        else:
            print("Limite de {LIMITE_SAQUES} saques diarios atingido.")
     

    elif opcao == "e":
        print("\nExtrato:")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")