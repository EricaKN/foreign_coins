import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

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
            message = f'{timestamp} - Preço atual (EURBRL): {price}\n'
        else:
            print('Price not found')
            message = "Price not found"
    else:
        print('Error: page not found')
        message = "Error: page not found"
    return message

if __name__ == '__main__':
    get_price()


def main():
    result = get_price() 

    with open("quotation_scraping.txt", "a") as file:
        logging.basicConfig(filename='quotation_logs_scraping.log', level=logging.INFO)
        logger.info('Started')
        file.write(result)
        logger.info("Quotation for EURBRL successfully saved: %s", result.strip())
    print(result)

if __name__ == '__main__':
    main()