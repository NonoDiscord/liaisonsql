import csv
import sys
import os
import platform
import psutil

import colorama
from colorama import Fore
from colorama import Style

colorama.init()

def main():
   menu()

def menu():
    print(Fore.YELLOW + '''
██╗     ██╗ █████╗ ██╗███████╗ ██████╗ ███╗   ██╗    ███████╗ ██████╗ ██╗     
██║     ██║██╔══██╗██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔═══██╗██║     
██║     ██║███████║██║███████╗██║   ██║██╔██╗ ██║    ███████╗██║   ██║██║     
██║     ██║██╔══██║██║╚════██║██║   ██║██║╚██╗██║    ╚════██║██║▄▄ ██║██║     
███████╗██║██║  ██║██║███████║╚██████╔╝██║ ╚████║    ███████║╚██████╔╝███████╗
╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚══▀▀═╝ ╚══════╝                                                                                                                              
                                         ''' + Style.RESET_ALL)
    print()


    choice = input('''
                     [1] -> lier son SQL
                     [2] -> GitHub
                     [0] -> Quitter

                      Entrer un numéro : ''')


    if choice == "1":
        print('')
        server = input('Ip de la database: ')
        database = input('Nom de la DB: ')
        userid = input('Userid: ')
        password = input('Password: ')
        print('')
        print('set mysql_connection_string "server={};database={};userid={};password={}"' .format(server, database, userid, password))
        print('')
        click = input('Cliquez sur entrée pour revenir au menu')
        os.system('{}' .format(click))
        os.system('cls')
        menu()


    elif choice == "2":
        print('')
        os.system('start https://github.com/NonoDiscord')
        click = input('Cliquez sur entrée pour revenir au menu')
        os.system('{}' .format(click))
        os.system('cls')
        menu()

    elif choice == "0":
        sys.exit
        print('')

    else:
        os.system('cls')
        menu()
    
main()

input('Cliquez sur entrée pour quitter')
