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
        print("\nSaque")
     

    elif opcao == "e":
        print("\nExtrato:")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")