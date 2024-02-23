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
from cell import Cell
from firecell import FireCell
from bucket import Bucket

class Selector:

    def chooseColor(num:int) -> str:
        colors ={0:"#FCFCFC", 1:"#968C8A", 2:"#EF7306",
                 3:"#DA0D10",4:"#DA0D10",5:"#05AB3F",6:"#06A1B9"}
        return colors[num]
    
    def choosePosition(orientation, agent, board) ->str:
        agentActalPos: Position = agent.getPosition(board.get())
        positions ={"up":Position(agentActalPos.getCordI() - 1, agentActalPos.getCordJ()),
                    "down":Position(agentActalPos.getCordI() + 1, agentActalPos.getCordJ()),
                    "left":Position(agentActalPos.getCordI(), agentActalPos.getCordJ()-1),
                    "right": Position(agentActalPos.getCordI(), agentActalPos.getCordJ()+1)}
        return positions[orientation]
    
    def chooseNewPosition(orientation, agentActalPos) ->str:
        positions ={"up":Position(agentActalPos.getCordI() - 1, agentActalPos.getCordJ()),
                    "down":Position(agentActalPos.getCordI() + 1, agentActalPos.getCordJ()),
                    "left":Position(agentActalPos.getCordI(), agentActalPos.getCordJ()-1),
                    "right": Position(agentActalPos.getCordI(), agentActalPos.getCordJ()+1)}
        return positions[orientation]
        
    #revertir posicion permite mover al agente si estaba a la izquierda a la derecha
    def reverseOrientation(orientation) ->str:
        positions ={"up":"down",
                    "down":"up",
                    "left":"right",
                    "right":"left",
                     None:"" }
        return positions[orientation]
    

    def chooseName(num:int) -> str:
        names ={0:"free", 1:"wall", 2:"fire",
                3:"1 liter bucket", 4:"2 liter bucket",
                5:"start", 6:"hydrant"}
        return names[num]
    
    def chooseCapacity(num:int) -> int:
        capacities ={3:1,4:2}
        return capacities[num]

    def findAgent(num:int) -> bool:
        boolValue = False
        if num == 5:
            boolValue=True
        return boolValue
    
    def createCell(i:int, j:int, num:int) -> Cell:
        cell= None
        properties = {
                    "position": Position(i,j),
                    "number": num,
                    "color": Selector.chooseColor(num),
                    "name": Selector.chooseName(num),
                    "agentHere": Selector.findAgent(num)}
        if(num != 2):
            cell = Cell(properties)
        else:
            properties["fireOn"] = True
            cell = FireCell(properties)    
        return cell
    

    def createBucket(num:int) -> Bucket:
        properties={
            "capacity": Selector.chooseCapacity(num),
            "load": 0}
        return Bucket(properties)
    
    