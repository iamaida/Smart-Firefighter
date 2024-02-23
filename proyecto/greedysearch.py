#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 15-10-2023
#--------------------------------------------------------------------------------------------------------
import math
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

class GreedySearch:
    
    queue:list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    name="Greedy Search"

    def search(board:Board, agent:Agent,operators):
        
        print("------ ",__class__.name," ------")
        state = State(board,agent)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)
       
        
        isGoal =Validation.isGoal(board)
       
        index=0
   
        #countExpandedNodes=1
        startTime = time.time()
        while(not(isGoal)):
     
            GreedySearch.generateCandidateNodes(operators,father)
            
            GreedySearch.moveBack(father)
          
            index=GreedySearch.getIndexLessCost(__class__.queue)
            father=__class__.queue[index]
            __class__.countExpandedNodes+=1
    
            GreedySearch.moveToward(father)
            isGoal = Validation.isGoal(father.getState().getBoard())
            if(not(isGoal)):
                  
                
                  __class__.queue.pop(index)
            else:
                 __class__.treeDeep = father.getDeep()
                 __class__.finalNode= father
                 GreedySearch.moveBack(father)
                 __class__.queue.clear()
          
            
        endTime = time.time()
        __class__.computingTime = round(endTime -startTime,4)
       
    def getExpandedNodes():
         return __class__.countExpandedNodes
    
    def getTreeDeep():
         return __class__.treeDeep
    
    def getComputingTime():
         return __class__.computingTime
    
    def getPath():
         return GreedySearch.findPath(__class__.finalNode,"reverse")

    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))
        #listResult= []
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, agent, board),agent,board):
                GreedySearch.createNodes(operator, father)

    def createNodes(operator, father):
         
         node = Node(father.getState(), father, operator, father.getDeep()+1, GreedySearch.h(father, operator))
         knowAboutRelatives=GreedySearch.knowIfRelativeCandidateToSon(node)
       
         if knowAboutRelatives["isCandidate"]:
                relativesNodes =GreedySearch.findNodePathToFinal(node,"unreverse")
         
                currentValues= Count.getStateValues(father)
             
                GreedySearch.moveBack(father)
                relative = relativesNodes[knowAboutRelatives["index"]]
                GreedySearch.moveToward(relative)
                preValues= Count.getStateValues(father)
               
                if Validation.canReturn(preValues,currentValues):
                     __class__.queue.append(node)
                 
                
                GreedySearch.moveBack(relative)
                GreedySearch.moveToward(father)
         else:
               __class__.queue.append(node)
            
    
    def findNodePath(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
            if form == "reverse":
                dirNodes.reverse()
            return dirNodes
    
    def findNodePathToFinal(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
                if(node.getFather() ==None):
                    dirNodes.append(node) 
            if form == "reverse":
                dirNodes.reverse()
            return dirNodes
    
    def findPath(node, form):
            directios =[]
            if node != None:
                while(node.getFather() != None):
                    directios.append(node.getOperator())
                    node = node.getFather()
                if form == "reverse":
                 directios.reverse()
            return  directios
    
    def knowIfRelativeCandidateToSon(node):
         relativesOperators = GreedySearch.findPath(node,"unreverse")
         counter = 2
         relativeCandidate = False
         while (counter <= len(relativesOperators)) and (relativeCandidate!=True):
             
             limit= math.floor(counter/2)
             lInf = GreedySearch.sliceList(0,limit,relativesOperators) 
             lSup = GreedySearch.sliceList(limit,counter,relativesOperators)
             relativeCandidate= GreedySearch.areListsEquals(lSup,lInf)
             counter+=2

         return {"isCandidate":relativeCandidate,"index":(counter-2)}
    
    def sliceList(init,end, lRelatives):
         return lRelatives[init:end]
        
    
    def areListsEquals(lSup,lInf):
         equalList = True
         i=0
         while(i < len(lSup)) and (equalList==True):
              equalList = lSup[i]==Selector.reverseOrientation(lInf[i])
              i+=1
         return equalList
   
    def moveBack(node):
           dirNodes = GreedySearch.findNodePath(node, "unreverse")
           for item in dirNodes:
               Move.back(item.getOperator(), item.getState())
    
    def moveToward(node):
            dirNodes = GreedySearch.findNodePath(node, "reverse")
            for item in dirNodes:
               Move.toward(item.getOperator(), item.getState())

    
    def getIndexLessCost(queue):
         index= 0
         lessCost = queue[0].getCost()
         for i in range(1,len(queue)):
              if queue[i].getCost()<lessCost:
                   lessCost = queue[i].getCost()
                   index = i
         return index

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
    
    #Return a dictionary with the agent position and list with the active fires positions              
    def __getFiresAgentPositions(node):
         agent = node.getState().getAgent()
         board = node.getState().getBoard()
         agentPos = agent.getPosition(board.get())
         firesPos = GreedySearch.__getFiresPositions(node)
         result = len(firesPos)
         if result > 0:
            result = {"agent": agentPos, "fires":firesPos}
         return result 
    #Return manhattan distance between two points
    def manhattan(pos1,pos2):
         #print("Posiciones: ", pos1, pos2)
         return abs(pos1.getCordI()- pos2.getCordI()) + abs(pos1.getCordJ()- pos2.getCordJ())
    

    def manhattanAgentToFire(agentPos,nearFirePos,operator):
         newAgentPos = Selector.chooseNewPosition(operator, agentPos)
         #print("Posiciones: ", pos1, pos2)
         return abs(newAgentPos.getCordI()- nearFirePos.getCordI()) + abs(newAgentPos.getCordJ()- nearFirePos.getCordJ())
    
    #Return a dictionary with the nearless position fire to the agent, the manhattan and the list of fires positions 
    def __getFireNearAgentFires(node,operator):
         firesAgentPos = GreedySearch.__getFiresAgentPositions(node)
         result= firesAgentPos
         if firesAgentPos != 0:
            agent = firesAgentPos["agent"]
            fires = firesAgentPos["fires"]
            fire = fires[0]
            short = GreedySearch.manhattanAgentToFire(agent,fire,operator)
            for i in range(1, len(fires)):
             if GreedySearch.manhattanAgentToFire(agent,fires[i],operator) < short:
                 fire= fires[i]
                 short = GreedySearch.manhattanAgentToFire(agent,fire,operator)
            result={"short": short, "fire":fire, "fires":fires}
         return result


    def h(node,operator):
       
        return GreedySearch.__sumOfmanhattanDistances(node,operator)

    #return a dictionary with manhathan of nearless fire to agent, this fire position and a list with the others fires
    def __getInterFireNearAgentFires(node,operator):
         result = GreedySearch.__getFireNearAgentFires(node,operator)
         final= result
         if result != 0: 
            #print("Fires: ", result["fires"])
            newfires = []
            for item in result["fires"]:
                if result["fire"] != item:
                    newfires.append(item)
            final = {"short": result["short"], "fire":result["fire"] , "fires":newfires}
            #print("fuego más cercano al agente: (", final["fire"].getCordI(),",",final["fire"].getCordJ(),")")
         return final
    
    def __getFinalFireNearAgentFires(node,operator):
         result = GreedySearch.__getInterFireNearAgentFires(node,operator)
         final = result
         if result != 0:
            fire = result["fire"]
            newList =[]
         
            for item in result["fires"]:
                newList.append(GreedySearch.manhattan(fire,item))
                fire = item
            final = {"short": result["short"],  "fires":newList}
            #print("distancia agente fuego cercano: ", final["short"], "distancia a otros fuegos: ", final["fires"])
           
         return final
    
    def __sumOfmanhattanDistances(node,operator):
         result = GreedySearch.__getFinalFireNearAgentFires(node,operator)
         final = result
         if result != 0:
            agentToNearFire = result["short"]
            sum = agentToNearFire
            for distance in result["fires"]:
                sum += distance
            final = sum
         return final
    


                  