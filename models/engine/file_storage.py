#!/usr/bin/python3
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
    '''class that serializes instances to a JSON file and deserializes JSON file to instances'''
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
            json.dump(serialized_obj, json_file, indent=4)


    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file'''
        json_dict = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as json_file:
                json_dict = json.load(json_file)
        for key, value in json_dict.items():
            class_name, obj_id = key.split('.')
            if class_name in self.__valid_classes:
                obj = self.__valid_classes[class_name](**value)
                self.__objects[key] = obj



storage = FileStorage()
storage.reload()
