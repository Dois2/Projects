import os

# Método utilizado para verificar a execução dos comandos no shell - OK
def shell(comando):

    # Executando o comando no shell
    confirmar = os.system(comando)

    # Definindo os retornos do método, onde True "sucesso" e False "falhou"
    if confirmar != 1:
        return True
    else:
        return False

def ler_arquivo(nome_do_arquivo):
    # Abrir o arquivo(nome_do_arquivo).
    nome_ler = nome_do_arquivo
    file = open(nome_ler, 'r')


    # Estrutura de repetição, reponsável por contruir uma string com os valores lidos do arquivo aberto à cima.

    leitura_arquivo = file.readlines()


    return leitura_arquivo



def testar_node():
    node__txt = 'node_versao.txt'
    os.system('node --version > {}'.format(node__txt))
    arquivo = ler_arquivo(node__txt)
    if arquivo.__len__() > 0:
        versao_do_node = arquivo[0]
        print('Node enconstra-se na versão: {}'.format(versao_do_node))
        return True
    else:
        print('Node não encontrado')
        return False


