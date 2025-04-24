
menu = """
==========================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
==========================
-> """ # Menu de opções do banco

saldo = 0 # Variável para armazenar o saldo do cliente
limite = 500 # Limite de saque
extrato = "" # Extrato bancário
numero_saques = 0 # Contador de saques realizados
LIMITE_SAQUES = 3 # Limite de saques por dia

while True: # Loop para manter o menu ativo
    print("=== Bem-vindo ao Banco ===")
    opçao = input(menu)


    if opçao == "1": # Opção de depósito
        print("=== Depósito ===")
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")

        else:
            print("Valor inválido para depósito!")



    elif opçao == "2": # Opção de saque
        print("=== Saque ===")
        saque = float(input("Informe o valor do saque: "))
        
        if saque > saldo:
            print("Saldo insuficiente para saque!")

        elif saque > limite:
            print("Valor do saque acima do limite!")
        
        elif numero_saques > LIMITE_SAQUES:
            print("Número máximo de saques atingido!")
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        
        else:
            print("Valor inválido para saque!")

    elif opçao == "3": # Opção de extrato
        print("=== Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=================")

    elif opçao == "4": # Opção de sair
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
    print("")

        
