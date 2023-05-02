import numpy as np

class Djikstra:
    def __init__(self,distance):
        self.distance = distance
    

    def minDistanceIndex(self):
    # INPUT  : None
    # OUTPUT : Return the Index of the list for which the distance is minimal
     
        L=[]
        minIndex = 0
        minDist=np.max(self.data[:,1])
        for floatNoeudsID in self.data[:,0]:
            noeudsID=int(floatNoeudsID)
            if self.data[noeudsID][3] == -1 and self.data[noeudsID][1] < minDist and self.data[noeudsID][1]!=-1:
                minIndex = noeudsID
                minDist = self.data[noeudsID][1]
            elif minIndex==0:
                minIndex=-1
        return minIndex
    


    def initDistanceMatrix(self,startNodeID):
    # INPUT  : Starting Node
    # OUTPUT : Matrix of distance for the Djikstra algorithm
    # Initialization of the distance Matrix :
    #       1st Column : Index
    #       2nd Column : Mimimal distance from the starting node
    #       3rd Column : Where does the fastest parh comes from 
    #       4th Column : 1 if the environment of this node has already been studied, -1 if it hasn't

        data=np.ones((self.distance.shape[0],3))*-1
        self.distance.shape[1]
        myId=np.arange(0,self.distance.shape[0]).reshape(-1,1)
        data=np.concatenate((myId,data),axis=1)
        data[startNodeID,1]=0
        data[startNodeID,3]=1
        self.data=data
        return self.data



    def calculateDistanceMatrix(self,startNodeID):
   # INPUT  : starting Node
   # OUTPUT : None
   # Calculate the fastest distance 
        selectID=startNodeID

        
        while selectID != -1:
            minDistance=np.max(self.data)
            for floatNoeudsID in self.data[:,0]:
                noeudsID=int(floatNoeudsID)

                if self.distance[int(selectID),noeudsID] !=-1 and noeudsID != selectID: # If a path exists betwenn the selected node and another node, and if the node has never been selected
                    
                    distance = self.distance[selectID,noeudsID]+self.data[selectID,1]
                    if distance < self.data[noeudsID,1] or self.data[noeudsID,1] ==-1 :
                        self.data[noeudsID,1]=distance
                        self.data[noeudsID,2]=selectID
            
              
            minIndex=self.minDistanceIndex()
            selectID=minIndex    
            self.data[selectID,3]=1 
        # PRINT A DECOMMENTER
        # print(self.data)
            
        
    
 
    def actualisePath(self,startNodeID, finishNodeID):
        

        self.initDistanceMatrix(startNodeID)
        self.calculateDistanceMatrix(startNodeID)

        L=[]
        path=str(finishNodeID)
        nextNodeID=int(finishNodeID)
        while nextNodeID != startNodeID:
            nextNodeID=int(self.data[nextNodeID,2])
            path= str(nextNodeID) + "  ->  " + path
            L.insert(0,str(nextNodeID))
        print(path)
        return L

            
                

        








