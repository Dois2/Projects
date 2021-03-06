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