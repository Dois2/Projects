import time
from teste import InstalManager
import os

print('Bem vindo ao assintente de instalação do MCC!'
      '\nAguarde enquanto estamos verificando os requisitos mínimos...')
time.sleep(3)

var = InstalManager()
var.teste_prerequisitos()
mensagem = var.instalation()
print(mensagem)










#nome_do_arquivo =  input('nome arquivo')
#var2 = InstalManager.ler_arquivo(InstalManager, nome_do_arquivo)
#print(var2)