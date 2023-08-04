while True:  # Loop infinito para repetir a solicitação do nome até que seja fornecido um nome válido
    nome = input(""" 
        Olá, como vai você? Tudo blz?!
        Vi que você é nosso cliente premium DioBank! 
        Como você gostaria de ser chamadx?
        """)

    if nome.strip():  # Verifica se o campo de nome não está em branco ou contém apenas espaços em branco
        break  # Se o nome for válido, sai do loop e continua o código

    print("Você precisa fornecer um nome válido.")

print(f'''
    ============================
    Bem vindx ao DioBank {nome.title()}
    Por favor, escolha uma das opções a seguir:
    ''')

menu = """

[G] Guardar
            [R] Retirar
                        [H] Histórico
                                    [E] Encerrar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()
    
    if opcao == "G":
        while True:
            try:
                valor = float(input("Informe o valor que você deseja guardar:"))
                if valor > 0:
                    break
                else: print("Por favor digite um numero válido")
            except ValueError:
                print("Digite apenas números!") 

        while True:
                    print(f'''
                    {nome.title()} tem certeza que deseja guardar R${valor:.2f}?
                    ''')
                
                    menu2 = """
                    SIM [S]                         NÃO [N]
                    => """
                    opcao2 = input(menu2).upper()
                    
                    if  opcao2 == "S":
                        saldo += valor
                        extrato += f"Guardado: R$ {valor:.2f}+\n"
                        print(f'''
                        R${valor:.2f} foram guardados com sucesso!
                        Por gentileza, escolha uma nova opção:''')
                        break
                    elif opcao2 == "N":
                            print(f'''Operação para guardar R${valor:.2f} foi cancelada pelo usuário
                            
                            Por gentileza, Escolha uma nova opção:''')
                            break
                    else:
                        print(f"Opção inválida, {nome.title()}! Por favor, escolha 'S' para SIM ou 'N' para NÃO.")
            
        else:
            print('''Operação falhou! O valor informado é inválido.
    
    Por gentileza, Escolha uma nova opção:''')

    elif opcao == "R":
        while True:
            try:
                valor = float(input("Informe o valor que você deseja retirar: "))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES
                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print("Operação falhou! O valor da retirada excedeu o limite.")
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de retiradas por dia foi excedido.")
                elif valor > 0:
                    break
                else:
                    print("Por favor digite um número válido!")
            except ValueError:
                print("Digite apenas números!")
        
        while True:           
                    print(f'''
                    {nome.title()} tem certeza que deseja retirar R${valor:.2f}?
                    ''')
                    menu2 = """
                    SIM [S]                         NÃO [N]    
                    => """
                    opcao2 = input(menu2).upper()
                    
                    if  opcao2 == "S":
                        saldo -= valor
                        extrato += f"""                        -R${valor:.2f} Retirado\n"""
                        numero_saques += 1
                        print(f'''
                        R${valor:.2f} foram retirados com sucesso!
                        Por gentileza, escolha uma nova opção:''')
                        break
                    elif opcao2 == "N":
                        print(f'''
    Operação para Retirar R${valor:.2f} foi cancelada pelo usuário.
                            
    Por gentileza, Escolha uma nova opção:''')
                        break
    
    elif opcao == "H":
        print("\n================ HISTÓRICO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f""""             \nSaldo: R$ {saldo:.2f}             """)
        print("==========================================")

    elif opcao == "E":
        print(f'{nome.title()}, obrigadx por ser nosso cliente')
        break
    else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")