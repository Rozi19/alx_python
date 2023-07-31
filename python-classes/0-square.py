class Square:
    def __init__(self, size):
        """ why size is private in __init__
        b/c it affect differnt propertyies
        Args:
            param1 (int): size of square
        """
        self.__size = size 
