import os
import cx_Oracle


class OracleManager:

    def select(self, usuario, password, ip, porta, comando):
        conn = cx_Oracle.connect('{}/{}@{}/{}'.format(usuario, password, ip , porta))
        cur = conn.cursor()

        try:
            cur.execute(comando)

            for row in cur:
                print(row)
        except cx_Oracle.DatabaseError:
            print('Não foi possível executar o comando "{}"'.format(comando))


usuario = 'GUAIUBA'
password = usuario
ip = '172.17.10.18'
porta = 'URANOBD'

iss_id = int(input('Insira o Issuer: '))
cd_id = int(input('Insira o Card Design: '))
cd_snr = int(input('Insira o Senial Nº: '))

comando = 'SELECT *' \
          '  FROM cardaccount' \
          ' WHERE ISS_ID = {}' \
          '   AND CD_ID = {}' \
          '   AND CRD_SNR = {};'.format(iss_id, cd_id, cd_snr)




orcl = OracleManager()

orcl.select(usuario, password, ip, porta, comando)

