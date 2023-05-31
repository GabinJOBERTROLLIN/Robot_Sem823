import cv2
from pyzbar import pyzbar
import qrcode
import pandas as pd
import importExcel



def Recognize(result):
    data = ""

    # initialize the camera
    cap = cv2.VideoCapture(0)
    
    while data == "":
        
        
        # capture a frame from the camera
        ret, frame = cap.read()

        # convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # find the QR codes in the frame
        qr_codes = pyzbar.decode(gray)

        # loop through the detected QR codes
        for qr_code in qr_codes:
            # extract the data from the QR code 
            data = qr_code.data.decode('utf-8')
            # print the instruction to the terminal
            print("Qr code detected :", data)


        # display the frame
        cv2.imshow('frame', frame)

        # wait for a key press
        key = cv2.waitKey(1)

        # if the 'q' key is pressed, exit the loop
        if key == ord('q'):
            break

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    result.append(data)


def generate():
    # Créer une liste de 9 numéros de 0 à 8
    numeros = list(range(9))

    # Créer un dictionnaire avec les directions du voisinage de 4 pour chaque numéro
    voisinage = importExcel.ImportExcel("py\map.xlsx").excelToVoisinage()
    #voisinage = excelToVoisinage("py\map.xlsx")
    #print(voisinage)

    # Parcourir les numéros et générer les codes QR correspondants
    for numero in numeros:
        # Créer les données pour le code QR
        data = str(numero) + ";"
        for direction, voisin in voisinage[numero].items():
            data += f"{voisin}:{direction},"
        data = data 
        # Générer le code QR avec les données
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
            
        # Enregistrer le code QR dans un fichier PNG avec le nom correspondant au numéro
        qr.make_image(fill_color="black", back_color="white").save(f"py\QRCode\QRCodes\{numero}.png")





