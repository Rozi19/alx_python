""" we have simple class
    class: square
    """

class Square:
    """ here we have a constructor call squre
    attribute: size
    """
    def __init__(self, size=0):
        """ puting size as private """
        self.__size = size
        @property
        def size(self):
            """ it is a getter to acces a class private attribute 
            @property is bulit in decorection it help to modify the attribute
            return modify value """
            return self.__size
        @size.setter
        def size(self, value):
            """ It is a setter to set the property of the value 
            checking if the value is digit or not and if the value is negaative number or not"""
            if value.isdigit():
                self.__size = value
            else:
                raise TypeError("size must be an integer")
            if value > 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
