#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 15-10-2023
#--------------------------------------------------------------------------------------------------------
from board import Board
from agent import Agent
from node import Node
from state import State
from utils.validation import Validation
from utils.printer import Printer
from move import Move
from utils.count import Count
from utils.selector import Selector
import time

class AStartSearch:
    
    queue:list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    costoTotal=0
    name="A*"

    def search(board:Board, agent:Agent,operators):
        
        print("--- ",__class__.name,"--- ")
        state = State(board,agent)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)
        
        isGoal =Validation.isGoal(board)

        index=0
   
        startTime = time.time()
        while(not(isGoal)):
            
            AStartSearch.generateCandidateNodes(operators,father)
            
            
            AStartSearch.moveBack(father)
           
            index=AStartSearch.getIndexLessCost(__class__.queue)
            father=__class__.queue[index]
            __class__.countExpandedNodes+=1
            
          
            AStartSearch.moveToward(father)
            isGoal = Validation.isGoal(father.getState().getBoard())
            if(not(isGoal)):
                  
                  __class__.queue.pop(index)
            else:
                 __class__.costoTotal= father.getCost()
                 __class__.treeDeep = father.getDeep()
                 __class__.finalNode= father
                 AStartSearch.moveBack(father)
                 __class__.queue.clear()
          
            
        endTime = time.time()
        __class__.computingTime = round(endTime -startTime,4) 

    def getExpandedNodes():
         return __class__.countExpandedNodes
    
    def getTreeDeep():
         return __class__.treeDeep
    
    def getComputingTime():
         return __class__.computingTime
    
    def getCostoTotal():
         return __class__.costoTotal
    
    def getPath():
         return AStartSearch.findPath(__class__.finalNode,"reverse")
            
    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))
       
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, agent, board),agent,board):
                AStartSearch.createNodes(operator, father)

    def createNodes(operator, father):
         node = Node(father.getState(), father, operator, father.getDeep()+1,AStartSearch.f(father, operator))
         if father.getOperator() == Selector.reverseOrientation(node.getOperator()):
                currentValues= Count.getStateValues(father)
             
                AStartSearch.moveBack(father)
                AStartSearch.moveToward(father.getFather())
                preValues= Count.getStateValues(father)
            
                if Validation.canReturn(preValues,currentValues):
                     __class__.queue.append(node)
                
                AStartSearch.moveBack(father.getFather())
                AStartSearch.moveToward(father)
         else:
               __class__.queue.append(node)
    
   
    def findPath(node, form):
            directios =[]
            if node != None:
                while(node.getFather() != None):
                    directios.append(node.getOperator())
                    node = node.getFather()
                if form == "reverse":
                 directios.reverse()
            return  directios
    
    def findNodePath(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
            if form == "reverse":
                dirNodes.reverse()
            return dirNodes
    
    def moveBack(node):
           dirNodes = AStartSearch.findNodePath(node, "unreverse")
           for item in dirNodes:
               Move.back(item.getOperator(), item.getState())

    def moveToward(node):
            dirNodes = AStartSearch.findNodePath(node, "reverse")
            for item in dirNodes:
               Move.toward(item.getOperator(), item.getState())
    
    def determineCost(state):
        bucket = state.getAgent().getBucket()
        cost = 1  
        if bucket.getLoad() > 0:
             cost += bucket.getLoad()

        return cost
    
    def getIndexLessCost(queue):
         index= 0
         lessCost = queue[0].getCost()
         for i in range(1,len(queue)):
              if queue[i].getCost()<lessCost:
                   lessCost = queue[i].getCost()
                   index = i
         return index
    
    #cost function g(n) calculate the cost of the path in each node
    def g(node):
         return node.getCost()+AStartSearch.determineCost(node.getState())           
    
    def __getFiresPositions(node):
         boardGrid = node.getState().getBoard().get()
         result =[]
         count=1
         for row in boardGrid:
            for cell in row:
                 
                 if cell.getNumber() == 2 and cell.isFireOn() == True:
                    count+=1
                    result.append(cell.getPosition())
         
         return result
                 
    def __getFiresAgentPositions(node):
         agent = node.getState().getAgent()
         board = node.getState().getBoard()
         agentPos = agent.getPosition(board.get())
         firesPos = AStartSearch.__getFiresPositions(node)
         result = len(firesPos)
         if result > 0:
            result = {"agent": agentPos, "fires":firesPos}
         return result 

    def manhattan(pos1,pos2):
         #print("Posiciones: ", pos1, pos2)
         return abs(pos1.getCordI()- pos2.getCordI()) + abs(pos1.getCordJ()- pos2.getCordJ())
    
    
    def manhattanAgentToFire(agentPos,nearFirePos,operator):
         newAgentPos = Selector.chooseNewPosition(operator, agentPos)
         #print("Posiciones: ", pos1, pos2)
         return abs(newAgentPos.getCordI()- nearFirePos.getCordI()) + abs(newAgentPos.getCordJ()- nearFirePos.getCordJ())
    
    
    def __getFireNearAgentFires(node,operator):
         firesAgentPos = AStartSearch.__getFiresAgentPositions(node)
         result= firesAgentPos
         if firesAgentPos != 0:
            agent = firesAgentPos["agent"]
            fires = firesAgentPos["fires"]
            fire = fires[0]
            short = AStartSearch.manhattanAgentToFire(agent,fire,operator)
            for i in range(1, len(fires)):
             if AStartSearch.manhattanAgentToFire(agent,fires[i],operator) < short:
                 fire= fires[i]
                 short = AStartSearch.manhattanAgentToFire(agent,fire,operator)
            result={"short": short, "fire":fire, "fires":fires}
         return result


    def h(node,operator):
       
        return AStartSearch.__sumOfmanhattanDistances(node,operator)

    
    def __getInterFireNearAgentFires(node,operator):
         result = AStartSearch.__getFireNearAgentFires(node,operator)
         final= result
         if result != 0: 
            #print("Fires: ", result["fires"])
            newfires = []
            for item in result["fires"]:
                if result["fire"] != item:
                    newfires.append(item)
            final = {"short": result["short"], "fire":result["fire"] , "fires":newfires}
         return final
    
    def __getFinalFireNearAgentFires(node,operator):
         result = AStartSearch.__getInterFireNearAgentFires(node,operator)
         final = result
         if result != 0:
            fire = result["fire"]
            newList =[]
         
            for item in result["fires"]:
                newList.append(AStartSearch.manhattan(fire,item))
                fire = item
            final = {"short": result["short"],  "fires":newList}
         return final
    
    def __sumOfmanhattanDistances(node,operator):
         result = AStartSearch.__getFinalFireNearAgentFires(node,operator)
         final = result
         if result != 0:
            agentToNearFire = result["short"]
            sum = agentToNearFire
            for distance in result["fires"]:
                sum += distance
            final = sum
         return final
    
    def f(node,operator):
        return AStartSearch.g(node) + AStartSearch.h(node,operator)
    


                  