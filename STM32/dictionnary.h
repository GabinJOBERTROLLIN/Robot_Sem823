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
	{1,0,0,0,"Arret d'urgence","","stop\r","",{"p","stop"}},
	{2,0,0,0,"Avancer","","mogo 1:100 2:100\r","",{"z"}},
	{3,0,0,0,"Reculer","","mogo 1:-100 2:-100\r","",{"s"}},
	{4,0,0,1,"Tourner à droite","","mogo 1:100 2:-100\r","",{"d"}},
	{5,0,0,0,"Tourner à gauche","","mogo 1:-100 2:100\r","",{"q"}},
	{6,0,0,1,"Avancer avec vitesse","vitesse","mogo 1:%speed 2:%speed\r","",{"avancer"}},
	{7,0,0,0,"Tourner 90° a droite","","??? \r","",{"D"}},
	{8,0,0,0,"Tourner 90° a gauche","","??? \r","",{"G"}},
	{9,0,0,0,"Demi-Tour","","??? \r","",{"R"}},
	{128,400,5,1,"Capteur ultrason","","","cm",{"ultrason"}},
	{129,10,0,1,"Capteur consommation","","","W",{"rshunt"}},
	{201,100,0,1,"Chemin complet que le robot doit effectuer","","","",{"chemin"}},
	{202,0,0,1,"Chemin complet que le robot doit effectuer","","","",{"direction"}}
};

// Prototypes des fonction
float BOT1_decodec_tofloat(int , unsigned char );
int BOT1_decodec_toint(int , unsigned char );
unsigned char BOT1_convert_float(int , float );
unsigned char BOT1_convert_int(int , int );

int BOT1_encode(int, int , unsigned char*, unsigned char*);
int BOT1_decode(unsigned char *, unsigned char *);


#endif