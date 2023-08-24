#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON file
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            # print("KEY: {}\nVALUE: {}".format(key, value))
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)
            # print("OBJECT SERIALIZED TO JSON FILE")

    def get(self, cls, id):
        """returns the object based on the class and ID
            or None if not found
        """
        key = "{}.{}".format(cls.__name__, id)
        try:
            obj = self.__objects[key]
        except:
            obj = None
        return obj

    def count(self, cls=None):
        """returns the number of objects in storage
            matching the given class. If no class is passed
            returns the count of all objects in storage
        """
        obj_count = 0
        if cls:
            for key, value in self.__objects.items():
                if type(value) == cls:
                    obj_count += 1
        else:
            for item in self.__objects:
                obj_count += 1

        return obj_count

    def reload(self):
        """deserialize JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload() method for deserializing JSON file to obj
        """
        self.reload()
