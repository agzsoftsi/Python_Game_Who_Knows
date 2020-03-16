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



def QuestionsL5():
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



def QuestionsL6():
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


def QuestionsL7():
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


def QuestionsL8():
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

def QuestionsL9():
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


def QuestionsL10():
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