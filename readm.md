Lien du git : https://github.com/GabinJOBERTROLLIN/Robot_Sem823

# Partie matériel
## Matériel requis
2 Capteurs infrarouges grooves
1 Télémétre à ultrason HCSR04
1 Raspberry pi3
1 STM32F3DISCOVERY
1 Plateforme robot


## Branchements sur la STM32
PC0 >> capteur ir gauche
PC1 >> capteur ir droit

A connecter au raspberry, on oublie pas de croiser RX/TX
PC10 >> UART4 TX
PC11 >> UART4 RX

A connecter au serializer, on oublie pas de croiser RX/TX
PC12 >> UART5 TX
PD2 >> UART5 RX

PA0 >> TRIG ultrason
PC5 >> ECHO ultrason

## Description du logiciel embarqué
La variable DIST_SECU permet de regler la distance en cm à partir de laquelle il s'arrete. Elle est réglée de base à 50cm.
En vous balandant dans le code, il est possible de changer les vitesses de rotation et en translation, elles sont déclarés en dure au début du code.

# Partie logiciel
## Mise en place de la raspberry

## Algorithme de plus court chemin
Pur tester l'algorithme de chemin automatique utilisant la lecture de QR codes, vous pouvez lancer le fichier **robotDriver.py**, il faut ensuite montrer à la caméra les QR codes dans l'ordre décrit par le chemin. Ces QR codes se trouvent dans le fichier **QRcode>QRcodes**, vous pouvez aussi les trouver dans le fichier pdf **QRcodes** fournis dans le même dossier.   