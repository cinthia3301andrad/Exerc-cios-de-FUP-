import random
def escolher_palavras():
    arquivo = open('palavras.txt', 'r')
    matriz_palavras = []
    for linha in arquivo.readlines():
        todas_palavras = linha.strip()
        matriz_palavras.append(todas_palavras)
    escolha = random.choice(matriz_palavras)
    return (escolha)

teste = escolher_palavras()
print(teste)