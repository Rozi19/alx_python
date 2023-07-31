class Square:
    """
    Represent square 
    Attributes:
        attr1 (str): It have size attribute
        """
    def __init__(self, size):
        """
        why size is private in __init__
        b/c it affect differnt propertyies
        Args:
            param1 (int): size of square
        """
        print(__import__("0-square_module").__doc__)
        self.__size = size 
