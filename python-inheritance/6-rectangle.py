""" parent class: BaseGeometry
    child class: Rectangle"""


from 5-base_geometry import BaseGeometry
class Rectangle(BaseGeometry):
    """" the class inherit from BaseGeometry"""
    def __init__(self, width, height):
        """" validet width and height from parent class """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
