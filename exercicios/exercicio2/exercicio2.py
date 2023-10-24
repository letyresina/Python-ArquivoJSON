'''
    Exercício 2:
    Considere o arquivo “foods.CSV”, com três colunas, no formato abaixo, onde cada linha representa um 
    indivíduo com suas respectivas informações. 
    NAME,ID,FAVORITE FOOD
    Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato (arquivo)
'''

import json

dicionario = {}

with open('exercicios/exercicio2/foods.csv', 'r', encoding='utf-8') as arquivo:
    cont = 1 # para pular a primeira linha
    for linha in arquivo:
        if cont > 1:
            lista = linha.split(';')
            dicionario[lista[1]] = {"nome": lista[0], "food": lista[2].replace('\n','')}
        cont += 1

with open('exercicios/exercicio2/dadosJSON.json', 'w') as arquivoJSON:
        json.dump(dicionario, arquivoJSON, indent=4)