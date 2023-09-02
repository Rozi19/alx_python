""" parent class: BaseGeometry
    child class: Rectangle"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ the class inherite from rectangle """
    def __init__(self, size):
        """use the rectangle methods"""
        super().__init__(size, size)
        self.size = size
        self.integer_validator("size", self.size)
        self.__str__()
        self.area()