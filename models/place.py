#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, ForeignKey, Integer, Float)
import os
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A place to stay with its description"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(60))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review", backref="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            from models import storage
            return [i for i in storage.all() if i.value().__class__ == 'Review'
                    and i.value().place_id == self.id]
