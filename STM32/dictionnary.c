#include "dictionnary.h"
#include <string.h>
#include <stdio.h>

// Implémentations des fonctions de traitement

//Fonction de conversion d'un int sur un octet pour émission sur UART
unsigned char BOT1_convert_int(int id, int itoconv){
	int index = -1;
	for(int i=0;i<CMD_TABSIZE;i++){
		if(id == TAB_CMD[i].id){
			index = i;
			break;
		}
	}
	float delta = (float)253/(TAB_CMD[index].max_unit - TAB_CMD[index].min_unit);
	float val = (delta*itoconv)+1;
	unsigned char utf8_val = (unsigned char)val;
	return utf8_val;
}

//Fonction de conversion d'un float sur un octet pour émission sur UART
unsigned char BOT1_convert_float(int id, float ftoconv){
	int index = -1;
	for(int i=0;i<CMD_TABSIZE;i++){
		if(id == TAB_CMD[i].id){
			index = i;
			break;
		}
	}
	float delta = (float)253/(TAB_CMD[index].max_unit - TAB_CMD[index].min_unit);
	float val = (delta*ftoconv)+1;
	unsigned char utf8_val = (unsigned char)val;
	return utf8_val;
}

//Fonction de conversion d'un charactere sur un int pour traitement en interne
int BOT1_decodec_toint(int id, unsigned char c){
	int index = -1;
	for(int i=0;i<CMD_TABSIZE;i++){
		if(id == TAB_CMD[i].id){
			index = i;
			break;
		}
	}
	float delta = (float)(TAB_CMD[index].max_unit - TAB_CMD[index].min_unit)/253;
	
	int val = (c-1)*delta;

	return val;
}

//Fonction de conversion d'un charactere sur un float pour traitement en interne
float BOT1_decodec_tofloat(int id, unsigned char c){
	int index = -1;
	for(int i=0;i<CMD_TABSIZE;i++){
		if(id == TAB_CMD[i].id){
			index = i;
			break;
		}
	}
	float delta = (float)(TAB_CMD[index].max_unit - TAB_CMD[index].min_unit)/253;
	float val = (c-1)*delta;

	return val;
}

// Fonction d'encodage des données
// Renvoit le message à transmettre dans l'UART
int BOT1_encode(int id, int size_tab, unsigned char *tab, unsigned char *out){
    // Recuperation de l'index de la commande à utiliser dans la CMD
    int index = -1;
    for(int i=0;i<CMD_TABSIZE;i++){
        if(TAB_CMD[i].id == id){
            index = i;
        }
    }
    if(index == -1){
        return 1;
    }
    else{
        int size_msg = 2+TAB_CMD[index].content_size;
        if(size_msg-2 == size_tab){   
        	//Declaration du tableau
            unsigned char encoded_msg[size_msg];
            //Inscription de l'ID
		encoded_msg[0] = (unsigned char)TAB_CMD[index].id;
         	//Inscription des données de TAB si présentes	
            for(int i=0;i<size_tab;i++){
            	encoded_msg[i+1]=tab[i];
            }
		encoded_msg[size_msg-1]=(unsigned char)255;
		//ATTENTION NE RECOPIE PAS JUSQU'A 0 !!!!
            strcpy(out,encoded_msg);
            return 0;
        }
        else{
            return 1;
        }
    }
};

// Fonction de decodage d'un string encodé avec le dictionnaire,
// Il execute les fonctions
int BOT1_decode(unsigned char *msg_encoded, unsigned char *out){
    int index = -1;
    for(int i=0;i<CMD_TABSIZE;i++){
        if((int)msg_encoded[0] == TAB_CMD[i].id){
            index = i;
            break;
        }
    }
    if(index == -1){
        return 1;
    }
    if (msg_encoded[1] == 255){
        strcpy(out, TAB_CMD[index].cmd_serializer);
    }
    else{
        int id = TAB_CMD[index].id;
        switch (id) {
        case 128:
            //INSERT YOUR BEHAVIOR HERE
            break;
        case 129:
            //INSERT YOUR BEHAVIOR HERE
            break;
        default:
            return 2;
            break;
    }
    return 0;
    }
};