# delphia_csv


Teste técnico Delphia


## Tarefa: Automatização de Processamento de Dados CSV

Você recebe um arquivo CSV com informações sobre transações financeiras. Cada linha contém: nome do cliente, valor da transação e data da transação. Sua tarefa é escrever um script Python que leia o arquivo CSV, identifique transações acima de um determinado valor (por exemplo, $1000) e as salve em um novo arquivo CSV.


## Requisitos:

* O script deve ser capaz de ler um arquivo CSV chamado transacoes.csv.
* Identificar transações com valor superior a $1000.
* Salvar as transações identificadas em um novo arquivo chamado transacoes_altas.csv.
* Utilize a biblioteca padrão do Python para manipulação de arquivos CSV.


## Critérios de Avaliação:

* Funcionalidade correta e precisa.
* Boa prática de código (Clean Code)
* Tratamento adequado de erros, a aplicação não pode quebrar caso tenha algum erro na planilha
* Logs em txt para registro de erros.
* Eficiência e desempenho do código.


## Observações:

* Comente seu código para explicar decisões ou abordagens específicas.
* Exemplo de Estrutura do Arquivo CSV que sera utilizado para teste (transacoes.csv):

```
Nome do Cliente,Valor da Transação,Data da Transação

Cliente A,1200,2023-01-15

Cliente B,800,2023-02-02

Cliente C,1500,2023-03-10

Cliente D,900,2023-04-05
```
