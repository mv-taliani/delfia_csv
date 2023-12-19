import csv
import logging

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)


def is_high_value(value, valor_minimo):
    return value and float(value) > valor_minimo


def processar_transacoes(
    arquivo_entrada: str, arquivo_saida: str, valor_minimo: int | float
) -> tuple[bool, str]:
    try:
        # Verifica se o valor_minimo é numérico, senão gera erro dentro da list_comprehension
        if not isinstance(valor_minimo, (int, float)):
            raise TypeError("Valor mínimo inválido")

        # open's separados para problemas em um arquivo não interferirem no outro
        with open(arquivo_entrada, "r", newline="") as infile:
            reader = csv.reader(infile)
            header = next(reader, None)

            high_value_transactions = [
                [name, float(value), date]
                for name, value, date in reader
                if is_high_value(value, valor_minimo)
            ]

        with open(arquivo_saida, "w", newline="") as outfile:
            writer = csv.writer(outfile)

            if header:
                writer.writerow(header)

            writer.writerows(high_value_transactions)

        # caso seja utilizado apenas no terminal
        print(f"Transações acima de ${valor_minimo} foram salvas em {arquivo_saida}.")

        return True, ""

    # excepts específicos para melhor explicação de erros ao usuário

    except csv.Error as e:
        mensagem_erro = f"Erro ao processar arquivo CSV: {str(e)}"
        logging.error(mensagem_erro)
        return False, mensagem_erro

    except FileNotFoundError as e:
        mensagem_erro = f"Arquivo não existe: {str(e)}"
        logging.error(mensagem_erro)
        return False, f"Arquivo não encontrado: {arquivo_entrada}"

    except (ValueError, TypeError) as e:
        mensagem_erro = f"Error: {str(e)}"
        logging.error(mensagem_erro)
        return False, mensagem_erro

    except Exception as e:
        mensagem_erro = f"Ocorreu um erro inesperado: {str(e)}"
        logging.error(mensagem_erro)
        return False, mensagem_erro


if __name__ == "__main__":
    ARQUIVO_ENTRADA = "transacoes.csv"
    ARQUIVO_SAIDA = "transacoes_altas.csv"
    VALOR_MINIMO = 1_000
    processar_transacoes("transacoes.csv", ARQUIVO_SAIDA, VALOR_MINIMO)
