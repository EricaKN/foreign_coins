import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_price():
    url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=BRL'  
 
    # To avoid block from an automatic User-Agent we add the "headers"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        price_tag = soup.find('p', class_='sc-294d8168-1 hVDvqw') 
        if price_tag:
            price = price_tag.text.strip()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{timestamp} - Preço atual: {price}')
        else:
            print('Preço não encontrado!')
    else:
        print('Erro ao acessar a página.')

if __name__ == '__main__':
    get_price()
