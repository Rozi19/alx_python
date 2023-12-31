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
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
    @property
    def width(self):
        """ getter width """ 
        return self.__width
    @width.setter
    def width(self, width):
        """ setter x """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        """ getter height """
        return self.__height
    @height.setter
    def height(self, height):
        """ setter x """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
    @property
    def x(self):
        """ getter x """
        return self.__x
    @x.setter
    def x(self, x):
        """ setter x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    @property
    def y(self):
        """ getter y """
        return self.__y
    @y.setter
    def y(self, y):
        """ setter y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    
    def area(self):
        """ retrun the value of area """
        return self.__width * self.__height

    def display(self):
        """ display # column width row height new line y space x"""
        for y in range(self.__y):
            print()
        for x in range(self.__height):
            for x in range(self.__x):
                print(" ", end = "")
            for y in range(self.__width):
                print("#", end = "")
            print()

    def update(self, *args, **kwargs):
        """ update the value of Rectangle by accept different value
            if its have only value use *args and if we have a key word and value use **kwargs """
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
    def __str__(self):
        """ object representation in a string format """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))