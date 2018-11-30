import re
import os
import time


class InstalManager:
    arquivo_bash = ''
    arquivo_bash_separado = ''
    frase_bash = ''
    adicionar_path = ';/home/centos/mcc/bin;$ORACLE_HOME/bin:'
    frase_bash_nova = ''
    arquivo_bash_novo = ''
    repo_mongo = ''
    a  =''
    l = ''

    def shell(mensagem):
        confirmar = os.system(mensagem)
        if confirmar != 1:
            return True
        else:
            return False

    def pre_install(self):
        print('')

    def criar_repo_mongo(self):
        #Defindo os dois poss[iveis do métodos.
        sucesso = 'Arquivo criado e movido com sucesso!'
        erro = 'Diretório /etc/yum.repos.d/mongodb-org.repo não localizado!'

        #Definindo a varíavel com os valores a serem escritos no arquivo de repositório
        mongo_repo = '[mongodb-org-4.0]\n' \
                     'name=MongoDB Repository\n' \
                     'baseurl=https://repo.mongodb.org/yum/redhat/7Server/mongodb-org/4.0/x86_64/\n' \
                     'gpgcheck=1\n' \
                     'enabled=1\n' \
                     'gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc'

        #Escrever os valores de mongo_repo, no arquivo especificado
        InstalManager.escrever('mongodb-org.repo', mongo_repo)

        #Se teste == 0, significa que o comando abaixo funcionou corretamente(conseguiu realocar os valores no diretório
        # especificado)
        teste_if = os.system('sudo mv mongodb-org.repo /etc/yum.repos.d/mongodb-org.repo')
        if teste_if != 1:

            #retorno se moveu o mongo-org.repo con sucesso
            return sucesso
        else:
            #retorno se não conseguiu mover o mongo-repo.
            return erro




    def instalation(self):
        success = 'Os componentes foram instalados com sucesso!'
        erro = 'Os pré requisitos não foram satisfeitos!'
        #Se os pré-requisitos não foram satisfeitos, a variável self.pre-requisitos será 1;
        if self.pre_requisitos == 1:

            #retorno com mensagem de erro
            return erro
        else:
            #Criar/alocar o arquivo de repositório do mongo.
            mensagem = InstalManager.criar_repo_mongo(self)
            if mensagem.__contains__("Diretório /etc/yum.repos.d/mongodb-org.repo não localizado!"):
                #retorno caso a função foi executada corretamente
                return success

            #os.system('sudo chmod 777 PREINSTALL.sh')




    def ler_arquivo_bash(self, nome_do_arquivo):
        #Abrir o arquivo(nome_do_arquivo).
        file = open(nome_do_arquivo,'r')

        #Estrutura de repetição, reponsável por contruir uma string com os valores lidos do arquivo aberto à cima.
        for line in file:
            self.arquivo_bash += file.readline()

        #A variávle arquivo_bash_separado recebe a arquivo_bash quebrada, para facilitar a localização da alteração
        # que faremos posteriormente.
        self.arquivo_bash_separado = self.arquivo_bash.split()

        #For responsável por selecionar e comparar o valor de frase_bash com o valor contido na variavel
        #procurar.
        for posicao in range(0, self.arquivo_bash_separado.__len__()):
            self.frase_bash = self.arquivo_bash_separado[posicao]
            procurar = 'PATH='
            if self.frase_bash.__contains__(procurar):

                #Criação de uma nova frase, com o valor da frase antiga + o valor a ser adicionado na variavel de ambiente
                self.frase_bash_nova = self.frase_bash +  self.adicionar_path

                #Substituição da frase antiga, pela frase nova contruida acima.
                self.arquivo_bash_novo = self.arquivo_bash.replace(self.frase_bash, self.frase_bash_nova)

                #Prints informativos para desenvolvimento, habilitar caso for necessário visualizar a diferença entre as duas
                #strings formuladas.
                #print(self.arquivo_bash)
                #print('-----------------------------------------')
                #print(self.arquivo_bash_novo)
        #Fechar arquivo aberto
        file.close()

    def ler_arquivo(nome_do_arquivo):
            # Abrir o arquivo(nome_do_arquivo).
            file = open(nome_do_arquivo, 'r')

            # Estrutura de repetição, reponsável por contruir uma string com os valores lidos do arquivo aberto à cima.


            leitura_arquivo = file.readlines()



            file.close()

            return leitura_arquivo


    def escrever_arquivo(self, file_name):
        #Chamada ao método ler_arquivo_bash, a fim de coletar e armazenar em suas variáveis os valores
        InstalManager.ler_arquivo_bash(InstalManager, file_name)

        #Abrir e criar o arquivo .bash_profile2 em modo de escrita
        file = open('.bash_profile2', 'w')

        #Escrever no arquivo a estrutura montada com os valores corretos, criada no método ler_arquivo_bash
        file.write(self.arquivo_bash_novo)

        #Fechar o arquivo aberto
        file.close()

    def achar_path(self):
        diretorio = '/home/centos/'
        nome_arquivo = diretorio + '.bash_profile'
        file = open(nome_arquivo, 'r')
        for i in file:
            if i.__contains__('asdafasfasdasd'):
                return True
        return False

    def escrever(file_name, escrever):

        #Abrir e criar o arquivo .bash_profile2 em modo de escrita
        file = open(file_name, 'w')

        #Escrever no arquivo a estrutura montada com os valores corretos, criada no método ler_arquivo_bash
        file.write(escrever)

        #Fechar o arquivo aberto
        file.close()

    def criar_repositorio_mongo(self, file_name):
        local_instalacao = '/etc/yum.repos.d/'
        file = open('mongodb-org.repo', 'w')

    def teste_prerequisitos(self):
        pre_requisitos = 0

        #Testar a instalaçãodo epel-release
        #Coletar, testar e exibir as variáveis de ambiente


        #Testar a instalação do pip
        pip_arquivo = 'pip_version.txt'
        pip_check = os.system('pip --version > {}'.format(pip_arquivo))

        #testar os diretórios do mcc
        diretorio_existente = 'Diretório existente!'
        diretorio_mcc = os.system('cd /home/centos/mcc')
        if diretorio_mcc == 0:
            InstalManager.escrever('diretorio_mcc.txt', diretorio_existente)


        diretorio_mcc_bin = os.system('cd /home/centos/mcc/bin')
        if diretorio_mcc_bin == 0:
            InstalManager.escrever('diretorio_mcc_bin.txt', diretorio_existente)


        diretorio_mcc_lib = os.system('cd /home/centos/mcc/lib')
        if diretorio_mcc_lib ==0:
            InstalManager.escrever('diretorio_mcc_lib.txt', diretorio_existente)

        #Testar repositório do Mongo
        repositorio_mongo_txt = 'mongo_repositorio.txt'
        repo_mongo_check = os.system('tail /etc/yum.repos.d/mongodb-org.repo > {}'.format(repositorio_mongo_txt))


        #Testar a instalação do Mongo
        mongo_txt = 'mongo.txt'
        mongo_instal_check = os.system('mongo -version > {}'.format(mongo_txt))




        #Coletar, testar e imprimir o valor do arquivo de configuração do mongo
        mongo_conf_txt = 'mongo_config.txt'
        mongo_conf_check = os.system('tail /etc/mongod.conf > {}'.format(mongo_conf_txt))




        #Coletar, testar e imprimir o arquivo de configuração de conexão do mongo
        config_conect_mongo_txt = 'mongo_conect_config.txt'
        mongo_conect_check = os.system('tail /etc/security/limits.d/99-mongodb-nproc.conf > {}'.format(config_conect_mongo_txt))




        #Coletar, testar e imprimir os valores de firewall do linux
        firewall_linux_txt = 'linux_firewall.txt'
        firewall_check = 1
        os.system('tail /etc/selinux/config > {}'.format(firewall_linux_txt))
        arquivo_firewall = InstalManager.ler_arquivo(firewall_linux_txt)
        x = 0
        while x <= arquivo_firewall.__len__():
            if x >= arquivo_firewall.__len__():
                break
            linha = arquivo_firewall[x]
            #print(linha.find('SELINUX=disabled'))
            if linha.find('SELINUX=disabled') == 0:
                #print('Achou')
                firewall_check =0
            #print(linha)
            x += 1


        #Coletar, testar e imprimir os valores do arquivo CONFIG.json
        arquivo_config_json_txt = 'config_json_check.txt'
        config_json_check = os.system('tail /home/centos/mcc/bin/config.json > {}'.format(arquivo_config_json_txt))

        #Testar instalação do node
        node__txt = 'node_versao.txt'
        node_check = os.system('node --version > {}'.format(node__txt))

        #Testar GCC
        gcc_txt = 'gcc_versao.txt'
        gcc_check = os.system('gcc --version > {}'.format(gcc_txt))

        #Testar a instalação do Oracle
        oracle_txt ='oracle_check.txt'
        caminho_oracle = os.system('cd /usr/lib/oracle')
        if caminho_oracle == 0:
            InstalManager.escrever(oracle_txt, diretorio_existente)


        #Coletar, testar e imprimir os valores ORACLE_HOME do .bash_profile

        #Testar a instalação do npm
        npm_txt = 'npm_version.txt'
        npm_check = os.system('npm --version > {}'.format(npm_txt))

        #Verificação dos requisitos
        time.sleep(3)

        print('-----------------------------Pré-requisitos satisfeitos------------------------------------------------')
        if pip_check ==0:
            arquivo = InstalManager.ler_arquivo('pip_version.txt')

            var = arquivo[0]
            var2 = var.split()
            print('Pip foi localizado na versão {}!\n'.format(var2[1]))
        if diretorio_mcc ==0:
            arquivo = InstalManager.ler_arquivo('diretorio_mcc.txt')

            var = arquivo[0]
            var2 = var.split()
            print('{} "/mcc" {}\n'.format(var2[0], var2[1]))
        if diretorio_mcc_bin == 0 :
            arquivo = InstalManager.ler_arquivo('diretorio_mcc_bin.txt')

            var = arquivo[0]
            var2 = var.split()
            print('{} "/mcc/bin" {}\n'.format(var2[0], var2[1]))
        if diretorio_mcc_lib == 0 :
            arquivo = InstalManager.ler_arquivo('diretorio_mcc_lib.txt')

            var = arquivo[0]
            var2 = var.split()
            print('{} "/mcc/lib" {}\n'.format(var2[0], var2[1]))
        if repo_mongo_check == 0 :
            arquivo = InstalManager.ler_arquivo('mongo_repositorio.txt')

            var = arquivo[0]
            var2 = var.split()
            print('Diretório "{}" localizado!\n '.format(var2[0]))
        if mongo_instal_check == 0 :
            arquivo = InstalManager.ler_arquivo('mongo.txt')

            var = arquivo[0]
            var2 = var.split()
            print('Mongo foi localizado na versão {}!\n'.format(var2[3]))
        if mongo_conf_check == 0 :
            #Não foi possível localizar alguma referencia à versão ou nome de arquivo, neste caso imprimimos diretamente
            #que o pré-requisito foi localizado.
            #arquivo = InstalManager.ler_arquivo('mongo_config.txt')

            #var = arquivo[0]
            #var2 = var.split()
            print('O arquivo de configuração do MongoDB foi localizado!\n')
        if mongo_conect_check == 0 :
            # Não foi possível localizar alguma referencia à versão ou nome de arquivo, neste caso imprimimos diretamente
            # que o pré-requisito foi localizado.
            #arquivo = InstalManager.ler_arquivo('mongo_conect_config.txt')

            #var = arquivo[0]
            #var2 = var.split()
            print('Arquivo de conexão do MongoDB localizado!\n')
        if firewall_check == 0 :
            arquivo = InstalManager.ler_arquivo('linux_firewall.txt')
            var = arquivo[2]
            var2 = var.split()
            print('Arquivo de firewall com os parâmetros "{}" localizado!\n'.format(var2[0]))
        if config_json_check == 0:
            arquivo = InstalManager.ler_arquivo('config_json_check.txt')
            var = arquivo[2]
            var2 = var.split()
            print('Arquivo de conexão com os MongoDB localizado!\n'
                  '-----> Acesso setado para: {}\n'.format(var2[1]))
        if node_check == 0:
            arquivo = InstalManager.ler_arquivo('node_versao.txt')
            var = arquivo[0]
            var2 = var.split()
            print('Node foi localizado na versão {}!\n'.format(var2[0]))
        if gcc_check == 0:
            arquivo = InstalManager.ler_arquivo('gcc_versao.txt')
            var = arquivo[0]
            var2 = var.split()
            print('Gcc foi localizado na versão {}!\n'.format(var2[2]))
        if caminho_oracle == 0 :
            arquivo = InstalManager.ler_arquivo('diretorio_mcc_lib.txt')

            var = arquivo[0]
            var2 = var.split()
            print('{} do Oracle {}\n'.format(var2[0], var2[1]))
        if npm_check == 0 :
            arquivo = InstalManager.ler_arquivo('npm_version.txt')

            var = arquivo[0]
            var2 = var.split()
            print('Npm foi localizado na versão {}!\n'.format(var2[0],))


        print('-----------------------------Pré-requisitos não satisfeitos--------------------------------------------')
        if pip_check != 0:
            print('**Pip não encontrado!')
            pre_requisitos = 1

        if diretorio_mcc != 0:
            print('**Diretório mcc não encontrado!'
                  '\n-----> Alocar/criar diretório "mcc", no caminho /home/centos.'
                  '\n----------> Utilizar o comando "sudo mkdir /home/centos/mcc"\n')
            pre_requisitos = 1
        if diretorio_mcc_bin != 0:
            print('**Diretório mcc/bin não encontrado!'
                  '\n-----> Alocar/criar o diretório "mcc/bin", no caminho /home/centos.'
                  '\n----------> Utilizar o comando "sudo mkdir /home/centos/mcc/bin"\n')
            pre_requisitos = 1
        if diretorio_mcc_lib != 0:
            print('**Diretório mcc/lib não encontrado!'
                  '\n-----> Alocar/criar o diretório "mcc/lib", no caminho /home/centos.'
                  '\n----------> Utilizar o comando "sudo mkdir /home/centos/mcc/lib"\n')
            pre_requisitos = 1
        if repo_mongo_check != 0:
            print('**Repositório do mongo não encontrado!'
                  '\n-----> Alocar/criar arquivo "mongodb-org.repo", no caminho /etc/yum.repos.d.'
                  '\n----------> Utilizar o comando "sudo nano /etc/yum.repos.d/mongodb-org.repo"'
                  '\n---------------> Inserir o texto abaixo:'
                  '\n---------------> [mongodb-org-4.0]'
                  '\n---------------> name=MongoDB Repository'
                  '\n---------------> baseurl=https://repo.mongodb.org/yum/redhat/7Server/mongodb-org/4.0/x86_64/'
                  '\n---------------> gpgcheck=1'
                  '\n---------------> enabled=1'
                  '\n---------------> gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc\n')
            pre_requisitos = 1
        if mongo_instal_check != 0:
            print('**Instalação do mongo não encontrada!'
                  '\n-----> Realizar a instalação do MongoDB(ATENÇÃO, NECESSÁRIO POSSUIR REPOSITÓRIO "/etc/yum.repos.d/mongodb-org.repo" )'
                  '\n----------> Com o repositório criado, utilizar o comando "sudo yum install mongodb-org"\n')
            pre_requisitos = 1
        if mongo_conf_check != 0:
            print('**Arquivo de configuração do mongo não encontrado!'
                  '\n-----> Alocar/criar o arquivo "mongod.conf" no diretório "/etc/"'
                  '\n----------> Utilizar o comando "sudo nano /etc/mongod.conf"\n')
            pre_requisitos = 1
        if mongo_conect_check != 0:
            print('**Arquivo de conexão do mongo não encontrado!'
                  '\n-----> Alocar/criar o arquivo "99-mongodb-nproc.conf", no diretório "/etc/security/limits.d"'
                  '\n----------> Utilizar o comando "sudo nano /etc/security/limits.d/99-mongodb-nproc.conf"'
                  '\n----------> Inserir o texto abaixo:'
                  '\n----------> mongod soft nofile 64000'
                  '\n----------> mongod hard nofile 64000'
                  '\n----------> mongod soft nproc 64000'
                  '\n----------> mongod hard nproc 64000\n')
            pre_requisitos = 1
        if firewall_check != 0:
            print('**Arquivo de firewall não encontrado!'
                  '\n-----> Editar/adicionar os valores necessários a fim de satisfazer este requisito!'
                  '\n----------> Verificar se o arquivo "/etc/selinux/config", se possui os valores "SELINUX=disabled"\n')
            pre_requisitos = 1
        if config_json_check != 0:
            print('**Arquivo config.json não encontrado!'
                  '\n-----> Alocar/criar o arquivo "config.json", no diretório "/home/centos/bin"'
                  '\n----------> Este arquyivo é responsável por fornecer a conexão do mongo aos nossos módulos!\n')
            pre_requisitos = 1
        if node_check != 0:
            print('**Instalação do node não encontrada!'
                  '\n-----> Para realizar a instalação, seguir os passos abaixo:'
                  '\n----------> Acessar a URL: https://nodejs.org/dist/latest-v8.x/'
                  '\n----------> Botão direito no link.tar.gz da última versão presente'
                  '\n----------> Copiar o link e utilizar o comando: "sudo wget + link copiado"'
                  '\n----------> Descompactar com: "sudo tar -xvfz + nome do arquivo.tar.gz"'
                  '\n----------> Dentro da pasta descompactada, utilizar os comandos: "./configure", "sudo make" e "sudo make install"\n')
            pre_requisitos = 1
        if gcc_check != 0:
            print('**Instalação do gcc não encontrada!'
                  '\n-----> Necessário GCC para instalar o Node!'
                  '\n----------> Utilizar o comando "yum install gcc gcc-c++"\n')
            pre_requisitos = 1
        if caminho_oracle != 0:
            print('**Oracle não encontrado!'
                  '\n-----> Baixar a última versão do Oracle.rpm, através do link "https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html"'
                  '\n----------> Descompactar e enviar para nosso servidor atravéz do serviço SFTP'
                  '\n----------> Instalar utilizando o comando "sudo yum localinstall oracle* --nogpcheck"'
                  '\n----------> ATENÇÃO, ALOCAR AS VARIÁVEIS DE AMBIENTE ORACLE_HOME\n')
            pre_requisitos = 1
        if npm_check != 0:
            print('**Instalação do NPM não encontrada!')
            pre_requisitos = 1
        print('-------------------------------------------------------------------------------------------------------')
        if pre_requisitos == 0:
            return True
        if pre_requisitos == 1:
            return False













