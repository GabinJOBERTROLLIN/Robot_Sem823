
import pandas as pd
import numpy as np
from threading import Thread

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
        data = pd.read_excel(link)
        mapDataframe=pd.DataFrame(data, columns=["x","y","liens"])
        mapDataframe.loc[:,"liens"] = mapDataframe.loc[:,"liens"].apply(self.strToList,1)

        nbrRow=mapDataframe.shape[0]
        distance =np.array([[-1 for j in range(nbrRow)] for i in range(nbrRow)])
        for idStart in range(nbrRow):
            distance[idStart,idStart] = 0
            for noeudCible  in mapDataframe.loc[idStart]["liens"]:

                distance[idStart,int(noeudCible[0])] = noeudCible[1]
        return distance
    
    def traitementQrResult(self,l):
        data=[]
        s=l[0]
        ns = s[:-2]
        ns=ns.split(";")
       
        dictionnary = dict((a, b)  
        for a, b in (element.split(':')  
            for element in ns[1].split(',')))  
        
        data.append(ns[0])
        data.append(dictionnary)
        print(dictionnary)
        return data
    def directionToAngle(direction):
        
        
    def pilotage(self):
        distance = self.excelToDistanceMatrix("py\map.xlsx")
        dji=Djikstra(distance)
        path = dji.actualisePath(0,5)
        
        for nodeListID in range(len(path)):
            resultQR = []
            thread = Thread(target = RecogniseQr.Recognize, args = (resultQR,))
            thread2 = Thread(target = print, args = ("SUIVRE LES LIGNES"))
            thread.start()
            thread2.start()
            thread.join()
            thread2.join()
            print("ARRETE DE SUIVRE LES LIGNES")
            
            QRData = self.traitementQrResult(resultQR)
            if QRData[0] == path[nodeListID] :
                if path[nodeListID] !=len(path):
                    nextQR = path[nodeListID + 1]
                    print("voici")
                    # direction = QRData[1][nextQR]
                    print("TOURNE DE")
                else:
                    print("ROBOT ARRIVE A DESTINATION")
            else:
                print("LE ROBOT S'EST PERDU, IL FAUT FAIRE UN TRUC")
            print(resultQR)

            
        
        
#BotMaster().traitementQrResult("1;"+"{nord:None,sud:4,est:2,ouest:0,}")    

BotMaster().pilotage()