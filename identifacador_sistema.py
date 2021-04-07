import os


"""
sysname - nome do sistema operacional
nodename - nome da máquina da rede(definido pela implementação)
release - versao do sistema operacional
version - versão do sistema operacional
machine - identificador de hardware
"""

conf = ('sysname =', 'nodename =', 'release =', 'version =', 'machine =')

for date, info in enumerate(os.uname()):
    print(conf[date].capitalize(), info)
