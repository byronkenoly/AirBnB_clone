#!/usr/bin/python3
"""
class FileStorage:
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """Class FileStorage

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): stores alll objects by <class name>.id
    """
    __file_path = 'BaseModel_objects.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        process of encoding JSON is usually called SERIALIZATION

        serializes __objects to the JSON file (path: __file_path)
        conversion to JSON done by dumps() function
        """
        json_dict = {}
        for key, val in self.__objects.items():
            json_dict[key] = val.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        DESERIALIZATION is the opposite of serialization
        Its the conversion of JSON objects into their respective python objects

        deserializes the JSON file to __objects only if __file_path exists
        conversion back to python object done by load() function
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f)
            for key, val in json_dict.items():
                self.__objects[key] = eval(val['__class__'])(**v)
