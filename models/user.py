#!/usr/bin/python3
'''The `user` module

It defines one class, `User()`,
which inherits the `BaseModel()` class.`
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class representing a real user'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
