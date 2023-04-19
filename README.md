# Caixa-Eletronico
O programa "Caixa Eletrônico" é uma aplicação simples desenvolvida em Python usando a biblioteca PySimpleGUI, 
que simula o funcionamento de um caixa eletrônico, permitindo ao usuário realizar um saque e exibindo a quantidade 
mínima de notas necessárias para compor o valor solicitado.

# Como usar
Clone o repositório ou baixe o arquivo caixa_eletronico.py.
Abra o terminal na pasta do arquivo e execute o comando python caixa_eletronico.py.
Informe o valor do saque desejado (entre R$10 e R$600) e clique no botão "Confirma".
Na tela de saque, clique no botão "Saque" para ver a quantidade mínima de cada nota necessária para compor o valor, ou no botão "Verificar valor de saque" para atualizar o valor do saque.
Para sair do programa, clique no botão "Fechar" ou feche a janela.

# Funcionamento
O programa funciona da seguinte maneira:

O usuário informa o valor do saque desejado na janela inicial.
Se o valor informado estiver fora do intervalo permitido (entre R$10 e R$600), uma mensagem de aviso é exibida. Caso contrário, o usuário clica no botão "Confirma".
Na tela de saque, é exibido o valor do saque e a quantidade mínima de cada nota necessária para compor o valor, calculada pelas funções converter_notas_centenas, converter_notas_50, converter_notas_dez, converter_notas_5 e converter_notas_unidades.
O usuário pode clicar no botão "Saque" para ver as quantidades de notas necessárias atualizadas, ou no botão "Verificar valor de saque" para atualizar o valor do saque.
Para sair do programa, o usuário pode clicar no botão "Fechar" ou fechar a janela.
