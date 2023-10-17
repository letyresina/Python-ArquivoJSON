'''
    Exercício 1:
    Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma. 
    Cada linha do arquivo apresenta os dados de um aluno, no formato:
    RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
    Implemente um programa que leia este arquivo e gere um novo arquivo JSON no formato (no arquivo de exercício)
'''

import json

dicionario = {}

with open('exercicios/exercicio1/notas.csv', 'r', encoding='utf-8') as arquivo:
    cont = 1 # para nao ler a primeira linha
    for linha in arquivo:
        if cont > 1:
            lista = linha.split(';')
            print(lista)
            dicionario[lista[0]] = {"nome": lista[1], "notas": [lista[2], lista[3], lista[4], lista[5].replace('\n','')]}
        cont += 1
    with open('exercicios/exercicio1/dadosJSON.json', 'w') as arquivoJSON:
        json.dump(dicionario, arquivoJSON, indent=4)