#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 25-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------
from utils.selector import Selector
from position import Position
from cell import Cell
from utils.validation import Validation
from utils.printer import Printer

class Board:
    grid:list = []
    fires: list =[]

    def __init__(self, template:list):
        self.template=template

    def setup(self) -> None:

        boardRow:list =[]
      
        for i,row in enumerate(self.template):
          
            for j,num in enumerate(row):
                cell= Selector.createCell(i,j,num)
                boardRow.append(cell)
                if num==2:
                    __class__.fires.append(cell)
            __class__.grid.append(boardRow)
            boardRow=[]
               
    def get(self)-> list:
        return __class__.grid
    
    def set(self, initBoard)-> list:
        __class__.grid = initBoard
    
    def getRowsNum(self)-> list:
        return len(__class__.grid)
    
    def getColumsNum(self)-> list:
        return len(__class__.grid[0])
    
    def getCell(self,pos: Position):
        
        if Validation.isInsideBorders(pos, self.getRowsNum(), self.getColumsNum()):
            return __class__.grid[pos.getCordI()][pos.getCordJ()]
        else:
            Printer.showMessage('¡Cell no available!')

    def getFiresCells(self) -> list:
        return __class__.fires
    
    def reset(self):
        __class__.grid=[]
        __class__.fires=[]

 