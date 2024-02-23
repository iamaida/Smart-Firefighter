#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------

from position import Position
from board import Board
from bucket import Bucket
from cell import Cell
from utils.selector import Selector
from utils.printer import Printer

class Agent:

    isBucketTake = False
    #Constructor
    def __init__(self, name:str):
        # Instance attribute
        self.bucket = Bucket(properties={"capacity":0,"load":0})
        self.name = name
        self.position = Position(-1,-1)
        

    
    def __findPosition(self, board:Board) -> None:
        
        for row in board:
            for cell in row:
                
                if cell.isAgentHere() == True:
                    self.position = cell.getPosition()
                    break
        
    
    def getPosition(self, board:Board)->Position:
        self.__findPosition(board)
        return self.position
    
    def getName(self) -> str:
        return self.name

    def getBucket(self) -> list:
        return self.bucket
    
    def takeBucket(self, cell:Cell) -> None:
            if self.bucket.getCapacity() == 0:
                
                self.bucket= Selector.createBucket(cell.getNumber())
                #print("!Take bucket¡")
                __class__.isBucketTake = True
            else:
                #Printer.showMessage("¡You already have a bucket!")
                __class__.isBucketTake = False

    def returnBucket(self) -> None:
           
           if self.bucket.getCapacity() > 0:
            self.bucket= Bucket(properties={"capacity":0,"load":0})
            #print("!Return bucket¡")
            #__class__.isBucketTake = False
           
    
    def getIsBucketTake()->bool:
         return __class__.isBucketTake