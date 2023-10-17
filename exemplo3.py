# Agora, abrindo um arquivo JSON para transformar em um dicionário

import json

with open('dadosJSON2.json', 'r', encoding='utf-8') as arquivo: # para evitar problema com caracteres especiais
    lista = json.load(arquivo) # carrega no meu dicionário
print(lista)

print('\n')

for item in lista: # acesso minha lista e meus itens separadamente, para poder manipular ao longo do programa
    print(item)

print('\n')

# realizando uma busca com nomes
for item in lista:
    if item['nome'] == 'Paulo Vieira':
        print("Encontrado!")