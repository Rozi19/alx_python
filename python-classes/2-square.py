""" we have simple class
    class: square """


class Square:
    """ here we have a constructor call squre
    attribute: size
    """
    def  __init__(self, size=0):
        """ using size attribute  check if size is integer or not and if size is negative or not"""
        self.size = size
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    def area(self):
        return int(self.__size) * int(self.__size)
