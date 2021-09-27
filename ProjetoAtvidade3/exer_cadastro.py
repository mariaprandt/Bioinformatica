"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-04
Nome: Maria Paula Henriques Prandt
"""

print('Exercício 4 - Discionários e Listas')
cadastros = []
print('Cadastro de Pessoas e Calculo de IMC')
print(30*'-')

print('NOVO CADASTRO', 15*'-')
dados = dict()
pesotot = atot = IMCtot = 0

#Inclusão dos dados
while True:
    dados.clear()
    dados['nome'] = str(input('Nome:'))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]:')).upper()[0]

        #Validação
        if dados['sexo'] in 'MF':
            break
        print('Erro! Digite [M/F]')

    dados['peso'] = float(input('Peso: '))
    pesotot += dados['peso']
    dados['altura'] = float(input('Altura: '))
    atot += dados['altura']
    dados['IMC'] = round(dados['peso'] / (dados['altura']**2), 2)
    IMCtot += dados['IMC']
    cadastros.append(dados.copy())

    #Continuar ou parar
    while True:
        c = str(input('Deseja continuar [S/N]: ')).upper()[0]

        #Validação
        if c in 'SN':
            break
        print('Eroo! Digite [S/N]')

    if c in 'N':
        break

#Exibir
for i in range(0, len(cadastros)):
    print(cadastros[i])

#Contagem de informações
print(f'\nA) O total de pessoas cadastradas foi de {len(cadastros)}')
print(f'\nB) O peso médio das pessoas é de {pesotot/len(cadastros)}')
print(f'\nC) A altura média das pessoas é de {atot/len(cadastros)}')
print(f'\nD) O IMC médio das pessoas é de {IMCtot/len(cadastros)}')
