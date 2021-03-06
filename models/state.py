#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Used when FileStorage is used instead of DBStorage"""
            from models import storage
            return [i for i in storage.all() if i.value().__class__ == 'City'
                    and i.value().state_id == self.state_id]
