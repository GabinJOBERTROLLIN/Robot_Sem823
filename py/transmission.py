import serial
import time

#linux
port_uart = "/dev/serial0"
path = "/var/www/html/instruction.txt"
baudrate = 19200

# windows tests
# port_uart = "COM2"
# path_wr = "vitesse.txt"
# path = "instruction.txt"
# baudrate = 9600


bytesize = 8


def receive():

    # Ouverture de la liaison UART
    # uart = serial.Serial(port_uart, baudrate, bytesize)
    # uart.timeout = 0.1

    # Récupération de caracètres
    msg = uart.read(100).decode()
    if (msg != ''):
            print("[... -> RASP] << " + str(msg))

    # uart.close()

    return msg

def send(c):

    # Ouverture de la liaison UART
    # uart = serial.Serial(port_uart, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts

    # Ecriture d'un caractère de test 'a'
    print("[RASP -> ...] >> "+str(c))
    uart.write(c.encode('utf-8'))

    # uart.close()

uart = serial.Serial(port_uart,baudrate,bytesize)
uart.timeout = 0.1

while 1:
    # sleep
    # time.sleep(0.1)

    # lecture des instructions
    f=open(path,'r')
    instruction=f.read()
    f.close()

    # on envoie l'instruction
    send(instruction)

    # on recoit les informations
    receive()

uart.close()