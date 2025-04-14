termo = int(input('Digite um número (como termo): '))
razao = int(input('Digite a razão da PA: '))
#FÓRMULA DO ENÉSIMO TERMO DE PA
decimo = termo + (10 - 1) * razao
for pa in range(termo, decimo + razao, razao):
    print(pa)
