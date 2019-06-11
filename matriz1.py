def Matriz_a(m, n):
    matrizA = []
    matrizB = []
    for linha in range(0, m):
        matrizA.append([])
        for coluna in range(0,n):
            matrizA[linha].append(input('Digite o valor: '))
    for linha in range(0,n):
        matrizB.append([])
        for coluna in range (0, m):
            matrizB[linha].append(matrizA[coluna][linha])
    print('Matriz A: ')
    for linha in range(0, len(matrizA)):
        print(matrizA[linha])
        print()
    print('Matriz B: ')
    for linha in range(0, len(matrizB)):
        print(matrizB[linha])
        print()
#Principal
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
Matriz_a(linhas, colunas)