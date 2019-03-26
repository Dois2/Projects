import time

import os

def fluxo_instalacao():
      print('Bem vindo ao assistente de instalação do MCC!'
            '\nPor favor, escolha uma de nossas opções:'
            '\n   (1)Verificar os pré requisitos.'
            '\n   (2)Instalar módulos.')
      while True:
            escolha = int(input('Escolha uma opção: '))
            if escolha == 1:
                  im.InstalManager.teste_prerequisitos(im)
                  break
            elif escolha == 2:
                  im.InstalManager.pre_install(im)
                  break
            else:
                  print('Escolha uma opção válida!')



fluxo_instalacao()