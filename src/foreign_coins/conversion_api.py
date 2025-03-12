import requests
import json
import logging
import argparse

logger = logging.getLogger(__name__)

def quotation(option=1):

    # Choose which conversion you would like
    if option == 1:
        coin = 'EURBRL'
    elif option == 2:
        coin = 'USDBRL'
    elif option == 3:
        coin = 'BTCBRL'
    else:
        return 'Invalid option!'


# API's URL
    url = 'https://economia.awesomeapi.com.br/json/last/'+ coin[0:3] +'-'+ coin[3:6]


# Request information
    quotation = requests.get(url).content

# Extract info
    dic = json.loads(quotation)

    return coin, dic[coin]

def main():
    parser = argparse.ArgumentParser(description='Currency quotation')
    parser.add_argument('--option', type=int, required=True, help='Options: (1: EURBRL, 2: USDBRL, 3: BTCBRL)')

    args = parser.parse_args()
    coin, result = quotation(args.option) 
     
    if isinstance(result, str): # check if there is an error message
        print("error!")
        print(result)
    else:
        date_hour = result["create_date"]
        message = (f'{date_hour[8:10]}/{date_hour[5:7]}/{date_hour[0:4]} {date_hour[10:19]} - Preço atual ({coin}): {result["bid"]} Brazilians Reais\n')
        with open("quotation_api.txt", "a") as file:
            logging.basicConfig(filename='quotation_logs_api.log', level=logging.INFO)
            logger.info('Started')
            file.write(message)
            logger.info("Quotation for %s successfully saved: %s", coin, message.strip())
        print(message)

if __name__ == '__main__':
    main()