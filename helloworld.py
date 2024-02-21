import random

answers = ("lower", "greater", "yes")

def startGame():
    isFinished = False
    random_number = random.randrange(1, 100)
    print(random_number)
    while not isFinished:

        userAnswer = int(input("Insert number from 1 to 100"))

        if random_number == userAnswer:
            print(answers[2])
            isFinished = True
        elif userAnswer < random_number:
            print(answers[1])
        elif userAnswer > random_number:
            print(answers[0])
        else:
            print("Error")
            isFinished = True

startGame()


