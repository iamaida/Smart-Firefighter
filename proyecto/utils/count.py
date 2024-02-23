
    
class Count:

    def activefires(board) -> int:
        counter:int =0
        for i,row in enumerate(board.get()):
          
            for j,cell in enumerate(row):
                if cell.getNumber()== 2:
                    if cell.isFireOn():
                        counter = counter + 1
        return counter

    def getStateValues(node) -> dict:
        
        agentBucket= node.getState().getAgent().getBucket()
        agentBucketCap= agentBucket.getCapacity()
        agentBucketLoad= agentBucket.getLoad()
        actfires =Count.activefires(node.getState().getBoard())
        #print({"capacity":agentBucketCap, "load":agentBucketLoad, "fires":actfires})
        return {"capacity":agentBucketCap, "load":agentBucketLoad, "fires":actfires}

    
       