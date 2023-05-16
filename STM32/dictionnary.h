#ifndef _DICTIONNARY_H
#define _DICTIONNARY_H

// Definition du format des clés
struct command_key {
    int id;
    int max_unit;
    int min_unit;
    int content_size;  
    char decription[30];
    char param[20];
    char cmd_serializer[30];
    char unit[5];
    char cmd[5][10];
};
typedef struct command_key command_key;

// CONSTANT STRUCT ARRAY HERE
const int CMD_TABSIZE = 9;
const command_key TAB_CMD[9] = {
	{1,0,0,0,"Arret d'urgence","","stop \r","","",{"p","stop"}},
	{2,0,0,0,"Avancer","","mogo 1:100 2:100\r","","",{"z"}},
	{3,0,0,0,"Reculer","","mogo 1:-100 2:-100\r","","",{"s"}},
	{4,0,0,1,"Tourner à droite","","mogo 1:100 2:-100\r","","",{"d"}},
	{5,0,0,0,"Tournedededexdxdxdxddedededer à gauche","","mogo 1:-100 2:100\r","","",{"q"}},
	{6,0,0,1,"Avancer avec vitesse","vitesse","mogo 1:%speed 2:%speed\r","","vitesse",{"avancer"}},
	{7,0,0,0,"Tourner avec angle","angle","??? \r","","angle",{"tourner"}},
	{128,0,0,1,"Capteur ultrason","","","cm","",{"ultrason"}},
	{129,0,0,1,"Capteur consommation","","","W","",{"rshunt"}}
};

// Prototypes des fonction
int BOT1_encode(int, int , unsigned char*, unsigned char*);

int BOT1_decode(unsigned char *, unsigned char *);


#endif