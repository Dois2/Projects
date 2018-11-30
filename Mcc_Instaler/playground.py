from teste import InstalManager
import re
import os
import time
import array as arr

def shell(mensagem):
    confirmar = os.system(mensagem)
    if confirmar != 1:
        return True
    else:
        return False

def pre_install():
    teste_prerequisitos = InstalManager.teste_prerequisitos(InstalManager)
    if teste_prerequisitos:
        funcionou = InstalManager.shell('sudo yum install python-pip')
        if funcionou:
            funcionou = InstalManager.shell('pip install --upgrade pip')






pre_install()




