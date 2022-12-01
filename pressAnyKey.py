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