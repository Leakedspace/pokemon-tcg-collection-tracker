import requests
import json
from pathlib import Path

#  creates folder for API data
def create_folders() -> None:
    api_folder = Path("api_data")
    user_folder = Path("user_data")

    api_folder.mkdir(exist_ok=True)
    user_folder.mkdir(exist_ok=True)

# Sends a request to the API and returns the available Pokémon card sets
def get_sets() -> list:
    url = "https://api.tcgdex.net/v2/en/sets"

    try:
        response = requests.get(url)
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        print("Unable to connect to the Pokémon API. Please try again later.")
        return None


# displays the card set names in a list for selection
def display_card_sets(card_sets: list) -> tuple:
    
    print()
    print("==============================")
    print("Available Card Sets:")
    print("==============================")
    print()

    for number, card_set in enumerate(card_sets, start=1):
        print(number, card_set["name"])
    while True:
        try:
            print()
            set_choice = int(input("Choose a set: "))

            if 1 <= set_choice <= len(card_sets):
                selected_set = card_sets[set_choice - 1]
                print()
                print(selected_set["name"])
                set_id = selected_set["id"]
                set_name = selected_set["name"]
                break
            else:
                print("invaild choice")

        except ValueError:
            print("must use numbers")
        # print(set_name)
        # print(set_id)
    return set_id, set_name


# calls the api for the cards in a set and returns the data
def get_cards_for_set(set_id: str) -> list:
    url = f"https://api.tcgdex.net/v2/en/cards?set={set_id}"
    try:
        response = requests.get(url)
        data = response.json()
        # print("SET ID:", set_id)
        # print("CARD REQUEST:", response.url)
        return data
    except requests.exceptions.RequestException:
        print("Unable to connect to the Pokémon API. Please try again later.")
        return None

# saves the card data to a json file
def save_cards_to_json(cards: list, set_name:str) -> None:
    api_folder = Path("api_data")
    filename = api_folder / f"{set_name}_data.json"
    with open(filename, "w") as file:
        json.dump(cards, file, indent=4)
    print(f"Cards saved to {filename}")


# ---------------------
#   TESTING SECTION
# ---------------------


# Uses a test list to save data to a JSON file
# and checks if the saved data matches
def test_save_cards_to_json():

    test_cards = [
        {"localId": "001", "name": "Tropius"},
        {"localId": "002", "name": "Grubbin"},
        {"localId": "003", "name": "Fomantis"},
    ]
    save_cards_to_json(test_cards, "test")

    api_folder = Path("api_data")
    selected_file = api_folder / "test_data.json"
    with open(selected_file, "r") as file:
        test_data = json.load(file)

        if test_cards == test_data:
            print("Passed, the data matches")
        else:
            print("Failed, the data does not match")


def run_tests():
    test_save_cards_to_json()


# run_tests()
