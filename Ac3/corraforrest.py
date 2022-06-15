""" O objetivo deste exercício é receber a entrada de valores em 
segundos dos tempos de corrida atingidos por Forrest e calcular
sua média aritmética exibindo também as entradas abaixo desta.
1: Receber um número de variáveis indeterminado enquanto maiores
que 0.
2: Calcular a média das corridas.
3: Verificar quais entradas estão abaixo da média.
"""
corrida = int(input())
total_corridas = []
while corrida > 0:
    total_corridas.append(corrida)
    corrida = int(input())
soma, i = 0, 0
while i < len(total_corridas):
    soma += total_corridas[i]
    i += 1
media = soma/len(total_corridas)
print(f"MEDIA: {media:.2f}")
i = 0
while i < len(total_corridas):
    if total_corridas[i] < media:
        print(total_corridas[i])
    i += 1
