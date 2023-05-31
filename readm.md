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

A connecter au raspberry, on oublie pas de croiser RX/TX (UART4)
PC10 >> UART4 TX
PC11 >> UART4 RX

A connecter au serializer, on oublie pas de croiser RX/TX (UART5)
PC12 >> UART5 TX
PD2 >> UART5 RX

PA0 >> TRIG ultrason
PC5 >> ECHO ultrason

## Description du logiciel embarqué
Vous trouverez dans les sources "src_PTC_STM32.zip" l'ensemble du programme qui tourne sur la STM32.
Si vous rencontrez un probleme sur l'execution des données sur l'UART, verifier que l'UART 5 est bien en drai ouvert.

Dans le main vous pourrez retrouver l'implémentation de l'algorithme de suivi de ligne ainsi que la façon dont les commandes sont envoyés à la carte serializer.
Des interruptions permettent de calculer la distance séparant le robot et un obstacle situé devant lui.

## Encodage de la liaison UART
Cette partie n'est pas implémentée dans l'intégration du projet. Néanmoins on peut retrouver le code produit dans la section py/Dico_BOT1. Il fournit des fonctions qui interpretent une liste de commandes (dictionnary.json). A haut niveau on peut donc associer une commande au format chaine de caractère intuitive "stop", "avancer" ... et la code pour l'émission en direction de la STM32.

Le fichier JSON n'est pas directement interprétable sur la STM32 ainsi on réalise une conversion du dictionnaire en une liste d'un struct que nous avons developpé. Le fichier permettant la conversion est le script "file_convert.py". Il génére alors dynamiquement à l'aide des h_header_bottom/h_header_top cette fameuse liste de commande dans "dictionnary.h". Les implémentations des fonctions sont dans "dictionnary.c".

## Branchements sur la Raspberry

brancher les pins de l'uart à la stm32

GPIO 14 >> UART TX
GPIO 15 >> UART RX

(voir les branchements sur https://www.etechnophiles.com/raspberry-pi-3-b-pinout-with-gpio-functions-schematic-and-specs-in-detail/)

brancher une caméra à un port usb

# Partie logiciel
## Structure des fichiers importants sur la raspberry


	-> /var/www/

		-> /var/www/py/
			-> transmission.py
			-> robotDriver.py
			-> mode.txt
			
			-> /var/www/py/QRcode/
				-> /var/www/py/QRcode/QRcodes/
					-> tous les QR codes utiles

		-> /var/www/html/
			-> index.php
			-> style3.css
			-> Scripts.php

			-> instruction.txt
			-> log.txt
			-> capteurs.json

## Gestion de l'UART Raspberry STM32

*/var/www/py/transmission.py* -> gestion de l'uart raspberry - stm32

se lance automatiquement au lancement du raspberry.
relancer la commande `python /var/www/py/transmission.py` pour afficher les codes

## Algorithme de plus court chemin

*/var/www/py/robotDriver.py* -> mode automatique

ne se lance pas automatiquement, exécuter `python /var/www/py/robotDriver.py`
utilise la caméra branchée au raspberry
	
Pour tester l'algorithme de chemin automatique utilisant la lecture de QR codes, vous pouvez lancer le fichier **robotDriver.py**, il faut ensuite montrer à la caméra les QR codes dans l'ordre décrit par le chemin. Ces QR codes se trouvent dans le fichier **QRcode>QRcodes**, vous pouvez aussi les trouver dans le fichier pdf **QRcodes** fournis dans le même dossier.

>>>>>>> e22cddda67b784e1e3ef4c57258998555b8504d8
