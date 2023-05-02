import serial
import time

#linux
port_uart = "/dev/serial0"
path = "/var/www/html/instruction.txt"
baudrate = 19200


bytesize = 8


uart = serial.Serial(port_uart,baudrate,bytesize)
uart.timeout = 0.1



def receive():
    # Récupération de caracètres
    msg = uart.read(100).decode()
    if msg != '':
            print("(reception) < " + str(msg))
    return msg

def send(c):
    # Ecriture de caractères
    print("            > "+str(c))
    uart.write(c.encode('utf-8'))


while 1:
    # lecture des instructions
    f=open(path,'r')
    instruction=f.read()
    f.close()

    # on envoie l'instruction
    send(instruction)
    
    # on recoit les informations
    receive()

uart.close()