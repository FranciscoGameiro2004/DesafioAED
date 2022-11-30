import os
from time import sleep

def optionKey(triggerKey, optionOne, keyOne, optionTwo=None, keyTwo=None):
    try:
        import keyboard
    except:
        from os import system
        system('pip install keyboard')
        import keyboard

    option= None
    trigger = False
    
    while True:
            if keyboard.is_pressed(keyOne) == True:
                option = optionOne
                return option, trigger
            if keyboard.is_pressed(triggerKey) == True:
                trigger = True
                return option, trigger
            if optionTwo != None and keyTwo !=None:
                if keyboard.is_pressed(keyTwo) == True:
                    option = optionTwo
                    return option, trigger

select = 0
opcao = 1
opcaoSelecionada = 1
while True:
    if select == 0:
        os.system('cls')
        if opcao == 1:
            print('-> Opção 1\nOpção 2\nOpção 3')
            opcaoSelecionada = opcao
            opcao, select = optionKey('enter', 2, 'seta abaixo')
            sleep(0.05)

        elif opcao == 2:
            print('Opção 1\n-> Opção 2\nOpção 3')
            opcaoSelecionada = opcao
            opcao, select = optionKey('enter', 3, 'seta abaixo', 1, 'seta acima')
            sleep(0.05)
        else:
            print('Opção 1\nOpção 2\n-> Opção 3')
            opcaoSelecionada = opcao
            opcao, select = optionKey('enter', 2, 'seta acima')
            sleep(0.05)


        
    else:
        break
os.system('cls')
print('Selecionou a opção {}'.format(opcaoSelecionada))