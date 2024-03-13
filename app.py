# Quais valores serão armazenados?
# email, nome, telefone, estado e cidade

# Quais opções serão liberadas para guardar os dados?
# .txt, .db(sqlite3) e xlsx

# Organização
# Vou dividir por modulos 

import json
from values.values import names, emails, telephone, cityByState, state
import random
import os 
from time import sleep

def generateDataJsonTxt(values, amount):
    # Pega o valor e a quantidade desejada, fazendo o tratamento dos dados e deixando em um formato que facilite
    # A visualização
    listData = []
    
    for _ in range(amount):
        dictData = {}
        for value in values.values():
            if value == 'names':
                dictData['name']=(random.choice(names))
            if value == 'telephone':
                dictData['telephone']=(random.choice(telephone))
            if value == 'emails':
                dictData['email']=(random.choice(emails))
            if value == 'state':
                dictData['state']=(random.choice(state))
            if value == 'cityByState':
                # Escolhe a cidade com base no estado, caso não tenha seleciona aleatoriamente
                if 'state' in values.values():
                    dictData['city']=(random.choice(cityByState[dictData['state']]))
                else:
                    dictData['city']=(random.choice(cityByState[random.choice(state)]))
        listData.append(dictData)          
    return listData
    


def generateDataTXT(values, amount):
    data = generateDataJsonTxt(values, amount)
    with open('data.txt', 'a', newline='', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def generateDataDB(values, amount):
    print('db')
def generateDataXlsx(values, amount):
    print('xlsx')

def generateDataJson(values, amount):
    data = generateDataJsonTxt(values, amount)
    with open('data.json', 'a', newline='', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        

def questionsToGenerateData():
    values = str(input('''
Informe os valores que deseja gerar
1 - Nome
2 - Telefone   
3 - Email
4 - Estado
5 - Cidade
Exemplo: 1,3,4
'''))  
    # Converter a resposta para uma lista de string com os valores selecionados

    listValues = {
        '1': 'names',
        '2': 'telephone',   
        '3': 'emails',
        '4': 'state',
        '5': 'cityByState'
    }
    valuesSelectedStr = list(values.replace(',', ''))
    filtredValue = {key: value for key, value in listValues.items() if key in valuesSelectedStr}
    
    # Decidir o formato do arquivo e a quantidade que será gerada
    fileType = int(input('''
Você deseja salvar os dados gerados onde?
1 - txt
2 - db(sqlite3)
3 - xlsx
4 - JSON
'''))
    amount = int(input('Quantos dados devem ser gerados? \n'))   

    valoresteste = {
        'values': filtredValue,
        'fileType': fileType,
        'amount': amount
    }
    return valoresteste

def main():
    #  Print de apresentação do programa
    print('''
Olá, seja bem vindo ao gerador de dados para teste. Adiante serão
feitas algumas perguntas para que o gerador funcione de acordo com o seu objetivo.
Todas as perguntas tem um valor padrão definido, então caso seja enviado
uma resposta em branco o valor será preenchido para o padrão. No caso de perguntas que permitem
multipla escolha, separe cada valor com uma ","(virgula), sem a necessidade de espaço após a ","(virgula)''')
    
    #  Variables
    stop = False 
    # Variables from input

    while True:
        try:
            startingApp = str(input('Deseja inciar o gerador de dados falso?  não/sim \n'))
            if startingApp == 'não' or startingApp == "nao":
                return False
            elif startingApp == 'sim':
                #  Pegar os valores para gerar o conteúdo        
                questions = questionsToGenerateData()
                # Gerar os dados no arquivo escolhido
                if questions['fileType'] == 1:
                    generateDataTXT(questions['values'], questions['amount'])
                elif questions['fileType'] == 2:
                    generateDataDB(questions['values'], questions['amount'])
                elif questions['fileType'] == 3:
                    generateDataXlsx(questions['values'], questions['amount'])
                elif questions['fileType'] == 4:
                    generateDataJson(questions['values'], questions['amount'])
            else:
                print('Digite um valor válido')
        except:
            print('Digite um valor válido')    
        
main()