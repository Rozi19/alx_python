""" class: BaseGeometry """


class BaseGeometry:
    """ creating an empty class """
    def __init__(self):
        """ using pass"""
        pass
    def __dir__(cls):
        """ remove __init_subclass"""
        attributes = super().__dir__()
        list_to_return = []
        for att in attributes:
            if att != "__init_subclass__":
                list_to_return.append(att)
        return list_to_return
    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")
