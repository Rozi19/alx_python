<h1>Python - Inheritance</h1>
<br><h2>0. Exact same object</h2>
<br>
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
<br>
Prototype: def is_same_class(obj, a_class):<br>
You are not allowed to import any module<br>
<br><h2>1. Same class or inherit from</h2>
<br>
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
<br>
Prototype: def is_kind_of_class(obj, a_class):<br>
You are not allowed to import any module<br>
<br><h2>2. Only sub class of</h2>
<br>
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
<br>
Prototype: def inherits_from(obj, a_class):<br>
You are not allowed to import any module<br>
<br><h2>3. Geometry module</h2>
<br>
Write an empty class BaseGeometry.
<br>
You are not allowed to import any module<br>
<br><h2>4. Improve Geometry</h2>
<br>
Write a class BaseGeometry (based on 3-base_geometry.py).
<br>
Public instance method: def area(self): that raises an Exception with the message area() is not implemented<br>
You are not allowed to import any module<br>
<br><h2>5. Integer validator</h2>
<br>
Write a class BaseGeometry (based on 4-base_geometry.py).
<br>
Public instance method: def area(self): that raises an Exception with the message area() is not implemented<br>
Public instance method: def integer_validator(self, name, value): that validates value:<br>
you can assume name is always a string<br>
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer<br>
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module<br>
