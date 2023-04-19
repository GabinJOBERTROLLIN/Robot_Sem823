
import pandas as pd
import numpy as np

from calculataPath import Djikstra
import RecogniseQr



#print(distance)





class BotMaster():

    def strToList(self,a):

        if isinstance(a,str):
            noeuds = list(a.split(","))
            noeudsFormat=[]
            for noeud in noeuds:
                noeudsFormat.append(list(noeud.split(":")))
            return noeudsFormat
        else:
            print("Erreur : l'element "+str(a)+" nest pas un str")


    def excelToDistanceMatrix(self,link):
        data =pd.read_excel(link)
        mapDataframe=pd.DataFrame(data, columns=["x","y","liens"])
        mapDataframe.loc[:,"liens"] = mapDataframe.loc[:,"liens"].apply(self.strToList,1)

        nbrRow=mapDataframe.shape[0]
        distance =np.array([[-1 for j in range(nbrRow)] for i in range(nbrRow)])
        for idStart in range(nbrRow):
            distance[idStart,idStart] = 0
            for noeudCible  in mapDataframe.loc[idStart]["liens"]:

                distance[idStart,int(noeudCible[0])] = noeudCible[1]
        return distance


    def pilotage(self):
        distance = self.excelToDistanceMatrix("map.xlsx")
        dji=Djikstra(distance)
        dji.actualisePath(0,5)

BotMaster().pilotage()