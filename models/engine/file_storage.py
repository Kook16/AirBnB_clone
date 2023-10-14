#!/usr/bin/python3
'''The file_storage module'''
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes intas to JSON file and deserializes JSON file to insta'''
    __file_path = 'file.json'
    __objects = {}
    __valid_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id'''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(serialized_obj, json_file)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file'''
        str_dict = {}
        try:
            # with open(self.__file_path) as json_file:
            #     str_dict = json.load(json_file)
            # for key, value in str_dict.items():
            #     class_name, obj_id = key.split('.')
            #     obj = self.__valid_classes[class_name](**value)
            #     self.__objects[key] = obj
            with open(self.__file_path, 'r') as f:
                str_oj = json.load(f)
            for key, value in str_oj.items():
                class_v = self.__valid_classes[value['__class__']](**value)
                self.__objects[key] = class_v
        except FileNotFoundError:
            pass
