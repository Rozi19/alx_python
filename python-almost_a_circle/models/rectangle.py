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
        return self.__width
    
    def set_width(self):
        return self.__width
   
    def get_height(self):
        return self.__height

    def set_height(self):
        return self.__height
  
    def get_x(self):
        return self.__x
    
    def set_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
   
    def set_y(self):
        return self.__y