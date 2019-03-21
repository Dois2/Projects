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
                
def get_user_mongo():
    user = get_user():
    mongo_db = user.split('.')
    
    

def get_user():
    arquivo = 'whoami.txt'
    shell('whoami > {}'.format(arquivo))
    file = open(arquivo, 'r')
    for line in file:
        user = line.split('\n')
        
        return user[0] 





print(get_user())