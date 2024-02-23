#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------



from utils.filemanager import FileManager
from utils.printer import Printer
from board import Board
from agent import Agent

from bfs import BFS
from dfs import DFS
from ucs import UCS
from greedysearch import GreedySearch
from astartsearch import AStartSearch


def main():
    FileManager.uploadFile("Prueba1.txt")
    Printer.showBoardNumbers(FileManager.getOutput())

    opmain= input("Desea ejecutar una busqueda: \n Digite S:Salir o C:Continuar ")
    while(opmain!="S"):
        print("--Bienvenido--")
        print("-----Ménu------")
        print("1. BFS")
        print("2. DFS")
        print("3. UCS")
        print("4. Greedy")
        print("5. A*")
        op=input("Digite una opción: ")
        
        aBoard = Board(FileManager.getOutput())
        aBoard.setup()
        agent =Agent("fireman")
        operators = "down,up,right,left"

        if(op=="1"):
           
            BFS.search(aBoard, agent, operators) #completa - solución no optima - finaliza EXPANDIDO: 563 - 20 - 3.1058  s
            print("Nodos expandidos = ",  BFS.getExpandedNodes())
            print("Profundidad del arbol = ",  BFS.getTreeDeep())  
            print("Tiempo de computo = ", BFS.getComputingTime()," s")
            print("Path = ", BFS.getPath())
            aBoard.reset()  
        elif(op=="2"):
           
            DFS.search(aBoard, agent, operators) #completa - solución no optima - finaliza EXPANDIDO: 563 - 20 - 3.1058  s
            print("Nodos expandidos = ",  DFS.getExpandedNodes())
            print("Profundidad del arbol = ",  DFS.getTreeDeep())  
            print("Tiempo de computo = ", DFS.getComputingTime()," s")
            print("Path = ", DFS.getPath())
            aBoard.reset()  
        elif(op=="3"):
            
            UCS.search(aBoard, agent, operators) #completa - solución optima - finaliza EXPANDIDOS: 563 - 20 - 3.0168 s
            print("Nodos expandidos = ",  UCS.getExpandedNodes())
            print("Profundidad del arbol = ",  UCS.getTreeDeep())  
            print("Tiempo de computo = ", UCS.getComputingTime()," s")
            print("Path = ", UCS.getPath())
            aBoard.reset() 
        elif(op=="4"):
           
            GreedySearch.search(aBoard, agent, operators)
            print("Nodos expandidos = ",  GreedySearch.getExpandedNodes())
            print("Profundidad del arbol = ",  GreedySearch.getTreeDeep())  
            print("Tiempo de computo = ", GreedySearch.getComputingTime()," s")
            print("Path = ", GreedySearch.getPath())
            aBoard.reset()   
        elif(op=="5"):
            
            AStartSearch.search(aBoard, agent, operators)  #completa - solución optima - finaliza
            print("Nodos expandidos = ",  AStartSearch.getExpandedNodes())
            print("Profundidad del arbol = ",  AStartSearch.getTreeDeep())  
            print("Tiempo de computo = ", AStartSearch.getComputingTime()," s")
            print("Path = ", AStartSearch.getPath())
            aBoard.reset() 
        else:
            print("opción invalida") 
        
        opmain= input("Desea ejecutar una busqueda: \n Digite S:Salir o C:Continuar ")
    #Printer.showBoardDetails(aBoard.get())
    

   
    

    
    
main()