#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 28-09-2023
# Last modification date: 10-10-2023
#--------------------------------------------------------------------------------------------------------

from cell import Cell
from position import Position
from utils.count import Count
from utils.selector import Selector

class Validation:
    
    #Class variable
    cause:str=""

    #Validate if a move is allowed by combining other constraints
    def moveIsAllowedAhead(agentPosFinal,agent,board):
     
       
       isNotTowardsAWall, isNotTowardsAFireWithOutWater= False,False
       isInsideBorders:bool = Validation.isInsideBorders(agentPosFinal,board.getRowsNum(),board.getColumsNum())
       if isInsideBorders:
        isNotTowardsAWall = Validation.__isNotTowardsAWall(board.getCell(agentPosFinal))
        isNotTowardsAFireWithOutWater = Validation.__isNotTowardsAFireWithOutWater(board.getCell(agentPosFinal),agent.getBucket().getLoad())
       return isInsideBorders and isNotTowardsAWall and isNotTowardsAFireWithOutWater
    
    def moveIsAllowedBack(agentPosFinal,agent,board):
     
       
       isNotTowardsAWall, isNotTowardsAFireWithOutWater= False,False
       isInsideBorders:bool = Validation.isInsideBorders(agentPosFinal,board.getRowsNum(),board.getColumsNum())
       if isInsideBorders:
        isNotTowardsAWall = Validation.__isNotTowardsAWall(board.getCell(agentPosFinal))
        #isNotTowardsAFireWithOutWater = Validation.__isNotTowardsAFireWithOutWater(board.getCell(agentPosFinal),agent.getBucket().getLoad())
        #isInsideBorders and isNotTowardsAWall and isNotTowardsAFireWithOutWater
       return isInsideBorders and isNotTowardsAWall
    
    #Validate if a move is not towards a wall   
    def __isNotTowardsAWall(cell:Cell):
       validate = not(cell.getName() == 'wall')
       if not(validate):
        __class__.cause= "Wall"
       return validate
    
   #Validate if there is a bucket in a cell   
    def thereIsABucket(cell:Cell):

        #range(n,m) check the numbers n, n+1...until m-1
        return  cell.getNumber() in range(3,5)
    
    #Validate if there is a hydrant in a cell   
    def thereIsAHydrant(cell:Cell):
        return  cell.getNumber() == 6

    #Validate if there is a fire in a cell   
    def thereIsAFire(cell:Cell):
        return  (cell.getNumber() == 2)

    def thereIsAFireAhead(cell:Cell):
       
        return  (cell.getNumber() == 2) and cell.isFireOn()
    
    #Validate if agent is towards a fire witouth water
    def __isNotTowardsAFireWithOutWater(cell:Cell,agentBucketload:int):
        validate = not(Validation.thereIsAFireAhead(cell) and agentBucketload==0 )
        if not(validate):
            __class__.cause= "Try to go through fire without water"
        return validate
    
    #Validate if a move is inside the board       
    def isInsideBorders(pos: Position, rows:int, columns:int):
        validate = (pos.getCordI()in range(0,rows)) and (pos.getCordJ() in range (0,columns))
        if not(validate): 
            __class__.cause= "Border"
        return validate
    
    #Validate if the goal os extinguished the fires is reached
    def isGoal(board):
        
        count = Count.activefires(board)
        #print("FUEGOS ENCENDIDOS: ",count)
        return count == 0
      

          
       

    def getCause():
        return __class__.cause
    
    def canReturn(preValues, actValues):
   
        difActiveFires, difCapacity,  sameCapDifLoad = False,False,False
        if preValues !={} and actValues != {}:
       #{"capacity":agentBucketCap, "load":agentBucketLoad, "fires":actfires}
            difActiveFires = preValues["fires"] != actValues["fires"]
            #print("FIRES: ", preValues["fires"], " ", actValues["fires"])
            difCapacity= preValues["capacity"] != actValues["capacity"]
            #print("CAPACITY: ", preValues["capacity"], " ", actValues["capacity"])
            sameCapDifLoad = not(difCapacity) and (preValues["load"] != actValues["load"])
            #print("LOAD: ", preValues["load"], " ", actValues["load"])
            #print("DIFERENTE CAPACIDAD: ",difCapacity)
        return sameCapDifLoad or difActiveFires or difCapacity
    
    def listFullChecked(counter,aList):
        return (counter+2 == len(aList) + 1) or (counter+2 == len(aList))
    
    