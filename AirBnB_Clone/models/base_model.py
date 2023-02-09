#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel():
    def __init__(self): 
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Function taht updates the public instance attribute `updated at` with the current date and time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Function that returns a dict rep of an instance
        """
        final_dict = {}
        key = "__class__"
        value = self.__class__.__name__
        final_dict[key] = value
        for key, value in self.__dict__.items():
            if key == "created_at":
                final_dict[key] = value.isoformat()
            if key == "updated_at":
                final_dict[key] = value.isoformat()
        return(final_dict)

