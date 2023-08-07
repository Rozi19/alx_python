""" import Base from base 
    class: rectangle inherit from Base class"""


from base import Base
class Rectangle(Base):
    """ attribute width height x and y id from Base class """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self):
        return self.__height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self):
        return self.__y