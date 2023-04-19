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


port_uart = "/dev/ttyS0"
port_uart = "/dev/serial0"
baudrate = 115200
bytesize = 8


def receive():

	# Ouverture de la liaison UART
	uart = serial.Serial(port_uart, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts
	uart.timeout = 0.1

	# Récupération de caracètres
	msg = uart.read(100).decode()
	if (msg != ''):
		print("[... -> RASP] << " + str(msg))

	uart.close()

	return msg


def send(c):

	# Ouverture de la liaison UART
	uart = serial.Serial(port_uart, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts

	# Ecriture d'un caractère de test 'a'
	print("[RASP -> ...] >> "+str(c))
	uart.write(c.encode('utf-8'))

	uart.close()


while 1:
	# sleep
	# time.sleep(0.1)
	
	# lecture des instructions
	f=open("/var/www/html/instruction.txt")
	instruction=f.read()
	f.close()

	# on envoie l'instruction
	send(instruction)
	
	# on recoit les informations
	receive()
