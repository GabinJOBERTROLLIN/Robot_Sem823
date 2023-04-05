#====== Projet Robot Sem823 : Transmission ======
#
# - Nom : essais du sérial
#
# - Protocole : UART Rx/Tx sans fioritures
# - Idle state : '1'
# - Baudrate : 9600/115200 Hz
# - Trame : <START_bit = '0'><DATA[7:0]><NO_parity><STOP_bit = '0'>
#
# >> Objectif : Transmission de la rasberryPi au Microcontrolleur
#==============================================


# Importation de la librairie Pyserial : https://pythonhosted.org/pyserial/ 
import serial 
import time

port_rd = "/dev/ttyAMA0"
port_wr = "/dev/ttyS0"
baudrate = 115200
bytesize = 8

def receive():

    # Ouverture de la liaison UART
    uart = serial.Serial(port_rd, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts

    # Récupération de caracètres
    print(uart.read(1))

    uart.close()


def send(c):

    # Ouverture de la liaison UART
    uart = serial.Serial(port_wr, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts

    # Ecriture d'un caractère de test 'a'
    print("Envoi : [PC : Tx >> Rx FPGA] "+str(c))
    uart.write(c.encode('utf-8'))

    uart.close()


while 1:
	# sleep
	time.sleep(0.1)
	
	# lecture des instructions
	f=open("/var/www/html/instruction.txt")
	instruction=f.read()
	f.close()

	# on envoie l'instruction
	send(instruction)

