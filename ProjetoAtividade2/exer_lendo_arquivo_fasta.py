"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-05
Nome: Maria Paula Henriques Prandt

O exercício é para aprender a abrir, realizar a leitura e fechar um arquivo .fasta
"""

dna = open('Corona_genomic.fasta','r')
dna.readlines(1)
for i in dna.readlines():
    print(i, end='')
dna.close()
