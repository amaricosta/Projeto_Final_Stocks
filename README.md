# Projeto de gestão de stocks

Programa de consola para registar produtos, pesquisar,
movimentar stock e consultar resultados.

## Execução

1. Utilizar Python 3.
2. Manter os ficheiros Python na mesma pasta.
3. Abrir principal.py no Spyder.
4. Confirmar a pasta de trabalho.
5. Executar o ficheiro completo.
6. Utilizar o menu e escolher 0 para terminar.

## Testes

Executar testes.py completo.
Uma execução sem falhas termina com a mensagem
"Todos os testes passaram.".

## Preços e valor do inventário

O preço representa o custo unitário de referência.
O registo aceita vírgula ou ponto como separador decimal,
sem separadores de milhares.
O preço é arredondado para duas casas decimais no registo.

O valor em stock resulta da quantidade multiplicada pelo preço.
As entradas e saídas mantêm o preço unitário.

## Relatório e dados entre execuções

O programa guarda relatorio_stock.txt na pasta de trabalho.
Cada gravação substitui o relatório anterior.

A lista de produtos começa vazia em cada execução.
Ler o relatório apresenta o texto guardado.
Essa leitura não recupera os produtos para a lista.
