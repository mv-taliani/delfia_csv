import unittest

import unittest
import tempfile
import os

# Importe a função que você deseja testar
from delphia_csv.app.app import processar_transacoes


class TestProcessarTransacoes(unittest.TestCase):

    def setUp(self):
        # Cria um arquivo temporário de entrada para os testes
        self.arquivo_entrada = tempfile.NamedTemporaryFile(delete=False)
        with open(self.arquivo_entrada.name, 'w', newline='') as file:
            file.write("Nome,Valor,Data\n")
            file.write("Cliente1,1500,2023-01-01\n")
            file.write("Cliente2,800,2023-01-02\n")
            file.write("Cliente3,1200,2023-01-03\n")

    def tearDown(self):
        # Remove o arquivo temporário de entrada após os testes
        self.arquivo_entrada.close()
        os.remove(self.arquivo_entrada.name)

    def test_processar_transacoes(self):
        # Cria um arquivo temporário de saída para os testes
        arquivo_saida = tempfile.NamedTemporaryFile(delete=False)

        try:
            # Chama a função que você deseja testar
            processar_transacoes(self.arquivo_entrada.name, arquivo_saida.name, 1000)

            # Lê o conteúdo do arquivo de saída gerado pela função
            with open(arquivo_saida.name, 'r', newline='') as file:
                linhas = file.readlines()

            # Verifica se a função gerou o resultado esperado
            self.assertEqual(len(linhas), 3)  # Incluindo o cabeçalho, deve haver três linhas
            self.assertIn("Cliente1,1500.0,2023-01-01\r\n", linhas)  # Transação acima de $1000
            self.assertIn("Cliente3,1200.0,2023-01-03\r\n", linhas)  # Transação acima de $1000

        finally:
            # Remove o arquivo temporário de saída após os testes
            arquivo_saida.close()
            os.remove(arquivo_saida.name)


if __name__ == '__main__':
    unittest.main()
