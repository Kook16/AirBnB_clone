#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    '''A class representing a real user'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
