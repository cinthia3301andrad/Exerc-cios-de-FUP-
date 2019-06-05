arquivo = open("notas2.txt" , "r")
dicio = {}
lista_aprovados=[]
lista_reprovados=[]

for linha in arquivo.readlines():
    lista = linha.split(",")
    nome = lista[0].strip()
    nota = float(lista[1].strip())
    dicio[nome] = nota
    if dicio[nome] >= 7:
        lista_aprovados.append(nome)
    else:
        lista_reprovados.append(nome)
print('='*30)
print('Os aprovados : ', sorted(lista_aprovados))
print('='*30)
print('Os reprovados : ', sorted(lista_reprovados))


print(dicio[nome])
arquivo.close()

