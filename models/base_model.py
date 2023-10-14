#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Initializer function'''
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        ft = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.datetime.strptime(val, ft))
                    else:
                        setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''print: [<class name>] (<self.id>) <self.__dict__>'''
        format_str = f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
        return format_str

    def save(self):
        '''updates the updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dict with all keys/vals of __dict__ of the instance'''
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
