class Square:
    """ simple square class """
    def __init__(self, size):
        """ the squre size is private.The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute."""
        self.__size = size 
