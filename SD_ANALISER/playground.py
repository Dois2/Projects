import os

teste =  'C:\\Users\\lucas.vieira\\Documents\\CONTROLE\\MCC\\PRODUCAO\\SANTOS'
# teste = os.walk(teste)
# print(teste)


def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            leitura = open(root+'\\'+file, 'r')
            linha = leitura.readline
            print(linha)
        print('------------------')
    return result

print(find_all('e.txt', teste))