#!/usr/bin/python3
"""
BaseModel module - defines all common attributes/methods for other classes
Universal Unique Identifier(uuid)
uuid: a python lib which helps in generating random objects of 128 bits as ids
"""

import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel

    Attributes:
        id (str): assigned with uuid when instance is created
        created_at (datetime): current datetime when an instance is created
        updated_at (datetime): time instance is updated
    """

    def __init__(self, *args, **kwargs):
        """
            __init__ assigns values when object of the class is created
            *args: used to pass variable no. of non-key worded arguments
            **kwargs: used to pass keyworded, variable length argument list
            strptime() method creates datetime object from given string
            
            setattr() method is used to assign object attribute its value
            syntax: setattr(obj, var, val)
            obj: object whose which attribute is to be assigned
            var: object attribute to be assigned
            val: value with which var is to be assigned
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    if isinstance(value, str):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return f'[<{self.__class__.__name__}>] ({self.id}) <{self.__dict__}>'

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dict containing all keys/values of __dict__ of the instance
        """
        self.__dict__.copy()['__class__'] = self.__class__.__name__
        self.__dict__.copy()['created_at'] = self.created_at.isoformat()
        self.__dict__.copy()['updated_at'] = self.updated_at.isoformat()

        return self.__dict__.copy()