"""Game Who Knows - Module of the All Questions """
__author__ = "Carlos Andres Garcia Morales"

from random import randint, uniform,random
def Questions():
    q = randint(1, 5)
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
    else:
        print(q)
