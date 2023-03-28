import pandas as pd
import numpy as np




class Djikstra:
    def __init__(self,distance):
        self.distance = distance
    

    def minDistance(self):
        L=[]
        minIndex=data[int(max(data[:,1]))][]
        for floatNoeudsID in data[:,0]:
            noeudsID=int(floatNoeudsID)
            if data[noeudsID][3] != -1 and :
                print(data[noeudsID])
                    
    def shortestDistance(self,startNodeID, finishNodeID):
        # Initialisation matrice distance
        data=np.ones((self.distance.shape[0],3))*-1
        self.distance.shape[1]
        myId=np.arange(0,self.distance.shape[0]).reshape(-1,1)
        data=np.concatenate((myId,data),axis=1)
        data[startNodeID,1]=0
        data[startNodeID,3]=1
        print(data)


        
        # Algorithme Djikstra
        selectID=startNodeID
        while data[finishNodeID,3] == -1:
            for floatNoeudsID in data[:,0]:
                noeudsID=int(floatNoeudsID)
                
                if self.distance[int(selectID),noeudsID] !=-1 : # If a path exists betwenn the selected node and another node, and if the node has never been selected
                    distance = self.distance[selectID,noeudsID]+ data[selectID,1]
                    if distance < data[noeudsID,1] or data[noeudsID,1] == -1:
                        data[selectID,1] = distance
                        data[selectID,2] = selectID 
                       # print(noeudsID)
            
            
            
            

            break
        print(data)



            
                

        

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
dji.shortestDistance(1,3)




#map=open("map.txt","r").read()
#print(map)


