#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 09-10-2023
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

#Breadth First Search
class BFS:
    #expande(Node)
    queue:list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    name="BFS"
    
    def search(board:Board, agent:Agent,operators):
       
        print("------ ",__class__.name," ------")
        #Printer.showBoardDetails(board.get())
        state = State(board,agent)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)
  
        
        isGoal =Validation.isGoal(board)
      
        startTime = time.time()
        
        while(not(isGoal)):
          
            BFS.generateCandidateNodes(operators,father)    
                
            BFS.moveBack(father)
     
            father=__class__.queue[0]
            __class__.countExpandedNodes+=1
           
            BFS.moveToward(father)
    
            isGoal = Validation.isGoal(father.getState().getBoard())
        
            if(not(isGoal)):
                  
                  __class__.queue.pop(0)
            else:
                
                __class__.treeDeep = father.getDeep()
                __class__.finalNode= father
                BFS.moveBack(father)
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
         return BFS.findPath(__class__.finalNode,"reverse")

    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))

        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, agent, board),agent,board):
                BFS.createNodes(operator, father)

    def createNodes(operator, father):
         node = Node(father.getState(), father, operator, father.getDeep()+1,0)
         #Son node is grandfather?
         if father.getOperator() == Selector.reverseOrientation(node.getOperator()):
                currentValues= Count.getStateValues(father)
      
                BFS.moveBack(father)
                BFS.moveToward(father.getFather())
                preValues= Count.getStateValues(father)
         
                if Validation.canReturn(preValues,currentValues):
                     __class__.queue.append(node)
                
                BFS.moveBack(father.getFather())
                BFS.moveToward(father)
         else:
               __class__.queue.append(node)


    def getAvailableDirections(movesCand:str,father):
        listofMoves = list(movesCand.split(","))
        listResult= []
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for item in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(item, agent, board),agent,board):
                listResult.append(item)
        return listResult   
   
    def findNodePath(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
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
    
    def moveBack(node):
           dirNodes = BFS.findNodePath(node, "unreverse")
           for item in dirNodes:
               Move.back(item.getOperator(), item.getState())
    
    def moveToward(node):
            dirNodes = BFS.findNodePath(node, "reverse")
            for item in dirNodes:
               Move.toward(item.getOperator(), item.getState())
