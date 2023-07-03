# ENTRADA
alunos = int(input("Quantidade de alunos: "))
trabalhos = int(input("Quantidade de trabalhos: "))

somap = 0
somat = 0
mp = 0
mt = 0
mf = 0
media_sala = 0
cont_apr = 0
cont_rec = 0
cont_rep = 0

# PROCESSAMENTO
i = 1
while i <= alunos:
    print('=' * 25)

    # ENTRADA DAS NOTAS
    p1 = float(input("Nota da 1º prova: "))
    p2 = float(input("Nota da 2º prova: "))
    ps = float(input("Nota da prova substitutiva: "))

    t = 1
    somat = 0
    while t <= trabalhos:

        # ENTRADA DA NOTA DO TRABALHO DO ALUNO
        nota_trab = float(input(f"Nota do Trabalho {t}: "))
        somat += nota_trab
        t += 1

    # CÁLCULO DAS NOTAS
    if ps > p2:
        mp = ((p1 + ps) / 2) * 0.6
    
    elif ps > p1:
        mp = ((p2 + ps) / 2) * 0.6

    else:
        mp = ((p1 + p2) / 2) * 0.6

    mt = (somat / trabalhos) * 0.4

    mf = mp + mt

    media_sala += mf

    mc = media_sala / alunos

    # MÉDIA FINAL DO ALUNO E SUA CONDIÇÃO
    if mf >= 6.0:
        print(f"Média final do aluno {i}: {mf:.2f} - Aprovado")
        cont_apr += 1

    elif mf >= 4.0 and mf < 6.0:
        print(f"Média final do aluno {i}: {mf:.2f} - Recuperação")
        cont_rec += 1

    elif mf < 4.0:
        print(f"Média final do aluno {i}: {mf:.2f} - Reprovado")
        cont_rep += 1

    i += 1

print('=' * 25)

# SAÍDA
print(f"Alunos aprovados: {cont_apr}")
print(f"Alunos de recuperação: {cont_rec}")
print(f"Alunos reprovados: {cont_rep}")
print(f"Média da Classe: {mc:.2f}")