import os
import time
from colorama import Fore, Back



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
        print('Node encontra-se na versão: {}'.format(versao_do_node))
        return True
    else:
        print('Node não encontrado')
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
        user= input(Fore.WHITE + Back.BLUE +'De acordo com as premissas, devemos possuir um usuário, senha, ip, porta' 
        +' e nome do banco válidos para o MongoDB. Estas informações serão utilizadas para gerar o arquivo Config.json.\n'
        'Insira um usuário para o banco MongoDB: ')


        senha = input('Insira uma senha para o banco MongoDB: ')
        ip = input('Insira um ip para o banco MongoDB: ')
        porta = input('Insira uma porta para o banco MongoDB: ')
        nome_do_banco = input('Insira um nome para o banco MongoDB: ')
        linha = '"database": "mongodb://{}:{}@{}:{}/{}"'.format(user, senha, ip, porta, nome_do_banco)

        # Alocando o texto a ser escrito na variavel escrever
        escrever = '{\n' \
                   '    "mongo": {\n' +linha +'\n' +'    }\n' \
                   '}\n'

        # Escrever no arquivo a estrutura montada com os valores corretos.
        file.write(escrever)

        # Fechar o arquivo aberto e informar que foi possivel escrever no diretorio especificado
        file.close()
        print(Fore.WHITE + Back.BLACK +'Arquivo "{}" criado com sucesso!'.format(arquivo_caminho))
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

        print("Node alocado com sucesso!")
        print(caminho+nome_do_node)
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
        print('não foi possível alocar o node, no caminho "{}"'.format(caminho))
        return False

# Método responsável por realizar a instalação do ORACLE
def alocar_instaladororcl(usuario):

    caminho = Fore.RESET + Back.RESET +'/home/{}/'.format(usuario)
    caminho_instalador = caminho + 'Mcc_Instaler/'
    print('Caminho do home: {}'.format(caminho))
    print('Caminho do instalador: {}'.format(caminho_instalador))
    nome_do_oracle = 'oracle-instantclient18.3-basic-18.3.0.0.0-3.x86_64.rpm'
    if shell('sudo cp {} {}'.format(caminho_instalador+nome_do_oracle, caminho + nome_do_oracle)):
        print('Oracle alocado em "{}" com sucesso!\n'.format(caminho+nome_do_oracle))
        print('Iniciando procedimento de instalação...')
        if shell('sudo yum install {}'.format(caminho+nome_do_oracle)):
            print('Oracle instalado com sucesso!')
            return True
    else:
        print('Não foi possível alocar o node, no caminho "{}"'.format(caminho))
        return False




# alocar_bashprofile()







# ------------------------------------------------------------------------------------------------
def instalar_prerequisitos():

    # Boas vindas ao instalador
    print(Fore.RESET + Back.RESET +'Bem vindo ao instalador do MCC!\n'
          'Por favor, insira as informações corretas para que a instalação ocorra corretamente.\n'
          '\nO manual do instalador está disponível no link: '+ Back.LIGHTWHITE_EX + Fore.MAGENTA+'"http://jira.prodatamobility.com.br:8090/confluence/pages/viewpage.action?pageId=26149257"' + Fore.RESET + Back.RESET+
          '\nInstalador desenvolvido por: Lucas Silveira Vieira - PRODATA Mobility Brasil.')

    while True:
        usuario = input(Fore.WHITE + Back.BLUE +'Insira o usuário da VM em que será realizado a instalação.'
        +'\nAtenção: O usuário deve ser equivalente ao login utilizado no software BITVISE.\n'
        +'Digite o usuário: ')
        try:
            os.chdir('/home/{}'.format(usuario))
            print(Fore.WHITE + Back.BLACK +'Usuário válido')
            break
        except FileNotFoundError:
            print('Por favor insira um usuário válido.')






    # Definição dos diretórios com base no usuário informado
    caminho_mcc = '/home/{}/mcc'.format(usuario)
    caminho_mcc_lib = '/home/{}/mcc/lib'.format(usuario)
    caminho_mcc_bin = '/home/{}/mcc/bin'.format(usuario)


    print('Iniciando procedimento de criação das pastas do MCC...\n\n\n')
    time.sleep(3)
# Verificação e criação do caminho mcc
    try:
        os.chdir(caminho_mcc)
        print('Diretório {} existente.'.format(caminho_mcc))
    except FileNotFoundError:
        print('Não foi localizado o caminho ~/mcc.\nRealizando a criação do mesmo.')
        shell('mkdir {}'.format(caminho_mcc))


    time.sleep(1)

# Verificação e criação do diretório mcc/lib
    try:
        # Comando para trocar para o diretório mcc/lib
        os.chdir(caminho_mcc_lib)
        # Retorno para o implantador
        print('Diretório {} existente'.format(caminho_mcc_lib))
    # Tratando a a exception gerada caso não exista o diretório mcc/lib
    except FileNotFoundError:
        # Retorno para o implantador
        print('Não foi localizado o diretório {}.\nRealizando a criação do mesmo.'.format(caminho_mcc_lib))
        shell('mkdir {}'.format(caminho_mcc_lib))


    # Temporizador para que seja possível a leitura dos logs em tempo real    
    time.sleep(1)


# Verificação e criação do diretório mcc/bin
    try:
        # ir até o diretório mcc/bin
        os.chdir(caminho_mcc_bin)
        # Retorno para o implantador
        print('Diretório {} existente'.format(caminho_mcc_bin))
        # Tratando a exception gerada caso nao exista o diretório mcc/bin
    except FileNotFoundError:
        # Retorno para o implantador
        print('Não foi localizado o diretório {}.\nRealizando a criação do mesmo.'.format(caminho_mcc_bin))
        # Comando para criar a pasta mcc/bin    
        shell('mkdir {}'.format(caminho_mcc_bin))


    # Realizar a criação do arquivo config.json
    print('\n\n\n----------MONGODB----------\n\n\n')
    print('Iniciando composição e criação do arquivo config.json para conexão ao MongoDB.')
    # Chamada ao método responsável pela criação do Config.json 
    escrever_arquivo_configjson(usuario)

    # Atualização do gerenciador de pacotes do LINUX(YUM)
    print('\n\n\n----------YUM----------\n\n\n')
    print('Iniciando atualização do YUM.\n')
    # Temporizador para que seja possível acompanhar o log em tempo real
    time.sleep(2)
    # Comando para atualizar o YUM
    if shell('sudo yum update'):
        # Retorno para o implantador
        print('Gerenciador YUM atualizado com sucesso')
        # Temporizador para acompanhar o log em tempo real
        time.sleep(2)
    else:
        print('Erro ao atualizar o gerenciador YUM.')

    # Realizar a instalação do editor de textos nano
    print('\n\n\n----------NANO----------\n\n\n')
    print('Iniciando a instalação do editor NANO.')
    shell('sudo yum install nano.x86_64')

    # Realizar a instalação do Epel-release
    print('\n\n\n----------EPEL_RELEASE----------\n\n\n')
    print('Iniciando a instalação do EPEL-RELEASE.')
    shell('sudo yum install epel-release.noarch')


    print('\n\n\n----------PIP----------\n\n\n')
    # Realizar a instalação do python-pip
    print('Iniciando a instalação do PIP...')
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    shell('sudo yum install python-pip')

    # Realizar o update do pip
    print('Iniciando a atualização do PIP...')
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    shell('sudo pip install --upgrade pip')


    # Realizara instalação do Bzip, Gcc e Gcc-c++
    print('\n\n\n----------PRÉ_REQUISITOS_NODE----------\n\n\n')
    print('Iniciando a instalação dos componentes: '
          '\n   -Bzip'
          '\n   -Gcc'
          '\n   -Gcc-C++')
    # Temporizador para conseguir acompanhar o log em tempo real
    time.sleep(3)
    # Instalando os pacotes
    shell('sudo yum install gcc gcc-c++ bzip2')

    # Verificar e caso seja inexistente, realizar a instalação do oracle
    try:
        # Tentar chegar a pasta da isntalaçao do oracle para verificar se ja existe
        os.chdir('/usr/lib/oracle/18.3')
        # Retorno ao implantador
        print('\n\n\n---------ORACLE----------\n\n\n')
        print('Instalação do oracle localizada em: /usr/lib/oracle/18.3\n\n\n')
        # Criando a estrutura de repetição para verificar se quer re-instalar o oracle
        sair_reinstal =0
        while sair_reinstal ==0:
            # Pergunta que controla a re-instalação
            reinstalar_oracle = input(Fore.WHITE + Back.BLUE +'Deseja instalar novamente o Oracle?\n (1) Sim (2) Não: ')
            # Controle que garante que o usuário escolha 1 ou 2    
            if reinstalar_oracle == '1' or reinstalar_oracle == '2':
                # Se a resposta do implantador atender 1 ou 2, saimos da estrutura de repetição
                sair_reinstal = 1
                # Se a resposta for 1, ele re-instala
                if reinstalar_oracle == '1':
                    # Método que realiza a instalação
                    alocar_instaladororcl(usuario)
            else:
                # Retorno para o implantador
                print(Fore.WHITE + Back.BLACK +'Por favor, selecione uma opção válida...')
    except FileNotFoundError:
        # Se não achar a pasta do Oracle, instalamos diretamente sem perguntas pro implantador
        alocar_instaladororcl(usuario)

    # Verificar a instalação do node, caso inexistente instalar
    print('\n\n\n----------NODE----------\n\n\n')
    if testar_node(usuario):
        # Mesma estrutura de repetição para o Oracle foi utilizada para o node
        sair_reinstalnode = 0
        
        while sair_reinstalnode ==0:
            pergunta = input(Fore.WHITE + Back.BLUE +'Deseja instalar novamente o Node?\n'
                             '(1)Sim (2)Não: ')
            if pergunta == '1' or pergunta == '2':
                sair_reinstalnode = 1
                if pergunta =='1':
                    alocar_instaladornode(usuario)
            else:
                print(Fore.WHITE + Back.BLACK +'Insira uma opção válida!')
    else:
        alocar_instaladornode(usuario)
    # Alocar o arquivo de permições do Linux
    print(Fore.WHITE + Back.BLACK +'Alterando as configurações de conexão do Linux...')
    alocar_selinux(usuario)

    # Realizar o comando set permissive
    print('Liberando acesso à este servidor.')
    if shell('sudo setenforce permissive'):
        print('Liberação de acesso ao servidor realizado com sucesso')
    else:
        print('Não foi possível realizar a liberação de porta.')

    # Procedimentos para finalizar instalação do ORACLE
    os.chdir('/usr/lib/oracle/18.3/client64/lib')
    shell('sudo ln -s libclntsh.so.18.1 libclntsh.so')
    os.chdir('/home/{}/Mcc_Instaler'.format(usuario))


    # Procedimentos petinentes ao NPM e instalação dos módulos em node
    print('\n\n\n----------NPM----------\n\n\n')
    print(Fore.WHITE + Back.BLACK +'Iniciando a configuração do Node Package Manager(NPM)')
    caminho = '/home/{}/mcc'.format(usuario)
    if shell('npm set prefix {}'.format(caminho)):
        print(Fore.WHITE + Back.BLACK +'Prefixo do NPM redirecionado para {}'.format(caminho))
        print('\n\n\n----------VERDACCIO----------\n\n\n')
        verdaccio = input(Fore.WHITE + Back.BLUE +'Para continuar com os procedimentos do NPM, devemos referenciar o repositório(Verdaccio) da Martonis.'
        +' O acesso padrão para este repositório, encontra-se em: http://dev01.martonis.net:11000.\n'
        +'Insira o acesso ao verdaccio da Martonis: ')
        shell('npm set registry {}'.format(verdaccio))
        shell('npm login')


        print(Fore.WHITE + Back.BLACK +'Iniciando a instalação do módulo STARTUP.')
        shell('npm i -g mcc.startup')

        print('Iniciando a instalação do módulo BROKER.')
        shell('npm i -g mcc.broker')

        print('Iniciando a instalação do módulo PORTAL.')
        shell('npm i -g mcc.portal')

        print('Iniciando a instalação do módulo GAMA.')
        shell('npm i -g msi.gama')
    else:
        # Caso não for possível alocar a ~/mcc, damos o retorno para o Implantador
        # OBSERVAÇÂO - Podemos realizar uma nova verificação neste ponto das pastas ~/mcc e ~/mcc/lib e ~/mcc/bin
        print('Não foi possível definir o diretório ~/mcc como pasta global ao NPM')
        print('teste')
instalar_prerequisitos()