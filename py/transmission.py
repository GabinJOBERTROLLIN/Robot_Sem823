import serial
import time
import robotDriver as rd

#linux
port_uart = "/dev/serial0"
path = "/var/www/html/instruction.txt"
baudrate = 19200


bytesize = 8


uart = serial.Serial(port_uart,baudrate,bytesize)
uart.timeout = 0.1

last_instruction = ""
mode = "manuel"
#robot = rd.BotMaster()

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
"""
def switchMode():
    if mode == "manuel":
        mode
        robot.pilotage(0,5)


switchMode()"""

while 1:
    # lecture des instructions
    f=open(path,'r')
    instruction=f.read()
    f.close()

    if last_instruction != "":
        if last_instruction != instruction and instruction != "m":
            send(instruction)
            last_instruction = instruction

        elif instruction == "m":
            switchMode()
    else:
        send(instruction)
        last_instruction = instruction
        
            
    # on recoit les informations
    receive()

uart.close()