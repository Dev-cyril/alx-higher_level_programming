#!/usr/bin/python3

"""This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
"""


import json
import turtle


class Base:
    """ A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of a list of dictionary"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation into a file"""
        filename = cls.__name__ + '.json'
        text = []
        if list_objs is not None:
            for i in list_objs:
                text.append(i.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json objects"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance from dictionary"""
        if cls.__name__ == 'Rectangle':
            new = cls(3, 4)
        elif cls.__name__ == 'Square':
            new = cls(2, 2)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads data from a json file and
            return the instances of the objects
        """
        filename = cls.__name__ + '.json'
        content_data = []
        with open(filename, 'r') as f:
            content = f.read()
            data = cls.from_json_string(content)
            for i in data:
                content_data.append(cls.create(**i))
        return content_data

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        filename = cls.__name__ + '.csv'
        text = []
        if list_objs is not None:
            for i in list_objs:
                text.append(i.to_dictionary())
        with open(filename, 'w', encoding='utf-8') as f:
            return (f.write(Base.to_json_string(text)))

    @classmethod
    def load_from_file_csv(cls):
        """loads data from a csv file"""
        filename = cls.__name__ + '.csv'
        content_data = []
        with open(filename, 'r') as f:
            content = f.read()
            data = cls.from_json_string(content)
            for i in data:
                content_data.append(cls.create(**i))
        return content_data

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw the figure
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
