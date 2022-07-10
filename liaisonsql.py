import sys
from os import system

print('LIAISON SQL.')

serv = input('Host: ')
database = input('Nom DB: ')
user = input('UserID: ')
passwd = input('Mdp: ')

print(f'\nset mysql_connection_string "server={serv};database={database};userid={user};password={passwd}"\n')

input('Quit')
