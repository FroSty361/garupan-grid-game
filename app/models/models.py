from flask_sqlalchemy_lite import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Table, Column
from typing import List

db = SQLAlchemy()

# Characters Data

class Base(DeclarativeBase):
    pass

character_attribute_association = Table(
    "character_attribute_association",
    Base.metadata,
    Column("character_id", ForeignKey("character.id"), primary_key=True),
    Column("attribute_id", ForeignKey("character_attributes.id"), primary_key=True),
)

class Character(Base):
    __tablename__ = 'character'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(50))
    icon_url: Mapped[str] = mapped_column()

    attributes: Mapped[List["CharacterAttribute"]] = relationship(secondary=character_attribute_association, back_populates="characters")

class CharacterAttribute(Base):
    __tablename__ = 'character_attributes'

    id: Mapped[int] = mapped_column(primary_key=True)

    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[str] = mapped_column(String(100), nullable=False)

    characters: Mapped[List["Character"]] = relationship(secondary=character_attribute_association, back_populates="attributes")

# User Data