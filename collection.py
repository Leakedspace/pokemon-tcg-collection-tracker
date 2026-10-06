import json

# Displays the user's currently owned cards
def view_owned_cards(owned_data: list, set_data: list) -> None:
    print()
    if not owned_data:
        print("You don't own any cards in this set.")
        return
    for cards in owned_data:
        for card in set_data:
            if cards == card["localId"]:
                print(card["localId"], card["name"] )


# Adds a card to the user's owned cards
def add_card(set_data: list, owned_cards: list) -> list:

    while True:
        print()
        selected_card = input("Add card number (enter 0 to quit): ")
        if selected_card == "0":
            break

        

        try:
            found = False

            for card in set_data:
                if int(selected_card) == int(card["localId"]):
                    if card["localId"] in owned_cards:
                        print(card["name"], "is already in your collection")
                    else:
                        owned_cards.append(card["localId"])
                        print(card["name"], "Saved")
                    found = True

            if not found:
                print("Card number does not exist in this set.")
        
        except ValueError:
            print("must use numbers")

    return owned_cards


# Removes a card from the user's owned cards
def remove_card(owned_cards: list) -> list:
    while True:
        print()
        selected_card = input("To remove a card enter number (enter 0 to quit): ")

        if selected_card == "0":
            break

        try:
            found = False

            for card in owned_cards:
                if int(selected_card) == int(card):
                    print()
                    owned_cards.remove(card)
                    print(card, "Removed")
                    found = True
                    break

            if not found:
                print()
                print("This card is not in the list")
                print()
        except ValueError:
            print("must use numbers")

    return owned_cards

# Displays the user's currently missing cards
def get_missing_cards(set_data: list, owned_cards: list) -> list:
    print()

    missing_cards = []
    
    for card in set_data:
        if card["localId"] not in owned_cards:
             missing_cards.append(card["localId"])
             print(card["localId"], card["name"] )
             

    if not missing_cards:
        print("You are not missing any cards. Collection complete!")
    
    return missing_cards

# Calculates and displays the user's current completion rate    
def calculate_completion(owned_cards: list, set_data : list) -> float:
    print()
    completion_percentage = len(owned_cards) / len(set_data) * 100
    completion_result = round(completion_percentage, 1)
    print(f'You have completed {completion_result}%, and collected {len(owned_cards)} out of {len(set_data)}')
    return completion_result

# ---------------------
#   TESTING SECTION
# ---------------------

# Tests that completion is 0% when no cards are owned
def test_calculate_completion():
    set_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    owned_cards = []

    results = calculate_completion(owned_cards, set_data)

    if results == 0:
        print(" Test passed")
    else:
        print("Test fail")


# Tests that the correct missing cards are returned
def test_get_missing_cards():

    set_data = [
    {"localId": "001", "name": "Tropius"},
    {"localId": "002", "name": "Grubbin"},
    {"localId": "003", "name": "Fomantis"}
    ]

    test_data = ["003"]
    expected_missing = ["001", "002"]

    missing_cards = get_missing_cards(set_data, test_data)
    
    if missing_cards == expected_missing:
        print("Passed")
    else:
        print("Failed")


def run_tests():
    test_calculate_completion()
    test_get_missing_cards()

# run_tests()