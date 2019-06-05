def criar_matriz(matriz):
    arquivo = open(matriz, 'r')
    matriz = []
    for linha in arquivo.readlines():
        lista = linha.strip().split(",")
        matriz.append(lista)
    return(matriz)


def multmatriz(matriz1,matriz2):
    matriz3 = []
    for linha in range(len(matriz1)):
        matriz3.append([])
        for coluna in range(len(matriz2[0])):
            matriz3[linha].append(0)
            for k in range(len(matriz1[0])):
                matriz3[linha][coluna] += (int(matriz1[linha][k]))* (int(matriz2[k][coluna]))				
    return matriz3


print('----- ESSA É A MATRIZ A ------')
matrizA = criar_matriz('a.txt')
print(matrizA)
print()
print('----- ESSA É A MATRIZ B ------')
matrizB = criar_matriz('b.txt')
print(matrizB)
print()
print('----- ESSA É A MATRIZ C ------')
matrizC = multmatriz(matrizA,matrizB)
print(matrizC)



