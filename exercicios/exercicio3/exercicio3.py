'''
    Exercício 3:
    Implemente um sistema para cadastro de Pets, com as opções Inserir, Excluir, Listar Todos. Utilize um 
    arquivo JSON para armazenar as informações. O arquivo JSON deve ter a estrutura abaixo e conforme as 
    operações realizadas, o arquivo deve ser modificado
'''

import time
import json

def menuOpcoes():
    print("Seja bem-vindo(a) ao sistema Pet Store!")
    print("Como podemos te ajudar hoje?")
    print("Menu de opções")
    print("\n 1 - Cadastrar Pet; \n 2 - Listar todos os Pets \n 3 - Editar Pet \n 4 - Excluir Pet \n 5 - Encerrar o programa")
    
dicionarioPet = {}
lista = []

while True:
    menuOpcoes()
    opcao = int(input("Qual a opção desejada? \n"))
    if opcao == 1:
        # Cadastrar pet novo, sem excluir outros pré-cadastrados
        with open ('exercicios/exercicio3/dadosPet.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        tipo = input("Qual o tipo do pet que iremos cadastrar? \n")
        nome = input("Qual o nome do pet que iremos cadastrar? \n")
        idade = int(input("Qual a idade do pet que iremos cadastrar? \n"))
        dicionarioPet = {"tipo": tipo, "nome": nome, "idade": idade}
        lista.append(dicionarioPet)
        with open('exercicios/exercicio3/dadosPet.json', 'w', encoding='utf-8') as arquivoJSON:
            json.dump(lista, arquivoJSON, indent=4, ensure_ascii=False)
        time.sleep(1)
    if opcao == 2:
        # Listar todos os pets existentes no sistema
        with open ('exercicios/exercicio3/dadosPet.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        print("Pets cadastrados em nosso sistema!")
        for item in lista:
            print(f"\n Tipo: {item['tipo']} \n Nome: {item['nome']} \n Idade: {item['idade']} \n")
        time.sleep(1)
    if opcao == 3:
        # Editar um pet pré-existente no sistema
        with open ('exercicios/exercicio3/dadosPet.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        nome = input("Qual nome do pet que deseja editar? \n")
        encontrado = False
        for item in lista:
            if item["nome"] == nome:
                encontrado = True
                print(f"O que você deseja editar para o {nome}?")
                print("\n 1 - Nome; \n 2 - Tipo; \n 3 - Idade")
                editaOpcao = int(input("Informe a opção desejada \n"))
                if editaOpcao == 1:
                    item["nome"] = input("Digite o novo nome: ")
                elif editaOpcao == 2:
                    item["tipo"] = input("Digite o novo tipo: ")
                elif editaOpcao == 3:
                    item["idade"] = input("Digite a nova idade: ")
                else:
                    print("Opção inválida.")
        if not encontrado:
            print(f"O nome {nome} não foi existe em nosso sistema!")

        with open('exercicios/exercicio3/dadosPet.json', 'w', encoding='utf-8') as arquivoJSON:
            json.dump(lista, arquivoJSON, indent=4, ensure_ascii=False)
        time.sleep(1)

    if opcao == 4:
        # Excluir um pet pré-existente no sistema
        with open ('exercicios/exercicio3/dadosPet.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        nome = input("Qual nome do pet que deseja excluir? \n")
        encontrado = False
        for item in lista:
            if item['nome'] == nome:
                lista.remove(item)
                print(f"O nome {nome} foi removido!")
                encontrado = True
        if not encontrado:
            print(f"O nome {nome} informado não existe em nosso sistema! Por favor tente novamente")

        with open('exercicios/exercicio3/dadosPet.json', 'w', encoding='utf-8') as arquivoJSON:
            json.dump(lista, arquivoJSON, indent=4, ensure_ascii=False)

        time.sleep(1)
    if opcao == 5:
        # Encerrar o programa
        print("Obrigada por utilizar o sistema Pet Store!")
        break