from sqlalchemy import Null

from data_seeds.characters.characters_seed_data import characters_data

character_names = []

def fill_character_names() -> bool:
    if len(character_names) == 0:
        if characters_data is None or len(characters_data) == 0:
            print("No Characters Seed Data Found For Retrieving Names In ui-utils")

            return True

        for character in characters_data:
            name = character["name"]

            character_names.append(name)

    return False

def character_search(character_name_input: str):
    # check if character has already been used in grid
    # if so, return "character already used!"

    had_error: bool = fill_character_names() # Only fills if character_names is None or empty

    if had_error:
        print("Stopping character search Due To Error")

        return Null

    character_name_input = character_name_input.strip()

    matched_character_names: list = []

    for character_name in character_names:
        character_name_nicks =  character_name.split("|") # names delimiter between is |

        if match_character_name_with_nicks(character_name_input, character_name_nicks, False):
            print(character_name_nicks[0])

            matched_character_names.append(character_name_nicks[0])

    return matched_character_names

def match_character_name_with_nicks(character_name_input: str, character_name_nicks: list, case_sensitive: bool):
    if character_name_input == "" or character_name_nicks == "":
        return False

    for character_name_nick in character_name_nicks:
        if not case_sensitive:
            character_name_input = character_name_input.lower()
            character_name_nick = character_name_nick.lower()

        if character_name_input in character_name_nick:
            return True

    return False

if __name__ == "__main__":
    fill_character_names()