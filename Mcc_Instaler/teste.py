import os


def shell(comando):

    # Executando o comando no shell
    confirmar = os.system(comando)

    # Definindo os retornos do método, onde True "sucesso" e False "falhou"
    if confirmar != 1:
        return True
    else:
        return False

def verificar_install(nome_pacote):
    nome_teste = 'teste.txt'
    if shell('rpm -qa |  grep {} > {}'.format(nome_pacote,nome_teste)):
        file = open(nome_teste, 'r')
        for line in file:
            
            if line.startswith(nome_pacote):
                
                return True
            else:
                return False
                


pacote = 'epel-releaseasdasdasdasdasd'

if verificar_install(pacote):
    print('true')
else:
    print('false')