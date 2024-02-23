#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 27-10-2023
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

#Depth-First Search
class DFS:
    #expande(Node)
    queue:list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    name="DFS"
    
    def search(board:Board, agent:Agent,operators):
        
        print("--- ",__class__.name," ---")
        #Printer.showBoardDetails(board.get())
        state = State(board,agent)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)
        
        isGoal =Validation.isGoal(board)

        startTime = time.time()

      
        while(not(isGoal)):
          
            DFS.generateCandidateNodes(operators,father)
            
           
            DFS.moveBack(father)
           
            index=DFS.getIndexMostDeeper(__class__.queue)
            father=__class__.queue[index]
            __class__.countExpandedNodes+=1
            
           
            DFS.moveToward(father)
           
            
            isGoal = Validation.isGoal(father.getState().getBoard())
            
           
            if(not(isGoal)):
                  
                  __class__.queue.pop(index)
            else:
                 __class__.treeDeep = father.getDeep()
                 __class__.finalNode= father
                 DFS.moveBack(father)
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
         return DFS.findPath(__class__.finalNode,"reverse")
    
    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))
        
     
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, agent, board),agent,board):
                DFS.createNodes(operator, father)

    def createNodes(operator, father):
         node = Node(father.getState(), father, operator, father.getDeep()+1,0)
         knowAboutRelatives=DFS.knowIfRelativeCandidateToSon(node)
       
         if knowAboutRelatives["isCandidate"]:
                relativesNodes =DFS.findNodePathToFinal(node,"unreverse")
         
                currentValues= Count.getStateValues(father)
             
                DFS.moveBack(father)
                relative = relativesNodes[knowAboutRelatives["index"]]
                DFS.moveToward(relative)
                preValues= Count.getStateValues(father)
               
                if Validation.canReturn(preValues,currentValues):
                     __class__.queue.append(node)
                
                DFS.moveBack(relative)
                DFS.moveToward(father)
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
    
    
    def moveBack(node):
           dirNodes = DFS.findNodePath(node, "unreverse")
           for item in dirNodes:
               Move.back(item.getOperator(), item.getState())
   
    def moveToward(node):
            dirNodes = DFS.findNodePath(node, "reverse")
            #print("Mover hacia adelante: ",dirNodes)
            for item in dirNodes:
               Move.toward(item.getOperator(), item.getState())
    
   
    
    def getIndexMostDeeper(queue):
         index= 0
         moreDeeper = queue[0].getDeep()
         for i in range(1,len(queue)):
              if queue[i].getDeep()>moreDeeper:
                   moreDeeper = queue[i].getDeep()
                   index = i
         return index
    

    def knowIfRelativeCandidateToSon(node):
         relativesOperators = DFS.findPath(node,"unreverse")
         counter = 2
         relativeCandidate = False
         while (counter <= len(relativesOperators)) and (relativeCandidate!=True):
             
             limit= math.floor(counter/2)
             lInf = DFS.sliceList(0,limit,relativesOperators) 
             lSup = DFS.sliceList(limit,counter,relativesOperators)
             relativeCandidate= DFS.areListsEquals(lSup,lInf)
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
         