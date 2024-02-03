#math multipluication game
import random
import math

questionNumber = int(input("How many questions would you like? "))
no_1 = random.randint(1,10)
no_2 = random.randint(1,10)

def main():

    random.seed()
    count = 0
    while count < questionNumber:
        question = int(input("What is ", str(no_1), "x", str(no_2), "? "))
        answer = str(no_1*no_2)
        correct = answer == question

        if correct:
            print("Bingo!")
        else:
            print("Sorry the answer is ", answer, ".")


main()
