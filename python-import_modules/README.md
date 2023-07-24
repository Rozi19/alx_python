<h1><strong>Python - import & modules</strong></h1>
<h1>0. Import a simple function from a simple file</h1>
<br>
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
<br>
You have to use print function with string format to display integers<br>
You have to assign:<br>
the value 1 to a variable called a<br>
the value 2 to a variable called b<br>
and use those two variables as arguments when calling the functions add and print<br>
a and b must be defined in 2 different lines: a = 1 and another b = 2<br>
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
You can only use the word add_0 once in your code<br>
You are not allowed to use * for importing or __import__<br>
Your code should not be executed when imported - by using __import__, like the example below
<br>
<h1>1. How to make a script dynamic!</h1>
<br>
Write a program that prints the number of and the list of its arguments.
<br>
The output should be:<br>
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by<br>
a new line, followed by (if at least one argument),
one line per argument:<br>
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported<br>
The number of elements of argv can be retrieved by using: len(argv)<br>
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.<br>
<h1>2. Everything can be imported</h1><br>
Write a program that imports the variable a from the file variable_load_2.py and prints its value.
<br>
You are not allowed to use * for importing or __import__<br>
Your code should not be executed when imported<br>
<h1>3. Integers division with debug</h1>
<br>
Write a function that divides 2 integers and prints the result.
<br>
Prototype: def safe_print_division(a, b):<br>
You can assume that a and b are integers<br>
The result of the division should print on the finally: section preceded by Inside result:<br>
Returns the value of the division, otherwise: None<br>
You have to use try: / except: / finally:<br>
You have to use "{}".format() to print the result<br>
You are not allowed to import any module<br>
