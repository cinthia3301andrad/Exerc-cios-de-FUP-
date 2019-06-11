def Adicionar_livros():
    quant = int(input('Quantos livros você quer adicionar?: '))
    estoque = {}
    for i in range(0, quant):
        estoque['nome'] = str(input('Digite o nome do livro: '))
        estoque['autor'] = str(input('Digite o autor do livro: '))
        estoque['codigo'] = str(input('Digite o código do livro: '))
        arquivo = open('livros.txt', 'a')
        arquivo.write(estoque['nome'] + ',' + estoque['autor'] + ',' + estoque['codigo'] + ',' + '\n')
        print('Pronto! Livro adicionado' )
    arquivo.close()


def Mostrar_estoque():
    livros = []
    arquivo = open('livros.txt', 'r')
    print('O estoque ficou assim: ', )
    print()
    cont = 0
    for linha in arquivo:
        linha = linha.strip().split(',')
        livros.append(linha)
        cont += 1
        print('-'*30)
        print('         LIVRO cod.', linha[2] )
        print(' Nome:', linha[0], '\n Autor:', linha[1] )
    arquivo.close()


def Fazer_emprestimo():
    arquivo = open('livros.txt', 'r')
    livros = []
    livro = input('Qual livro você deseja pedir? ')
    for linha in arquivo:
        linha = linha.strip().split(',') 
        livros.append(linha[0])
    if livro in livros:
        print('Este livro está disponível para emprestimo!')
        return livro
    else:
        print('Não temos esse livro!')
        return None

def livro_emprestado(livro):
    arquivo = open('livros.txt', 'r+')
    for linha in arquivo:
        if livro in linha:
            arquivo.write('livro emprestado' + linha[2])
            print('OKay!')
            break
    arquivo.close()

print('Escolha uma opção: \n 1 - Adicionar livros \n 2 - Mostrar livros \n 3 - Pedir livro ')
opção =  int(input('')) 
if opção == 1:
    Adicionar_livros()
elif opção == 2:
    Mostrar_estoque()
elif opção == 3:
    livro = Fazer_emprestimo()
    if livro is not None:
        livro_emprestado(livro)