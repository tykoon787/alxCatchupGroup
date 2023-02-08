#!/usr/bin/python3
"""
This module contains the parent class `BaseModel` to be inherited
by the subclasses of the AirBnB clone project
"""
from uuid import uuid4
from datetime import datetime
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
            date_created = datetime.today()
            self.created_at = date_created
            self.updated_at = date_created

    def __str__(self):
        """Prints out specified attributes of an instance"""
        classname = type(self).__name__
        iid = self.id
        i_dic = self.__dict__
        return "[{}] ({}) {}".format(classname, iid, i_dic)

    def save(self):
        """updates the `update_at` attribute with current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary with all key/values of __dict__"""
        d = self.__dict__
        d["__class__"] = type(self).__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
