import io
import logging
import os
import tempfile
import unittest
from tkinter import Tk
from unittest.mock import patch


from delphia_csv.app.app import processar_transacoes


class TestProcessarTransacoes(unittest.TestCase):
    def setUp(self):
        # Cria um arquivo temporário de entrada para os testes
        self.arquivo_entrada = tempfile.NamedTemporaryFile(delete=False)
        # Cria um arquivo temporário de saída para os testes
        self.arquivo_saida = tempfile.NamedTemporaryFile(delete=False)

        self.arquivo_vazio = tempfile.NamedTemporaryFile(delete=False)

        with open(self.arquivo_entrada.name, "w", newline="") as file:
            file.write("Nome,Valor,Data\n")
            file.write("Cliente1,1500,2023-01-01\n")
            file.write("Cliente2,800,2023-01-02\n")
            file.write("Cliente3,1200,2023-01-03\n")

    def tearDown(self):
        # Remove os arquivo temporários após os testes
        self.arquivo_entrada.close()
        os.remove(self.arquivo_entrada.name)
        self.arquivo_saida.close()
        os.remove(self.arquivo_saida.name)

    def test_processar_transacoes(self):
        processar_transacoes(self.arquivo_entrada.name, self.arquivo_saida.name, 1000)

        # Lê o conteúdo do arquivo de saída gerado pela função
        with open(self.arquivo_saida.name, "r", newline="") as file:
            linhas = file.readlines()

        # Verifica se a função gerou o resultado esperado
        self.assertEqual(
            len(linhas), 3
        )  # Incluindo o cabeçalho, devem haver três linhas
        self.assertIn(
            "Cliente1,1500.0,2023-01-01\r\n", linhas
        )  # Transação acima de $1000
        self.assertIn(
            "Cliente3,1200.0,2023-01-03\r\n", linhas
        )  # Transação acima de $1000

    def test_processamento_com_sucesso_sem_transacoes_acima_do_valor(self):
        sucesso, mensagem_erro = processar_transacoes(
            self.arquivo_vazio.name, self.arquivo_saida.name, 5000
        )

        self.assertTrue(sucesso)
        self.assertEqual("", mensagem_erro)

    def test_processamento_com_erro_csv(self):
        sucesso, mensagem_erro = processar_transacoes(
            "arquivo_invalido.csv", self.arquivo_saida.name, 1000
        )

        self.assertFalse(sucesso)
        self.assertIn("Arquivo não encontrado: arquivo_invalido.csv", mensagem_erro)

    def test_processamento_com_erro_valor(self):
        sucesso, mensagem_erro = processar_transacoes(
            self.arquivo_entrada.name, self.arquivo_saida.name, "valor_invalido"
        )

        self.assertFalse(sucesso)
        self.assertIn("Valor mínimo inválido", mensagem_erro)


if __name__ == "__main__":
    unittest.main()
