import cv2
from pyzbar import pyzbar




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





