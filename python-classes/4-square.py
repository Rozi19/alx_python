""" we have simple class
    class: square """


class Square:
    """ here we have a constructor call squre
    attribute: size
    """
    def  __init__(self, size=0):
        """ using size attribute  """
        self.size = size
        
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
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    def area(self):
        """ Return the area of the square """
        return int(self.__size) * int(self.__size)
    def my_print(self):
        """ if size == 0 it print new line else it print # equale to size the row and the column """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end = '')
                print()
