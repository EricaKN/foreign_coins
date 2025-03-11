# FOREIGN COINS
The idea of the project is to have simple bot that will store the values of a given currency (let's start with EUR) and store it in a file.

# RUN WEBSCRAPING CODE
poetry run src/foreign_coins/scraping.py

# RUN CONVERSION API CODE
poetry run src/foreign_coins/conversion_api.py


On this code we use "AwesomeAPI", there is an important consideration about its use:


https://docs.awesomeapi.com.br/aviso-sobre-limites


"
Devido ao rápido e grande aumento no número de requisições nos últimos meses, que agora estão chegando a 100 milhões por dia, a AwesomeAPI implementará uma nova política para o plano gratuito a partir de 31 de março de 2025. As requisições mensais serão limitadas a 100 mil, com a contagem sendo reiniciada no primeiro dia de cada mês.

Essa ação de limitação é necessária para que possamos continuar oferecendo um serviço de alta qualidade e estabilidade para todos os nossos usuários. Para aqueles cujas necessidades excedem esse limite, recomendamos explorar nossos planos pagos.

Se tiver dúvidas ou precisar de assistência, entre em contato com nossa equipe de suporte.

Agradecemos por escolher a AwesomeAPI.
"

# SETUP
python3 -m venv venv
source venv/bin/activate

poetry 2.1.1

## POETRY
### To add a new library use:
poetry add <library>


### To install all dependecies listed at pyproject.toml:
poetry install


### To run the project:
poetry run python3 <script.py>


### To update dependecies:
poetry update requests