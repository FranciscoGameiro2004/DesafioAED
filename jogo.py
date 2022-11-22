from os import system

def coodernadas(x, y, lista, valor, listaLinhas):
    """
    Esta função permite a modificação de um elemento de uma dada lista bidimensional para um determinado valor.
    """
    listatemporaria = lista[y].copy() # Criação de uma lista temporária que é uma cópia da linha y da lista a alterar.

    # Modificação de um valor da lista temporária através da remoção do elemento que estava presente na posição x e a inserção do valor na mesma posição.
    del listatemporaria[x]
    listatemporaria.insert(x, valor)
    
    # Remoção da linha y e a inserção da lista temporária à mesma posição.
    del lista[y]
    lista.insert(y, listatemporaria)
    
    # Para que não existam sobreposições, será feita uma alteração do da linha a ocupar baseando na coluna.
    # Será feita uma subtração entre o valor da linha utilizada e 1 se esse valor não for igual a 0.
    linhaUsada = listaLinhas[x]
    if linhaUsada != 0:
        del listaLinhas[x]
        listaLinhas.insert(x,linhaUsada-1)


tabuleiro = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]] # Configuração do tabuleiro do 4 em linha

linhaLivre = [5,5,5,5,5,5,5] # Determina a última linha lívre de cada coluna

sair = 0
while True:
    erro = 0
    while erro == 0:
        """
        Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
        """
        system('cls')
        print('\t4 EM LINHA\n1 - Jogar\n0 - Sair')
        opcao = int(input('\n\nOpção: '))
        if opcao == 0:
            sair = 1
            break
        elif opcao == 1:
            while True:
                system('cls')
                for i in range(len(tabuleiro)):
                    print('-'*27)
                    for j in range(len(tabuleiro[i])):
                        print(tabuleiro[i][j], end=' | ')
                    print()
                colunaEscolhida = int(input())
                coodernadas(colunaEscolhida, linhaLivre[colunaEscolhida], tabuleiro, 1, linhaLivre)
    if sair == 1:
        break