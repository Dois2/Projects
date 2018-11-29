arquivo = open('teste2.txt', 'w')
arquivo.write('exemplo')
row = arquivo.read()
nome = arquivo.name
print(row)
arquivo.close()