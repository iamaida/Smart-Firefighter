#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 25-10-2023
#--------------------------------------------------------------------------------------------------------
class Bucket:

    isReloaded= False
    isUsed= False

    #Constructor
    def __init__(self, properties:dict):
        # Instance attribute
        self.properties=properties

    def use(self):
        if self.properties["load"] > 0:
            self.properties["load"] = self.properties["load"]-1
            #print("!Bucket used!")

    def unuse(self):
        #print("ENTRADA POR UN USED")
        if self.properties["capacity"] > 0:
            self.properties["load"] = self.properties["load"]+1
            #print("!Bucket unused!")
        

    def getLoad(self):
        return self.properties["load"]

    def getCapacity(self):
        return self.properties["capacity"]

    def reload(self):
        if self.properties["capacity"]>0:
            if self.properties["load"] == 0 :
            
                self.properties["load"] = self.properties["capacity"]
            
                #print("Hydrant say: ¡Reloaded Bucket!")
             
            #else:
            #    print("Hydrant say: ¡Bucket still had water!")
        #else:
        #    print("Hydrant say: ¡Agent without bucket!")

    def unload(self):
        if self.properties["load"] > 0:
            self.properties["load"] = self.properties["load"]-self.properties["capacity"]
            #print("Hydrant say: ¡Unloaded Bucket!")  
        #else:
        #    print("Hydrant say: ¡It is not necessary unload!")