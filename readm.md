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

# Partie logiciel
## Mise en place de la raspberry

## Encodage de la liaison UART
Cette partie n'est pas implémentée dans l'intégration du projet. Néanmoins on peut retrouver le code produit dans la section py/Dico_BOT1. Il fournit des fonctions qui interpretent une liste de commandes (dictionnary.json). A haut niveau on peut donc associer une commande au format chaine de caractère intuitive "stop", "avancer" ... et la code pour l'émission en direction de la STM32.

Le fichier JSON n'est pas directement interprétable sur la STM32 ainsi on réalise une conversion du dictionnaire en une liste d'un struct que nous avons developpé. Le fichier permettant la conversion est le script "file_convert.py". Il génére alors dynamiquement à l'aide des h_header_bottom/h_header_top cette fameuse liste de commande dans "dictionnary.h". Les implémentations des fonctions sont dans "dictionnary.c".