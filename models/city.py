#!/usr/bin/python3
"""City module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Attributes:
        state_id (str): state id
        name (str): city name
    """
    state_id = ''
    name = ''
