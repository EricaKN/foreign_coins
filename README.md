# FOREIGN COINS
The idea of the project is to have simple bot that will store the values of a given currency (let's start with EUR) and store it in a file.

# SETUP

## CREATE AND ACTIVATE VENV
python3 -m venv venv


source venv/bin/activate

## INSTALL DEPENDECIES AT PYPROJECT.TOML
poetry install

# RUN SCRIPT
## RUN CONVERSION API CODE
poetry run api --option <1, 2 or 3>

### HELP
poetry run api --help


poetry run api -h

## WEBSCRAPING CODE
poetry run scraping 

### [TODO] Add another conversion options like <RUN CONVERSION API CODE>

# CRON SCHEDULING
## LOCALLY
### RUN THE COMMAND EVERY 1'
Add a new task for your cron service. For that:


1. Run the command: crontab -e 


2. Add the following line:


* * * * * cd /path/to/your/project/foreign_coins && . venv/bin/activate && poetry run api --option 1

### CHECK CRON SERVICE
To check if the cron service is running as expected, run the following command:


systemctl status cron

## ON LAST BASTION SERVER

# REMOTE SERVER
## ADD REMOTE SERVER AT /ETC/HOSTS
<server_ip_address> <server-name>

## ADD PUBLIC SSH-KEY AT AUTHORIZED_KEYS FILE
Add my public ssh-key at /home/<user>>/.ssh/authorized_keys

## ACCESS REMOTE SERVER
ssh <user>@<server-name>
# LITERATURE
## AWESOMEAPI
On this code we use "AwesomeAPI", there is an important consideration about its use:


https://docs.awesomeapi.com.br/aviso-sobre-limites


"
Devido ao rápido e grande aumento no número de requisições nos últimos meses, que agora estão chegando a 100 milhões por dia, a AwesomeAPI implementará uma nova política para o plano gratuito a partir de 31 de março de 2025. As requisições mensais serão limitadas a 100 mil, com a contagem sendo reiniciada no primeiro dia de cada mês.

Essa ação de limitação é necessária para que possamos continuar oferecendo um serviço de alta qualidade e estabilidade para todos os nossos usuários. Para aqueles cujas necessidades excedem esse limite, recomendamos explorar nossos planos pagos.

Se tiver dúvidas ou precisar de assistência, entre em contato com nossa equipe de suporte.

Agradecemos por escolher a AwesomeAPI.

## POETRY
poetry 2.1.1

### To add a new library use:
poetry add <library>

### To run the project:
poetry run python3 <script.py>

### To update dependecies:
poetry update requests
