# FOREIGN COINS
The idea of the project is to have simple bot that will store the values of a given currency (let's start with EUR) and store it in a file.

# RUN
poetry run src/foreign_coins/scraping.py


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