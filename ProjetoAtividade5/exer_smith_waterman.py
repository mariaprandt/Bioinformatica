"""
Algoritmos-em-bioinformatica
atividade-05-exercicio-02
Nome: Maria Paula Henriques Prandt
"""

import numpy as np

# Função Smith Waterman
def smith_waterman(seq1, seq2):
    t1 = len(seq1) + 1
    t2 = len(seq2) + 1
    m = np.zeros((t2, t1))
    back = np.zeros((t2, t1))

    # Construindo a matriz de smith waterman
    for i in range(1, t2):
        for j in range(1, t1):
            topo = m[i - 1, j] - 2
            esquerda = m[i, j - 1] - 2
            if seq1[j - 1] == seq2[i - 1]:
                diagonal = m[i - 1, j - 1] + 1
            else:
                diagonal = m[i - 1, j - 1] - 1
            valor = np.array([topo, esquerda, diagonal])
            if valor.max() > 0:
                m[i, j] = valor.max()

                # Construindo uma matriz auxiliar para o processo de backtracking, nela ficará guardado a informação de qual direção veio o valor de cada posição
                if valor.max() == topo:
                    back[i, j] = 1
                elif valor.max() == esquerda:
                    back[i, j] = 2
                else:
                    back[i, j] = 3
            else:
                m[i, j] = 0
    print(f'A Matriz de Smith Waterman é: \n {m}')

    # Realizando o processo de backtracking
    s1 = ' ' + seq1
    s2 = ' ' + seq2
    match1 = list()
    match2 = list()
    contador = 0
    print('\nOs possiveis alinhamentos locais são: \n')

    # O FOR ira percorrer a matriz em buscas das posições em que os valores máximos aparecem
    for i in range(0, t2):
        for j in range(0, t1):
            if m[i, j] == m.max():
                ii = i
                jj = j
                contador += 1
                # Toda vez que um valor máximo for encontrado, o processo de backtracking se inicia
                print(f'\n{contador}) Partindo da posição ({ii},{jj})')
                while m[ii, jj] != 0:

                    # Vamos checar de onde veio o valor da posição em que estamos
                    if back[ii, jj] == 3:
                        # o valor veio da "diagonal"
                        match1.append(s1[jj])
                        match2.append(s2[ii])
                        jj -= 1
                        ii -= 1
                    elif back[ii, jj] == 1:
                        # o valor veio do "topo"
                        match1.append('-')
                        match2.append(s2[ii])
                        ii -= 1
                    else:
                        # o valor veio do "lado"
                        match2.append('-')
                        match1.append(s1[jj])
                        jj -= 1
                match1 = match1[::-1]
                match2 = match2[::-1]
                print(f'\n {match1}\n {match2}')
                match1.clear()
                match2.clear()

#Determinando as sequêcias de nucleotídeos usadas.
sequencia1 = 'GGATAT'
sequencia2 = 'GATGAT'
smith_waterman(sequencia1, sequencia2)
