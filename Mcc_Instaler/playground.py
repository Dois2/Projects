from teste import InstalManager

teste = InstalManager.ler_arquivo('linux_firewall.txt')
x = 0
y = False
print(teste.__len__())
while x <= teste.__len__():
    if x>=teste.__len__():
        break
    var = teste[x]
    print(var.find('SELINUX=disabled'))
    if var.find('SELINUX=disabled') == 0:
        print('Achou!!!!')
    print(var)
    x +=1

var2 = var.split()
print(var2[0])


