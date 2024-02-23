#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 30-09-2023
#--------------------------------------------------------------------------------------------------------

from board import Board
from agent import Agent

class State:
    def __init__(self,board:Board, agent:Agent):
        self.board = board
        self.agent = agent

    def getBoard(self):
        return self.board
    
    def getAgent(self):
        return self.agent
    
  