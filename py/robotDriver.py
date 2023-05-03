
import pandas as pd
import numpy as np
from threading import Thread

from calculataPath import Djikstra
from QRCode import RecogniseQr
import Dico_BOT1.DicoBOT1 as UART




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
            #print(link)
            mapDataframe=pd.DataFrame(data, columns=["x","y","nord","sud","est","ouest"])
            #print(mapDataframe)
            mapDataframe.loc[:,"nord"] = mapDataframe.loc[:,"nord"].apply(self.strToList,1)
            mapDataframe.loc[:,"sud"] = mapDataframe.loc[:,"sud"].apply(self.strToList,1)
            mapDataframe.loc[:,"est"] = mapDataframe.loc[:,"est"].apply(self.strToList,1)
            mapDataframe.loc[:,"ouest"] = mapDataframe.loc[:,"ouest"].apply(self.strToList,1)
            #print(mapDataframe)

            nbrRow=mapDataframe.shape[0]
            distance =np.array([[-1 for j in range(nbrRow)] for i in range(nbrRow)])
            for idStart in range(nbrRow):
                distance[idStart,idStart] = 0
                for direction in ["nord","sud","est","ouest"]:
                    if distance[idStart,int(mapDataframe.loc[idStart][direction][0][0])] == -1:
                        distance[idStart,int(mapDataframe.loc[idStart][direction][0][0])] = int(mapDataframe.loc[idStart][direction][0][1])
                    else:
                        distance[idStart,int(mapDataframe.loc[idStart][direction][0][0])] += int(mapDataframe.loc[idStart][direction][0][1]) # + int(distance[idStart,int(mapDataframe.loc[idStart][direction][0][0])]) 

            print(distance)
            return distance
    
    def traitementQrResult(self,l):
        data=[]
        s=l[0]
        ns = s[:-1]

        ns=ns.split(";") 
        dictionnary = dict((a, b)  
        for a, b in (element.split(':')  
            for element in ns[1].split(',')))  
        
        data.append(ns[0])
        data.append(dictionnary)
        return data
    
    def toggleDoiteGauche(self,Value):
        if Value == 'G':
            retour ='D'
        else:
            retour = 'G'
        return retour
    
    def directionToAngle(self,start,direction):
        dic = { ("nord","est"):('G',1),
                ("nord","ouest"):('D',1),
                ("nord","nord"):('G',2),

                ("ouest","sud"):('D',1),
                ("ouest","nord"):('G',1),
                ("ouest","ouest"):('G',2),

                ("sud","est"):('D',1),
                ("sud","ouest"):('G',1),
                ("sud","sud"):('G',2),

                ("est","sud"):('G',1),
                ("est","nord"):('D',1),
                ("est","est"):('G',2)
                
                }
        
        return dic.get((start,direction), ('',0))

        
    def pilotage(self):
        BOT1 = UART.DicoBOT1('py\Dico_BOT1\dictionnary.json')
        print("test1")
        distance = self.excelToDistanceMatrix("py\map.xlsx")
        print("test2")
        dji=Djikstra(distance)
        path = dji.actualisePath(0,5)
        print(path)
        
        for nodeListID in range(len(path)):
            resultQR = []
            thread = Thread(target = RecogniseQr.Recognize, args = (resultQR,))
            thread2 = Thread(target = print, args = ("SUIVRE LES LIGNES"))
            thread.start()
            thread2.start()
            thread.join()
            thread2.join()

            print("ROBOT SUR LE QR CODE " + str(path[nodeListID]))
            print("ARRETE DE SUIVRE LES LIGNES")
            
            QRData = self.traitementQrResult(resultQR)
            if QRData[0] == path[nodeListID] :
                
                if path[nodeListID] !=len(path):

                    if nodeListID == 0:
                        start="sud"
                        direction = QRData[1][path[nodeListID+1]]
                    elif nodeListID == len(path):
                        start = QRData[1][path[nodeListID-1]]
                        direction = QRData[1][path[nodeListID+1]]
                        
                    else:
                        start = QRData[1][path[nodeListID-1]]
                        direction = direction
                    
                    directionAngle = self.directionToAngle(start,direction)
                    if directionAngle ==("",0):
                        print("TOUT DROIT, NE TOURNE PAS")
                    for i in range(directionAngle[1]):
                        #Encodage d'un message pour émission dans l'UART :
                        msg_tosend = BOT1.encode(directionAngle[0])
                        print(msg_tosend)
                        print("TOURNE DE 90 a " + directionAngle[0])
                else:
                    print("ROBOT ARRIVE A DESTINATION")
            else:
                print("LE ROBOT S'EST PERDU, IL FAUT FAIRE UN TRUC")
                break
            

            
        
        
#BotMaster().traitementQrResult(['0;1:nord,6:sud,None:est,None:ouest,'])    

BotMaster().pilotage()
#print(BotMaster().directionToAngle("nord","sud"))