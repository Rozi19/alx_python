
""" parent class: BaseGeometry
    child class: Rectangle"""


class BaseGeometry:
    """ creating an empty class """
    def __init__(self):
        """ using pass"""
        pass
    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value
        if isinstance(value, int):
            if value > 0:
                self.__value = value
            else:
                raise ValueError("{} must be greater than 0".format(self.__name))
        else:
            raise TypeError("{} must be an integer".format(self.__name))
class Rectangle(BaseGeometry):
    """" the class inherit from BaseGeometry"""
    def __init__(self, width, height):
        """" validet width and height from parent class """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
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
    
