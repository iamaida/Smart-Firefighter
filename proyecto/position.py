#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 25-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------

class Position:

    def __init__(self,cordI:str, cordJ:str):
        self.cordI = cordI
        self.cordJ = cordJ

    def setCordI(self,cordI):
        self.cordI = cordI
    
    def setCordJ(self, cordJ):
        self.cordJ = cordJ
    
    def getCordI(self):
        return self.cordI
    
    def getCordJ(self):
        return self.cordJ
    
    def isSame(self,otherPos):
        isSameRow = self.cordI == otherPos.getCordI()
        isSameColunm = self.cordJ == otherPos.getCordJ()
        return isSameRow and isSameColunm


