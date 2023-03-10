#!/usr/bin/python3
"""
The base model/class used for other shapes
"""
import json


class Base:
    """
    A class that defines the basis of shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Sets the id of an instance of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the given JSON string (given by to_json_string)
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            j_string = cls.to_json_string(dict_list)
            f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            json_string = []
            return json_string

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instance with all attributes already set
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                j_string = f.read()
                dict_list = cls.from_json_string(j_string)
                instance_list = []
                for dictionary in dict_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []
