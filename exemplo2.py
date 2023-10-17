import json

dicionario1 = {
    'codigo': 123,
    'nome': 'Paulo Vieira',
    'idade': 30,
    'altura': 1.80,
    'notas': [9, 7.5, 10, 8],
}

dicionario2 = {
    'codigo': 124,
    'nome': 'João Pedro',
    'idade': 32,
    'altura': 1.72,
    'notas': [9, 7.5, 10, 8],
}

lista = [dicionario1, dicionario2]

# Gerar um arquivo físicio JSON através dos dicionários em uma lista
with open('dadosJSON2.json', 'w', encoding='utf-8') as arquivo: # preciso dizer que é no modelo utf-8
    json.dump(lista, arquivo, indent=4, ensure_ascii=False) # O último parametro é para gerar um JSON com acentos! 