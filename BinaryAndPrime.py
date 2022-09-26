#IMPORTS
import random as rand
import time

#FUNCTIONS
def num2bina(num):
    #LIST TO BE ADDED TOO
    bina = []
    #CHANGING THIS CHANGES THE LENGTH 
    for x in range(8):
        #GOES THROUGH EACH POWER OF 2 FROM 7
        #THEN REMOVES THIS VALUE FROM THE NUM
        #IF REMAINDER, 1 IS APPENDED
        #IF NOT, 0 IS APPENDED
        if (num - 2**(7-x)) >= 0:
            bina.append("1")
            num -= 2**(7-x)
        else:
            bina.append("0")
    return bina

def prime(num):
    #CHECKS IF THE NUMBER IS ODD
    #EVEN NUMBERS CANNOT BE PRIME
    if not (((num) % 2) == 0):
        prime = True
        #NOW WE KNOW ITS ODD, IT DIVIDES EVERY NUMBER LESS
        #THAN HALF OF IT UNTIL ONE, IF ANY NUMBER BUT ONE
        #CAN BE DIVEDED INTO ITS AUTOMATICALLY NOT PRIME
        #AND ENDS THE LOOP AND SETS PRIME TO FALSE
        #IF IT GETS TO 1, IT IS PRIME
        for x in range(int(num // 2)):
            #VISUAL PROCESS
            #print(str(num % ((num // 2) - x)), end=" ")
            if (num % ((num // 2) - x)) == 0:
                if ((num // 2) - x) == 1:
                    break
                else:
                    prime = False
                    break
        if prime:
            return True
    return False
        
    
        
        
#MAIN




