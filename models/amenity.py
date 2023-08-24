#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv

class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialiazes Amenity instance"""
        super().__init__(*args, **kwargs)
