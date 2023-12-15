import time
import serial
import serial.tools.list_ports
import os
import sys
from os import system
from colorama import *
import requests
import keyboard

# Colors
blue = Fore.BLUE
purple = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX
orange = Fore.LIGHTYELLOW_EX

# Settings
developer_mode = True

# Init
system('title M-Terminal (Loading)')
version = "1.0.1"

def get_latest_release(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        return release_info['tag_name']
    else:
        print(f"Error: Unable to get release information. Status code: {response.status_code}")
        return None

repo_owner = "justcallmekoko"
repo_name = "ESP32Marauder"
marauder_version = get_latest_release(repo_owner, repo_name)


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
    else:
        print(yellow + "There are no active ports")
        input(f"{gray}Press {green}ENTER{gray} to continue")
        main()
            

def connect_to_serial(port, baudrate=115200, timeout=1):
    try:
        return serial.Serial(port, baudrate, timeout=timeout)
    except serial.SerialException as e:
        print(f"Error: {e}")
        return None


def serial_console(serial_connection):
    print(f"{yellow}M-Terminal {gray}{version}{yellow} - Hold 'Spacebar' to exit")

    accumulated_data = []
    user_input = input("> ")

    if user_input == "exit":
        main()

    while True:     
        accumulated_data.append(user_input)
        serialized_data = "\n".join(accumulated_data) + "\n"
        serial_connection.write(serialized_data.encode())
        received_data = serial_connection.read_all().decode("utf-8")
        print(received_data, end="")
        if keyboard.is_pressed("space"):
            print(f"Ending loop")
            break
        time.sleep(3)


def menu3():
    os.system('cls')
    print(yellow + "Please specify which port (e.g., COM1)" + white)
    port_name = input("> ")

    serial_connection = connect_to_serial(f"COM{port_name}")

    if serial_connection:
        try:
            os.system('cls')
            system(f'title M-Terminal (Active - COM{port_name})')
            serial_console(serial_connection)
        finally:
            serial_connection.close()
            main()
    

def menu4():
    os.system('cls')   
    print(f"""
{gray}[{yellow}Developer{gray}] {blue}jbablestime
{gray}[{yellow}Version{gray}] {green}{version}
{gray}[{yellow}Marauder Version{gray}] {marauder_version}""")
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

if __name__ == "__main__":
    file_path = sys.argv[0]

    if file_path.lower().endswith(".py") and developer_mode == False:
        print(f"{red}Error: {yellow}This script cannot be executed as a Python file. Please run the {green}installer.bat")
        time.sleep(5)
        sys.exit()
    elif file_path.lower().endswith(".exe") and developer_mode == False:
        print("Starting...")
        print(f"You're using {blue}M-Terminal {green}{version}" + white)
        time.sleep(2)
        main()
    elif file_path.lower().endswith(".py") and developer_mode == True:
        print("Starting...")
        print(f"You're using {blue}M-Terminal {green}{version}" + white)
        time.sleep(2)
        main()
