#!/usr/bin/python3
"""Place module
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name
        description (str): descriptio
        number_rooms (int): number of available rooms
        max_guest (int): max no. of guests
        price_by_night (int): price of establishment
        latitude (float): lat
        longitude (float): longitude
        amenity_ids (list): amenity list
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
