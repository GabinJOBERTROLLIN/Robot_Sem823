import qrcode

# Créer une liste de 9 numéros de 0 à 8
numeros = list(range(9))

# Créer un dictionnaire avec les directions du voisinage de 4 pour chaque numéro
voisinage = {
    0: {"nord": None, "sud": 3, "est": 1, "ouest": None},
    1: {"nord": None, "sud": 4, "est": 2, "ouest": 0},
    2: {"nord": None, "sud": 5, "est": None, "ouest": 1},
    3: {"nord": 0, "sud": 6, "est": 4, "ouest": None},
    4: {"nord": 1, "sud": 7, "est": 5, "ouest": 3},
    5: {"nord": 2, "sud": 8, "est": None, "ouest": 4},
    6: {"nord": 3, "sud": None, "est": 7, "ouest": None},
    7: {"nord": 4, "sud": None, "est": 8, "ouest": 6},
    8: {"nord": 5, "sud": None, "est": None, "ouest": 7}
}

# Parcourir les numéros et générer les codes QR correspondants
for numero in numeros:
    # Créer les données pour le code QR
    data = str(numero) + " : "
    for direction, voisin in voisinage[numero].items():
        if voisin is not None:
            data += f"{direction} : {voisin}, "
    
    # Générer le code QR avec les données
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Enregistrer le code QR dans un fichier PNG avec le nom correspondant au numéro
    qr.make_image(fill_color="black", back_color="white").save(f"{numero}.png")
