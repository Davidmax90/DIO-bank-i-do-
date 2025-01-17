# Desafio Backend em Python DIO + VIVO                                           |
# Operação Bancária                                                              |
# por: David Oliveira Marques                                                    |
# 14/01/2025                                                                     |
|================================================================================|

menu = """
|===============================|
|    Seja muito Bem-Vindo ao    |
|          Nosso Banco!         |
|           Bank i do!          |
|-------------------------------|
|  Selecione a opção desejada:  |
|-------------------------------|
| [1] - Depositar               |
| [2] - Sacar                   |
| [3] - Extrato                 |
| [0] - Sair                    |
|===============================|

=>Digite a opção desejada: \n"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1": #Depositar
        valor = float(input("Informe o valor do depósito: \n"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"\nDeposito no valor de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("\nOperação falhou! O valor informado é inválido.\n Retornando..")


    elif opcao == "2": #Sacar
        valor = float(input("Informe o valor do saque: \n"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.\n Retornando..")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite diário.\n Retornando..")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.\n -> Obs: Você pode realizar até 3 saques por dia no valor de até R$500.00 cada saque.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            print(f"\nSaque no valor de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif opcao == "3": #Extrato
        print("\n==================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "0": #Sair
        print("Saindo...\n \nObrigado pela preferência!\nE até a proxima!\nBank i do! Agradece!\n")
        break 

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")

|================================================================================================|
#                                                                                                |
# Desafio Backend em Python DIO                                                                  |
# Operação Bancária                                                                              |
# por: David Oliveira Marques                                                                    |
# 14/01/2025                                                                                     |
#________________________________________________________________________________________________|
#--- Você foi contratado por um grande banco                                                     |
# para desenvolver o seu novo sistema.                                                           |
#  Esse banco deseja modernizar suas operações                                                   |
# e para isso escolheu a linguagem Python.                                                       |
#  Para a Primeira versão do sistema devemos implementar apenas 3 operações:                     |
# 1.Depósito, 2.Saque e 3.Extrato.                                                               |
#________________________________________________________________________________________________|
# # 01. Operação de DEPÓSITO #                                                                   |
# Deve ser possível depositar valores positivos para a conta bancária.                           |
# A v1 do projeto trabalha apenas com 1 usuário,                                                 |
# então não precisamos nos preocupar em idenficiar qual é o número da agência e conta banária.   |
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.    |
#                                                                                                |
#________________________________________________________________________________________________|
# # 02. Operação de EXTRATO #                                                                    |
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.     |
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem                    |
# informando que não será possível sacar o dinheiro por falta de saldo.                          |
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.       |
#                                                                                                |
#________________________________________________________________________________________________|
# # 03. Operação de EXTRATO #                                                                    |
# Essa operação deve listar todos os depósitos e saques realizados na conta.                     |
# No fim da listagem deve ser exibido o saldo atual da conta.                                    |
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx,                                   |
# Exemplo: 1400.45 = R$1400.45                                                                   |
#                                                                                                |
#________________________________________________________________________________________________|
# houveram algumas incrementações a mais do projeto inicial,_____________________________________|
# com a finalidade de exercitar mais o aprendizado.______________________________________________|
# _______________________________________________________________________________________________|
|================================================================================================|
