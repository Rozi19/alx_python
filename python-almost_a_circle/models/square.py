""" import Rectangle class from rectangle 
    class squre inherite from Rectangle """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ attribute size which is rectangle width an height """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x =  x
        self.y = y
        
    def __str__(self):
        """object(square) representation in a string format"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))