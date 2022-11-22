from os import system

sair = 0
while True:
    erro = 0
    while erro == 0:
        system('cls')
        print('\t4 EM LINHA\n1 - Jogar\n0 - Sair')
        opcao = int(input('\n\nOpção: '))
        if opcao == 0:
            sair = 1
            break
        elif opcao == 1:
            system('cls')
            break
    if sair == 1:
        break