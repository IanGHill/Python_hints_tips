#w rong way
# username = input('Username: ')
# password = input('Password: ')
#
# print('Logging In...')

from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')

print('Logging In...')