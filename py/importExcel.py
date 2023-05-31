import numpy as np
import pandas as pd

class ImportExcel():
    def __init__(self,link):
        self.link = link
        

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


        
    def excelToAdjacencyMatrix(self):
    # INPUT  : Link to the excel file
    # OUTPUT : Adjacency mathix, which is a matrix of weight to differents ondes in graph theory
    # GOAL : Translate the excel to an Adjacency Matrix
    
            data = pd.read_excel(self.link)
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
    

    def removeEnd(car):
        character =':'
        car = str(car)
        if character in car:
            return car.split(character)[0]
        else:
            return car
        
        

    def excelToVoisinage(self):
        data = pd.read_excel(self.link)
        #print(link)
        mapDataframe=pd.DataFrame(data, columns=["nord","sud","est","ouest"])
        mapDataframe["nord"] = mapDataframe["nord"].apply(self.removeEnd)
        mapDataframe["sud"] = mapDataframe["sud"].apply(self.removeEnd)
        mapDataframe["est"] = mapDataframe["est"].apply(self.removeEnd)
        mapDataframe["ouest"] = mapDataframe["ouest"].apply(self.removeEnd)
        
        
        return mapDataframe.to_dict('index')
    
obj = ImportExcel("map.xlsx")    
print(obj.excelToAdjacencyMatrix())