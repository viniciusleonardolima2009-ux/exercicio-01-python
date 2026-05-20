# Pesquise e mostre qual é o valor máximo que um número inteiro pode ter em Python.
import sys

# Em Python 3, o tipo 'int' não tem um limite fixo estabelecido pela linguagem, 
# ele cresce conforme a memória disponível na máquina.
# Porém, podemos ver o valor máximo de uma variável inteira do C (tamanho da palavra do sistema)
# usando a biblioteca sys:
limite_pratico = sys.maxsize

print("Em Python 3, os inteiros têm tamanho arbitrário (limitado apenas pela memória RAM).")
print(f"Mas o valor máximo para índices e listas no seu sistema atual é: {limite_pratico}")