from data_seeds.characters.characters_seed_data import characters_data

character_names = []

def character_search(character_name_input: str):
    # check if character has already been used in grid
    # if so, return "character already used!"

    for character_name in character_names:
        if character_name_input.lower().strip() == character_name.lower():
            print(character_name)

if __name__ == "__main__":
    if characters_data is None or len(characters_data) == 0:
        print("No Characters Seed Data Found For Retrieving Names In ui-utils")

    print("Hi!")

    for character in characters_data:
        name = character["name"]

        character_names.append(name)