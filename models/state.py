#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models import storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class which contains __tablename__, name"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """gets all cities related to this state"""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            city_objs = []
            all_city = storage.all(City)
            for k, v in all_city.items():
                if v.state_id == self.id:
                    city_objs.append(v)
            return city_objs
