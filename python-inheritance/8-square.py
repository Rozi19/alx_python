
""" parent class: BaseGeometry
    child class: Rectangle"""

Rectangle = __import__('7-rectangle').Rectangle
class BaseGeometry(type):
    """ every thing in python is an object soo the class is also an object.
    so if it is an object it have type.type is a metaclass, of which classes
    are instances. Just as an ordinary object is an instance of a class,
    any new-style class in Python, and thus any class in Python 3,
    is an instance of the type metaclass """
    def __dir__(cls):
        """ remove the init subclass"""
        attributes = super().__dir__()
        list_to_return = []
        for att in attributes:
            if att != "__init_subclass__":
                list_to_return.append(att)
        return list_to_return


class BaseGeometry(metaclass=BaseGeometry):

    """ Metaclasses allow for code to manipulate classes.
    Often this change happens when an object of the class is instantiated
    """

    def __dir__(cls):
        """ remove the init subclass"""
        attributes = super().__dir__()
        list_to_return = []
        for att in attributes:
            if att != "__init_subclass__":
                list_to_return.append(att)
        return list_to_return

    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value
        if isinstance(value, int):
            self.__value = value
        else:
            raise TypeError("{} must be an integer".format(self.__name))
        if value > 0:
            self.__value = value
        else:
            raise ValueError("{} must be greater than 0".format(self.__name))


class Rectangle(BaseGeometry):
    """" the class inherit from BaseGeometry"""
    def __init__(self, width, height):
        """" validet width and height from parent class """
        self.__width = width
        self.__height = height

    def area(self):
        """" return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ returns the object representation in a string format """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ the class inherite from rectangle """
    def __init__(self, size):
        """useing the rectangle methods"""
        Rectangle.__init__(self, size, size)
        self.__size = size
        self.integer_validator("size", self.__size)
        self.__str__()
        self.area()
