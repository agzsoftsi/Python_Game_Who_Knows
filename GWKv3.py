""" Game Who Knows - Module of the All Game """
__author__ = "Carlos Andres Garcia Morales"


from Questions import QuestionsL1
from Answers import Answers

print("WHO KNOWS")
print("CHALLENGE QUESTIONS ABOUT PYTHON BASIC")
print("LEVEL: DUMMIES")

print("ONLY TYPE THE NUMBER OF THE ANSWER")

score = 0
score_g = 0
# print("PLEASE ENTER YOUR NAME: ", end = "")
# name = str(input())

if __name__ == '__main__':

    for i in range(1, 11):
        print("----------------------------------------QUESTION {:d} ------------------------------------------".format(i))
        q1 = QuestionsL1()
        print("ENTER YOUR ANSWER: ", end="")
        r = Answers(input())
        print("es {}".format(r))
       
        if q1[0] == 1 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 2 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 3 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 4 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 5 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 6 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 7 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 8 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 9 and q1[1] == r:
            print("GOOD ANSWER")
        elif q1[0] == 10 and q1[1] == r:
            print("GOOD ANSWER")
        else:
            print("WRONG ANSWER")
            score_g = 1

        if score_g == 0:
            score += 10

    
    print("Your Score:  {:d}".format(score))
