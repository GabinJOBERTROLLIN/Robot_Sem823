import json

class DicoBOT1():
    def __init__(self, file):
        self.file = file
        # Lecture du dictionnaire
        with open(file, 'r') as f:
            self.json_dict = json.load(f)
        self.end_char = chr(255)
        
        self.json_path = "Dico_BOT1/dictionnary.json"
        self.instructionPath = "/var/www/html/instruction.txt"


    def print(self):
        for k in self.json_dict:
            print(k,self.json_dict[k])
            print(type(k),type(self.json_dict[k]))
            for i,v in enumerate(self.json_dict[k]):
                print(v,type(v))

    def encode(self, cmd, val=0):
    #Préparation d'une commande pour l'émission par UART
    #La commande fournit correspond au "cmd" du json
        #Extraction de la clé de la commande
        key = ''
        for k in self.json_dict["embedded_cmd"]:
            if cmd in k["cmd"]:
                key = k
                break
        #Formatage de la commande : modèle [cmd id][content][cara de fin]
        str_tosend = chr(key["id"])
        if key["content_size"] > 0:
            str_tosend += chr(val)
        str_tosend += self.end_char
        return str_tosend
    
    def addData(self,key,data):
    #add data to json (not ready to be sent by UART)
        with open(self.file,'r') as outfile:
            content = json.load(outfile)
        content[key]=data

        with open(self.file,'w') as outfile:   
            json.dump(str(content),outfile)
            print("voici le content" +str(content))

    def writeInstruction(self,data):
        with open(self.instructionPath,'w') as outfile:   
            json.dump(data,outfile)
            print("voici le content" +str(data))


    def encodeDecode(self,cmd,val=0):
    #encode and decode
        ret = self.encode(cmd,val)
        print(ret)
        return self.decode(ret)
    

    def decode(self, data_chain):
    #Lecture d'un stream de données issues de l'UART et écriture dans un fichier capteurs.json
    #On part du principe pour le moment que les commandes sont envoyés une à une
        #Determinaison de la commande reçu
        cmd_id = ord(data_chain[0])
        #Extraction de la clé de la commande
        for k in self.json_dict["embedded_cmd"]:
            if cmd_id == k["id"]:
                key = k
                break
        #Decodage du message
        if key["content_size"] > 0:
            raw_val = ord(data_chain[1])
            conv_steps = (int(key["max_unit"])-int(key["min_unit"]))/(256**int(key["content_size"])-1)
            decoded_entry = {key["cmd"][0] : round(raw_val*conv_steps,3)}
            #Ouverture du fichier json
            with open(self.json_path,'r') as outfile:
                content = json.load(outfile)
            #Actualisation des nouvelles entrées
            for k in decoded_entry:
                content[k] = decoded_entry[k]
            #Renvoit sous json
            with open(self.json_path,'w') as outfile:
                json.dump(content, outfile)
        else:
            decoded_entry = {key["cmd"][0]:None}
            with open(self.json_path,'r') as outfile:
                content = json.load(outfile)
            #Actualisation des nouvelles entrées
            for k in decoded_entry:
                content[k] = decoded_entry[k]
            #Renvoit sous json
            with open(self.json_path,'w') as outfile:
                json.dump(content, outfile)
        return decoded_entry
    
    def test():
        #Exemple de fonctionnement
        BOT1 = DicoBOT1('Dico_BOT1\dictionnary.json')

        #Encodage d'un message pour émission dans l'UART :
        msg_tosend = BOT1.encode('ultrason',120)
        print("tosend"+str(msg_tosend))
        #Decodage du message pour traitement dans l'UART :
        msg_received = BOT1.decode(msg_tosend)
        print(msg_received)

        #Avec une commande quelconque :
        msg_tosend = BOT1.encode('stop')
        print(msg_tosend)
        #Decodage du message pour traitement dans l'UART :
        msg_received = BOT1.decode(msg_tosend)
        print(msg_received)
DicoBOT1.test()