<h1>Python - Classes and Objects</h1>
This iis my first python OOP project
<br>
<h2>0. Square with size</h2>
<br>
Write a class Square that defines a square by:
<br>
Private instance attribute: size<br>
Instantiation with size (no type/value verification)<br>
You are not allowed to import any module<br>
<h2>1. Size validation</h2>
<br>
Write a class Square that defines a square by: (based on 0-square.py)
<br>
Private instance attribute: size<br>
Instantiation with optional size: def __init__(self, size=0):<br>
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
You are not allowed to import any module<br>
<h2>2. Area of a square</h2>
<br>
Write a class Square that defines a square by: (based on 1-square.py)
<br>
Private instance attribute: size<br>
Instantiation with optional size: def __init__(self, size=0):<br>
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
Public instance method: def area(self): that returns the current square area<br>
You are not allowed to import any module<br>
<h2>3. Access and update private attribute</h2>
<br>
Write a class Square that defines a square by: (based on 2-square.py)
<br>
Private instance attribute: size:<br>
property def size(self): to retrieve it<br>
property setter def size(self, value): to set it:<br>
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
Instantiation with optional size: def __init__(self, size=0):<br>
Public instance method: def area(self): that returns the current square area<br>
You are not allowed to import any module<br>
<strong>Why?</strong>
<br>
Why a getter and setter?
<br>
Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.<br>
<h2>4. Printing a square</h2>
<br>
Write a class Square that defines a square by: (based on 3-square.py)
<br>
Private instance attribute: size:<br>
property def size(self): to retrieve it<br>
property setter def size(self, value): to set it:<br>
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer<br>
if size is less than 0, raise a ValueError exception with the message size must be >= 0<br>
Instantiation with optional size: def __init__(self, size=0):<br>
Public instance method: def area(self): that returns the current square area<br>
Public instance method: def my_print(self): that prints in stdout the square with the character <strong>#</strong>:<br>
if size is equal to 0, print an empty line<br>
You are not allowed to import any module<br>
