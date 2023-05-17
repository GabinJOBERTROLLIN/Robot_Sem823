import qrcode
import pandas as pd
import importExcel

def strToList(a):
    if isinstance(a,str):
        noeuds = list(a.split(","))
        noeudsFormat=[]
        for noeud in noeuds:
            noeudsFormat.append(list(noeud.split(":")))
        return noeudsFormat
    else:
        print("Erreur : l'element "+str(a)+" nest pas un str")

def removeEnd(car):
    character =':'
    car = str(car)
    if character in car:
        return car.split(character)[0]
    else:
        return car
    
    
def excelToVoisinage(link):
    data = pd.read_excel(link)
    #print(link)
    mapDataframe=pd.DataFrame(data, columns=["nord","sud","est","ouest"])
    mapDataframe["nord"] = mapDataframe["nord"].apply(removeEnd)
    mapDataframe["sud"] = mapDataframe["sud"].apply(removeEnd)
    mapDataframe["est"] = mapDataframe["est"].apply(removeEnd)
    mapDataframe["ouest"] = mapDataframe["ouest"].apply(removeEnd)
    
    
    return mapDataframe.to_dict('index')

    # mapDataframe.loc[:,"nord"] = mapDataframe.loc[:,"nord"].apply(strToList,1)
    # mapDataframe.loc[:,"sud"] = mapDataframe.loc[:,"sud"].apply(strToList,1)
    # mapDataframe.loc[:,"est"] = mapDataframe.loc[:,"est"].apply(strToList,1)
    # mapDataframe.loc[:,"ouest"] = mapDataframe.loc[:,"ouest"].apply(strToList,1)
    #print(mapDataframe.loc[:,"ouest"][1][0][1])

    
    #print(mapDataframe)
    

def generate():
    # Créer une liste de 9 numéros de 0 à 8
    numeros = list(range(9))

    # Créer un dictionnaire avec les directions du voisinage de 4 pour chaque numéro
    voisinage = importExcel.ImportExcel("py\map.xlsx").excelToVoisinage()
    #voisinage = excelToVoisinage("py\map.xlsx")
    #print(voisinage)

    # Parcourir les numéros et générer les codes QR correspondants
    for numero in numeros:
        # Créer les données pour le code QR
        data = str(numero) + ";"
        for direction, voisin in voisinage[numero].items():
            data += f"{voisin}:{direction},"
        data = data 
        # Générer le code QR avec les données
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        # Enregistrer le code QR dans un fichier PNG avec le nom correspondant au numéro
        qr.make_image(fill_color="black", back_color="white").save(f"py\QRCode\QRCodes\{numero}.png")
generate()