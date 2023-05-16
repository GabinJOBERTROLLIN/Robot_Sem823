#ifndef _DICTIONNARY_H
#define _DICTIONNARY_H

// Definition du format des clés
struct command_key {
    int max_unit;
    int min_unit;
    int id;
    int content_size;  
    char decription[20];
    char param[20];
    char cmd_serializer[30];
    char unit[5];
    char param[10];
    char cmd[5][10];
};
typedef struct command_key command_key;

// CONSTANT STRUCT ARRAY HERE
const int CMD_TABSIZE = 13;
const command_key TAB_CMD[13] = {
	{0,0,0,0,"Arret d'urgence","","stop
","","",{"p","stop"}},
	{1,0,0,0,"Avancer","","mogo 1:100 2:100
","","",{"z"}},
	{2,0,0,0,"Reculer","","mogo 1:-100 2:-100
","","",{"s"}},
	{3,0,0,1,"Tourner à droite","","mogo 1:100 2:-100
","","",{"d"}},
	{4,0,0,0,"Tourner à gauche","","mogo 1:-100 2:100
","","",{"q"}},
	{5,0,0,1,"Avancer avec vitesse","vitesse","mogo 1:%speed 2:%speed
","","vitesse",{"avancer"}},
	{6,0,0,0,"Tourner 90° a droite","","??? 
","","",{"D"}},
	{6,0,0,0,"Tourner 90° a gauche","","??? 
","","",{"G"}},
	{6,0,0,0,"Demi-Tour","","??? 
","","",{"R"}},
	{128,0,0,1,"Capteur ultrason","","","cm","",{"ultrason"}},
	{129,0,0,1,"Capteur consommation","","","W","",{"rshunt"}},
	{201,0,0,1,"Chemin complet que le robot doit effectuer","","","","",{"chemin"}},
	{202,0,0,1,"Chemin complet que le robot doit effectuer","","","","",{"direction"}}
};

// Prototypes des fonction
float BOT1_decodec_tofloat(int , unsigned char );
int BOT1_decodec_toint(int , unsigned char );
unsigned char BOT1_convert_float(int , float );
unsigned char BOT1_convert_int(int , int );

int BOT1_encode(int, int , unsigned char*, unsigned char*);
int BOT1_decode(unsigned char *, unsigned char *);


#endif