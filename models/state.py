#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns a list of cities that have the same state_id as State.id."""
        from models import storage
        all_cities_dict = storage.all(City)
        cities_list = []
        for city in all_cities_dict.keys():
            if State.id in city:
                cities_list.append(all_cities_dict[city])
        return cities_list
