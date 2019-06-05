def ler_matriz(matriz):
    arquivo = open(matriz, 'r')
    listamatriz = arquivo.readlines()
    return listamatriz

def criar_matriz(matriz):
    matrizfinal = []
    for i in range(0,len(matriz)):
	    matrizfinal.append(matriz[i].strip().split(','))
    return matrizfinal


matrizA = ler_matriz('a.txt')
matrizAcriada = criar_matriz(matrizA)


matrizB = ler_matriz('b.txt')
matrizBcriada = criar_matriz


print (matrizA)
print (matrizAcriada)
print ('-'*30)
print(matrizB)