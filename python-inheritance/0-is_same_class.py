""" checking object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """ if they are same return true else false"""
    if obj.__class__ == a_class:
        return True
    else:
        return False
