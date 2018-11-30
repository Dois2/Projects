from teste import InstalManager
import re
import os
import time
import array as arr



def pre_install():
    teste_prerequisitos = InstalManager.teste_prerequisitos(InstalManager)
    if teste_prerequisitos:
        a =['sudo yum install python-pip', 'pip install --upgrade pip']
        for x in range(0, a.__len__()):
            funcionou = InstalManager.shell(a[x])
            if funcionou:
                x += 1
            else:
                break




pre_install()




