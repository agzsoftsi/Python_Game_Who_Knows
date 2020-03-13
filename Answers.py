"""Game Who Knows - Module of the All Answers """
__author__ = "Carlos Andres Garcia Morales"

from random import randint, uniform,random
def Answers(r):
    try:
        r = int(r)
        return r
    except ValueError:
        r = 0
        return r


