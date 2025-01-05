#!/usr/bin/python3
"""Contains the Place model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


place_amenity = Table('place_amenity', Base.metadata,
                     Column('place_id', String(60),
                           ForeignKey('places.id'),
                           primary_key=True,
                           nullable=False),
                     Column('amenity_id', String(60),
                           ForeignKey('amenities.id'),
                           primary_key=True,
                           nullable=False))


class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship("Amenity", secondary="place_amenity",
                           viewonly=False)
    amenity_ids = []

    if models.storage_type != 'db':
        @property
        def amenities(self):
            """Getter for amenities in file storage"""
            amenity_list = []
            for amenity in models.storage.all("Amenity").values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities in file storage"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
