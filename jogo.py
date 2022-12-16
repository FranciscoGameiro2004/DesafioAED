import os

def umOUdois(var):
    """
    Esta função à medida que for acionada vai retornando os valores 1 e 2, de forma alternada.
    """
    if var == 1:
        var = 2
    elif var == 2:
        var = 1
    return var
    

def coodernadas(x, y, lista, valor, listaLinhas=None):
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
    import math

    pontoInicialX = x
    pontoInicialY = y
    vitoria = False

    for i in range(4):
        try:
            if lista[y][i] == valorAlvo and lista[y][i + 1] == valorAlvo and lista[y][i + 2] == valorAlvo and lista[y][i + 3] == valorAlvo:
                vitoria = True
        except:
            ()
    
    for i in range(3):
        try:
            if lista[i][x] == valorAlvo and lista[i + 1][x] == valorAlvo and lista[i + 2][x] == valorAlvo and lista[i + 3][x] == valorAlvo:
                vitoria = True
        except:
            ()

    for i in range(7):
        if pontoInicialX != 0 and pontoInicialY != 0:
            pontoInicialX -= 1
            pontoInicialY -= 1
        else:
            break
    
    for i in range(3):
        try:
            if lista[pontoInicialY + i][pontoInicialX + i] == valorAlvo and lista[pontoInicialY + i + 1][pontoInicialX + i + 1] == valorAlvo and lista[pontoInicialY + i + 2][pontoInicialX + i + 2] == valorAlvo and lista[pontoInicialY + i + 3][pontoInicialX + i + 3] == valorAlvo:
                vitoria = True
        except:
            ()
    
    pontoInicialX = x
    pontoInicialY = y

    for i in range(7):
        if pontoInicialX != 0 and pontoInicialY != 5:
            pontoInicialX -= 1
            pontoInicialY += 1
        else:
            break
    
    for i in range(3):
        try:
            if lista[pontoInicialY - i][pontoInicialX + i] == valorAlvo and lista[pontoInicialY - i - 1][pontoInicialX + i + 1] == valorAlvo and lista[pontoInicialY - i - 2][pontoInicialX + i + 2] == valorAlvo and lista[pontoInicialY - i - 3][pontoInicialX + i + 3] == valorAlvo:
                vitoria = True
        except:
            ()

    return vitoria

def reiniciar(lista, listaLinhas):
    """
    Esta função reinicia as listas pedidas nos parâmetros para os seus valores padrão. 
    """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = 0
    
    for i in range(len(listaLinhas)):
        listaLinhas[i] = 5

def gerarTabuleiro(lista, colunaDestacada=None, linhaDestacada=None):
    for i in range(len(lista)):
        print('-'*27)
        for j in range(len(lista[i])):
            if (j != colunaDestacada or i != linhaDestacada) or (colunaDestacada == None and linhaDestacada == None):
                print(lista[i][j], end=' | ')
            else:
                print('S', end=' | ')
        print()
    print('-'*27)

def existeEmpate(lista):
    """
    Esta função determina se houve empate ou não.
    """
    houveEmpate = False
    nLinhasEmpatadas = 0
    for i in range(len(lista)):
        if 0 not in lista[i]:
            nLinhasEmpatadas += 1
    if nLinhasEmpatadas == 6:
        houveEmpate = True
    
    return houveEmpate

def menu():
    """
    Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
    """
    from pressAnyKey import optionKey
    from time import sleep

    opcaoAtual = 1
    opcaoSelecionada = 1
    select = 0

    while select == 0:
        opcaoSelecionada = opcaoAtual
        if opcaoAtual == 1:
            os.system('cls')
            print('\t4 EM LINHA\n-> 1 - Jogar\n0 - Sair')
            opcaoAtual, select = optionKey('ctrl direito', 0, 'seta abaixo')
            sleep(0.05)
        elif opcaoAtual == 0:
            os.system('cls')
            print('\t4 EM LINHA\n1 - Jogar\n-> 0 - Sair')
            opcaoAtual, select = optionKey('ctrl direito', 1, 'seta acima')
            sleep(0.05)
    

    return opcaoSelecionada

def selecionarColuna(lista, listaColunas, nJogador):
    """
    Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
    """
    from pressAnyKey import optionKey
    from time import sleep

    opcaoAtual = int(0)
    opcaoSelecionada = int(0)
    select = int(0)
    colunaAtual = int(0)

    while True:

        opcaoSelecionada = opcaoAtual
        os.system('cls')
        print('Jogador {}'.format(nJogador))
        gerarTabuleiro(lista, colunaAtual, listaColunas[colunaAtual])
        opcaoAtual, select = optionKey('ctrl direito', 1, 'seta à direita', 0, 'seta à esquerda')
        sleep(0.5)

        if select == 0:
            if opcaoAtual == 1:
                colunaAtual += 1
                while listaColunas[colunaAtual] < 0:
                    colunaAtual += 1
            else:
                colunaAtual -= 1
                while listaColunas[colunaAtual] < 0:
                    colunaAtual -= 1

            if colunaAtual < 0:
                colunaAtual = 0
            elif colunaAtual > 6:
                colunaAtual = 6
        else:
            break
    

    return colunaAtual


tabuleiro = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]] # Configuração do tabuleiro do 4 em linha

linhaLivre = [5,5,5,5,5,5,5] # Determina a última linha lívre de cada coluna
jogador = 2

sair = 0
vence = False
while True:
    erro = 0
    while erro == 0:
        opcao = menu()
        if opcao == 0: # Se for acionada a opção 0, então a variável sair terá como valor 1 e será feito um break ao loop while
            sair = 1
            break
        elif opcao == 1: # Se for acionada a opção 1, então será acionado um loop while onde o jogo será iniciado.
            colunaEscolhida = -1
            while True:
                if colunaEscolhida != -1:
                    vence = existeVitoria(colunaEscolhida, linhaLivre[colunaEscolhida] + 1, tabuleiro, jogador)

                    if vence == True:
                        break
                    else:
                        empate = existeEmpate(tabuleiro)
                        if empate == True:
                            break
                
                jogador = umOUdois(jogador)
                os.system('cls')
                print('Jogador {}'.format(jogador))
                colunaEscolhida = selecionarColuna(tabuleiro, linhaLivre, jogador)
                coodernadas(colunaEscolhida, linhaLivre[colunaEscolhida], tabuleiro, jogador, linhaLivre)
                
                    

            os.system('cls')
            if vence == True:    
                print('Jogador {} vence!'.format(jogador))
            elif empate ==  True:
                print('Houve um empate.')
            gerarTabuleiro(tabuleiro)
            input('Prima ENTER para continuar. ')
            reiniciar(tabuleiro, linhaLivre)
            jogador = 2
    if sair == 1:
        break