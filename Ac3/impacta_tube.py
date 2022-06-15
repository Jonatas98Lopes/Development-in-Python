""" Criar um programa par simular um banco de dados de uma site
conhecimo como ImpactaTube onde nós temos valores de bonificação
para cada mil inscritos depedendo da produção de conteúdo
premium.
"""
qtd = int(input())
while qtd < 1 or qtd > 200:
    qtd = int(input())
i = 1
canais = []
inscritos = []
monetização = []
conteudo_premium = []
while i <= qtd:
    entrada = input() . split(";")
    canais.append(entrada[0])
    inscritos.append(int(entrada[1]))
    monetização.append(float(entrada[2]))
    conteudo_premium.append(entrada[3])
    i += 1
premiação_premium = float(input())
premiação = float(input())
print("-----\nBÔNUS\n-----")
i = 0
for y in canais:
    if inscritos[i] >= 1000:
        x = inscritos[i]
        contador = 0
        while x >= 1000:
            x -= 1000
            contador += 1
        x = contador * 1000
        if conteudo_premium[i] == "sim":
            print(f"{y}: R$", end=" ")
            print(f"{((x * premiação_premium) / 1000) + monetização[i]:.2f}")
        else:
            print(f"{y}: R$", end=" ")
            print(f"{((x * premiação) / 1000) + monetização[i] :.2f}")
    else:
        print(f"{y}: R$ {monetização[i]:.2f}")
    i += 1
