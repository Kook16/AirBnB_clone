#!/usr/bin/python3
'''A module which inherits from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''A class representing a real city'''
    state_id = ""
    name = ""
