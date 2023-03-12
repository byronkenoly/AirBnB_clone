#!/usr/bin/python3
"""
class BaseModel module - defines all common attributes/methods for other classes
Universal Unique Identifier(uuid)
uuid is a python lib which helps in generating random objects of 128 bits as ids
"""

import uuid
from datetime import datetime

class BaseModel:
    """Class BaseModel
	    
    Attributes:
        id (str): assigned with uuid when instance is created
        created_at (datetime): assign with the current datetime when an instance is created
        updated_at (datetime): time instance is updated
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f'[<{self.__class__.__name__}>] ({self.id}) <{self.__dict__}>'

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        self.__dict__.copy()['__class__'] = self.__class__.__name__
        self.__dict__.copy()['created_at'] = self.created_at.isoformat()
        self.__dict__.copy()['updated_at'] = self.updated_at.isoformat()
        
        return self.__dict__.copy()