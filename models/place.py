#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class Place:
    """ A place to stay """
    __tablename__ = 'place'
    city_id = ""
    user_id = ""
    name = Column(String, primary_key=True, nullable=False  )
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
