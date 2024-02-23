#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 30-09-2023
#--------------------------------------------------------------------------------------------------------
from state import State


class Node:
    

    def __init__(self, state:State, father:'Node', operator:str, deep:int, cost:int):
        
        #__class__.acumDeep = __class__.acumDeep +1
        #self.deep = __class__.acumDeep
        self.state = state
        self.father = father
        self.operator = operator
        self.deep = deep
        self.cost = cost

    def getState(self):
        return self.state
    
    def getFather(self):
        return self.father
    
    def getGrandFather(self):
        if self.deep >= 2:
            grandfather = self.father.getFather()
        else:
            grandfather = None
        return grandfather

    def getOperator(self):
        return self.operator
    
    def getDeep(self):
        return self.deep
    
    def getCost(self):
        return self.cost
 
   