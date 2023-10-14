#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class representing user reviews'''
    place_id = ""
    user_id = ""
    text = ""
