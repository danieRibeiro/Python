import os
import filtro_string

arquivo = ''

while True:
    print(f"{'-' * 10} BUSCADOR {'-' * 10}")
    caminho_diretorio = str(input('Insira o caminho do diretório: '))

    # Verifica se o caminho do diretório é válido
    if os.path.exists(caminho_diretorio):

        # Nome do arquivo que você deseja procurar
        procura_termo = str(input('Nome do arquivo: '))

        contador_arquivos = contador_total = 0

        # Percorre a raiz, diretório e os arquivos
        for raiz, diretorios, arquivos in os.walk(caminho_diretorio):

            # Percorre os arquivos
            for arquivo in arquivos:

                if procura_termo in arquivo:
                    # Faz a soma de quantos arquivos existem com o nome da busca inserida.
                    contador_arquivos += 1

                    # Faz a soma total de quantos arquivos foram contados no diretório/arquivo.
                    contador_total += 1
                else:
                    contador_total += 1

        print('-' * 40)
        print(f'\033[1;31m{contador_total}\033[m arquivo(s) foi/foram examinado(s)!')
        print(f'Foram encontrados \033[1;31m{contador_arquivos}\033[m arquivos!')
        if contador_arquivos == 0:
            break
        else:
            while True:
                print('-' * 40)
                exibir = str(input('Você deseja ver os arquivos? (S/N) ')).upper()[0]
                print('-' * 40)

                if 'S' in exibir:
                    for raiz_dois, diretorios_dois, arquivos_dois in os.walk(caminho_diretorio):

                        for arquivo in arquivos_dois:
                            if procura_termo in arquivo:
                                print(raiz_dois, arquivo, sep='/')

                    while True:
                        abrir = str(input('Deseja abrir algum arquivo/diretório? (S/N) ')).upper().strip()[0]

                        if 'S' in abrir:
                            abrir_arquivo = str(input('Diretório do arquivo: ')).strip()
                            filtro_string.filtracao_string(abrir_arquivo)

                        elif 'N' in abrir:
                            while True:
                                voltar = str(input('Voltar ao área inicial? (S/N)')).upper().strip()[0]
                                if 'S' in voltar:
                                    break
                                elif 'N' in voltar:
                                    print(f'{"PROGRAMA ENCERRADO!".center(37)}')
                                    exit()
                                else:
                                    print(f'\033[1;31m{"OPÇÃO INVÁLIDA!".center(37)}\033[m')
                                    continue
                            break

                        else:
                            print(f'\033[1;31m{"OPÇÃO INVÁLIDA!".center(37)}\033[m')
                            continue

                    # 'break' para voltar ao topo
                    break

                elif 'N' in exibir:
                    print(f'{"PROGRAMA ENCERRADO!".center(37)}')
                    break

                else:
                    print(f'\033[1;31m{"OPÇÃO INVÁLIDA!".center(37)}\033[m')
                    continue
    else:
        print(f'\033[1;31m{"Diretório Inválido!".center(20 * 3)}\033[m')
        continue
