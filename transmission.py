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



def receive():

    # Déclaration des variables utiles pour la com UART
    port = 'COM4' #PS>> py -3 -m serial.tools.list_ports, liste des ports utilisables
    baudrate = 9600
    bytesize = 8

    # Ouverture de la liaison UART
    uart = serial.Serial(port, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts
    uart.open()

    # Récupération de caracètres
    for i in range(1,10) :
        print(uart.read(1))

    uart.close()





def send(c):
    # Déclaration des variables utiles pour la com UART
    port = 'COM4' #PS>> py -3 -m serial.tools.list_ports, liste des ports utilisables
    baudrate = 9600
    bytesize = 8

    # Ouverture de la liaison UART
    uart = serial.Serial(port, baudrate, bytesize) #stopbits, serial.PARITY_NONE, stopbits, timeout, xonxoff, rtscts
    uart.close()

    uart.open()

    # Ecriture d'un caractère de test 'a'
    print("Envoi : [PC : Tx >> Rx FPGA] "+str(c))
    uart.write(c.encode('utf-8'))

    # Reception d'un caractère du FPGA
    print("Reception : [PC : Rx << Tx FPGA] ' ")
    print(uart.read(1))
    print("'")

    uart.close()


f=open("/var/www/html/instruction.txt")
instruction=f.read()
send(instruction)


