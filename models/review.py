#!/usr/bin/python3
"""Review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): actual review
    """
    place_id = ''
    user_id = ''
    text = ''
