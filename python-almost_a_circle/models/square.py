""" import Rectangle class from rectangle 
    class squre inherite from Rectangle """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ attribute size which is rectangle width an height """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """size setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value

        
    def __str__(self):
        """object(square) representation in a string format"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))