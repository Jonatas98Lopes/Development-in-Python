def exibir():
    carrinho.sort()
    i = 0
    while i < len(carrinho):
        if i == len(carrinho) - 1:
            print(carrinho[i])
            break
        print(carrinho[i], end=" ")
        i += 1

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
        exibir()
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
        exibir()
        break
