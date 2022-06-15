""" A segunda chance consiste que em um proposta desenvolvida por
professores para acrescentar dois pontos extras na média de cada 
aluno caso seja necessário.
1: Precisamos a entradas relativa à quantidade de
alunos da classes sendo ela de 0 <= qtd_de_alunos <= 999;
2 : Receber as notas de cada aluno sendo elas números reais;
3 : Receber as notas da segunda chance de cada aluno sendo elas
números reais;
4: Recalcular as médias sabendo que a segunda acrescenta, no
máximo, dois pontos a mais na média final.
"""
qtd_de_alunos = int(input())
while (qtd_de_alunos < 0) or (qtd_de_alunos > 999):
    qtd_de_alunos = int(input())
alunos = []
segunda_chance = []
for x in range(qtd_de_alunos):
    nota = float(input())
    alunos.append(nota)
for y in range(qtd_de_alunos):
    atividade = float(input())
    segunda_chance.append(atividade)
nota_bônus = []
for z in range(qtd_de_alunos):
    if segunda_chance[z] == 10:
        nota_bônus.append(alunos[z] + 2)
        if (alunos[z] + 2) > 10:
            nota_bônus[z] = float(10)
    else:
        nota_bônus.append(alunos[z])
contador = 0
b = 0
while b < len(nota_bônus):
    if nota_bônus[b] != alunos[b]:
        contador += 1
    b += 1
a = 0   
print(f"NOTAS ALTERADAS: {contador}")
while a < len(nota_bônus):
    if nota_bônus[a] == alunos[a]:
        print(f"-(00{a+1}) original: {alunos[a]:05.2f} | final: {nota_bônus[a]:05.2f}")
    else:
        print(f"*(00{a+1}) original: {alunos[a]:05.2f} | final: {nota_bônus[a]:05.2f}")
    a += 1
