linha = list()

for c in range(1,6):
    for i in range (1,c+1):
        linha.append(c*i)
    print(f'{linha}')
    linha.clear()

print('\n')

for j in range(1,6):
    for b in range (1,j+1):
        print(f'{j*b}', end=' ')
    print('')