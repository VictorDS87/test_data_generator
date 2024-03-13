import os 

import json
import random
from values.values import names, emails, telephone, cityByState, state
from time import sleep

class questionsToGenerateData():
    # Faz as perguntas e retorna o valor e confere se o valor é valido
    # No fim retorna um dicionario com os valores 
    def __init__(self):
        if not self.valuesSelected() or not self.filetypeSelected() or not self.amountSelected():
            return  # Sai do método __init__ e interrompe a execução do programa

        self.returnData()
    def valuesSelected(self):
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
        # Verifica se o valor selecionado é válido 
        if all(value in listValues for value in valuesSelectedStr):
            self.filtredValue = {key: value for key, value in listValues.items() if key in valuesSelectedStr}
            return True
        else:
            print('deu false mas n pa')
            return False
    def filetypeSelected(self):
        self.fileType = int(input('''
Você deseja salvar os dados gerados onde?
1 - txt
2 - db(sqlite3)
3 - xlsx
4 - JSON
'''))
        # Converte a resposta para uma lista de valores, logo após verifica se o valor escolhido é valido 
        listFileType = {
            1: 'txt',
            2: 'db',   
            3: 'xlsx',
            4: 'JSON'
        }
    
        if self.fileType in listFileType:
            filtredValue = {key: value for key, value in listFileType.items() if key == self.fileType}
            return filtredValue
        else:
            return False
    def amountSelected(self):
        self.amount = int(input('Quantos dados devem ser gerados? obs: Quanto maior a quantidade mais tempo levará\n'))   
    def returnData(self):
        data = {
        'values': self.filtredValue,
        'fileType': self.fileType,
        'amount': self.amount
        }
        print(data)
        return data
    
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
def generateDataJson(values, amount):
    data = generateDataJsonTxt(values, amount)
    with open('data.json', 'a', newline='', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def generateDataDB(values, amount):
    print('db')
def generateDataXlsx(values, amount):
    print('xlsx')





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
                questions = questionsToGenerateData().returnData()
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