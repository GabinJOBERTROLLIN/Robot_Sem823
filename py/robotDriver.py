
import pandas as pd
import numpy as np
from threading import Thread


from calculataPath import Djikstra
from QRCode import RecogniseQr
import Dico_BOT1.DicoBOT1 as UART
import importExcel



class BotMaster():

    def strToList(self,a):
    # INPUT  : String following a List format
    # OUTPUT : List version of the input String
    # GOAL : TRansform a String into a List

        if isinstance(a,str):
            noeuds = list(a.split(","))
            noeudsFormat=[]
            for noeud in noeuds:
                noeudsFormat.append(list(noeud.split(":")))
            return noeudsFormat
        else:
            print("Erreur : l'element "+str(a)+" nest pas un str")

    
    def excelToAdjacencyMatrix(self,link):
    # INPUT  : Link to the excel file
    # OUTPUT : Adjacency mathix, which is a matrix of weight to differents ondes in graph theory
    # GOAL : Translate the excel to an Adjacency Matrix
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

            #print(distance)
            return distance
    


    def traitementQrResult(self,l):
    # INPUT  : List containg QR code information on the folofing format [0;1:nord,6:sud,None:est,None:ouest,]
    # OUTPUT : Dictionnary containing the input information
    # GOAL : Turn the input data into usable data, in the following format : ['0', {'1': 'nord', '6': 'sud', 'None': 'ouest'}]

        data=[]
        s=l[0]
        ns = s[:-1]

        ns=ns.split(";") 
        dictionnary = dict((a, b)  
        for a, b in (element.split(':')  
            for element in ns[1].split(',')))  
        
        data.append(ns[0])
        data.append(dictionnary)
        print(data)
        return data
    

    def toggleDoiteGauche(self,Value):
    # INPUT  : String Value, containing 'G' or 'D'
    # OUTPUT : String Value, containing 'G' or 'D'
    # GOAL : Toggle between G and D
     
        if Value == 'G':
            retour ='D'
        else:
            retour = 'G'
        return retour
    


    def directionToAngle(self,start,direction):
    # INPUT  : Start and direction are Strings which can be ether nord/sud/est/ouest
    # OUTPUT : (char directionOfTurn, int numberOfTurn) a dictionnary using the previous format,
    #          where directionOfTurn is either G or D (Left and Right) and numberOfTurn, the number of 90° turn.
    # GOAL : From the starting orientation, and the aimed orientation, calculate the direction to turn, and the number of 90° turns

        dic = { ("nord","est"):'G',
                ("nord","ouest"):'D',
                ("nord","nord"):'R',

                ("ouest","sud"):'D',
                ("ouest","nord"):'G',
                ("ouest","ouest"):'R',

                ("sud","est"):'D',
                ("sud","ouest"):'G',
                ("sud","sud"):'R',

                ("est","sud"):'G',
                ("est","nord"):'D',
                ("est","est"):'R'
                
                }
        
        return dic.get((start,direction), '')

        
    def pilotage(self,startNode,endNode):
    # INPUT  : int ID of the starting and ending nodes.
    # OUTPUT : None
    # GOAL   : Calculate the fastest path between the starting and ending node and drive the robot from the start to the end
    #          by scanning QR code and sending information to the microcontroller using UART.

        BOT1 = UART.DicoBOT1('Dico_BOT1/capteurs.json')
        BOT2 = UART.DicoBOT1('Dico_BOT1/capteurs.json')
        #distance = self.excelToAdjacencyMatrix("py\map.xlsx")
        distance = importExcel.ImportExcel("map.xlsx").excelToAdjacencyMatrix()
        dji = Djikstra(distance)
        path = dji.actualisePath(startNode,endNode)
        msg_tosend = BOT1.addData('chemin',path)
        print(msg_tosend)
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
                    msg_tosend = BOT1.encodeDecode("direction",5)
                    directionAngle = self.directionToAngle(start,direction)
                    if directionAngle == "":
                        print("TOUT DROIT, NE TOURNE PAS")
                    else:
                        #Encodage d'un message pour émission dans l'UART :
                        msg_tosend = BOT1.encodeDecode(directionAngle[0])
                        BOT1.writeInstruction(directionAngle[0])
                        
                        print(msg_tosend)
                        #print("TOURNE DE 90 a " + directionAngle[0])
                else:
                    print("ROBOT ARRIVE A DESTINATION")
            else:
                print("LE ROBOT S'EST PERDU, IL FAUT FAIRE UN TRUC")
                break
            

            
        
        
#BotMaster().traitementQrResult(['0;1:nord,6:sud,None:est,None:ouest,'])    

BotMaster().pilotage(0,5)
#print(BotMaster().directionToAngle("nord","sud"))