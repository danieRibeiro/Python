import os


def filtracao_string(abrir_arquivo):
    """
    Essa função serve para filtrar o caminho do arquivo/diretório, colocando os ente aspas('')
    as palavras que contiverem espaços entre elas. Com o intuito de evitar o erro
    (xdg-open: unexpected argument Try 'xdg-open --help' for more information.) ao tentar abrir o arquivo.
    :param abrir_arquivo: caminho do arquivo/diretório
    :return: retorna a string filtrada.
    """
    nova = ''
    for barra in abrir_arquivo:
        if '/' in barra:
            nova += '\n'
        else:
            nova += barra

    fragmentado = nova.split('\n')
    for space in fragmentado:

        if ' ' in space:

            fragmentado = str(nova).replace(space, f"'{space}'")
            nova = ''.join(fragmentado)

        else:

            nova = '/'.join(fragmentado)

    return os.system('xdg-open ' + fragmentado)


if __name__ == '__main__':

    # Exemplo
    index = '/home/ex/Downloads/Program Developer/'
    print(filtracao_string(index))
