import csv
import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s [%(levelname)s]: %(message)s')


def processar_transacoes(arquivo_entrada: str, arquivo_saida: str, valor_minimo: int | float) -> None:
    try:
        # Leitura do arquivo CSV de entrada e abertura do de saída, sem abrir 2 with's separados
        with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
            leitor_csv = csv.reader(entrada)
            escritor_csv = csv.writer(saida)

            # Segundo parâmetro para evitar StopIteration caso não haja cabeçalho
            cabecalho = next(leitor_csv, None)

            # Filtro acima do valor minimo
            transacoes_acima_de = [
                [nome, float(valor), data]
                for nome, valor, data in leitor_csv
                if valor and float(valor) > valor_minimo
            ]

            # Gravação das transações acima do valor minimo no novo arquivo CSV
            escritor_csv.writerow(cabecalho)
            escritor_csv.writerows(transacoes_acima_de)

        print(f'Transações acima de ${valor_minimo} foram salvas em {arquivo_saida}.')

    except csv.Error as e:
        logging.error(f'Erro ao processar arquivo CSV: {str(e)}')
        print('Ocorreu um erro ao processar o arquivo CSV.')
    except ValueError as e:
        logging.error(f'Erro de valor: {str(e)}')
        print('Ocorreu um erro de valor durante o processamento.')
    except Exception as e:
        logging.error(f'Ocorreu um erro inesperado: {str(e)}')
        print('Ocorreu um erro inesperado. Consulte o arquivo error_log.txt para obter mais detalhes.')


if __name__ == '__main__':
    ARQUIVO_ENTRADA = 'transacoes.csv'
    ARQUIVO_SAIDA = 'transacoes_altas.csv'
    VALOR_MINIMO = 1_000
    processar_transacoes('transacoes.csv', ARQUIVO_SAIDA, VALOR_MINIMO)
