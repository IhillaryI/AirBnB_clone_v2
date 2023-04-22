#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k in ['updated_at', 'created_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                if k != '__class__':
                    setattr(self, k, v)
                if os.getenv('HBNB_TYPE_STORAGE') == 'db':
                    if not kwargs.get('id'):
                        setattr(self, 'id', str(uuid.uuid4()))
                    if not kwargs.get('created_at'):
                        setattr(self, 'created_at', datetime.utcnow())
                    if not kwargs.get('updated_at'):
                        setattr(self, 'updated_at', datetime.utcnow())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        parse_dict = self.__dict__.copy()
        if parse_dict.get('_sa_instance_state'):
            del parse_dict['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, parse_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete()
