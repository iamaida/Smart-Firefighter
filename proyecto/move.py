#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 09-10-2023
#--------------------------------------------------------------------------------------------------------
from board import Board
from agent import Agent
from position import Position
from cell import Cell
from utils.validation import Validation
from utils.printer import Printer
from utils.selector import Selector

class Move:
    
    direction:str =""
    failMessag:str =""

    #Move agent to the position indicate by the orientation
    def toward(orientation, state):
        agentPosFinal: Position = Selector.choosePosition(orientation, state.getAgent(), state.getBoard())
        __class__.direction =orientation
        Move.__goAhead( agentPosFinal,state.getBoard(),state.getAgent())
    
    #Move agent to the opposite position indicate by the orientation
    def back(orientation,state):
        agentActalPos: Position = state.getAgent().getPosition(state.getBoard().get())
        #####
        #print("---CELL INFO---")
        #Printer.showCellInfo(state.getBoard().getCell(agentActalPos))
        ####
        if state.getBoard().getCell(agentActalPos).getNumber()!=5:
            
            agentPosFinal: Position = Selector.choosePosition(Selector.reverseOrientation(orientation), state.getAgent(), state.getBoard())
            __class__.direction ="Reverse "+Selector.reverseOrientation(orientation)
            Move.__goBack( agentActalPos,agentPosFinal,state.getBoard(),state.getAgent())
        else:
            #print("entrada por aqui")
            state.getAgent().returnBucket()
            for cell in state.getBoard().getFiresCells():
                cell.fireOn()
            state.getBoard().getCell(agentActalPos).removeAgentFromHere()

        #agentPosFinal: Position = Selector.choosePosition(Selector.reverseOrientation(orientation), state.getAgent(), state.getBoard())
        #__class__.direction ="Reverse "+Selector.reverseOrientation(orientation)
        #Move.__goBack( agentPosFinal,state.getBoard(),state.getAgent())

    #Switch the value of isAgentHere propertie depents of agent final position
    def __changeAgentPosition(agentPosFinal,agent:Agent,board:Board):
        agentPosInit: Position = agent.getPosition(board.get())
        initCell: Cell = board.getCell(agentPosInit)
        #initCell.changeAgentHere()
        initCell.removeAgentFromHere()
        finalCell: Cell = board.getCell(agentPosFinal)
        #finalCell.changeAgentHere()
        finalCell.changeAgentToHere()
       
    
    #Switch the value of isAgentHere propertie depents of agent final position
    def __changeAgentPositionBack(agentPosInit,agentPosFinal,agent:Agent,board:Board):
        #agentPosInit: Position = agent.getPosition(board.get())
        initCell: Cell = board.getCell(agentPosInit)
        #initCell.changeAgentHere()
        initCell.removeAgentFromHere()
        finalCell: Cell = board.getCell(agentPosFinal)
        #finalCell.changeAgentHere()
        finalCell.changeAgentToHere()
        #Printer.showMessage(f'Move Back: {__class__.direction} ')
        #print("CAMBIO POSICIÓN BACK-----")

    #Execute a valid agent move ahead
    def __goAhead(agentPosFinal,board:Board,agent:Agent):
        
        
        if Validation.moveIsAllowedAhead(agentPosFinal,agent,board):
            
            Move.__changeAgentPosition(agentPosFinal,agent, board)
            if Validation.thereIsABucket(board.getCell(agentPosFinal)):
                agent.takeBucket(board.getCell(agentPosFinal))
            
            if Validation.thereIsAHydrant(board.getCell(agentPosFinal)):
                agent.getBucket().reload()
            
            if Validation.thereIsAFireAhead(board.getCell(agentPosFinal)):
                    agent.getBucket().use()
                    board.getCell(agentPosFinal).fireOff()

        else:
            __class__.failMessag ="not allowed"
            #Printer.showMessage(f'¡{Validation.getCause()}:Move {__class__.direction} is {__class__.failMessag}!')
    
    #Execute a valid agent move back

    def __goBack(agentPosInit,agentPosFinal,board:Board,agent:Agent):
       
         #print("POR AQUI: Posicion final: ",agentPosFinal.getCordI()," ",agentPosFinal.getCordJ() , " ", Validation.moveIsAllowedBack(agentPosFinal,agent,board))
         if Validation.moveIsAllowedBack(agentPosFinal,agent,board):
            Move.__changeAgentPositionBack(agentPosInit,agentPosFinal,agent, board)
            if Validation.thereIsABucket(board.getCell(agentPosInit)):
                agent.returnBucket()
            if Validation.thereIsAHydrant(board.getCell(agentPosInit)):
                agent.getBucket().unload()
            if Validation.thereIsAFire(board.getCell(agentPosInit)):
                    agent.getBucket().unuse()
                    board.getCell(agentPosInit).fireOn()
         else:
            #print("POR AQUI: Posicion final: ",agentPosFinal.getCordI()," ",agentPosFinal.getCordJ() , " ", not(Validation.moveIsAllowedBack(agentPosFinal,agent,board)) and Validation.moveIsAllowedBack(agentPosInit,agent,board))
            if not(Validation.moveIsAllowedBack(agentPosFinal,agent,board)) and Validation.moveIsAllowedBack(agentPosInit,agent,board):
                initCell: Cell = board.getCell(agentPosInit)
                initCell.changeAgentHere()
                #Printer.showMessage(f'Move Back: {__class__.direction} ')
                if Validation.thereIsABucket(board.getCell(agentPosInit)):
                    agent.returnBucket()
                if Validation.thereIsAHydrant(board.getCell(agentPosInit)):
                    agent.getBucket().unload()
                if Validation.thereIsAFire(board.getCell(agentPosInit)):
                    agent.getBucket().unuse()
                    board.getCell(agentPosInit).fireOn()
            else:
                __class__.failMessag ="not allowed"
          

         
            #Printer.showMessage(f'¡{Validation.getCause()}:Move {__class__.direction} is {__class__.failMessag}!')
