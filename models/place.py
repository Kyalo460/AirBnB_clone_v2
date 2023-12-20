#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    description = Column(String(128), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='places', cascade='all, delete-orphan')
    amenity_ids = []

    @property
    def reviews(self):
        """Returns a list of Review intances that have the same place_id as Place.id."""
        from models import storage
        all_reviews_dict = storage.all(Review)
        reviews_list = []
        for review in all_reviews_dict.keys():
            if Review.id in review:
                reviews_list.append(all_reviews_dict[review])
        return reviews_list
