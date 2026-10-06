# Pokémon TCG Collection Tracker

The Pokémon TCG Collection Tracker is a menu-driven Python program for recording progress toward completing a Pokémon card set. It retrieves card and set information from the TCGdex API, stores the selected set locally, and allows the user to view owned cards, add or remove cards, view missing cards, and calculate collection completion.

## Requirements

- Python 3
- An internet connection when starting a new set
- The Python `requests` package

Install the required package with:

python -m pip install requests

No API key is required.

## Running the program

Open a terminal in the project folder and run:


python pokemon_tracker.py

The main menu provides three options:

1. **Start a new set** - retrieves the available Pokémon card sets, saves the selected set's card data, and creates an empty user collection.
2. **Load Collection** - loads a saved collection and opens the collection menu.
3. **Quit** - closes the program.

After loading a collection, the collection menu allows the user to:

- view owned cards;
- add a card by entering its card number;
- remove an owned card;
- view missing cards; and
- view the number and percentage of cards collected.

## Project structure


KIT101_assingment_2/
├── pokemon_tracker.py
├── pokemon_api.py
├── collection.py
├── storage.py
├── GENAI_DISCLOSURE.md
├── api_data/
└── user_data/

- `pokemon_tracker.py` contains the main menu and collection menu.
- `pokemon_api.py` retrieves set and card data from the TCGdex API and saves card data locally.
- `collection.py` manages owned and missing cards and calculates collection completion.
- `storage.py` saves and loads user collections and their corresponding set data.
- `api_data` stores card data in files named `<set_name>_data.json`.
- `user_data` stores owned-card lists in files named `<set_name>_user.json`.

The folders are created automatically when the program starts.

## Testing

Test functions are included in `collection.py`, `pokemon_api.py`, and `storage.py`.

To run the tests in a module, uncomment the `run_tests()` call at the bottom of that file and run the module. For example:

python collection.py

Run the tests in `pokemon_api.py` before the tests in `storage.py`, because the storage test expects the API test data file to exist.

## Data and external service

The program uses the English-language TCGdex API:

https://api.tcgdex.net/v2/en/

A new set requires an internet connection. Previously saved collections can be loaded from the local JSON files without contacting the API.
