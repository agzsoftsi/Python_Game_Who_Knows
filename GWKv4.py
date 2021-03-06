""" Game Who Knows - Module of the All Game """
__author__ = "Carlos Andres Garcia Morales"

from colorama import init
from colorama import Fore, Back, Style
from Questions import *
from Answers import Answers

print(Fore.WHITE + "WHO KNOWS")
print("CHALLENGE QUESTIONS ABOUT PYTHON BASIC")
print("LEVEL: DUMMIES")
print("Author : {} ".format(__author__))

print("ONLY TYPE THE NUMBER OF THE ANSWER")

score = 0
score_g = 0
# print("PLEASE ENTER YOUR NAME: ", end = "")
# name = str(input())

if __name__ == '__main__':

    for i in range(1, 13):
        print(Fore.YELLOW + "----------------------------------------QUESTION {:d} ------------------------------------------".format(i))
        print(Style.RESET_ALL)
        if i == 1:
            q1 = QuestionsL1()
        elif i == 2:
            q1 = QuestionsL2()
        elif i == 3:
            q1 = QuestionsL3()
        elif i == 4:
            q1 = QuestionsL4()
        elif i == 5:
            q1 = QuestionsL5()
        elif i == 6:
            q1 = QuestionsL6()
        elif i == 7:
            q1 = QuestionsL7()
        elif i == 8:
            q1 = QuestionsL8()
        elif i == 9:
            q1 = QuestionsL9()
        elif i == 10:
            q1 = QuestionsL10()
        elif i == 11:
            q1 = QuestionsL11()
        elif i == 12:
            q1 = QuestionsL12()

        print()    
        print("ENTER YOUR ANSWER: ", end="")
        r = Answers(input())
        score_g = 0

        if q1[0] == 1 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 2 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 3 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 4 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 5 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 6 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 7 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 8 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 9 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 10 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 11 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        elif q1[0] == 12 and q1[1] == r:
            print(Fore.GREEN + "GOOD ANSWER")
        else:
            print(Fore.RED + "WRONG ANSWER")
            score_g = 1

        if score_g == 0:
            score += 10

    print(Fore.YELLOW + """----------------------------------------------------------------------------------------------""")
    print(Fore.YELLOW + "                                        Your Score:  {:d}".format(score))
    print(Style.RESET_ALL)
    
