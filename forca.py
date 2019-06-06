import random
def escolher_palavras():
    arquivo = open('palavras.txt', 'r')
    lista_palavras = []
    for linha in arquivo.readlines():
        todas_palavras = linha.strip()
        lista_palavras.append(todas_palavras)
    escolha = random.choice(lista_palavras)
    return (escolha)


def jogada(escolha):
    print('Tente adivinhar a palavra:  ', end='')
    print(escolha)
    palavra = []
    for i in range(len(escolha)): #Adiciono traços na quantidade da minha palavra random.
         palavra.append('-')
    print(palavra)
    quant_chutes = 0
    aux = 0
    letra_usada = [] #Lista de letras que o usuário já digitou
    while quant_chutes <= 6:
        letra = input('Digite uma letra: ')
        letra_usada.append(letra)
        if letra in escolha: #Condição da letra estar na minha palavra random.
                if letra_usada.count(letra) == 1: #E o usuário não ter digitado ela ainda
                        print('Você acertou!')
                        for i in range(len(escolha)):
                                if letra == escolha[i]:#Verificar onde a letra que o usuário digitou é igual a letra da palavra random.
                                        resposta[i] = letra #Substitui o traço pela letra digitada
                else:#Caso o usuário já tenha digitado a letra
                        print('Letra já usada!')
                print(resposta)
        else:
                quant_chutes += 1
                print(quant_chutes)
                print('Você errou!')
                print(resposta)
                if quant_chutes == 6:
                        print('Suas chances acabaram!')
                        print('A palavra era: ', escolha)
                        break



print('='*30)
print('         JOGO DA FORCA')
print('---- Você terá 6 chances! ----')
print('='*30)

palavra = escolher_palavras()
jogada(palavra)