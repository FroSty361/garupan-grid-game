from sqlalchemy import select
from app import create_app
from models.models import db, Base, Character, CharacterAttribute
from characters_seed_attribute_data import character_attributes_data
from characters_seed_data import characters_data

def seed_characters_database():
    app = create_app()

    with app.app_context():
        Base.metadata.create_all(db.engine)

        character_attributes = {}

        for category_name, value in character_attributes_data:
            lookup_key = f"{category_name}:{value}"

            if lookup_key in character_attributes:
                continue

            character_attribute_statement = select(CharacterAttribute).where(CharacterAttribute.category_name == category_name, CharacterAttribute.value == value)
            character_attribute = db.session.scalars(character_attribute_statement).first()

            if not character_attribute: # If It Does Not Exist Yet
                attribute = CharacterAttribute(category_name=category_name, value=value)
                character_attributes[lookup_key] = attribute

                db.session.add(attribute)
            else:
                character_attributes[lookup_key] = character_attribute

        db.session.commit()

        for character_data in characters_data:
            character_statement = select(Character).where(Character.name == character_data["name"])
            character = db.session.scalars(character_statement).first()

            if not character: # If It Does Not Exist Yet
                new_character = Character(name=character_data["name"], icon_url=character_data["icon_url"])

                for attribute in character_data["character_attributes"]:
                    category_name, values = attribute.split(":", 1)

                    for value in values.split("|"):
                        lookup_key = f"{category_name}:{value}"

                        if lookup_key in character_attributes:
                            new_character.attributes.append(character_attributes[lookup_key])
                        else:
                            print(f"No Attribute Found For{lookup_key}")

                db.session.add(new_character)
            else:
                # If Data Updated

                for character_attribute_key in character_attributes_data:
                    pass

        db.session.commit()

if __name__ == "__main__":
    seed_characters_database()