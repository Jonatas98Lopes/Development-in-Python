""" O nosso objetivo é receber dois números inteiros e
exibir a tabuada a partir do menor número até 10 até o maior.
1: Recebe dois números inteiros.
2: Identifique qual é o maior número.
3: Criar uma range identificando todos os números do menor ao maior
4: Criar outra range de 1 à 10 identificando os números de um a
10 para a multiplicação
"""
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print("Nenhuma tabuada no intervalo!")
else:
    for y in range(num1, num2 + 1):
        for i in range(1, 11):
            print(f"{y} x {i} = {y * i}")
        print("----------")
