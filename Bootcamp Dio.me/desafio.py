menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques foi atingido. Tente amanha!")
        else:
            valor = float(input("Informe o valor do saque: "))
            if (valor > limite):
                print(f"O valor máximo para saque é de R$ {limite:.2f}. Tente um valor menor.")          
            elif (valor > saldo):    
                print("Não há saldo suficiente para saque.")
            elif valor > 0:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("O valor informado para saque é inválido.")

    elif opcao == "e":
        print("\n**********************************************")
        print("\n************** EXTRATO BANCARIO **************")
        print("\n**********************************************")
        if extrato:
            print(extrato)
        else:
            print("Não há registro de movimentações na conta.\n")
        print(f"\n\nSaldo atual: R$ {saldo:.2f}")
        print("\n**********************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")