#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd
from base_model import BaseModel
from AirBnB_Clone import storage

class HBNBCommand(cmd.Cmd):
    """command processor for the AirBnb console"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        creates a new instance of BaseModel
        saves it to the json file and prints
        the id
        """
        
        if arg:
            try:
                cls = globals()[arg]
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        prints the string representation of an instance based
        on the class name and id
        """
        if arg:

            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            print(value)
                        else:
                            print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_destroy(self, arg):
        """
        deletes an instance based on name and id
        updates the changes to the JSON file
        """
        if arg:
            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    dict_cpy = {}
                    for key, value in file_data.items():
                        if key != name_id:
                            dict_cpy[key] = value 
                    else:
                        print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def emptyline(self):
        """console to execute nothing when you press enter without an argument"""
        pass

    def do_quit(self, line):
        """Exits the program"""
        exit(1)
    
    def do_EOF(self, line):
        """handles End of File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
