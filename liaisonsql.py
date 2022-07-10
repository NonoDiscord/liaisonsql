print('\n\nLIAISON SQL.\n\n')

serv = input('Host: ')
database = input('Nom DB: ')
user = input('UserID: ')
passwd = input('Mdp: ')

print(f'\nset mysql_connection_string "server={serv};database={database};userid={user};password={passwd}"\n')

input('Quit')
