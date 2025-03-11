#Importando as bibliotecas
import requests
import json

#Função para retornar apenas o valor da cotação
def cotacao(escolha=1):

    #Escolha da moeda que se deseja buscar a cotação
    if escolha == 1:
        moeda = 'USDBRL'
    elif escolha == 2:
        moeda = 'EURBRL'
    elif escolha == 3:
        moeda = 'BTCBRL'
    else:
        return 'Moeda inválida!'


#Url da API
    url = 'https://economia.awesomeapi.com.br/json/last/'+ moeda[0:3] +'-'+ moeda[3:6]


#Capturando a cotação
    cotacao = requests.get(url).content


#Extraindo a cotação
    dic = json.loads(cotacao)


#Exibindo os resultados em tela
    return float(dic[moeda]["bid"])

if __name__ == '__main__':
    # Exemplo: Escolhendo a cotação do USD para BRL (USDBRL)
    resultado = cotacao(2)  # 1 para USDBRL, 2 para EURBRL, 3 para BTCBRL
    print(f'Cotação: {resultado}')