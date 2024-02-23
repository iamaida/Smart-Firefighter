#-----------------------------------------------------------------------------------------------
# Curso: Inteligencia Artificial
# Profesor: Oscar Bedoya
# Tema: Proyecto 1
# Nombre:Aida Milena Mina Caicedo
# Codigo: 1225328
# Fecha última modificación: 11-07-2022
#--------------------------------------------------------------------------------------------------------

from tkinter import*
import time
import os 
from tkinter import filedialog
from utils.filemanager import FileManager
from utils.printer import Printer
from utils.selector import Selector
from board import Board
from agent import Agent
from position import Position

from bfs import BFS
from dfs import DFS
from ucs import UCS
from greedysearch import GreedySearch
from astartsearch import AStartSearch

#---------------------------------------------------MAIN WINDOW PARAMETERS --------------------------
#Create main window
root = Tk()
#Title the window
root.title("Project 1")

#Set the geometry
#widht x height
root.geometry("1322x599")

root.resizable(True, False)

root.configure(bg='white')

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------DATA---------------------------------------------

#Images
searchImage = PhotoImage(file = './images/search.png')
fileImage = PhotoImage(file = './images/upload.png')

#Lists
#Search names
searchNames = ["BFS", "Uniform Cost", "DFS", "Greedy", "A*"]
searchResults = []
searchSelected= []
environment= []




#Tkinter variable to radiobuttons
radioV= IntVar()
#Set radiobuttons with option 1 BFS like default option
radioV.set("1")
#Get current directory
#selection = StringVar()



#-------------------------------------------------------------------------------------------------
#----------------------------------------FRAMES CREATIONS---------------------------------------
#Create title frame
titleFrame = LabelFrame(root,highlightthickness=0, borderwidth=0)# space about grid
titleFrame.pack() #space about window

#Create main frame
mainFrame = LabelFrame(root, padx=20, pady=10, width=500, height=150, bg="white")# space about grid
mainFrame.pack() #space about window

#Create world frame
worldFrame = LabelFrame(mainFrame, padx=20,pady=20,bg="black")# space about grid
worldFrame.grid(padx=10, pady=20, row=0, rowspan=75,column=45, columnspan=90) #space about window

#Create options frame
optionsFrame = LabelFrame(mainFrame, padx=20,pady=20,highlightthickness=0, borderwidth=0, bg="white")# space about grid
optionsFrame.grid(padx=10, pady=20, row=0, rowspan=60,column=0, columnspan=45) #space about window

#Create  Buttonframe
buttonFrame = LabelFrame(mainFrame)# space about grid
buttonFrame.grid(padx=10, row=76,rowspan=140,column=45, columnspan=90) #space about window
showButton = Button(buttonFrame, text="Show", font=("Consolas", 12, "bold"), command =lambda: showAnimation(), fg="white", bg="black", state=DISABLED)
showButton.pack()

#Create Searchtitleframe
searchTitleFrame = LabelFrame(mainFrame,highlightthickness=0, borderwidth=0, bg="white")# space about grid
searchTitleFrame.grid(padx=10, row=61,column=0, columnspan=45) #space about window
#Create Report frame
#Remove report border highlightthickness=0, borderwidth=0
reportFrame = LabelFrame(mainFrame, highlightthickness=0, borderwidth=0)# space about grid
reportFrame.grid(padx=10,row=64, rowspan=150,column=0, columnspan=45) #space about window

#---------------------------------------------------------------------------------------------------

#-----------------------------------------TITLEFRAME WIDGETS--------------------------------------
#Show project title
def showGameTitle(title):
    titleLabel = Label(titleFrame, width= 75, height= 2, padx=7, pady=3,text= title,font=("Consolas", 24, "bold"),fg="white", bg="black")
    titleLabel.pack()
#-------------------------------------------------------------------------------------------------

#------------------------------------------OPTIONSFRAME WIDGET----------------------------------------
#Show  menu options
def showMenuOptions(img, sNames):
    #CREATE

    #Options  main image
    searchImage = Label(optionsFrame, width=64, height=64, padx=7, pady=3,image=img, bg="white")
    #Options main title
    searchTitle = Label(optionsFrame, width= 50, padx=7, pady=3,text= "Searching Strategies",font=("Consolas", 18, "bold"),fg="black")
    
    # Uninformed options title
    uninformedTitle =  Label(optionsFrame, width= 15, padx=5, pady=3,text= "Uninforme Search",font=("Consolas", 17, "bold"),fg="black",bg="white")
    # Informed options title
    informedTitle =  Label(optionsFrame, width= 15, padx=5, pady=3,text= "Informed Search",font=("Consolas", 17, "bold"),fg="black",bg="white")

    #FIX
    searchImage.grid(row=0,column=0, columnspan=4)
    searchTitle.grid(row=1,column=0, columnspan=4)
   
    uninformedTitle.grid(row=2,column=1)

    #Fix radiobutton uninformed options
    showUninformedOptions(sNames)
    
    informedTitle.grid(row=4,column=1)

    #Fix radiobutton informed options
    showInformedOptions(sNames)
    
    for child in optionsFrame.winfo_children():
        child.configure(state=DISABLED)

#Create radio buttons with uninformed search options
def showUninformedOptions(sNames:list)->None:

    # 1. Breadth-first-search --- Amplitud
    # 2. Uniform Cost --- Costo Uniforme
    # 3. Depth-first-search --- Profundidad evitando ciclos

    for i in range(1,4):
        
        uninformeSearchOption = Radiobutton(optionsFrame, width=11,text= sNames[i-1], font=("Consolas", 14, "bold"), variable=radioV, value= i,bg="white", command= lambda: showSearchSelected(searchNames[radioV.get()-1]))
        uninformeSearchOption.grid(row=3,column=i)
  

#Create radio buttons with informed search options
def showInformedOptions(sNames:list)->None:

    # 4. Greedy --- Avara
    # 5. A*
    columValue = 1
    for i in range(4,6):
        
        informeSearchOption = Radiobutton(optionsFrame, width=11,text= sNames[i-1], font=("Consolas", 14, "bold"), variable=radioV, value= i, bg="white", command= lambda: showSearchSelected(searchNames[radioV.get()-1]))
        informeSearchOption.grid(row=5,column=columValue)
        columValue +=2

#--------------------------------------------------------------------------------------------------


#---------------------------------------------------WORLDFRAME WIDGETS----------------------------------        
#Show world using Label widgets
def showWorld(environment:list)->None:
    
    
    #rows
    for i in range(len(environment)):
        #colums
        for j in range(len(environment[i])):
            #get cell number
            number = environment[i][j]
            #Create label widget
            a_label = Label(worldFrame, padx=15, pady=10, bg= Selector.chooseColor(number), border=1, relief="solid")
            #add label widget
            a_label.grid(row=i,column=j)
    
    

    

def showWorldEmtyWorld()->None:
   
    e = [0,0,0,0,0,0,0,0,0,0,]
    eList=[e,e,e,e,e,e,e,e,e,e]
 
    #rows
    for i in range(len(eList)):
        #colums
        for j in range(len(eList[i])):
            #get cell number
            number = eList[i][j]
            #Create label widget
            a_label = Label(worldFrame, padx=15, pady=10, bg= Selector.chooseColor(number), border=1, relief="solid")
            #add label widget
            a_label.grid(row=i,column=j)


def showWorldNotExecute(environment:list)->None:
  
    
    #rows
    for i in range(len(environment)):
        #colums
        for j in range(len(environment[i])):
            #get cell number
            number = environment[i][j]
            #Create label widget
            a_label = Label(worldFrame, padx=15, pady=10, bg= Selector.chooseColor(number), border=1, relief="solid")
            #add label widget
            a_label.grid(row=i,column=j)

def showWorldAnimation(positions, environment)->None:
            
            for pos in positions: 

                a_label = Label(worldFrame, padx=15, pady=10, bg= "#7D3C98", border=1, relief="solid")
                    #add label widget
                a_label.grid(row=pos.getCordI(),column=pos.getCordJ())
                time.sleep(0.2)
                root.update()
                number = environment[pos.getCordI()][pos.getCordJ()]
                a_label = Label(worldFrame, padx=15, pady=10, bg= Selector.chooseColor(number), border=1, relief="solid")
                    #add label widget
                a_label.grid(row=pos.getCordI(),column=pos.getCordJ())
                time.sleep(0.2)
                root.update()

            
          



#--------------------------------------------------------------------------------------------------

#--------------------------------------------BUTTONFRAME WIDGETS----------------------------------

#-------------------------------------------------------------------------------------------------
def showAnimation():
 
    showWorldNotExecute(environment[0])
    path=searchResults[0][4]
    showWorldAnimation(getPositions(environment[0], path),environment[0])

def getStartPosition(environment):
     for i in range(len(environment)):
        #colums
        for j in range(len(environment[i])):
            #get cell number
            number = environment[i][j]
            if number == 5:
                pos =Position(i,j)
     return pos

def getPositions(environment, path):
     posInit = getStartPosition(environment)
     positions=[]
     positions.append(posInit)
     for i in range(len(path)):
         posInit=Selector.chooseNewPosition(path[i], posInit)
         positions.append(posInit)
     return positions


def showUploadFileImage(img):
    uploadImage = Button(mainFrame, width=30, height=30, padx=7, pady=3,image=img, bg="white", command=lambda: chooseFile(os.getcwd()))
    uploadImage.grid(column= 0, row=0)


#------------------------------------------- SEARCHTITLEFRAME WIDGETS---------------------------------
def showSearchSelected(searchName:str):
    #Create title label
    #print(searchName)
    searchLabel = Label(searchTitleFrame, width= 15, padx=7, pady=18,text= searchName, font=("Consolas", 18, "bold"),fg="black", highlightthickness=0, borderwidth=0, bg="white")
    searchLabel. grid(row=0, column=1, columnspan=4)
    
    #["BFS", "Uniform Cost", "DFS", "Greedy", "A*"]

    showWorldNotExecute(environment[0])
    searchSelected.clear()
    searchSelected.append(searchName)
    
    if searchName=="BFS":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName=="Uniform Cost":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName=="DFS":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName=="Greedy":
        executeSearch(environment[0], searchName)
        showReport()
    else:
        executeSearch(environment[0], searchName)
        showReport()

    showButton.config(state=NORMAL)

    
#--------------------------------------------------------------------------------------------------   
    

#------------------------------------------------------REPORTFRAME WIDGETS-------------------------
#Create and fix report 
def showReport():
    
    columsTitles =["Expaded Nodes", "Tree Deep", "Time", "Cost"]
    searchs = searchResults[0]

    for i in range(len(columsTitles)):

        a_title = Label(reportFrame, width= 25, padx=7, pady=3,text= columsTitles[i], font=("Consolas", 11, "bold"),bg="black",fg="white", border=1, relief="raised")
        a_title. grid(row=1, column=i)
        a_answer = Label(reportFrame, width= 25, padx=7, pady=3,text= searchs[i], font=("Consolas", 11, "bold"),bg="white",fg="black")
        a_answer.grid (row=2, column=i)

def showReportEmpty():
    searchLabel = Label(searchTitleFrame, width= 15, padx=7, pady=18,text= "Report", font=("Consolas", 18, "bold"),fg="black", highlightthickness=0, borderwidth=0, bg="white")
    searchLabel. grid(row=0, column=1, columnspan=4)

    columsTitles =["Expaded Nodes", "Tree Deep", "Time", "Cost"]

    for i in range(len(columsTitles)):

        a_title = Label(reportFrame, width= 20, padx=7, pady=3,text= columsTitles[i], font=("Consolas", 11, "bold"),bg="black",fg="white", border=1, relief="raised")
        a_title. grid(row=1, column=i)
        a_answer = Label(reportFrame, width= 20, padx=7, pady=3,text= " ", font=("Consolas", 11, "bold"),bg="white",fg="black")
        a_answer.grid (row=2, column=i)
#--------------------------------------------------------------------------------------------------   
def executeSearch(environment, searchName):
    searchResults.clear()
    #["BFS", "Uniform Cost", "DFS", "Greedy", "A*"]
    #FileManager.uploadFile("Prueba1.txt")
    #Printer.showBoardNumbers(FileManager.getOutput())
   
    aBoard = Board(environment)
    aBoard.setup()
    agent =Agent("fireman")
    operators = "down,up,right,left"
    
    if searchName=="BFS":
        BFS.search(aBoard, agent, operators) #completa - solución no optima - finaliza EXPANDIDO: 563 - 20 - 3.1058  s
        search = []
        search.append(BFS.getExpandedNodes())
        search.append(BFS.getTreeDeep())
        search.append(BFS.getComputingTime())
        search.append("No aplica")
        search.append(BFS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName=="Uniform Cost":
        UCS.search(aBoard, agent, operators) #completa - solución optima - finaliza EXPANDIDOS: 563 - 20 - 3.0168 s
        search = []
        search.append(UCS.getExpandedNodes())
        search.append(UCS.getTreeDeep())
        search.append(UCS.getComputingTime())
        search.append(UCS.getCostoTotal())
        search.append(UCS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName=="DFS":
        DFS.search(aBoard, agent, operators) #completa - solución no optima - finaliza EXPANDIDO: 563 - 20 - 3.1058  s
        search = []
        search.append(DFS.getExpandedNodes())
        search.append(DFS.getTreeDeep())
        search.append(DFS.getComputingTime())
        search.append("No aplica")
        search.append(DFS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName=="Greedy":
        GreedySearch.search(aBoard, agent, operators)
        search = []
        search.append(GreedySearch.getExpandedNodes())
        search.append(GreedySearch.getTreeDeep())
        search.append(GreedySearch.getComputingTime())
        search.append("No aplica")
        search.append(GreedySearch.getPath())
        searchResults.append(search)
        aBoard.reset()  
    else:
        AStartSearch.search(aBoard, agent, operators)  #completa - solución optima - finaliza
        search = []
        search.append(AStartSearch.getExpandedNodes())
        search.append(AStartSearch.getTreeDeep())
        search.append(AStartSearch.getComputingTime())
        search.append(AStartSearch.getCostoTotal())
        search.append(AStartSearch.getPath())
        searchResults.append(search)
        aBoard.reset() 
#--------------------------------------------------------------------------------------------------   

#Open a file dialog box to choose the file to upload
def chooseFile(currentpath):
    filepath = filedialog.askopenfilename(initialdir=currentpath,title="Select a file", filetypes = (
        ('text files', '*.txt'),))

    FileManager.uploadFile(filepath)
    environment.clear()
    environment.append(FileManager.getOutput())
    showWorld(environment[0])
    for child in optionsFrame.winfo_children():
        child.configure(state=NORMAL)
    showReportEmpty()
    #executeSearch(environment[0])
    



#-----------------------------------------------------------------------------------------------

#------------------------------------------GUI CREATION------------------------------------------
#Invocate function

def main():

#--------------------------------------------UPLOAD DATA FROM FILE----------------------------------------------------
    
    #
    #FileManager.uploadFile("Prueba1.txt")
  
    #environment.append(FileManager.getOutput())

    showGameTitle("Smart Fireman")
    showUploadFileImage(fileImage)
    #chooseFile(os.getcwd())
    showMenuOptions(searchImage,searchNames)
    #showWorld(environment[0])
    showWorldEmtyWorld()
    showReportEmpty()
    #showButton()
    

    #Generate constant loop
    root.mainloop()

main()

#------------------------------------------------------------------------------------------------

#---------------------------------------GUI EXECUTION------------------------------------------

#---------------------------------------------------------------------------------------------