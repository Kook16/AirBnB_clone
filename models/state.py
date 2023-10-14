#!/usr/bin/python3
'''The `State` module

It defines one class, `State(),
which inherits from `BaseModel()` class.`
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''A class representing a real state'''
    name = ''
