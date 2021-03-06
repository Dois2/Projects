import os
import cx_Oracle


class OracleManager:

    def select(self, usuario, password, ip, porta, comando, filtro):
        conn = cx_Oracle.connect('{}/{}@{}/{}'.format(usuario, password, ip , porta))
        cur = conn.cursor()

        try:
            cur.execute(comando)

            for row in cur:
                print(row)
        except cx_Oracle.DatabaseError:
            print('Não foi possível executar o comando "{}"'.format(comando))


    def select_packagesxfiles(self, usuario, password, ip, porta, comando):
        try:
            conn = cx_Oracle.connect('{}/{}@{}/{}'.format(usuario, password, ip , porta))
            cur = conn.cursor()


            cur.execute(comando)

            for row in cur:

                teste = ''
                teste = str(row[0])
                return teste



        except cx_Oracle.DatabaseError:
            print('Não foi possível executar o comando "{}"'.format(comando))

    def select_verificar(self, usuario, password, ip, porta, comando, filtro):

        try:
            conn = cx_Oracle.connect('{}/{}@{}/{}'.format(usuario, password, ip , porta))


            cur = conn.cursor()


            cur.execute(comando)

            for row in cur:
                i = 0
                teste = ''
                teste = str(row[i])
                teste_separado = teste.split()

                for a in teste_separado:
                    if a.__contains__(filtro):

                        return True
                i += 1

            return False

        except cx_Oracle.DatabaseError:
            print('Não foi possível executar o comando "{}"'.format(comando))
        except cx_Oracle.DatabaseError:
            print('Não foi possível se conectar no banco com as credenciais informadas.')

# Definição de variáveis onde iremos verificar o ORACLE
integapps = 0
integmcc = 0
par2 = 0
eod_filesmt = 0
eod_filesdt = 0
packagexfiles = 0
bathexec = 0

# Intanciamento de uma classe oracle OracleManager
orcl = OracleManager()



# Definir os valores de conexão ao banco:
usuario = input('Insira o usuário para conectar ao banco: ')
password =input('Insira a senha do usuário acima: ')
ip = input('Insira o ip do banco: ')
porta =input('Insira o SSID do banco: ')



# Definição dos selects para verificar a existencia do campo CRT_MCCINTEGAPPS
# SYSTEMPARAMETERS
# ---------> SP_CODE = 'CRT_INTEGAPPS'
verificar_integapps = "SELECT SP_VALUE" \
                      "  FROM SYSTEMPARAMETERS" \
                      " WHERE SP_CODE = 'CRT_MCCINTEGAPPS'"

# ---------> SP_CODE = 'CRT_ENABLEINTEGMCC'
verificar_integmcc = "SELECT SP_VALUE" \
                     "  FROM SYSTEMPARAMETERS" \
                     " WHERE SP_CODE = 'CRT_ENABLEINTEGMCC'"

# ---------> SP_TYPE = 'PARAMBUSVAL2'
verificar_par2 = "SELECT SP_VALUE" \
                 "  FROM SYSTEMPARAMETERS" \
                 " WHERE SP_TYPE = 'PARAMBUSVAL2'" \
                 "   AND SP_CODE = 'MCCURL'"

# EOD_FILESMT
# ---------> EFM_STATUS = A e EFM_FILENAME = PAR2
verificar_eodfilesmt = "SELECT EFM_STATUS" \
                       "  FROM EOD_FILESMT" \
                       " WHERE EFM_FILENAME = 'PAR2'"

# EOD_FILESDT
# ---------> EFD_STATUS = A
verificar_eodfilesdt = "SELECT EFD_STATUS" \
                       "  FROM EOD_FILESDT" \
                       " WHERE EFM_ID IN (SELECT EFM_ID" \
                       "  FROM EOD_FILESMT" \
                       " WHERE EFM_FILENAME = 'PAR2')"
# VERIFICAR EPKG_ID
verificar_epkgid = "SELECT EPKG_ID" \
         "  FROM EOD_PACKAGES" \
         " WHERE EPKG_DESC = 'EODBUS'"

# PACKAGESXFILES
# ---------> EPKD_ID
verificar_packagesxfiles = "SELECT *" \
                           "  FROM EOD_PACKAGESXEOD_FILESMT" \
                           " WHERE EFM_ID IN (SELECT EFM_ID" \
                           "  FROM EOD_FILESMT" \
                           " WHERE EFM_FILENAME = 'PAR2')"

# EOD_PACKAGEBATHEXEC
# ---------> EPBE_STATUS
verificar_bathexec = "SELECT EPBE_STATUS" \
                     "  FROM EOD_PACKAGESBATCHEXEC" \
                     " WHERE EPBE_PROCNAME = 'EOD_EOD_PARAMETERS_2'"

# Definição do filtro.
filtro = input('Informe a aplicação para verificar se está habilitada: ')


# If para verificar se existe a aplicação no integapps.
if orcl.select_verificar(usuario, password, ip, porta, verificar_integapps, filtro):
    integapps = 1
else:
    print('\n\nAplicação "{}" não encontrada no SP_CODE CRT_MCCINTEGAPPS, tabela SYSTEMPARAMETERS.\n'
          'Necessário realizar a configuração do valor de SP_CODE = CRT_MCCINTEGAPPS, na tabela SYSTEMPARAMETERS.'.format(filtro))

# If para verificar se o integmcc esta habilitado.
if orcl.select_verificar(usuario, password, ip, porta, verificar_integmcc, '1'):
    integmcc = 1
else:
    print('Necessário realizar a configuração do valor de SP_CODE = CRT_ENABLEINTEGMCC, na tabela SYSTEMPARAMETERS.')

# If para verificar o mccurl no systemparameters
if orcl.select_verificar(usuario, password, ip, porta, verificar_par2,'0003$' ):
    par2 = 1
else:
    print('Necessário realizar a configuração do valor SP_CODE = MCCURL, na tabela SYSTEMPARAMETERS.')

# If para verificar o status da EOD_FILESMT
if orcl.select_verificar(usuario, password, ip, porta, verificar_eodfilesmt, 'A'):
    eod_filesmt = 1
else:
    print('Necessário realizar a ativação do EFM_FILENAME = PAR2, na tabela EOD_FILESMT')

# If para verificar o status de EOD_FILESDT
if orcl.select_verificar(usuario, password, ip, porta, verificar_eodfilesdt, 'A'):
    eod_filesdt = 1
else:
    print('Necessário realizar a configuração da tabela EOD_FILESDT.')

# If para verificar packagesxfiles
if orcl.select_verificar(usuario, password, ip, porta, verificar_packagesxfiles, orcl.select_packagesxfiles(usuario, password, ip, porta, verificar_epkgid)):
    packagexfiles = 1
else:
    print('Necessário realizar as configurações necessárias na tabela EOD_PACKAGESXEOD_FILESMT')

# If para verificar a existencia do bathexec
if orcl.select_verificar(usuario, password, ip, porta, verificar_bathexec, 'A'):
    bathexec = 1
else:
    print('Necessário realizar as configurações necessárias na tabela EOD_PACKAGESBATCHEXEC')

print('\n\nVerificação da SYSTEMPARAMETERS:\n')
if par2 == 1:
    print('---------> Campo MCCURL configurado corretamente!')
if integmcc == 1 :
    print('---------> Campo CRT_ENABLEINTEGMCC configurado corretamente!')
if integapps == 1:
    print('---------> Campo CRT_MCCINTEGAPPS configurado corretamente!')

print('\n\nGeração do PAR2:\n')
if eod_filesmt ==1 :
    print('---------> Geração do PAR2 ativada na tabela EOD_FILESMT!')
if eod_filesdt ==1:
    print('---------> Geração do PAR2 ativada na tabela EOD_FILESDT!')
if bathexec ==1:
    print('---------> Geração do PAR2 ativada na tabela EOD_PACKAGESBATCHEXEC!')
if packagexfiles ==1:
    print('---------> Existe a ligação entre o EOD_PACKAGES e o FILESMT!')

fim = input('\n\n\nAperte enter para finalizar a verificação.')