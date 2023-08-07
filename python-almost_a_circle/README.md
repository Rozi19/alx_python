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
<br>This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)