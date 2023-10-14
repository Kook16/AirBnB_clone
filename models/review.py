#!/usr/bin/python3
'''The `Review` module

It defines one class, `Review(),
which inherits from `BaseModel()` class.`
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class representing user reviews'''
    place_id = ""
    user_id = ""
    text = ""
