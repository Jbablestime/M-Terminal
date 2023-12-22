
import time
import serial
import serial.tools.list_ports
import os
import sys
from os import system
from colorama import *
import requests
import keyboard
import shutil
import tkinter as tk
from tkinter import filedialog
import psutil
import subprocess

# Colors
blue = Fore.BLUE
purple = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX
orange = Fore.LIGHTYELLOW_EX

ports = serial.tools.list_ports.comports()
repo_owner = "justcallmekoko"
repo_name = "ESP32Marauder"
developer_mode = False
version = "0.1.2"
system(f"title M-Terminal │ Startup")

def menu1():
    os.system('cls')
    if ports:
        system('title M-Terminal │ Connected')
    if not ports:
        system('title M-Terminal │ Not Connected')
    try:
        print(f"""{yellow}attack
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
    except Exception:
        print(f"{gray}[{yellow}System{gray}] {red}There was a issue loading the menu. If the issue persists, contact a developer.")
        main()

def menu2():
    os.system('cls')
    try:
        ports = serial.tools.list_ports.comports()
        if ports:
            for port in ports:
                print(f"{yellow}{port.device}")
                input(f"{gray}Press {green}ENTER{gray} to continue")
                main()
        else:
            print(yellow + "There are no active ports")
            input(f"{gray}Press {green}ENTER{gray} to continue")
            main()
    except Exception:
        print(f"{gray}[{yellow}System{gray}] {red}There was a issue loading the menu. If the issue persists, contact a developer.")
        main()

def connect_to_serial(port, baudrate=115200, timeout=1):
    try:
        return serial.Serial(port, baudrate, timeout=timeout)
    except serial.SerialException as e:
        print(f"{gray}[{yellow}System{gray}] {red}Please ensure that your device is connected properly and that you have the proper drivers installed.")
        time.sleep(10)
        main()

def serial_console(serial_connection):
    print(f"{yellow}M-Terminal {gray}{version}{yellow}")
    print(red + "You must restart the program to exit console" + yellow)
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
        time.sleep(3)



def menu3():
    os.system('cls')
    try:
        print(yellow + "Please specify which port (e.g., COM1)" + white)
        port_name = input("> ")
        serial_connection = connect_to_serial(f"COM{port_name}")
        if serial_connection:
            try:
                os.system('cls')
                system(f'title M-Terminal (Active - COM{port_name})')
                serial_console(serial_connection)
            except Exception:
                main()
            finally:
                serial_connection.close()
                main()
    except Exception:
        print(f"{gray}[{yellow}System{gray}] {red}There was a issue loading the menu. If the issue persists, contact a developer.")
        main()

def menu4():
    os.system('cls')
    try: 
        print(f"""{gray}[{yellow}Developer{gray}] {blue}jbablestime
{gray}[{yellow}Version{gray}] {green}{version}
{gray}[{yellow}Marauder Version{gray}] {release_info['tag_name']}""")
        input(f"{gray}Press {green}ENTER{gray} to continue")
        main()
    except Exception:
        print(f"{gray}[{yellow}System{gray}] {red}There was a issue loading the menu. If the issue persists, contact a developer.")
        main()


def menu5():
    os.system('cls')
    try:
        print(f"{gray}[{yellow}System{gray}] {red}This feature is not ready yet!")
        time.sleep(5)
        main()
    except Exception:
        main()

        


def main():
    os.system('cls')
    if ports:
        system('title M-Terminal │ Connected')
    if not ports:
        system('title M-Terminal │ Not Connected')
    try:
        print(f"{gray}[{yellow}1{gray}] {blue}Help{white}  {gray}[{yellow}2{gray}] {green}Ports{white}  {gray}[{yellow}3{gray}] {orange}Console{white}  {gray}[{yellow}4{gray}] {purple}Info{white}  {gray}[{yellow}5{gray}] {red}Upload{white}")
        command = input(yellow + "> ")

        if command == "1":
            menu1()
        elif command == "2":
            menu2()
        elif command == "3":
            menu3()
        elif command == "4":
            menu4()
        elif command == "5":
            menu5
        elif command == "6":
            os.system('cls')
            print(f"{gray}[{yellow}System{gray}] {yellow}Restarting...")
            time.sleep(2.5 )
            os.system('cls')
            python = sys.executable
            subprocess.run([python] + sys.argv)
        else:
            os.system('cls')
            print(f"{gray}[{yellow}System{gray}] {red}That page doesn't exist!")
            time.sleep(2.5)
            main()
    except Exception:
        system('title M-Terminal │ Error')
        print(f"{gray}[{yellow}System{gray}] {red}There was a issue loading the menu. If the issue persists, contact a developer.")


try:
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    print(f"{yellow}Welcome to {blue}M-Terminal{yellow}")
    time.sleep(1.5)
    os.system('cls')
    print(f"{gray}[{yellow}System{gray}] {yellow}Starting...")
    print(f"{gray}[{yellow}System{gray}] {yellow}Getting latest Marauder version...")
    if response.status_code == 200:
        release_info = response.json()
        print(f"{gray}[{yellow}System{gray}] {yellow}The latest version is " + green + release_info['tag_name'])
        time.sleep(2.5)
        os.system('cls')
    print(f"{gray}[{yellow}System{gray}] {yellow}Checking application files...")
    file_path = sys.argv[0]
    if file_path.lower().endswith(".py") and developer_mode == False:
        system('title M-Terminal │ Error')
        print(f"{gray}[{yellow}System{gray}] {red}This file cannot be ran as a Python file, please run the {yellow}installer.bat{red}.")
        time.sleep(5)
        sys.exit()
    elif file_path.lower().endswith(".py") and developer_mode == True:
        print(f"{gray}[{yellow}System{gray}] {yellow}Bypassing application check, hello developer.")
        time.sleep(2.5)
        os.system('cls')
        print(f"{gray}[{yellow}System{gray}] {green}Start complete, continuing...")
        time.sleep(2)
        main()
    elif file_path.lower().endswith(".exe"):
        os.system('cls')
        print(f"{gray}[{yellow}System{gray}] {green}Start complete, continuing...")
        time.sleep(2)
        main()
    elif response.status_code == 404:
        system('title M-Terminal │ Error')
        print(f"{gray}[{yellow}System{gray}] {red}There was a problem getting the latest version, check your internet connection and try again.")
        pass
except Exception:
    system('title M-Terminal │ Error')
    print(f"{gray}[{yellow}System{gray}] {red}There was a problem, check your internet connection and try again.")
    os.system('pause')

