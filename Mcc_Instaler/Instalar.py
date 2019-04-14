import os
import time
from colorama import Fore, Back

def get_user_mongo(usuario):
    
    mongo_db = usuario.split('.')
    usuario_certo =  mongo_db[1] + '_MCC'
    return usuario_certo

def get_user_new_mongo():
    arquivo = 'whoami.txt'
    shell('sudo whoami > {}'.format(arquivo))
    shell('sudo chmod 777 ~/{}'.format(arquivo))
    time.sleep(2)
    print('chmod on')
    time.sleep(2)
    file = open(arquivo, 'r')
    print('abri o arquivo')
    time.sleep(2)
    for line in file:
        user = line.split('.')
        nome_certo = user[0] + '_' + user[1]
        return nome_certo

def get_user():
    arquivo = 'whoami.txt'
    shell('whoami > {}'.format(arquivo))
    file = open(arquivo, 'r')
    for line in file:
        user = line.split('\n')
        
        return user[0]

def verificar_install(nome_pacote):
    nome_teste = 'teste.txt'
    if shell('rpm -qa |  grep {} > {}'.format(nome_pacote,nome_teste)):
        file = open(nome_teste, 'r')
        for line in file:
            
            if line.startswith(nome_pacote):
                
                return True
            else:
                return False


    

# Método utilizado para verificar a execução dos comandos no shell - OK
def shell(comando):

    # Executando o comando no shell
    confirmar = os.system(comando)

    # Definindo os retornos do método, onde True "sucesso" e False "falhou"
    if confirmar != 1:
        return True
    else:
        return False

    

# Método responsável por verificar a instalação do node
def testar_node(usuario):

    # Definindo o caminho do instalador ~/Mcc_Instaler
    caminho_intalador = '/home/{}/Mcc_Instaler/'.format(usuario)
    # Definindo o nome do arquivo de texto
    node__txt = 'node_versao.txt'
    # Realizando a verificação da versão do node, e alocando o retorno no arquivo denominado acima
    os.system('node --version > {}'.format(caminho_intalador+node__txt))
    # ler o retorno obtido acima
    arquivo = ler_arquivo(caminho_intalador, node__txt)
    # Se o arquivo tiver algo escrito, o método retorna um True, caso contrário ele retorna False
    if arquivo.__len__() > 0:
        versao_do_node = arquivo[0]
        print(Fore.GREEN+'Node já instalado.\n     ->Versão: {}'.format(versao_do_node))
        print(Fore.RESET + Back.RESET)
        return True
    else:
        return False

# Método responsável pela leitura dos arquivos - OK
def ler_arquivo(caminho_do_arquivo ,nome_do_arquivo):
    # Abrir o arquivo(nome_do_arquivo).
    nome_ler = caminho_do_arquivo+nome_do_arquivo
    comando_testar = 'cd {}'.format(caminho_do_arquivo)

    try:
        os.chdir(caminho_do_arquivo)
    except FileNotFoundError:
        print('Não foi possível realizar o chdir.')


    if shell(comando_testar):

        file = open(nome_ler, 'r')
        

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
def escrever_arquivo_configjson(usuario):
    # definindo o usuário, nome do arquivo e o caminho para criação do mesmo
    nome = 'config.json'
    caminho = '/home/{}/'.format(usuario)
    arquivo_caminho = caminho + '{}'.format(nome)

    # verificando a existencia do caminho informado
    if shell('cd {}'.format(caminho)):

        # Abrir o arquivo em formato de escrita
        file = open(arquivo_caminho, 'w')


        # Definindo o: Usuário, senha, ip, porta e nome do banco
        
        user = input(Back.BLUE+"Insira o usuário para acessar o MongoDB: ")
        senha =  input(Back.BLUE+"Insira a senha para acessar o MongoDB: ")
        print(Back.RESET)
        ip = 'cluster01-jmpzs.mongodb.net' 
        # input(Fore.WHITE+ Back.BLUE +'Insira um ip para o banco MongoDB: ')
        # print(Fore.RESET+Back.RESET)
        porta = '27017'
        try: 
            nome_do_banco = get_user_mongo(usuario)
            nome_do_banco =nome_do_banco.upper()
        except IndexError:
            print('Nome de usuário no sigular,  banco referenciado somente como {}'.format(usuario))
            nome_do_banco = usuario.capitalize

        linha = '"database": "mongodb+srv://{}:{}@{}/{}?retryWrites=true""'.format(user, senha, ip, nome_do_banco)

        # Alocando o texto a ser escrito na variavel escrever
        escrever = '{\n' \
                   '    "mongo": {\n' +linha +'\n' +'    }\n' \
                   '}\n'

        # Escrever no arquivo a estrutura montada com os valores corretos.
        file.write(escrever)

        # Fechar o arquivo aberto e informar que foi possivel escrever no diretorio especificado
        file.close()
        print(Fore.GREEN + Back.BLACK +'\n\nArquivo "{}" criado com sucesso!'.format(arquivo_caminho))
        print(Fore.RESET+Back.RESET)
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
    if shell('sudo cp {} {}'.format(nome, caminho+nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!'.format(nome, caminho))
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))

# Método para alocar o arquivo .bash_profile no diretório correto - VERIFICAR PARA UTILIZAR NA MAO
def alocar_bashprofile(usuario):
    # Definindo o caminho e o nome do arquivo

    caminho = '/home/{}/'.format(usuario)
    nome = '.bash_profile'


    # Verificação, onde caso consigamos copiar o arquivo recebemos um retorno informando sobre isto.
    if shell('cp {} {}'.format(nome, caminho + nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!')
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))

# Método para alocar o arquivo config no diretório correto - OK
def alocar_selinux(usuario):
    # Definindo o caminho e o nome do arquivo
    caminho = '/etc/selinux/'
    caminho_instalador = '/home/{}/Mcc_Instaler/'.format(usuario)
    nome = 'config'
    print(caminho+nome)

    # Verificação, onde caso consigamos copiar o arquivo recebemos um retorno informando sobre isto.
    if shell('sudo cp {} {}'.format(caminho_instalador+nome, caminho + nome)):
        print('Arquivo "{}" movido para "{}" com sucesso!'.format(nome, caminho))
    else:
        print('Não foi possível mover o arquivo {} para o diretório {}'.format(nome, caminho))

# Método para alocar o arquivo zipado do node - OK
def alocar_instaladornode(usuario):
    caminho = '/home/{}/'.format(usuario)
    nome_do_node = 'node-v8.15.0.tar.gz'
    node_descom = 'node-v8.15.0'
    caminho_intalador = '/home/{}/Mcc_Instaler/'.format(usuario)
    if shell('cp {} {}'.format(caminho_intalador+nome_do_node, caminho+nome_do_node)):

        
        os.chdir(caminho)

        if shell('sudo tar -xvf {}'.format(caminho+nome_do_node)):
            print('Node descompactado com sucesso')
            os.chdir('/home/{}/node-v8.15.0'.format(usuario))

            shell('sudo ./configure')
            os.chdir('/home/{}/node-v8.15.0'.format(usuario))
            shell('pwd')
            shell('sudo make')
            os.chdir('/home/{}/node-v8.15.0'.format(usuario))
            shell('pwd')
            shell('sudo make install')
            os.chdir('/home/{}/Mcc_Instaler/'.format(usuario))
            return True

    else:
        print('Não foi possível alocar o node, no caminho "{}"'.format(caminho))
        return False

# Método responsável por realizar a instalação do ORACLE
def alocar_instaladororcl(usuario):

    caminho = '/home/{}/'.format(usuario)
    caminho_instalador = caminho + 'Mcc_Instaler/'
    print('Caminho do home: {}'.format(caminho))
    print('Caminho do instalador: {}'.format(caminho_instalador))
    nome_do_oracle = 'oracle-instantclient18.3-basic-18.3.0.0.0-3.x86_64.rpm'
    if shell('sudo cp {} {}'.format(caminho_instalador+nome_do_oracle, caminho + nome_do_oracle)):
        print('Oracle alocado em "{}" com sucesso!\n'.format(caminho+nome_do_oracle))
        print('Iniciando procedimento de instalação...')
        if shell('sudo yum localinstall {}'.format(caminho+nome_do_oracle)):
            print('Oracle instalado com sucesso!')
            return True
    else:
        print('Não foi possível alocar o node, no caminho "{}"'.format(caminho))
        return False




# alocar_bashprofile()







# ------------------------------------------------------------------------------------------------
def instalar_prerequisitos():

    usuario = get_user()
    
    # Boas vindas ao instalador
    print(Fore.RESET + Back.RESET +'Bem-vindo ao instalador do MCC!\n'
          'Por favor, insira as informações corretas para que a instalação ocorra corretamente.\n Preste atenção nos logs, alguymas etapas precisam da sua confirmação com Y ou N.\n'
          '\nO manual do instalador está disponível no link: '+ Back.LIGHTWHITE_EX + Fore.MAGENTA+'"http://jira.prodatamobility.com.br:8090/confluence/pages/viewpage.action?pageId=26149257"' + Fore.RESET + Back.RESET+
          '\nInstalador desenvolvido por: Lucas Silveira Vieira (Matriz) - Prodata Mobility Brasil.')

    while True:
        try:
            usuario_pergunta = int(input(Fore.WHITE + Back.BLUE +'Detectado o usuário: {}'.format(usuario)
            +'\nDeseja realizar a instalação no usuário detectado? (1)Sim (2)Não. \n'
            +'Digite sua resposta: '))
            print(Fore.RESET + Back.RESET)
        except ValueError: 
            print('Insira um valor numérico em sua resposta!')
            time.sleep(2)
        
        try:

            if usuario_pergunta == 1:
                print('\nIniciando o processo de instalação no usuário {}'.format(usuario))
                break
            elif usuario_pergunta == 2:
                print('\nPor favor, acesse a máquina com o usuário desejado.')
                time.sleep(3)
                return
            else:
                print('\nPor favor responda com "1" ou "2".\n') 
                time.sleep(3)
        except UnboundLocalError:
            print('')


    # Definição dos diretórios com base no usuário informado
    caminho_mcc = '/home/{}/mcc'.format(usuario)
    caminho_mcc_lib = '/home/{}/mcc/lib'.format(usuario)
    caminho_mcc_bin = '/home/{}/mcc/bin'.format(usuario)

    caminho_private = '/home/{}/key/'.format(usuario)
    caminho_public = '/home/{}/public/'.format(usuario)


    nome_key = 'privatekey.pem'
    nome_public = 'publickey.pem'

    alocar_public = 'Mcc_Instaler/{}'.format(nome_public)
    
    alocar_key = 'Mcc_Instaler/{}'.format(nome_key)
    
    while True:
        try:
            os.chdir(caminho_private)
            os.chdir('/home/')
            break
        except FileNotFoundError:
            print('Caminho "{}" não definido, realizando criação...'.format(caminho_private))
            shell('mkdir {}'.format(caminho_private))
            time.sleep(2)
    
    while True:
        try:
            os.chdir(caminho_public)
            os.chdir('/home/')
            break
        except FileNotFoundError:
            print('Caminho "{}" não definido, realizando criação...'.format(caminho_public))
            shell('mkdir {}'.format(caminho_public))
            time.sleep(2)
        

    print('Iniciando procedimento de criação das pastas do MCC...\n\n\n')
    time.sleep(3)
# Verificação e criação do caminho mcc
    try:
        os.chdir(caminho_mcc)
        print(Fore.GREEN +'Diretório {} já existente.'.format(caminho_mcc))
        print(Fore.RESET + Back.RESET)
    except FileNotFoundError:
        print('Não foi localizado o caminho ~/mcc.\nRealizando a criação do diretório.')
        shell('mkdir {}'.format(caminho_mcc))


    time.sleep(1)

# Verificação e criação do diretório mcc/lib
    try:
        # Comando para trocar para o diretório mcc/lib
        os.chdir(caminho_mcc_lib)
        # Retorno para o implantador
        print(Fore.GREEN +'Diretório {} existente'.format(caminho_mcc_lib))
        print(Fore.RESET + Back.RESET)
    # Tratando a a exception gerada caso não exista o diretório mcc/lib
    except FileNotFoundError:
        # Retorno para o implantador
        print('Não foi localizado o diretório {}.\nRealizando a criação do diretório.'.format(caminho_mcc_lib))
        shell('mkdir {}'.format(caminho_mcc_lib))


    # Temporizador para que seja possível a leitura dos logs em tempo real    
    time.sleep(1)


# Verificação e criação do diretório mcc/bin
    try:
        # ir até o diretório mcc/bin
        os.chdir(caminho_mcc_bin)
        # Retorno para o implantador
        print(Fore.GREEN+ 'Diretório {} existente'.format(caminho_mcc_bin))
        print(Fore.RESET + Back.RESET)
        # Tratando a exception gerada caso nao exista o diretório mcc/bin
    except FileNotFoundError:
        # Retorno para o implantador
        print('Não foi localizado o diretório {}.\nRealizando a criação do diretório.'.format(caminho_mcc_bin))
        # Comando para criar a pasta mcc/bin    
        shell('mkdir {}'.format(caminho_mcc_bin))


    # Realizar a criação do arquivo config.json
    print('\n\n\n----------Iniciando instalação do MONGODB----------\n\n\n')
    print('Iniciando a criação do arquivo config.json para conexão ao MongoDB.')
    # Chamada ao método responsável pela criação do Config.json 
    escrever_arquivo_configjson(usuario)
    print(Fore.GREEN +'\n\nArquivo Config.json criado com sucesso.') 

    print(Fore.RESET + Back.RESET+'\n\n\n----------Iniciando instalação de pré-requisitos----------\n\n\n')

    # Atualização do gerenciador de pacotes do LINUX(YUM)
    print('\n\n\n----------Atualizando o pacote YUM----------\n\n\n')
    # Temporizador para que seja possível acompanhar o log em tempo real
    time.sleep(2)

    # Realizar a instalação do editor de textos nano
    print(Fore.RESET+Back.RESET+'\n\n\n----------Iniciando instalação do Nano----------\n\n\n')
    if shell('sudo yum install nano.x86_64'):
        print(Fore.GREEN+'\n\nNano instalado com sucesso.')
    

    # Realizar a instalação do Epel-release
    print(Fore.RESET+Back.RESET+'\n\n\n----------Iniciando instalação do Epel Release----------\n\n\n')

    # checar a instalação do epel-release com o npm -na
    
    os.chdir('/home/{}'.format(usuario))


    if verificar_install('epel-release'):
        print(Fore.GREEN+'Epel-release já instalado.')
        print(Fore.RESET + Back.RESET)
        time.sleep(2)
    else:
        shell('sudo yum install epel-release.noarch')
        print(Fore.GREEN+'Epel Release instalado com sucesso.\n')

    # Realizar a instalação do python-pip
    print(Fore.RESET+Back.RESET+'\n\n\n----------Iniciando instalação do PIP----------\n\n\n')
    
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    shell('sudo yum install python-pip')

    # Realizar o update do pip
    print('Iniciando a atualização do PIP...')
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    shell('sudo pip install --upgrade pip')
    print(Fore.GREEN+'Pip instalado/atualizado com sucesso.\n')


    # Realizara instalação do Bzip, Gcc e Gcc-c++
    print(Fore.RESET+Back.RESET+'\n\n\n----------Pré-requisitos para instalar o NODE----------\n\n\n')
    print('   -Gcc'
          '\n   -Gcc-C++'
          '\n   -Bzip\n')
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    # Instalando os pacotes
    shell('sudo yum install gcc gcc-c++ bzip2')
    print(Fore.GREEN+'\n\nPré-requisitos do node instalados com sucesso.')

    
    # Verificar e caso seja inexistente, realizar a instalação do oracle
    
    print(Fore.RESET+Back.RESET+'\n\n\n---------Iniciando instalação do Oracle Client----------\n\n\n')
    # Tentar chegar a pasta da isntalaçao do oracle para verificar se ja existe
    if verificar_install('oracle'):
        print(Fore.GREEN + 'Oracle já instalado.')
        print(Fore.RESET + Back.RESET)
        time.sleep(2)              
           
    else:
        alocar_instaladororcl(usuario)
           
        

    # Verificar a instalação do node, caso inexistente instalar
    print(Fore.RESET + Back.RESET +'\n\n\n----------Iniciando instalação do Node----------\n\n\n')
        
    if testar_node(usuario):
        print('\n')

    else:
        alocar_instaladornode(usuario)
        print(Fore.GREEN+ '\nNode instalado com sucesso.')
    # Alocar o arquivo de permições do Linux
    print(Fore.RESET + Back.RESET +'Alterando as configurações de conexão do Linux...')
    alocar_selinux(usuario)

    # Realizar o comando set permissive
    print('Liberando acesso à este servidor.')
    if shell('sudo setenforce permissive'):
        print(Fore.GREEN+'Liberação de acesso ao servidor realizado com sucesso')
    else:
        print(Fore.RED+'Não foi possível realizar a liberação de porta.')

    # Procedimentos para finalizar instalação do ORACLE
    os.chdir('/usr/lib/oracle/18.3/client64/lib')
    shell('sudo ln -s libclntsh.so.18.1 libclntsh.so')
    os.chdir('/home/{}/Mcc_Instaler'.format(usuario))


    # Procedimentos petinentes ao NPM e instalação dos módulos em node
    print(Fore.RESET+Back.RESET+'\n\n\n----------Iniciando configuração do NPM----------\n\n\n')
    caminho = '/home/{}/mcc'.format(usuario)
    if shell('npm set prefix {}'.format(caminho)):
        print(Fore.RESET+Back.RESET+'Prefixo do NPM redirecionado para {}\n'.format(caminho))
        print('Para continuar com os procedimentos do NPM, devemos referenciar o repositório(Verdaccio) da Martonis.'
        +' O acesso padrão para este repositório, encontra-se em: http://dev01.martonis.net:11000.\n')
        verdaccio = input(Fore.WHITE + Back.BLUE +'Insira o acesso ao verdaccio da Martonis: ')
        shell('npm set registry {}'.format(verdaccio))
        shell('npm login')

        # Os valores do Mcc-startup voram removidos do instalador
        # print(Fore.WHITE + Back.BLACK +'Iniciando a instalação do módulo STARTUP.\n')
        # shell('npm i -g mcc.startup@19.3.1')
        # print(Fore.GREEN +'Fim da instalação do módulo STARTUP\n\n')
        # print(Fore.RESET)

        print('\n\nIniciando a instalação do módulo BROKER.\n')
        shell('npm i -g mcc.broker@19.4.1')
        print(Fore.GREEN +'Fim da instalação do módulo BROKER\n\n')
        print(Fore.RESET)

        print('\n\nIniciando a instalação do módulo PORTAL.\n')
        shell('npm i -g mcc.portal@19.1.1')
        print(Fore.GREEN +'Fim da instalação do módulo PORTAL\n\n')
        print(Fore.RESET)

        print('\n\nIniciando a instalação do módulo PROCESSOR.\n')
        shell('npm i -g mcc.processor@19.4.1')
        print(Fore.GREEN +'Fim da instalação do módulo PROCESSOR\n\n')
        print(Fore.RESET)

        print('\n\nIniciando a instalação do módulo GAMA.\n')
        shell('npm i -g msi.gama@0.3.38')
        print(Fore.GREEN +'Fim da instalação do módulo GAMA\n\n')
        print(Fore.RESET)

        shell('npm i -g forever')
    else:
        # Caso não for possível alocar a ~/mcc, damos o retorno para o Implantador
        # OBSERVAÇÂO - Podemos realizar uma nova verificação neste ponto das pastas ~/mcc e ~/mcc/lib e ~/mcc/bin
        print(Fore.RED+'Não foi possível definir o diretório ~/mcc como pasta global ao NPM')
        
instalar_prerequisitos()

print(Fore.GREEN+'Fim da instalação dos pré requisitos e módulos em node.'+
'Continuar os procedimentos a partir da edição das variáveis de ambiente.')
print(Fore.RESET)


