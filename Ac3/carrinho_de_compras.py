""" Neste exercício, estamos simulando um sistema de conclusão
de compras de uma loja online, onde a minha entrada é o código
dos produtos adicionados ao carrinho, caso haja produtos salvos
no carrinho.
# 1 Tarefa: Receber, como entrada, o código dos produtos do
carrinho.
# 2 Tarefa: Adicioná-los a uma lista.
# 3 Tarefa: Quando o usuário digitar exibir, exiba o valor na
tela.
"""
codigo = input() .split()
carrinho = []
i = 0
while i < len(codigo):
    carrinho.append(int(codigo[i]))
    i += 1
carrinho.sort()
operação = input()
while True:
    if operação == "exibir":
        i = 0
        carrinho.sort()
        while i < len(carrinho):
            if i == len(carrinho) - 1:
                print(carrinho[i])
                break
            print(carrinho[i], end=" ")
            i += 1
        operação = input()
    elif operação[0:9] == "adicionar":
        carrinho.append(int(operação[10:]))
        carrinho.sort()
        operação = input()
    elif operação[0:7] == "remover":
        i = 0
        while i < len(carrinho):
            if carrinho[i] == int(operação[8:]):
                del carrinho[i]
                break
            i += 1
        else:
            print(f"código {int(operação[8:])} não encontrado")
        operação = input()
    elif operação == "encerrar":
        carrinho.sort()
        i = 0
        if len(carrinho) > 0:
            while i < len(carrinho):
                if i == len(carrinho) - 1:
                    print(carrinho[i])
                    break
                print(carrinho[i], end=" ")
                i += 1
        else:
            print()    
        break
