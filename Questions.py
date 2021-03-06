"""Game Who Knows - Module of the All Questions """
__author__ = "Carlos Andres Garcia Morales"

from random import randint, uniform,random


def QuestionsL1():
    q = randint(1, 10)
    if q == 1:
        print("WHO IS THE CREATOR OF PYTHON")
        print("1 - Guido Van Rossum\n2 - Bill Gates\n3 - Julien Barbier\n4 - Richard Stallman")
        a = 1
    elif q == 2:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> print("Easy Stuff")""")
        print("""1 - easy Stuff\n2 - "Easy Stuff"\n3 - Easy Stuff\n4 - 'Easy Stuff'""")
        a = 3
    elif q == 3:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> print("{:d} karlgarmor".format(32))""")
        print("""1 - 32 karlgarmor\n2 - karlgarmor 32\n3 - 32Karlgarmor\n4 - 32 Karlgarmor""")
        a = 1
    elif q == 4:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> print("{:d} is, {}".format(1, "int"))""")
        print("""1 - 1 is int\n2 - int is 1\n3 - 1 is, int\n4 - 1is,int""")
        a = 3
    elif q == 5:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[4])""")
        print("""1 - P\n2 - n\n3 - o\n4 - h""")
        a = 3
    elif q == 6:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[0:6])""")
        print("""1 - Python is cool\n2 - Python is\n3 - Pytho\n4 - Python""")
        a = 4
    elif q == 7:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[:6])""")
        print("""1 - Pytho\n2 - Python\n3 - Python is\n4 - is cool""")
        a = 2
    elif q == 8:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[7:])""")
        print("""1 - is cool\n2 - cool\n3 - Python is\n4 - Python i""")
        a = 1
    elif q == 9:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[7:-5])""")
        print("""1 - si\n2 - nohtyP\n3 - on\n4 - is""")
        a = 4 
    elif q == 10:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> a = "Python is cool"\n>>> print(a[-2])""")
        print("""1 - ol\n2 - si\n3 - o\n4 - l""")
        a = 3      
    else:
        print(q)

    return (q,a)


def QuestionsL2():
    q = randint(1, 10)
    if q == 1:
        print("WHAT STAND FOR PIP?")
        print("""1 - Python In Package\n2 - Package Installer for Python\n3 - Python Is Push\n4 - Package Inside Package""")
        a = 2
    elif q == 2:
        print("WHAT STAND FOR PEP?")
        print("""1 - Python Enhancement Proposal\n2 - Python Enter Package\n3 - Package Extra Python\n4 - Python Eight Path""")
        a = 1
    elif q == 3:
        print("WHAT IS THE CORRECT WAY TO COMMENT MULTIPLE LINES OF CODE")
        print("""1 - /* comment */\n2 - ### comment '''\n3 - --- comment ---\n4 - ''' comentario '''""")
        a = 4
    elif q == 4:
        print("HOW DO YOU DEFINE A VARIABLE BY ASSIGNING IT A VALUE?")
        print("""1 - number v = 0\n2 - var v = 0\n3 - int v = 0\n4 - v = 0""")
        a = 4
    elif q == 5:
        print("""WHAT DOES THIS COMMAND LINE PRINT? \n>>> print('%.2f' % 1714.666)""")
        print("""1 - 1714.67\n2 - 1714.0\n3 - 1714.66\n4 - 1715""")
        a = 1
    elif q == 6:
        print("WHICH OF THE FOLLOWING IS NOT A VALID ASSIGNMENT OPERATOR?")
        print("""1 - |=1\n2 - @=1\n3 - //=1\n4 - +=1""")
        a = 2
    elif q == 7:
        print("WHAT IS PYTHON?")
        print("""1 - A low-level, non-object-oriented compiled programming language\n2 - A machine language executed in a java virtual machine\n3 - A high-level object-oriented interpreted programming language\n4 - A programming language invented by the creator of Linux""")
        a = 3
    elif q == 8:
        print("HOW TO KNOW THE TYPE OF A CERTAIN VARIABLE?")
        print("""1 - TypeOf(1)\n2 - type(1)\n3 - is_a?\n4 - typeof 1""")
        a = 2
    elif q == 9:
        print("TRANSFORM A COMPATIBLE OBJECT INTO A CHARACTER STRING")
        print("""1 - str()\n2 - int()\n3 - char()\n4 - transform()""")
        a = 1 
    elif q == 10:
        print("THAT DATA TYPE IS NOT INTEGER")
        print("""1 - 0x18\n2 - 0b010011\n3 - 12.\n4 - 60""")
        a = 3      
    else:
        print(q)

    return (q,a)


def QuestionsL3():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT?\nif True:\n    print("Hello")\nelse:\n    print("World")""")
        print("""1 - Hello World\n2 - Hello\n3 - World\n4 - hello""")
        a = 2
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT?\nif 12 == 48/4:\n    print("Hello")\nelse:\n    print("World")""")
        print("""1 - Hello\n2 - 12\n3 - 48/4\n4 - World""")
        a = 1
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT?\nif 12 == 48/4 and False:\n    print("Hello")\nelse:\n    print("World")""")
        print("""1 - Hello\n2 - False\n3 - world\n4 - World""")
        a = 4
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT?\nif 12 == 48/3 or 12 is 12:\n    print("Hello")\nelse:\n    print("World")""")
        print("""1 - 48/3\n2 - 12\n3 - World\n4 - Hello""")
        a = 4
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT?\na = 12\nif a > 2:\n    if a % 2 == 0:\n        print("Bye")\n    else:\n        print("Hello")\nelse:\n    print("World")""")
        print("""1 - Bye\n2 - Hello\n3 - World\n4 - 12""")
        a = 1
    elif q == 6:
        print("""WHAT DO THESE LINES PRINT?\na = 12\nif a < 2:\n    print("Bye")\nelif a % 2 == 0:\n    print("Hello")\nelse:\n    print("World")""")
        print("""1 - Bye\n2 - Hello\n3 - World\n4 - 12""")
        a = 2
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT?\nfor i in range(4):\n    print(i, end=" ")""")
        print("""1 - 1 2 3 4\n2 - 1 2 3\n3 - 0 1 2 3\n4 - 0 1 2 3 4""")
        a = 3
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT?\nfor i in range(2, 4):\n    print(i, end=" ")""")
        print("""1 - 2 4\n2 - 2 3\n3 - 2 3 4\n4 - 3 4""")
        a = 2
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT?\nfor i in range(2, 10, 2):\n    print(i, end=" ")""")
        print("""1 - 2 4 6 8\n2 - 4 6 8 10 12 14 16 18\n3 - 2 3 4 5 6 7 8 9\n4 - 2 3 4 5 6 7 8 9 1 0""")
        a = 1 
    elif q == 10:
        print("TO ADD AN ALTERNATIVE CONDITION TO A CONDITIONAL IF STATEMENT USE")
        print("""1 - elsif\n2 - else if\n3 - elif\n4 - elseif""")
        a = 3      
    else:
        print(q)

    return (q,a)


def QuestionsL4():
    q = randint(1, 10)
    if q == 1:
        print("WHAT IS THE CORRECT WAY TO WRITE A WHILE LOOP?")
        print("""1 - while (a < 5)\n2 - while a foreach[0..4]\n3 - while a < 5:\n4 - while a in range(0..4)""")
        a = 3
    elif q == 2:
        print("WHAT IS THE CORRECT WAY TO WRITE A FOR LOOP?")
        print("""1 - for a in range(0, 3):\n2 - for(a in range[0..3])\n3 - for a in range(0..3)\n4 - for(a=0; a<3; a++)""")
        a = 1
    elif q == 3:
        print("A CONDITIONAL STATEMENT IS WRITTEN")
        print("""1 - if v == true:\n2 - if v == true then\n3 - if v == true\n4 - if (v == true)""")
        a = 1
    elif q == 4:
        print("TO SHOW THE VALUE OF POSITION 2 OF AN ARRAY CALLED 'micoleccion' WE USE")
        print("""1 - print(micoleccion[2])\n2 - printf(micoleccion[2])\n3 - print(micoleccion[1])\n4 - puts(micoleccion[2])""")
        a = 3
    elif q == 5:
        print("""WHICH OF THE FOLLOWING IS A DICTIONARY TYPE OBJECT?""")
        print("""1 - dicc = {'Num' -> 1, 'Name' -> 'Carlos'}\n2 - dicc = {'Num' => 1, 'Name' => 'Carlos'}\n3 - dicc = ('Num': 1, 'Name': 'Carlos')\n4 - dicc = {'Num': 1, 'Name': 'Carlos'}""")
        a = 1
    elif q == 6:
        print("WHAT IS A LIST IN PYTHON?")
        print("""1 - is a collection which is ordered and changeable. Allows duplicate members.\n2 - is a collection which is ordered and unchangeable. Allows duplicate members.\n3 - is a collection which is unordered and unindexed. No duplicate members.\n4 - is a collection which is unordered, changeable and indexed. No duplicate members.""")
        a = 1
    elif q == 7:
        print("WHAT IS A TUPLE IN PYTHON?")
        print("""1 - is a collection which is ordered and changeable. Allows duplicate members.\n2 - is a collection which is ordered and unchangeable. Allows duplicate members.\n3 - is a collection which is unordered and unindexed. No duplicate members.\n4 - is a collection which is unordered, changeable and indexed. No duplicate members.""")
        a = 2
    elif q == 8:
        print("WHAT IS A SET IN PYTHON?")
        print("""1 - is a collection which is ordered and changeable. Allows duplicate members.\n2 - is a collection which is ordered and unchangeable. Allows duplicate members.\n3 - is a collection which is unordered and unindexed. No duplicate members.\n4 - is a collection which is unordered, changeable and indexed. No duplicate members.""")
        a = 3
    elif q == 9:
        print("WHAT IS A DICTIONARY IN PYTHON?")
        print("""1 - is a collection which is ordered and changeable. Allows duplicate members.\n2 - is a collection which is ordered and unchangeable. Allows duplicate members.\n3 - is a collection which is unordered and unindexed. No duplicate members.\n4 - is a collection which is unordered, changeable and indexed. No duplicate members.""")
        a = 4 
    elif q == 10:
        print("WHAT IS A FROZENSET IN PYTHON?")
        print("""1 - is an inbuilt function is Python which takes an iterable object as input and makes them immutable.\n2 - is an inbuilt function is Python which takes an non-iterable object as input and makes them immutable.\n3 - is an inbuilt function is Python which takes an iterable object as input and makes them mutable.\n4 - None""")
        a = 1      
    else:
        print(q)

    return (q,a)



def QuestionsL5():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function():\n>>>     print("In my function")\n>>>\n>>> my_function()""")
        print("""1 - In my function\n2 - “In my function”\n3 - function my_function at …\n4 - Nothing""")
        a = 1
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function():\n>>>     print("In my function")\n>>>\n>>> my_function""")
        print("""1 - In my function\n2 - “In my function”\n3 - function my_function at …\n4 - Nothing""")
        a = 3
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function(counter):\n>>>     print("Counter: {}".format(counter))\n>>>\n>>> my_function(12)""")
        print("""1 - Counter: counter\n2 - Counter: c\n3 - Counter: 12\n4 - 12""")
        a = 3
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function(counter=89):\n>>>     print("Counter: {}".format(counter))\n>>>\n>>> my_function(12)""")
        print("""1 - Counter: 12\n2 - Counter: 89\n3 - Counter: 101\n4 - 89""")
        a = 1
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function(counter=89):\n>>>     print("Counter: {}".format(counter))\n>>>\n>>> my_function()""")
        print("""1 - Counter: 12\n2 - Counter: 89\n3 - Counter: 101\n4 - Nothing""")
        a = 2
    elif q == 6:
        print("""WHAT DO THESE LINES PRINT? \n>>> def my_function(counter=89):\n>>>     return counter + 1\n>>>\n>>> print(my_function())""")
        print("""1 - 1\n2 - 89\n3 - 891\n4 - 90""")
        a = 4
    elif q == 7:
        print("""ONE WAY TO ADD A BREAKPOINT WITHIN THE CODE IS?""")
        print("""import pdb; pdb.setBreakpoint()\n2 - import pdb; debugger\n3 - import pdb; pdb.set_trace()\n4 - import pdb; debug""")
        a = 2
    elif q == 8:
        print("""THE CORRECT WAY TO WRITE A FUNCTION IS?""")
        print("""1 - define nombrefuncion()\n2 - function nombrefuncion():\n3 - nombrefuncion: function()\n4 - def nombrefuncion():""")
        a = 4
    elif q == 9:
        print("""WHICH OF THESE STATEMENTS ABOUT FUNCTIONS IS NOT VALID""")
        print("""1 - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).\n2 - The first statement of a function can be an optional statement - the documentation string of the function or docstring.\n3 - A return statement with arguments is the same as return None.\n4 - The code block within every function starts with a colon (:) and is indented.""")
        a = 3 
    elif q == 10:
        print("""WHICH OF THESE STATEMENTS ABOUT THE ANONYMOUS FUNCTIONS IS NOT VALID?""")
        print("""1 - Are not declared in the standard manner by using the def keyword.\n2 - You can use the lambda keyword to create small anonymous functions.\n3 - They can contain commands or multiple expressions.\n4 - An anonymous function cannot be a direct call to print because lambda requires an expression""")
        a = 3      
    else:
        print(q)

    return (q,a)



def QuestionsL6():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a[0]""")
        print("""1 - 1\n2 - 2\n3 - [1]\n4 - [1, 2]""")
        a = 1
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a[-1]""")
        print("""1 - -1\n2 - 2\n3 - 4\n4 - [4, 3, 2, 1]""")
        a = 3
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a[-3]""")
        print("""1 - -3\n2 - [4, 3]\n3 - 2\n4 - [4, 3, 2, 1]""")
        a = 3
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> len(a)""")
        print("""1 - 2\n2 - 4\n3 - 6\n4 - 8""")
        a = 2
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a.append(5)\n>>> len(a)""")
        print("""1 - 2\n2 - 5\n3 - 6\n4 - 4""")
        a = 2
    elif q == 6:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a[1:3]""")
        print("""1 - [1, 2, 3]\n2 - [1, 2]\n3 - [2, 3]\n4 - 4""")
        a = 4
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> a[2] = 10\n>>> a""")
        print("""1 - [1, 2, 3, 4]\n2 - [1, 10, 3, 4]\n3 - [1, 2, 10, 4]\n4 - [1, 2, 10, 10]""")
        a = 3
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> b = a\n>>> b""")
        print("""1 - [1, 2, 3, 4]\n2 - [1, 10, 3, 4]\n3 - [1]\n4 - a""")
        a = 1
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> b = a\n>>> a[2] = 10\n>>> a""")
        print("""1 - [1]\n2 - [1, 2, 10, 4]\n3 - [1, 2, 3, 4]\n4 - a""")
        a = 2 
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = [1, 2, 3, 4]\n>>> b = a\n>>> a[2] = 10\n>>> b""")
        print("""1 - [1]\n2 - [1, 2, 10, 4]\n3 - [1, 2, 3, 4]\n4 - b""")
        a = 32     
    else:
        print(q)

    return (q,a)


def QuestionsL7():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John" }\n>>> a['id']""")
        print("""1 - id\n2 - a[‘id’]\n3 - 89\n4 - John""")
        a = 3
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John" }\n>>> a.get('id')""")
        print("""1 - ‘id’\n2 - a[‘id’]\n3 - id\n4 - 89""")
        a = 4
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John" }\n>>> a.get('age')""")
        print("""1 - ‘age’\n2 - Not found\n3 - 89\n4 - Nothing""")
        a = 4
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John" }\n>>> a.get('age', 0)""")
        print("""1 - ‘age’\n2 - Nothing\n3 - 0\n4 - 89""")
        a = 3
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }\n>>> a.get('projects')""")
        print("""1 - ‘projects’\n2 - [1, 2, 3, 4]\n3 - [1]\n4 - Nothing""")
        a = 2
    elif q == 6:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }\n>>> a.get('projects')[3]""")
        print("""1 - 4\n2 - [4]]\n3 - [1, 2, 3, 4]\n4 - 3""")
        a = 1
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT? \n>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }\n>>> a.get('friends')[-1].get("name")""")
        print("""1 - [ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]\n2 - ‘Amy’\n3 - ‘Bob’\n4 - 89""")
        a = 2
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT? \n>>> for i in range(0, 3):\n>>>     print(i, end=" ")""")
        print("""1 - 1 2 3\n2 - 0 1 2 3\n3 - 0 1 2\n4 - 1 2 3 4""")
        a = 3
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT? \n>>> for i in range(1, 4):\n>>>     print(i, end=" ")""")
        print("""1 - 1 2 3\n2 - 1 2 3 4\n3 - 0 1 2 3\n4 - 0 1 2 3 4""")
        a = 1 
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT? \n>>> for i in [1, 2, 3, 4]:\n>>>     print(i, end=" ")""")
        print("""1 - 0 1 2 3\n2 - 0 1 2 3 5\n3 - 1 2 3\n4 - 1 2 3 4""")
        a = 4      
    else:
        print(q)

    return (q,a)


def QuestionsL8():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT? \n>>> for i in [1, 3, 4, 2]:\n>>>     print(i, end=" ")""")
        print("""1 - 0 1 2 3\n2 - 1 2 3 4\n3 - 1 3 4 2\n4 - 1 3 4 2 0""")
        a = 3
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT? \n>>> for i in ["Hello", "Wold", "To", 98]:\n>>>     print(i, end=" ")""")
        print("""1 - 0 1 2 3\n2 - Hello World To 98\n3 - String String String Int\n4 - "Hello" "World" "To" 98""")
        a = 2
    elif q == 3:
        print("""IN THIS FOLLOWING CODE, WHAT IS User? \n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name""")
        print("""1 - A class\n2 - An attribute\n3 - A method\n4 - An instance""")
        a = 1
    elif q == 4:
        print("""IN THIS FOLLOWING CODE, WHAT IS id? \n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name""")
        print("""1 - A public instance attribute\n2 - A public class attribute\n3 - A public instance method\n4 - A protected class attribute""")
        a = 2
    elif q == 5:
        print("""IN THIS FOLLOWING CODE, WHAT IS __password? \n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name""")
        print("""1 - A public instance attribute\n2 - A protected class attribute\n3 - A private class attribute\n4 - A private instance attribute""")
        a = 3
    elif q == 6:
        print("""IN THIS FOLLOWING CODE, WHAT IS is_new? \n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name""")
        print("""1 - A public instance attribute\n2 - A protected class attribute\n3 - A protected instance attribute\n4 - A private instance attribute""")
        a = 1
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name\n\n u = User()\n u.is_new""")
        print("""1 - is_new\n2 - Nothing\n3 - False\n4 - True""")
        a = 4
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name\n\n u = User()\n u.id""")
        print("""1 - 89\n2 - id\n3 - User.id\n4 - Nothing""")
        a = 1
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name\n\n u = User("John")\n u.name""")
        print("""1 - name\n2 - None\n3 - ‘John’\n4 - ‘no name’""")
        a = 3 
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 89\n     name = "no name"\n     __password = None\n     __password = None\n\n     def __init__(self, new_name=None):\n         self.is_new = True\n         if new_name is not None:\n             self.name = new_name\n\n u = User()\n u.name""")
        print("""1 - name\n2 - None\n3 - ‘John’\n4 - ‘no name’""")
        a = 4      
    else:
        print(q)

    return (q,a)

def QuestionsL9():
    q = randint(1, 10)
    if q == 1:
        print("IS THIS A STANDARDIZED WAY TO COMMENT A FUNCTION IN PYTHON?")
        print("""1 - /* Addition function */\n2 - # Addition function\n3 - \""" Addition function \"""\n4 - Addition function""")
        a = 3
    elif q == 2:
        print("WHAT IS __init__?")
        print("""1 - A class attribute\n2 - A class method\n3 - The instance method called when a new object is created\n4 - The instance method called when a class is called for the first time""")
        a = 3
    elif q == 3:
        print("WHAT IS __str__?")
        print("""1 - Instance method that returns an “informal” and nicely printable string representation of an instance\n2 - Instance method that returns the dictionary representation of an instance\n3 - Instance method that prints an “informal” and nicely printable string representation of an instance\n4 - A class attribute""")
        a = 1
    elif q == 4:
        print("WHAT IS __repr__?")
        print("""1 - Instance method that prints an “official” string representation of an instance\n2 - Instance method that returns an “official” string representation of an instance\n3 - Instance method that returns the dictionary representation of an instance\n4 - A class attribute""")
        a = 2
    elif q == 5:
        print("WHAT IS __del__?")
        print("""1 - Instance method that removes the last character of an instance\n2 - Instance method that prints the memory address of an instance\n3 - Instance method called when an instance is deleted\n4 - A class attribute""")
        a = 3
    elif q == 6:
        print("WHAT IS __doc__?")
        print("""1 - The string documentation of an object (based on docstring)\n2 - Prints the documentation of an object\n3 - Creates man file\n4 - A class attribute""")
        a = 2
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n print(User.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 2
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n u = User()\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 2
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n u = User()\n u.id = 89\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 3
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n User.id = 98\n u = User()\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 4      
    else:
        print(q)

    return (q,a)


def QuestionsL10():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n u = User()\n User.id = 98\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 4
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n User.id = 98\n u = User()\n u.id = 89\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 3
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n User.id = 98\n u = User()\n u.id = 89\n print(User.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 4
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n u = User()\n u.id = 89\n User.id = 98\n print(User.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 4
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT?\n class User:\n     id = 1\n\n u = User()\n u.id = 89\n User.id = 98\n print(u.id)""")
        print("""1 - None\n2 - 1\n3 - 89\n4 - 98""")
        a = 3
    elif q == 6:
        print("""IN THE FOLLOWING CODE, DO a AND b POINT TO THE SAME OBJECT? ANSWER WITH YES OR NO\n>>> a = 89\n>>> b = a + 1""")
        print("""1 - Yes\n2 - No""")
        a = 2
    elif q == 7:
        print("WHAT IS THE FUNCTION TO GET THE VARIABLE IDENTIFIER (WHICH IS THE MEMORY ADDRESS IN THE CPYTHON IMPLEMENTATION)?")
        print("""1 - type\n2 - mem\n3 - id\n4 - store""")
        a = 3
    elif q == 8:
        print("""IN THE FOLLOWING CODE, DO a AND b POINT TO THE SAME OBJECT? ANSWER WITH YES OR NO\n>>> a = 89\n>>> b = 100""")
        print("""1 - Yes\n2 - No""")
        a = 2
    elif q == 9:
        print("""IN THE FOLLOWING CODE, DO a AND b POINT TO THE SAME OBJECT? ANSWER WITH YES OR NO\n>>> a = 89\n>>> b = 89""")
        print("""1 - Yes\n2 - No""")
        a = 1 
    elif q == 10:
        print("""IN THE FOLLOWING CODE, DO a AND b POINT TO THE SAME OBJECT? ANSWER WITH YES OR NO\n>>> a = 89\n>>> b = a""")
        print("""1 - Yes\n2 - No""")
        a = 1      
    else:
        print(q)

    return (q,a)


def QuestionsL11():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT?\n>>> s1 = "Python"\n>>> s2 = s1\n>>> print(s1 == s2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT?\n>>> s1 = "Python"\n>>> s2 = s1\n>>> print(s1 is s2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT?\n>>> s1 = "Python"\n>>> s2 = "Python"\n>>> print(s1 == s2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 4:
        print("""WHAT DO THESE LINES PRINT?\n>>> s1 = "Python"\n>>> s2 = "Python"\n>>> print(s1 is s2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 5:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = [1, 2, 3]\n>>> print(l1 == l2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 6:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = [1, 2, 3]\n>>> print(l1 is l2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 4
    elif q == 7:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = l1\n>>> print(l1 == l2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = l1\n>>> print(l1 is l2)""")
        print("""1 - None\n2 - Python\n3 - True\n4 - False""")
        a = 3
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = l1\n>>> l1.append(4)\n >>> print(l2)""")
        print("""1 - [1, 2, 3, 4]\n2 - [1, 2, 3]\n3 - [0, 1, 2, 3]\n4 - None""")
        a = 1 
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT?\n>>> l1 = [1, 2, 3]\n>>> l2 = l1\n>>> l1 = l1 + [4]\n>>> print(l2)""")
        print("""1 - [1, 2, 3, 4]\n2 - [1, 2, 3]\n3 - [0, 1, 2, 3]\n4 - [4, 4, 4, 4]""")
        a = 2      
    else:
        print(q)

    return (q,a)

def QuestionsL12():
    q = randint(1, 10)
    if q == 1:
        print("""WHAT DO THESE LINES PRINT?\n def increment(n):\n     n += 1\n\n a = 1\n increment(a)\n print(a)""")
        print("""1 - n\n2 - 3\n3 - 1\n4 - 0""")
        a = 3
    elif q == 2:
        print("""WHAT DO THESE LINES PRINT?\n def increment(n):\n     n.append(4)\n\n l = [1, 2, 3]\n increment(l)\n print(l)""")
        print("""1 - [1, 2, 3, 4]\n2 - [1, 2, 3]\n3 - [0, 1, 2, 3]\n4 - [4]""")
        a = 1
    elif q == 3:
        print("""WHAT DO THESE LINES PRINT?\n def assign_value(n, v):\n     n = v\n\n l1 = [1, 2, 3]\n l2 = [4, 5, 6]\n assign_value(l1, l2)\n print(l1)""")
        print("""1 - [1, 2, 3, 4]\n2 - [0, 1, 2]\n3 - [1, 2, 3]\n4 - [4, 3, 2, 1]""")
        a = 3
    elif q == 4:
        print("""Tuple or not?\n>>> a = ()""")
        print("""1 - Yes\n2 - No""")
        a = 1
    elif q == 5:
        print("""Tuple or not?\n>>> a = (1, 2)""")
        print("""1 - Yes\n2 - No""")
        a = 1
    elif q == 6:
        print("""Tuple or not?\n>>> a = (1)""")
        print("""1 - Yes\n2 - No""")
        a = 2
    elif q == 7:
        print("""Tuple or not?\n>>> a = (1, )""")
        print("""1 - Yes\n2 - No""")
        a = 1
    elif q == 8:
        print("""WHAT DO THESE LINES PRINT?\n>>> a = (1)\n>>> b = (1)\n>>> a is b""")
        print("""1 - No\n2 - Yes\n3 - True\n4 - False""")
        a = 3
    elif q == 9:
        print("""WHAT DO THESE LINES PRINT?\n>>> a = (1, 2)\n>>> b = (1, 2)\n>>> a is b""")
        print("""1 - No\n2 - Yes\n3 - True\n4 - False""")
        a = 4 
    elif q == 10:
        print("""WHAT DO THESE LINES PRINT?\n>>> a = ()\n>>> b = ()\n>>> a is b""")
        print("""1 - No\n2 - Yes\n3 - True\n4 - False""")
        a = 3      
    else:
        print(q)

    return (q,a)