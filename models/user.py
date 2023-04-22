#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', back_populates='users',
                              cascade='all, delete')
        reviews = relationship('Review', back_populates='users')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
