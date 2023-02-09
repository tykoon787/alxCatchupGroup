#!/usr/bin/python3
"""
This module contains the parent class `BaseModel` to be inherited
by the subclasses of the AirBnB clone project
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    Parent class that defines all common attributes and
    methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialises all instances with id and date attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Prints out specified attributes of an instance"""
        classname = type(self).__name__
        iid = self.id
        i_dic = self.__dict__
        return "[{}] ({}) {}".format(classname, iid, i_dic)

    def save(self):
        """updates the `update_at` attribute with current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns a dictionary with all key/values of __dict__"""
        
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict["__class__"] = type(self).__name__
        return new_dict
