import json
#==============================================
#  Fonctions d'ajout pour la creation du dico
#==============================================
#  
#
header_top = "./STM32/h_header_top.txt"
#----------------------------------------------
header_bot = "./STM32/h_header_bottom.txt"
#----------------------------------------------
json_file = "./py/Dico_BOT1/dictionnary.json"
#----------------------------------------------
c_file = "./STM32/dictionnary.h"
#----------------------------------------------

def add_inttoc(i):
    if type(i) == int :
        valren = str(i)
    else:
        valren = str(0)
    return valren

def add_strtoc(s):
    valren = '"'
    valren += s
    valren += '"'
    return valren

def add_tabtoc(tab):
    valren = '{'
    for i,s in enumerate(tab):
        valren += '"'+ s+ '"'
        if i < len(tab)-1:
            valren += ','
        else :
            valren += "}"
    return valren


#==============================================
#  Lecture de l'entete du fichier .h
#==============================================

with open(header_top, 'r') as file:
    header_for_h_top = file.read()

#==============================================
#  Lecture du dictionnaire .json
#==============================================
#Lecture du dictionnaire sous la forme :
# struct command_key {
#   int id;
#   int max_unit; 
#   int min_unit;
#   char descrption[30]; 
#   char param[20]
#   char cmd_serializer[20];
#   char unit[5];
#   char cmd[5][10];    
# };
# typedef struct command_key command_key;
#----------------------------------------------

with open(json_file, 'r') as file:
    json_dict = json.load(file)




i = 0
n_cmd = len(json_dict["embedded_cmd"])
cmd_for_c = "const int CMD_TABSIZE = "+str(n_cmd)+";\n"
cmd_for_c += "const command_key TAB_CMD[" + str(n_cmd)+ "] = {\n\t"
for cmd_list in json_dict["embedded_cmd"]:
    cmd_for_c += "{"
    cmd_for_c += add_inttoc(cmd_list["id"])
    cmd_for_c += ","
    cmd_for_c += add_inttoc(cmd_list["max_unit"])
    cmd_for_c += ","
    cmd_for_c += add_inttoc(cmd_list["min_unit"])
    cmd_for_c += ","
    cmd_for_c += add_inttoc(cmd_list["content_size"])
    cmd_for_c += ","
    cmd_for_c += add_strtoc(cmd_list["description"])
    cmd_for_c += ","
    cmd_for_c += add_strtoc(cmd_list["param"])
    cmd_for_c += ","
    cmd_for_c += add_strtoc(cmd_list["cmd_serializer"])
    cmd_for_c += ","
    cmd_for_c += add_strtoc(cmd_list["unit"])
    cmd_for_c += ","
    cmd_for_c += add_strtoc(cmd_list["param"])
    cmd_for_c += ","
    cmd_for_c += add_tabtoc(cmd_list["cmd"])
    cmd_for_c += "}"
    if i < n_cmd-1:
        cmd_for_c += ",\n\t"
        
    else:
        cmd_for_c += "\n};"
    i += 1

#==============================================
#  Lecture de la fin de l'entete du fichier .h
#==============================================
with open(header_bot, 'r') as file:
    header_for_h_bot = file.read()

#==============================================
#  Ecriture dans le fichier .c
#==============================================

with open(c_file, 'w') as file:
    file.write(header_for_h_top + cmd_for_c + header_for_h_bot)
