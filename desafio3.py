#[1] Depositar

#[2] Sacar

#[3] Extrato

#[4] Sair


saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3



while True:


    opcao = input()


    if opcao == "1":

        dep = (float(input('Qual valor do depósito: R$')))

        if dep > 0:

            saldo += dep

            print('Depósito  realizado com sucesso!')

            extrato += (f'\nDepósito: R$ {dep:.2f}')

           

        else:

            print('Operação falhou. Digite um valor válido!')

                       

    elif opcao == "2":

       

        saq = (float(input("Qual valor você deseja sacar? ")))


        excedeu_saldo = saq > saldo #verificações


        excedeu_limite = saq > limite


        excedeu_saques = numero_saques >= LIMITE_SAQUES


       

        if excedeu_saldo:

            print('Operação falhou! Você não tem saldo suficiente.')

       

        elif excedeu_limite:

            print ('Operação falhou o valor do saque excede o limite.')

       

        elif excedeu_saques:

            print('Operação falhou! Número máximo de saques excedido')

       

        elif saq > 0:

            saldo -= saq

            extrato += f'Saque: R$ {saq:.2f}\n'

            numero_saques += 1

           

        else:

            print('Operação Falhou! O valor é inválido.')            


    elif opcao == "3":

        depositos = saldo

        print('\n----------EXTRATO --------------')

        print('Não foram realizadas movimentações.' if not extrato else extrato)

        print(f'\nSaldo: R$ {saldo:.2f}')

        print('----------------------------------')


    elif opcao == "4":

        break

   

    else:

        print("Operação inválida, por favor selecione a operação desejada.")