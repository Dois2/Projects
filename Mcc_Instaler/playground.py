from teste import InstalManager



mongo_repo = '[mongodb-org-4.0]\n' \
                         'name=MongoDB Repository\n' \
                         'baseurl=https://repo.mongodb.org/yum/redhat/7Server/mongodb-org/4.0/x86_64/\n' \
                         'gpgcheck=1\n' \
                         'enabled=1\n' \
                         'gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc'
InstalManager.escrever('mongodb-org.repo', mongo_repo)


InstalManager.instalation(InstalManager)