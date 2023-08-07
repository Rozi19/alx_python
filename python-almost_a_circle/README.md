<h1>Python - Almost a circle</h1>
<h2> 0. Base class </h2>
<br>
Write the first class Base:
<br>
Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
<br>
Create a file named models/base.py:
<br>
Class Base:
<br>private class attribute __nb_objects = 0
<br>class constructor: def __init__(self, id=None)::
<br>if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
<br>otherwise, increment __nb_objects and assign the new value to the public instance attribute id
<br>This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)<br>
<h2>1. First Rectangle</h2>
<br>
Write the class Rectangle that inherits from Base:
<br>
In the file models/rectangle.py
<br>Class Rectangle inherits from Base
<br>Private instance attributes, each with its own public getter and setter:
<br>__width -> width
<br>__height -> height
<br>__x -> x
<br>__y -> y
<br>Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
<br>Call the super class with id - this super call with use the logic of the __init__ of the Base class
<br>Assign each argument width, height, x and y to the right attribute
<br>Why private attributes with getter/setter? Why not directly public attribute?
<br>
Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.<br>
<h2>2. Validate attributes</h2>
<br>
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
<br>
If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer<br>
If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0<br>
If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0<br>
<h2>3. Area first</h2>
<br>
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.<br>











