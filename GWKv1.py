"""Game Who Knows - Module of the All Game """
__author__ = "Carlos Andres Garcia Morales"
print("WHO KNOWS")
print("CHALLENGE QUESTIONS ABOUT PYTHON BASIC")
print("LEVEL: DUMMIE")

print("ONLY TYPE THE NUMBER OF THE ANSWER")

score = 0
print("PLEASE ENTER YOUR NAME: ", end = "")
name = str(input())


from Questions import Questions
if __name__ == '__main__':
    print("----------------------------------------QUESTION 1-------------------------------------------")
    Questions()
    r = Questions()
    print(r)

