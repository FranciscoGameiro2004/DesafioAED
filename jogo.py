from os import system

def umOUdois(var):
    """
    Esta função à medida que for acionada vai retornando os valores 1 e 2, de forma alternada.
    """
    if var == 1:
        var = 2
    elif var == 2:
        var = 1
    return var
    

def coodernadas(x, y, lista, valor, listaLinhas):
    """
    Esta função altera elemento de uma dada lista bidimensional para um determinado valor.
    """
    if listaLinhas[x] != -1:
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
        if linhaUsada >= 0:
            del listaLinhas[x]
            listaLinhas.insert(x,linhaUsada-1)

def existeVitoria(x, y, lista, valorAlvo):
    """
    Esta função verifica se um jogador que tenha acabado de colocar uma peça consegue, de acordo com as regras do
    "4 em Linha", uma vitória ou não.
    """

    vitoria = False

    for i in range(4):
        if lista[y][i] == valorAlvo and lista[y][i + 1] == valorAlvo and lista[y][i + 2] == valorAlvo and lista[y][i + 3] == valorAlvo:
            vitoria = True
    
    for i in range(3):
        if lista[i][x] == valorAlvo and lista[i + 1][x] == valorAlvo and lista[i + 2][x] == valorAlvo and lista[i + 3][x] == valorAlvo:
            vitoria = True
    
    

    return vitoria


tabuleiro = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]] # Configuração do tabuleiro do 4 em linha

linhaLivre = [5,5,5,5,5,5,5] # Determina a última linha lívre de cada coluna
jogador = 1

sair = 0
vence = False
while True:
    erro = 0
    while erro == 0:
        """
        Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
        """
        system('cls')
        print('\t4 EM LINHA\n1 - Jogar\n0 - Sair')
        opcao = int(input('\n\nOpção: '))
        if opcao == 0: # Se for acionada a opção 0, então a variável sair terá como valor 1 e será feito um break ao loop while
            sair = 1
            break
        elif opcao == 1: # Se for acionada a opção 1, então será acionado um loop while onde o jogo será iniciado.
            colunaEscolhida = -1
            while True:
                if colunaEscolhida != -1:
                    vence = existeVitoria(colunaEscolhida-1, linhaLivre[colunaEscolhida-1] + 1, tabuleiro, jogador)

                    if vence == True:
                        break

                jogador = umOUdois(jogador)
                system('cls')
                for i in range(len(tabuleiro)):
                    print('-'*27)
                    for j in range(len(tabuleiro[i])):
                        print(tabuleiro[i][j], end=' | ')
                    print()
                colunaEscolhida = int(input())
                coodernadas(colunaEscolhida-1, linhaLivre[colunaEscolhida-1], tabuleiro, jogador, linhaLivre)

            system('cls')    
            print('Jogador {} vence!'.format(jogador))
            for i in range(len(tabuleiro)):
                    print('-'*27)
                    for j in range(len(tabuleiro[i])):
                        print(tabuleiro[i][j], end=' | ')
                    print()
            input('Prima ENTER para continuar. ')
    if sair == 1:
        break