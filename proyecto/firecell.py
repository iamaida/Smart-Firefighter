#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 30-09-2023
#--------------------------------------------------------------------------------------------------------

from cell import Cell
class FireCell(Cell):
    #Constructor
    def __init__(self, properties:dict):
        super().__init__(properties)

    def isFireOn(self):
        return self.properties["fireOn"]
    
    def fireOff(self):
        if self.properties["fireOn"]:
            self.properties["fireOn"] = False
            #print("¡Fire extinguished!")

    def fireOn(self):
          if not(self.properties["fireOn"]):
            self.properties["fireOn"] = True
            #print("¡Fire unextinguished!")   