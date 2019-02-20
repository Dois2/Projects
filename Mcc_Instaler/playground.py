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

# Método responsável pela leitura dos arquivos - OK
def ler_arquivo(caminho_do_arquivo ,nome_do_arquivo):
    # Abrir o arquivo(nome_do_arquivo).
    nome_ler = caminho_do_arquivo+nome_do_arquivo
    comando_testar = 'cd {}'.format(caminho_do_arquivo)
    if shell(comando_testar):

        file = open(nome_ler, 'r')
        print(file)

        # Estrutura de repetição, reponsável por contruir uma string com os valores lidos do arquivo aberto à cima.

        leitura_arquivo = file.readlines()

        file.close()

        return leitura_arquivo
    else:
        print('Arquivo/Caminho não encontrado.')
        return False

# Método utilizado para escrever o arquivo mongodb-org.repo - OK
def escrever_arquivo_mongorepo():

    # definindo o usuário, nome do arquivo e o caminho para criação do mesmo
    usuario = input('Informe o usuário utilizado nesta instalação: ')
    nome = 'mongodb-org.repo'
    caminho ='/etc/yum.repos.d/'

    # verificando a existencia do caminho informado
    if shell('cd {}'.format(caminho)):

        # Abrir o arquivo em formato de escrita
        file = open(caminho+nome, 'w')

        # Alocando o texto a ser escrito na variavel escrever
        escrever = '[mongodb-org-4.0]\n' \
                   'name=MongoDB Repository\n' \
                   'baseurl=https://repo.mongodb.org/yum/redhat/7Server/mongodb-org/4.0/x86_64/\n' \
                   'gpgcheck=1\n' \
                   'enabled=1\n' \
                   'gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc\n'

        # Escrever no arquivo a estrutura montada com os valores corretos.
        file.write(escrever)

        # Fechar o arquivo aberto e informar que foi possivel escrever no diretorio especificado
        file.close()
        print('Arquivo "{}" criado com sucesso!'.format(caminho+nome))
    else:
        # Caso caminho seja inválido, exibimos a mensagem que não foi possivel escrever
        print('Caminho "{}" inexistente'.format(caminho))

# Método utilizado para escrever o arquivo config.json - OK
def escrever_arquivo_configjson():
    # definindo o usuário, nome do arquivo e o caminho para criação do mesmo
    usuario = input('Informe o usuário utilizado nesta instalação: ')
    nome = 'config.json'
    caminho = '/home/{}/'.format(usuario)
    arquivo_caminho = caminho + '{}'.format(nome)

    # verificando a existencia do caminho informado
    if shell('cd {}'.format(caminho)):

        # Abrir o arquivo em formato de escrita
        file = open(arquivo_caminho, 'w')


        # Definindo o: Usuário, senha, ip, porta e nome do banco
        user= input('Insira um usuário válido para o banco MongoDB: ')
        senha = input('Insira uma senha válida para o banco MongoDB: ')
        ip = input('Insira um ip válido para o banco MongoDB: ')
        porta = input('Insira uma porta válida para o banco MongoDB: ')
        nome_do_banco = input('Insira um nome válido para o banco MongoDB: ')
        linha = '"database": "mongodb://{}:{}@{}:{}/{}"'.format(user, senha, ip, porta, nome_do_banco)

        # Alocando o texto a ser escrito na variavel escrever
        escrever = '{\n' \
                   '    "mongo": {\n' +linha +'\n' +'    }\n' \
                   '}\n'

        # Escrever no arquivo a estrutura montada com os valores corretos.
        file.write(escrever)

        # Fechar o arquivo aberto e informar que foi possivel escrever no diretorio especificado
        file.close()
        print('Arquivo "{}" criado com sucesso!'.format(arquivo_caminho))
    else:
        # Caso caminho seja inválido, exibimos a mensagem que não foi possivel escrever
        print('Caminho "{}" inexistente'.format(caminho))

# Método utilizado para escrever o arquivo mongo-nproc - OK
def escrever_arquivo_mongonproc():
    # definindo o nome do arquivo e o caminho para criação do mesmo
    nome = '99-mongodb-nproc.conf'
    caminho = '/etc/security/limits.d/'
    # caminho = 'C:\\Users\\lucas.vieira\\Documents\\CONTROLE\\MCC\\PRODUCAO\\'
    arquivo_caminho = caminho + '{}'.format(nome)

    # verificando a existencia do caminho informado
    if shell('cd {}'.format(caminho)):

        # Abrir o arquivo em formato de escrita
        file = open(arquivo_caminho, 'w')


        # Alocando o texto a ser escrito na variavel escrever
        escrever = 'mongod soft nofile 64000\n' \
                   'mongod hard nofile 64000\n' \
                   'mongod soft nproc 64000\n' \
                   'mongod hard nproc 64000'

        # Escrever no arquivo a estrutura montada com os valores corretos.
        file.write(escrever)

        # Fechar o arquivo aberto e informar que foi possivel escrever no diretorio especificado
        file.close()
        print('Arquivo "{}" criado com sucesso!'.format(arquivo_caminho))
    else:
        # Caso caminho seja inválido, exibimos a mensagem que não foi possivel escrever
        print('Caminho "{}" inexistente'.format(caminho))

# Método para alocar o arquivo mongod.conf no diretório correto - OK
def alocar_mongod():
    # Definindo o caminho e o nome do arquivo
    caminho = '/etc/'
    nome = 'mongod.conf'

    # Verificação, onde caso consigamos copiar o arquivo recebemos um retorno informando sobre isto.
    if shell('cp {} {}'.format(nome, caminho+nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!')
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))

# Método para alocar o arquivo .bash_profile no diretório correto - OK
def alocar_bashprofile():
    # Definindo o caminho e o nome do arquivo
    usuario = input('Informe o usuário para editar as variáveis de ambiente: ')
    caminho = '/home/{}/'.format(usuario)
    nome = '.bash_profile'


    # Verificação, onde caso consigamos copiar o arquivo recebemos um retorno informando sobre isto.
    if shell('cp {} {}'.format(nome, caminho + nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!')
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))

# Método para alocar o arquivo config no diretório correto - OK
def alocar_selinux():
    # Definindo o caminho e o nome do arquivo
    caminho = '/etc/selinux/'
    nome = 'config'
    print(caminho+nome)

    # Verificação, onde caso consigamos copiar o arquivo recebemos um retorno informando sobre isto.
    if shell('cp {} {}'.format(nome, caminho + nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!')
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))


alocar_selinux()


