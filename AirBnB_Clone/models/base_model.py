#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs): 
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()
       date_time_format = "%Y-%m-%dT%H:%M:%S.%f"

       if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        datetime.strptime(value, date_time_format)
                    if key == "updated_at":
                        datetime.strptime(value, date_time_format)
                    setattr(self, key, value)
       else:
           self.id = uuid4()        
           self.created_at = datetime.now()
           storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Function taht updates the public instance attribute `updated at` with the current date and time
        """
        storage.save()
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
                final_dict[key] = datetime.isoformat(value)
            if key == "updated_at":
                final_dict[key] = datetime.isoformat(value) 
        return(final_dict)

if __name__ == "__main__":

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
