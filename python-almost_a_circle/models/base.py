""" class: base """


class Base:
    """ have private attribute nb_objects and have public instance attribute id """
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

