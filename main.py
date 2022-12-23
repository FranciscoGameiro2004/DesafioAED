# Numero: 40220426
# Nome: Francisco João Moreira de Castro Neves Gameiro

import os
from colorama import Fore, Back, Style
from pressAnyKey import optionKey
from time import sleep

try:
    """
    Este try-except serve para verificar se o programa VLC está instalado no computador ou não.
    #Nota 1: No caso de 'existeVLC' for 'False', será emitido um aviso a dizer que é necessário o VLC instalado para que o som funcione no programa.
    """

    import vlc
    
    optionSound= vlc.MediaPlayer('audio\option.wav')
    selectSound = vlc.MediaPlayer('audio\select.wav')
    victorySound = vlc.MediaPlayer('audio\victory.wav')

    existeVLC = True
    somAtivo = True
except:
    existeVLC = False

def umOUdois(var):
    """
    Esta função à medida que for acionada vai retornando os valores 1 e 2, de forma alternada.
    Isto é, se o valor for 1, então o mesmo passa a ser 2, e vice-versa.
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

    #As variáveis de pontos iniciais são inicializadas com o posicionamento do ponto colocado.
    #O ponto inicial será necessário para verificar, de forma oblíqua, se a vitória existe ou não.
    pontoInicialX = x
    pontoInicialY = y
    vitoria = False # Por defeito, a variável 'vitoria' está como False.

    for i in range(4):
        try:
            if lista[y][i] == valorAlvo and lista[y][i + 1] == valorAlvo and lista[y][i + 2] == valorAlvo and lista[y][i + 3] == valorAlvo:
                vitoria = True
                for j in range(4):
                    """
                    #Nota 2: Em caso de esta condição ser verdadeira, não só será atribuida 'True' à variável 'vitoria',
                    como vão sendo acrescentados as coodernadas de cada ponto para a lista 'coodernadasLista' no seguinte formato: [linha,coluna]
                    """
                    coodernadasLinha.append([y,i+j])
        except:
            ()
    
    for i in range(3):
        try:
            if lista[i][x] == valorAlvo and lista[i + 1][x] == valorAlvo and lista[i + 2][x] == valorAlvo and lista[i + 3][x] == valorAlvo:
                vitoria = True
                for j in range(4):
                    #Nota 2
                    coodernadasLinha.append([i+j,x]) 
        except:
            ()

    for i in range(7):
        if pontoInicialX != 0 and pontoInicialY != 0:
            # Enquanto que o ponto inicial não se situar no limite do tabuleiro, o ponto inicial desloca-se da seguinte forma:
            pontoInicialX -= 1
            pontoInicialY -= 1
        else:
            break
    
    for i in range(3):
        try:
            if lista[pontoInicialY + i][pontoInicialX + i] == valorAlvo and lista[pontoInicialY + i + 1][pontoInicialX + i + 1] == valorAlvo and lista[pontoInicialY + i + 2][pontoInicialX + i + 2] == valorAlvo and lista[pontoInicialY + i + 3][pontoInicialX + i + 3] == valorAlvo:
                vitoria = True
                for j in range(4):
                    #Nota 2
                    coodernadasLinha.append([pontoInicialY + i + j, pontoInicialX + i + j]) 
        except:
            ()
    
    #As variáveis de pontos iniciais são inicializadas, de novo, com o posicionamento do ponto colocado.
    pontoInicialX = x
    pontoInicialY = y

    for i in range(7):
        if pontoInicialX != 0 and pontoInicialY != 5:
            # Enquanto que o ponto inicial não se situar no limite do tabuleiro, o ponto inicial desloca-se da seguinte forma:
            pontoInicialX -= 1
            pontoInicialY += 1
        else:
            break
    
    for i in range(3):
        try:
            if lista[pontoInicialY - i][pontoInicialX + i] == valorAlvo and lista[pontoInicialY - i - 1][pontoInicialX + i + 1] == valorAlvo and lista[pontoInicialY - i - 2][pontoInicialX + i + 2] == valorAlvo and lista[pontoInicialY - i - 3][pontoInicialX + i + 3] == valorAlvo:
                vitoria = True
                for j in range(4):
                    #Nota 2
                    coodernadasLinha.append([pontoInicialY - i - j, pontoInicialX + i + j]) 
        except:
            ()
    
    return vitoria

def reiniciar(lista, listaLinhas):
    """
    Esta função reinicia as listas pedidas nos parâmetros para os seus valores padrão. 
    """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            # Os valores do tabuleiro voltam ao padrão.
            lista[i][j] = 0
    
    for i in range(len(listaLinhas)):
        # Os valores da 'listaLinhas' voltam ao padrão.
        listaLinhas[i] = 5
    
    # Para evitar conflitos, serão limpas estas duas listas:
    coodernadasLinha.clear()
    nomeJogador.clear()

def gerarTabuleiro(lista, colunaDestacada=None, linhaDestacada=None, listaCoodernadas=[]):
    for i in range(len(lista)):
        print(Back.BLUE + ' '*37 + Style.RESET_ALL)
        print(Back.BLUE + '  ' + Style.RESET_ALL, end='' + ' ')
        for j in range(len(lista[i])):
            if listaCoodernadas != [] and [i,j] in listaCoodernadas:
                    if lista[i][j] == 1:
                        print(Back.RED + '●' + Style.RESET_ALL, end = ' ' + Back.BLUE + '  ' + Style.RESET_ALL + ' ')
                    elif lista[i][j] == 2:
                        print(Back.YELLOW + '●' + Style.RESET_ALL, end = ' ' +  Back.BLUE + '  ' + Style.RESET_ALL + ' ')
                    else:
                        print(Fore.BLACK + ' ' + Style.RESET_ALL, end = ' ' +  Back.BLUE + '  ' + Style.RESET_ALL + ' ')
            else:
                if (j != colunaDestacada or i != linhaDestacada) or (colunaDestacada == None and linhaDestacada == None):
                    if lista[i][j] == 1:
                        print(Fore.RED + '●' + Style.RESET_ALL, end = ' ' + Back.BLUE + '  ' + Style.RESET_ALL + ' ')
                    elif lista[i][j] == 2:
                        print(Fore.YELLOW + '●' + Style.RESET_ALL, end = ' ' +  Back.BLUE + '  ' + Style.RESET_ALL + ' ')
                    else:
                        print(Fore.BLACK + ' ' + Style.RESET_ALL, end = ' ' +  Back.BLUE + '  ' + Style.RESET_ALL + ' ')
                else:
                    print(Back.WHITE + Fore.WHITE + ' ' + Back.RESET, end = ' ' +  Back.BLUE + '  ' + Style.RESET_ALL + ' ')
        print()
    print(Back.BLUE + ' '*37 + Style.RESET_ALL)

def existeEmpate(lista):
    """
    Esta função determina se houve empate ou não.
    """
    houveEmpate = False # Por defeito, a variável 'houveEmpate' está como False.
    nLinhasEmpatadas = 0 # Por defeito, a variável 'nLinhasEmpatadas' tem valor 0.
    for i in range(len(lista)):
        if 0 not in lista[i]:
            nLinhasEmpatadas += 1 # Se não houver 0 em uma linha, então será acrescentado 1 valor na variável 'nLinhasEmpatadas'.
    if nLinhasEmpatadas == 6:
        houveEmpate = True # Se 'nLinhasEmpatadas' tiver valor 6, então 'houveEmpate' terá como valor True.
    
    return houveEmpate

def menu():
    """
    Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
    """

    global optionSound, selectSound, somAtivo

    from pressAnyKey import optionKey
    from time import sleep

    opcaoAtual = 0
    opcaoSelecionada = 0
    select = 0
    
    while True:
        while select == 0:
            opcaoSelecionada = opcaoAtual

            if existeVLC == True:
                if somAtivo == True:
                    textoOpcao3 = 'Desativar som'
                else:
                    textoOpcao3 = 'Ativar som'
            else:
                textoOpcao3 = Fore.RED + 'PARA ATIVAR O SOM, É NECESSÁRIO INSTALAR VLC' + Style.RESET_ALL

            try:
                #Nota 1
                if somAtivo == True:
                    optionSound.stop()
            except:
                    ()
            if opcaoAtual == 0:
                try:
                    #Nota 1
                    if somAtivo == True:
                        optionSound.play()
                except:
                    ()
                os.system('cls')
                print('\t4 EM LINHA\n-> Jogar\nSair\n{}'.format(textoOpcao3))
                opcaoAtual, select = optionKey('ctrl direito', 1, 'seta abaixo')
                
                sleep(0.1)
            elif opcaoAtual == 1:
                try:
                    #Nota 1
                    if somAtivo == True:
                        optionSound.play()
                except:
                    ()
                os.system('cls')
                print('\t4 EM LINHA\nJogar\n-> Sair\n{}'.format(textoOpcao3))
                opcaoAtual, select = optionKey('ctrl direito', 0, 'seta acima', 2, 'seta abaixo')
                
                sleep(0.1)
            elif opcaoAtual == 2:
                try:
                    #Nota 1
                    if somAtivo == True:
                        optionSound.play()
                except:
                    ()
                os.system('cls')
                print('\t4 EM LINHA\nJogar\nSair\n-> {}'.format(textoOpcao3))
                opcaoAtual, select = optionKey('ctrl direito', 1, 'seta acima')
                
                sleep(0.1)
        
        if opcaoSelecionada == 2:
            configurarSom()
            break
        else:
            break
    

    try:
        #Nota 1
        if somAtivo == True:
            selectSound.play()
    except:
        ()
    

    return opcaoSelecionada

def selecionarColuna(lista, listaColunas, nJogador, listaNomes):
    """
    Esta é a tela inicial do jogo. Nela, o utilizador poderá escolher uma das opções.
    """
    from pressAnyKey import optionKey
    from time import sleep

    global optionSound, selectSound

    opcaoAtual = int(0)
    
    opcaoSelecionada = int(0)
    select = int(0)
    colunaAtual = int(0)
    colMinima = int(0)
    while listaColunas[colMinima] < 0:
        colMinima += 1
    colMaxima = int(6)
    while listaColunas[colMaxima] < 0:
        colMaxima -= 1

    while True:
        opcaoSelecionada = opcaoAtual

        if colunaAtual < colMinima:
            colunaAtual = colMinima
        elif colunaAtual > colMaxima:
            colunaAtual = colMaxima

        os.system('cls')
        if nJogador == 1:
            print('É a vez de ' + Fore.RED + '{}'.format(listaNomes[nJogador-1]) + Fore.RESET)
        elif nJogador == 2:
            print('É a vez de ' + Fore.YELLOW + '{}'.format(listaNomes[nJogador-1]) + Fore.RESET)
        gerarTabuleiro(lista, colunaAtual, listaColunas[colunaAtual])
        opcaoAtual, select = optionKey('ctrl direito', 1, 'seta à direita', 0, 'seta à esquerda')

        sleep(0.25)

        try:
            #Nota 1
            if somAtivo == True:
                optionSound.stop()
        except:
            ()

        if select == 0:
            if opcaoAtual == 1:
                try:
                    #Nota 1
                    if somAtivo == True:
                        optionSound.play()
                except:
                    ()
                colunaAtual += 1
                try:
                    while listaColunas[colunaAtual] < 0:
                        colunaAtual += 1
                except:
                    colunaAtual -= 1
            else:
                try:
                    #Nota 1
                    if somAtivo == True:
                        optionSound.play()
                except:
                    ()   
                colunaAtual -= 1
                try:
                    while listaColunas[colunaAtual] < 0:
                        colunaAtual -= 1
                except:
                    colunaAtual += 1
                

            
        else:
            try:
                #Nota 1
                if somAtivo == True:
                    selectSound.stop()
                    selectSound.play()
            except:
                ()
            break
    

    return colunaAtual

def nomearJogadores(lista):
    """
    Esta função serve para nomear os jogadores do 4 em linha.
    """
    os.system('cls')

    for i in range(2):
        if i == 0:
            n = Fore.RED + '1' + Style.RESET_ALL
        else:
            n = Fore.YELLOW + '2' + Style.RESET_ALL
        
        lista.append(input('Nome do jogador {}: '.format(n)))
        if lista[i].replace(' ','') == '':
            del lista[i]
            lista.insert(i, 'Jogador {}'.format(i + 1))
        try:
            if somAtivo == True:
                selectSound.stop()
                selectSound.play()
        except:
            ()

def configurarSom():
    try:
        global somAtivo
        if somAtivo == True:
            somAtivo = False
        elif somAtivo == False:
            somAtivo = True
    except:
        ()

tabuleiro = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]] # Configuração do tabuleiro do 4 em linha

linhaLivre = [5,5,5,5,5,5,5] # Determina a última linha lívre de cada coluna

coodernadasLinha = []

jogador = 2
nomeJogador = []

sair = 0
vence = False

if existeVLC == False:
    select = 0
    while select == 0:
        os.system('cls')
        print('\tAtenção!\nPara que o programa tenha o som, é necessário que o programa VLC esteja instalado no seu computador.\nLink para instalar o VLC: https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe#google_vignette\n\nPressione CTRL para continuar')
        select = optionKey('ctrl direito')
        sleep(0.25)



while True:
    erro = 0
    while erro == 0:
        opcao = menu()
        if opcao == 1: # Se for acionada a opção 0, então a variável sair terá como valor 1 e será feito um break ao loop while
            sair = 1
            break
        elif opcao == 0: # Se for acionada a opção 1, então será acionado um loop while onde o jogo será iniciado.
            nomearJogadores(nomeJogador)
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
                colunaEscolhida = selecionarColuna(tabuleiro, linhaLivre, jogador, nomeJogador)
                coodernadas(colunaEscolhida, linhaLivre[colunaEscolhida], tabuleiro, jogador, linhaLivre)
                
                    

            os.system('cls')
            if vence == True:
                if jogador == 1:
                    print('{} vence!'.format(Fore.RED + nomeJogador[jogador-1] + Style.RESET_ALL))
                else:
                    print('{} vence!'.format(Fore.YELLOW + nomeJogador[jogador-1] + Style.RESET_ALL))
                
                if somAtivo == True:
                    victorySound.play()
            elif empate ==  True:
                print('Houve um empate.')
            gerarTabuleiro(tabuleiro, listaCoodernadas=coodernadasLinha)
            print('Pressione CTRL para continuar. ')
            select = 0
            while select == 0:
                select = optionKey('ctrl direito')
                sleep(0.25)
            reiniciar(tabuleiro, linhaLivre)
            jogador = 2
            try:
                #Nota 1
                if somAtivo == True:
                    victorySound.stop()
            except:
                ()
    if sair == 1:
        break