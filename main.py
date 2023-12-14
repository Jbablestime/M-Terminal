import time
import serial
import serial.tools.list_ports
import os
from os import system
from colorama import *

# Colors
blue = Fore.BLUE
purple = Fore.MAGENTA
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX
orange = Fore.LIGHTYELLOW_EX

# Init
system('title M-Terminal (Loading)')

# Menus

def menu1():
    os.system('cls')
    print(green + 
f"""{yellow}
attack
btspamall
btwardrive
channel
clearlist
evilportal
gpsdata
help
led
list
reboot
scanap
scansta
select
settings
sigmon
sniffraw
sniffbeacon
sniffdeauth
sniffesp
sniffpmkid
sniffpwn
sourapple
ssid
stopscan
samsungblespam
swiftpair
update
wardrive""")
    input(f"{gray}Press {green}ENTER{gray} to continue")
    main()


def menu2():
    os.system('cls')
    ports = serial.tools.list_ports.comports()
    if ports:
        for port in ports:
            print(f"{yellow}- {port.device}")
            input(f"{gray}Press {green}ENTER{gray} to continue")
            main()


def connect_to_serial(port, baudrate=115200, timeout=1):
    try:
        return serial.Serial(port, baudrate, timeout=timeout)
    except serial.SerialException as e:
        print(f"Error: {e}")
        return None

def serial_console(serial_connection):
    print(green + "Console - Version 1.0.0" + yellow)

    accumulated_data = []
    user_input = input("> ")

    while True:
        
        if user_input.lower() == 'exit':
            break

        accumulated_data.append(user_input)
        serialized_data = "\n".join(accumulated_data) + "\n"
        serial_connection.write(serialized_data.encode())
        received_data = serial_connection.read_all().decode("utf-8")
        print(received_data, end="")
        time.sleep(3)

def menu3():
    os.system('cls')
    print(green + "Please specify which port (e.g., COM1)" + white)
    port_name = input("> ")

    serial_connection = connect_to_serial(f"COM{port_name}")

    if serial_connection:
        try:
            os.system('cls')
            system(f'title M-Terminal (Active - COM{port_name})')
            serial_console(serial_connection)
        finally:
            # Close the serial connection when done
            serial_connection.close()
            main()
    

def menu4():
    os.system('cls')
    print(
f"""
{blue}Developer: {gray}jbablestime
""")
    input(f"{gray}Press {green}ENTER{gray} to continue")
    main()

def main():
    system('title M-Terminal (Inactive)')
    os.system('cls')
    print(f"{gray}[{yellow}1{gray}] {blue}Help{white}  {gray}[{yellow}2{gray}] {green}Ports{white}  {gray}[{yellow}3{gray}] {orange}Console{white}  {gray}[{yellow}4{gray}] {purple}Info{white}")
    command = input(yellow + "> ")

    if command == "1":
        menu1()
    elif command == "2":
        menu2()
    elif command == "3":
        menu3()
    elif command == "4":
        menu4()

# Run
main()

