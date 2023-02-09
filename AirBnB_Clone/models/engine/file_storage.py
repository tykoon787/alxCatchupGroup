#!/usr/bin/python3
import json
import os

class FileStorage():
    """
    File Storage Class 
    .... 
    Attributes
    ----------
    file_path: String
    objects: dictionary

    ....
    Methods
    -------

    """
    def init(self):
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        """
        Function that returns the dictonary objects
        """
        self.__objects = self.__dict__
        return (self.__objects)

    def new(self, obj):
        """
        Function that sets in objects dictionary the obj key
        with <obj class name>.id
        """
        key = "{}.{}".format(self.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Function that serializes the obj dict to a json file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="w", encoding="utf-8") as f:
                json_string = json.dumps(self.__objects)
                f.write(json_string)
        else:
            print("File Path Does not exist")


    def reload(self): 
        """
        Deserialzes the JSON file to __objects (dictionary), then into an instance
        """
        with open(self.__file_path, mode="r", encoding="utf-8") as f:
            read_file = f.read().splitlines()
            # List of instances containing a list of dicts
            list_of_instances = json.loads(read_file)
            for item in list_of_instances:
                self.__objects = item.to_dictionary()
