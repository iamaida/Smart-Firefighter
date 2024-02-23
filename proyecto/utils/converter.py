#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------

class Converter:

    #Remove all the ocurrences of a character (char) in each item of the list
    def removeCharacterInEachRow(aList:list ,char:str) -> None:
        i = 0
        for row in aList:
            new_string = aList[i].replace(char,'')
            aList[i] = new_string
            i+= 1
    
    #Conver each item of the list in a list of integers
    def transEachRowInListOfIntegers(aList:list) -> None:

        i = 0
        for row in aList:
            listOfStrings = aList[i].split()
            listOfIntegers = list(map(int,listOfStrings))
            aList[i] = listOfIntegers
            i += 1
    