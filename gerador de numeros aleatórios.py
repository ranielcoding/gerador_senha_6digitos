# -*- coding: utf-8 -*-
# Importa a biblioteca random para gerar números aleatórios
import random

# Define uma variável 'y' com o valor 55
y = 55

# Define uma função chamada 'contagem'
def contagem():
    # Inicia um loop que irá executar 55 vezes (de 0 a 54)
    for i in range(y):
        # Gera um número inteiro aleatório no intervalo de 100,000 a 999,999
        x = random.randint(100000, 999999)

        # Imprime o número aleatório
        print(x)

# Chama a função 'contagem' para executar o código dentro dela
contagem()
