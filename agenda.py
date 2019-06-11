agenda = {}

def Insert_contact(agenda):
    nome = str(input('Digite o nome do contato: '))
    numero = str(input('Digite o número do contato: '))
    agenda[nome] = numero
    print(agenda)

def Consult_agenda(agenda):
    nome = input('Digite o nome que deseja consultar: ')
    if nome in agenda:
        return agenda[nome]
    else:
        return None

def Save_agenda(agenda):
    nome_arquivo = input('Digite o nome do arquivo: ')
    arquivo = open(nome_arquivo, 'w')
    for nome in agenda:
        arquivo.write(nome + agenda[nome] + '\n')
    arquivo.close()
    print('Agenda salva!')



#Principal
print('='*30)
print( '       AGENDA TELEFONICA' )
print('='*30)
print('1. Inserir um contato \n2. Consultar telefone \n3. Remover um contato', '\n'
    '4. Listar toda a agenda \n5. Ler contatos de arquivo \n6. Salvar agenda \n7. Finalizar')
opção = input('Digite a opção desejada: ')
if opção == '1':
    Insert_contact(agenda)
elif opção == '2':
    telefone = Consult_agenda(agenda)
    print('\nConsultando Telefone...')
    if telefone is None:
        print('Contato não existe.')
    else:
        print('O contato é: ', telefone)
elif opção == '6':
    Insert_contact(agenda)
    Save_agenda(agenda)


