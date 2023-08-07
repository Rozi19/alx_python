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

    def get_width(self):
        """ getter width """ 
        return self.__width
    
    def set_width(self, width):
        """ setter x """
        self.__width = width
   
    def get_height(self):
        """ getter height """
        return self.__height

    def set_height(self, height):
        """ setter x """
        self.__height = height
  
    def get_x(self):
        """ getter x """
        return self.__x
    
    def set_x(self, x):
        """ setter x """
        self.__x = x
    
    def get_y(self):
        """ getter y """
        return self.__y
   
    def set_y(self, y):
        """ setter y """
        self.__y = y