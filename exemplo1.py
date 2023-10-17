dicionario = {
    'codigo': 123,
    'nome': 'Paulo Vieira',
    'idade': 30,
    'altura': 1.80,
    'notas': [9, 7.5, 10, 8],
    
}

import json # para importar as funcionalidades

texto = json.dumps(dicionario) # gera uma string em formato JSON
print(texto)

# Gerar um arquivo físicio JSON através do dicionário
with open('dadosJSON.json', 'w') as arquivo:
    json.dump(dicionario, arquivo, indent=4) # isso gera um arquivo em formato JSON no programa