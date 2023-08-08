""" import Rectangle class from rectangle 
    class squre inherite from Rectangle """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ attribute size which is rectangle width an height """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x =  x
        self.__y = y
    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter """
        self.width = value
        self.height = value
        
    def __str__(self):
        """object(square) representation in a string format"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size))