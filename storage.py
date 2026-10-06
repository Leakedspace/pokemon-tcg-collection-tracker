from pathlib import Path 
import json

# Loads the user's selected collection from the user data folder
def load_collection() -> tuple:
    user_folder = Path("user_data")
    json_files = list(user_folder.glob("*.json"))
    if not json_files:
        print("No saved collections found. Please start a new collection.")
        print()
        return None

    for number, json_file in enumerate(json_files, start=1):
        print()
        print(number, json_file.name)
        print()
    while True:
        try:
            set_choice = int(input("Choose a file: "))

            if 1 <= set_choice <=len(json_files):
                selected_file = json_files[set_choice - 1]
                break
            else:
                print("invaild choice")

        except ValueError:
            print("must use numbers")  

    set_name = selected_file.name.replace("_user.json", "")

    with open(selected_file, "r") as file:
            owned_cards = json.load(file)
    return owned_cards, set_name


# Loads the card set data for the user's selected collection
def load_set_data(set_name: str) -> tuple:
    api_folder = Path("api_data")
    selected_file = api_folder / f"{set_name}_data.json"
    with open(selected_file, "r") as file:
        set_data = json.load(file)
    return set_data, set_name

# Saves the user's collection to the user data folder
def save_collection(owned_cards: list, set_name: str) -> None:
    user_folder = Path("user_data")
    filename = user_folder / f"{set_name}_user.json"
    with open(filename, "w") as file:
        json.dump(owned_cards, file, indent=4)


# ---------------------
#   TESTING SECTION
# ---------------------


#checks if the correct file was loaded
def test_load_set_data():

    test_cards = [
                {
                "localId": "001",
                "name": "Tropius"
            },
            {
                "localId": "002",
                "name": "Grubbin"
            },
            {
                "localId": "003",
                "name": "Fomantis"
            }
        ]

    data_folder = Path("api_data")
    selected_file = data_folder / "test_data.json"
    with open(selected_file, "w") as file:
            json.dump(test_cards, file, indent=4)

    loaded_set_data, name = load_set_data("test")

    if name == "test":
        print("Passed, set name matches")
    else:
        print("Failed, set name does not match")

# Checks if the user data JSON was created and saved correctly
def test_save_collection():

    test_cards = ["001", "002", "003"]


    save_collection(test_cards, "test")

    data_folder = Path("user_data")
    selected_file = data_folder / "test_user.json"
    with open(selected_file, "r") as file:
        test_data = json.load(file)

    if test_cards  == test_data:
        print("Passed, the data matches")
    else:
        print("Failed, the data does not match")




def run_tests():
    
    test_save_collection()
    test_load_set_data()

# run_tests()