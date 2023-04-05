import pandas as pd
import numpy as np


class Djikstra:
    def __init__(self,distance):
        self.distance = distance
    

    def minDistanceIndex(self):
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
    


    def initShortDistance(self,startNodeID, finishNodeID):
    # Initialisation matrice distance
        
        data=np.ones((self.distance.shape[0],3))*-1
        self.distance.shape[1]
        myId=np.arange(0,self.distance.shape[0]).reshape(-1,1)
        data=np.concatenate((myId,data),axis=1)
        data[startNodeID,1]=0
        data[startNodeID,3]=1
        self.data=data
        return self.data



    def shortestDistance(self,startNodeID, finishNodeID):
        # Algorithme Djikstra
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
            
        print(self.data)


    def whichPath(self,startNodeID, finishNodeID):
        

        self.initShortDistance(startNodeID, finishNodeID)
        self.shortestDistance(startNodeID,finishNodeID)

        path=str(finishNodeID)
        nextNodeID=int(finishNodeID)
        while nextNodeID != startNodeID:
            print(nextNodeID)
            nextNodeID=int(self.data[nextNodeID,2])
            path= str(nextNodeID) + "  ->  " + path
        print(path)

            
                

        

def strToList(a):

    if isinstance(a,str):
        noeuds = list(a.split(","))
        noeudsFormat=[]
        for noeud in noeuds:
            noeudsFormat.append(list(noeud.split(":")))
        return noeudsFormat
    else:
        print("Erreur : l'element "+str(a)+" nest pas un str")
         


data =pd.read_excel("map.xlsx")
mapDataframe=pd.DataFrame(data, columns=["x","y","liens"])
mapDataframe.loc[:,"liens"] = mapDataframe.loc[:,"liens"].apply(strToList,1)

nbrRow=mapDataframe.shape[0]
distance =np.array([[-1 for j in range(nbrRow)] for i in range(nbrRow)])
for idStart in range(nbrRow):
    distance[idStart,idStart] = 0
    for noeudCible  in mapDataframe.loc[idStart]["liens"]:

        distance[idStart,int(noeudCible[0])] = noeudCible[1]
        
            

print(distance)
dji=Djikstra(distance)

dji.whichPath(0,2)





