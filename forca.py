import random
def escolher_palavras(arquivos):
    arquivo = open(arquivos, 'r')
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
        if letra in escolha: #1° Condição da letra estar na minha palavra random.
                if letra_usada.count(letra) == 1:#2° condição, o usuário ter digitado a letra pela primeira vez
                        print('Você acertou!')
                        for i in range(len(escolha)):
                                if letra == escolha[i]:#Verificar onde a letra que o usuário digitou é igual a letra da palavra random.
                                        palavra[i] = letra #Substitui o traço pela letra digitada
                                        aux += 1
                        if aux == len(escolha):
                                print('Você ganhou!')
                                print(palavra)
                                break
                else:#Caso o usuário já tenha digitado a letra, ou seja, mais de 1 vez
                        print('Letra já usada!')
                print(palavra)
        else:#Se a letra não estiver na palavra random.
                quant_chutes += 1
                print('Você errou! Você tem mais', 6-quant_chutes, 'chances de errar')
                if quant_chutes == 6:
                        print('Suas chances acabaram!')
                        print('A palavra era: ', escolha)
                        break
                        



print('='*30)
print('         JOGO DA FORCA')
print('---- Você terá 6 chances! ----')
print('='*30)
palavra = escolher_palavras('gabriel.txt')
jogada(palavra)