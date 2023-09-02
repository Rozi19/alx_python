
""" parent class: BaseGeometry
    child class: Rectangle"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ the class inherite from rectangle """
    def __init__(self, size):
        """useing the rectangle methods"""
        Rectangle.__init__(self, size, size)
        self.__size = size
        self.integer_validator("size", self.__size)
        self.__str__()
        self.area()
