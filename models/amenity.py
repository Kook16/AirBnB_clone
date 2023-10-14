#!/usr/bin/python3
'''The `Amenity` module

It defines one class, `Amenity(),
which inherits from `BaseModel()` class.`
'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''A class represemting amenities'''
    name = ""
