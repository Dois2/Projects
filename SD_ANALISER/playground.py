from SD_ANALISER import OracleManager

usuario = 'GUAIUBA'
password = usuario
ip ='172.17.10.18'
porta = 'URANODB'

select = "SELECT EPKG_ID" \
         "  FROM EOD_PACKAGES" \
         " WHERE EPKG_DESC = 'EODBUS'"

orcl = OracleManager.OracleManager()



a = orcl.select_packagesxfiles(usuario, password, ip, porta, select)
print('Valor de a: {}'.format(a))