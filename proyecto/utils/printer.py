#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------

from utils.validation import Validation


class Printer:

    def __obtainCellInfo(aCell)->str:
        finalString=""
        if aCell != None:
            finalString = finalString+ f"position: ({aCell.getPosition().getCordI()},{aCell.getPosition().getCordJ()})\n"
            finalString = finalString+ f"number: {aCell.getNumber()}\n"
            finalString = finalString+ f"name: {aCell.getName()}\n"
            finalString = finalString+ f"color: {aCell.getColor()}\n"
            finalString = finalString+ f"agent here: {aCell.isAgentHere()}\n"
            if aCell.getNumber() == 2:
                finalString = finalString+ f"fireOn: {aCell.isFireOn()}\n"

        return finalString
    
    def __obtainNodeInfo(aNode)->str:
        finalString=""
        if aNode != None:
            finalString = finalString+ f"operator: {aNode.getOperator()}\n"
            finalString = finalString+ f"deep: {aNode.getDeep()}\n"
            finalString = finalString+ f"cost: {aNode.getCost()}\n"
        
        return finalString


    def __obtainBucketInfo(aBucket)->str:
        finalString=""
        if aBucket != None:
         finalString = finalString+f"capacity: {aBucket.getCapacity()}\n"
         finalString = finalString+ f"load: {aBucket.getLoad()}\n"
      
        return finalString
    
    def showBoardDetails(aList:list)->None:
        for row in aList:
           
            for cell in row:
                
               print(Printer.__obtainCellInfo(cell))
            print("\n")

    def showQueueDetails(aList)->None:
        print("-----Queue starting----")
        for node in aList:
            print("operator: ", node.getOperator()," deep: ",node.getDeep()," cost: ", node.getCost()," ")
        print("-----Queue finishing----")

    def showBoardNumbers(listOfList: list)->None:
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in listOfList]))

    def showCellInfo(aCell)-> None:
        print(Printer.__obtainCellInfo(aCell))

    def showMessage(message:str)-> None:
        print(message)
    
    def showBucketInfo(aBucket)-> None:
        print(Printer.__obtainBucketInfo(aBucket))
    
    def showNodeInfo(aNode)-> None:
        print(Printer.__obtainNodeInfo(aNode))