import pokemon_api
import storage
import collection

import pathlib
from urllib import response
from pathlib import Path
import json


def menu() ->None:
    pokemon_api.create_folders()
    print()
    print("==============================")
    print("      POKÉMON TCG TRACKER")
    print("==============================")
    print()
    while True:
        print("1. Start a new set")
        print("2. Load Collection")
        print("3. Quit")
        print()

        choice = input("Choose an option: ")

        if choice == "1":
            card_sets = pokemon_api.get_sets()

            if card_sets is None:
                continue
            set_id, set_name = pokemon_api.display_card_sets(card_sets)
            cards = pokemon_api.get_cards_for_set(set_id)

            if cards is None:
                continue
            
            pokemon_api.save_cards_to_json(cards, set_name)

            user_file = Path("user_data") / f"{set_name}_user.json"

            if user_file.exists():
                print("You already have a collection for this set.")
            else:
                owned_cards = []
                storage.save_collection(owned_cards, set_name)

            print()
        # Call upon display_card_sets()

        elif choice == "2":
            result = storage.load_collection()
            
            if result is None:
                continue
            owned_cards, set_name = result
            set_data, set_name = storage.load_set_data(set_name)
            collection_menu(owned_cards, set_data, set_name)

        # Load existing json

        elif choice == "3":
            break
        # ends the program
      
        else:
            print("Invalid choice")


def collection_menu(owned_cards: list, set_data:list, set_name:str) -> None:
    while True:
        print()
        print("1. View owned cards")
        print("2. Add card")
        print("3. Remove card")
        print("4. View missing cards")
        print("5. View completion")
        print("6. Back")
        print()
        
        choice = input("Choose an option: ")

        if choice == "1":
            collection.view_owned_cards(owned_cards, set_data)

        elif choice == "2":
            collection.add_card(set_data, owned_cards)
            storage.save_collection(owned_cards,set_name)

        elif choice == "3":
            collection.remove_card(owned_cards)
            storage.save_collection(owned_cards,set_name)

        elif choice == "4":
            collection.get_missing_cards(set_data, owned_cards)

        elif choice == "5":
            collection.calculate_completion(owned_cards, set_data)

        elif choice == "6":
            print()
            break

        else:
            print("Invalid choice")

def main():
    menu()


main()
