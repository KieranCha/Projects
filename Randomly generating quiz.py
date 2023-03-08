#IMPORTS
import random as r
import os

#FUNCTIONS
def questionGen(number):
    for x in range(number):
        #Randomises everything
        number1 = r.randint(0,100)
        number2 = r.randint(0,100)
        operator = r.choice(list(operatorsfunc.keys()))
        #Contrusts the question and adds it to the questions dictionary
        questions[str(number1) + operator + str(number2)] = operatorsfunc[operator](number1, number2)

#MAIN

operatorsfunc = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "/": lambda a,b: a / b,
    "*": lambda a,b: a * b
    } # This dictionary has the operators as keys and lambda functions as their mathmatical functions
      # this way we can call a random selection of the keys and and get the lambda the same way
      # allowing for random selection of operators

questions = {
    }

questNum = int(input("Number of questions: "))
os.system("CLS")

questionGen(questNum)
correct = 0
for x in range(questNum):
    question = list(questions.keys())[x]
    #Picks a random letter to be correct
    ansletter = r.choice(["a","b","c"])
    
    print("Question " + str(x + 1) + "\n" + question + "= ?\n")
    #Here when printing out the options it checks if the letter is the correct one, if so, it prints the answer as it
    #however, if not it prints the answer within a int range of 50
    print("A)" + str(questions[question]) if ansletter == "a" else "A)" + str(questions[question] + r.randint(-50,50)))
    print("B)" + str(questions[question]) if ansletter == "b" else "B)" + str(questions[question] + r.randint(-50,50)))
    print("C)" + str(questions[question]) if ansletter == "c" else "C)" + str(questions[question] + r.randint(-50,50)))
    ans = input("Choice: ")
    if ans.lower() == ansletter:
        input("Correct")
        correct += 1
    else:
        input("Wrong...")
    #Checks if user gets it correct and increases score if so
    os.system("CLS") #Clears the UI to make it cleaner

# Positive reinforcement only if they get higher than 60%
if correct >= (questNum * 0.6):
    print(str(correct) + " correct, well done!")
    for x in range(5):
        # Im not gonna lie i dont know why it does this
        print("Well done")
else:
    print(str(correct) + " correct try harder...")
input() # Keeps UI open until user presses enter

    
