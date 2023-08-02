""" class: BaseGeometry """


class BaseGeometry:
    """ creating an empty class """
    def __init__(self):
        """ using pass"""
        pass
    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validate the value if it is an intereger or not
        and if it's negative or not """
        self.__name = name
        self.__value = value
        if isinstance(value, int):
            if value > 0:
                self.__value = value
            else:
                raise ValueError("{} must be greater than 0".format(self.__name))
        else:
            raise TypeError("{} must be an integer".format(self.__name))
