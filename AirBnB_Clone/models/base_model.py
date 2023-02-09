#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

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
                        value = value.strptime(value, date_time_format)
                    if key == "updated_at":
                        value = value.strptime(value, date_time_format)
                    setattr(self, key, value)
       else:
           self.id = uuid4()        
           self.created_at = datetime.now()

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
        date_time_format = "%Y-%m-%dT%H:%M:%S.%f"
        final_dict = {}
        key = "__class__"
        value = self.__class__.__name__
        final_dict[key] = value
        for key, value in self.__dict__.items():
            if key == "created_at":
                final_dict[key] = value.strftime(date_time_format)
            if key == "updated_at":
                final_dict[key] = value.strftime(date_time_format)
        return(final_dict)

if __name__ == "__main__":

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
