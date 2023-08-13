import os
import eauth
from datetime import datetime
import platform
import time

# Init request
if (not eauth.init_request()):
    print(eauth.error_message)
    time.sleep(1.5)
    exit(0)

now = datetime.now()
my_system = platform.uname()
print("[+] initializing api")
time.sleep(0.5)
print("[+] attached to server")
time.sleep(1)
os.system('cls')
eauth.run_pause_command()
def main_f():
    os.system('cls')
    print("▒█▀▀▀ ░█▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█░▒█ ")
    print("▒█▀▀▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▀▀█ ")
    print("▒█▄▄▄ ▒█░▒█ ░▀▄▄▀ ░▒█░░ ▒█░▒█")
    print(" ")
    print(" ")
    print("[ 1 ] Login     [ 2 ] Register")
    print(" ")
    current_time = now.strftime("%X")
    print("[",current_time,"]",end=" ")
    value = input("user@eauth:~$ ")
    if value == "1":
        os.system('cls')
        username = input("Username: ")
        password = input("Password: ")
        if (eauth.login_request(username, password)):
            os.system('cls')
            print(eauth.logged_message)
            print(" ")
            print("Rank: " + eauth.rank)
            print("Create Date: " + eauth.register_date)
            print("Expire Date: " + eauth.expire_date)
            print("Hardware ID: " + eauth.user_hwid)
        else:
            print(eauth.error_message)
        time.sleep(3)
        main_f()
    elif value == "2":
        os.system('cls')
        username = input("Username: ")
        password = input("Password: ")
        invite = input("License Key: ")
        if (eauth.register_request(username, password, invite)):
            os.system('cls')
            print(eauth.registered_message)
        else:
            print(eauth.error_message)
        time.sleep(1.5)
        main_f()
    else:
        os.system('cls')
        print("Invalid input!")
        time.sleep(1)
        main_f()
main_f()
eauth.run_pause_command()
