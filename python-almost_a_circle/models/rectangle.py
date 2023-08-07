""" import Base from base 
    class: rectangle inherit from Base class"""


from models.base import Base
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
        """ getter width """ 
        return self.__width
    @width.setter
    def width(self, width):
        """ setter x """
        self.__width = width
    @property
    def height(self):
        """ getter height """
        return self.__height
    @height.setter
    def height(self, height):
        """ setter x """
        self.__height = height
    @property
    def x(self):
        """ getter x """
        return self.__x
    @x.setter
    def x(self, x):
        """ setter x """
        self.__x = x
    @property
    def y(self):
        """ getter y """
        return self.__y
    @y.setter
    def y(self, y):
        """ setter y """
        self.__y = y