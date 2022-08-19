ApplicationKey = "" #required
AccountKey = "" #required

import os
import subprocess
import requests
import os
from os import system
import time
import hashlib
e_hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
eauth_sens = ('https://eauth.000webhostapp.com/api/', ApplicationKey, AccountKey)
def wahid(altashfir):
    altashfir = altashfir.replace("0", "-QZ-")
    altashfir = altashfir.replace("1", "-SA-")
    altashfir = altashfir.replace("2", "-IF-")
    altashfir = altashfir.replace("3", "DE-")
    altashfir = altashfir.replace("4", "-EE-")
    altashfir = altashfir.replace("5", "-JJ-")
    altashfir = altashfir.replace("6", "-GG-")
    altashfir = altashfir.replace("7", "MP-")
    altashfir = altashfir.replace("8", "-WI-")
    altashfir = altashfir.replace("9", "-ZF-")
    altashfir = altashfir.replace("a", "-XC-")
    altashfir = altashfir.replace("b", "-YU-")
    altashfir = altashfir.replace("c", "-OL-")
    altashfir = altashfir.replace("d", "MV-")
    altashfir = altashfir.replace("e", "-RS-")
    altashfir = altashfir.replace("f", "-EV-")
    altashfir = altashfir.replace("g", "-WZ-")
    altashfir = altashfir.replace("h", "DP-")
    altashfir = altashfir.replace("i", "-IJ-")
    altashfir = altashfir.replace("j", "-KN-")
    altashfir = altashfir.replace("k", "-CA-")
    altashfir = altashfir.replace("l", "-TW-")
    altashfir = altashfir.replace("m", "-BI-")
    altashfir = altashfir.replace("n", "-JH-")
    altashfir = altashfir.replace("o", "-MW-")
    altashfir = altashfir.replace("p", "-IS-")
    altashfir = altashfir.replace("q", "-LA-")
    altashfir = altashfir.replace("r", "-ME-")
    altashfir = altashfir.replace("s", "-EP-")
    altashfir = altashfir.replace("t", "-ON-")
    altashfir = altashfir.replace("u", "-WK-")
    altashfir = altashfir.replace("v", "-NB-")
    altashfir = altashfir.replace("w", "-BA-")
    altashfir = altashfir.replace("x", "-RE-")
    altashfir = altashfir.replace("y", "-IN-")
    altashfir = altashfir.replace("z", "-LU-")
    return altashfir
def aithnayn(tabadal):
    tabadal = tabadal.replace("-QZ-", "0")
    tabadal = tabadal.replace("-SA-", "1")
    tabadal = tabadal.replace("-IF-", "2")
    tabadal = tabadal.replace("DE-", "3")
    tabadal = tabadal.replace("-EE-", "4")
    tabadal = tabadal.replace("-JJ-", "5")
    tabadal = tabadal.replace("-GG-", "6")
    tabadal = tabadal.replace("MP-", "7")
    tabadal = tabadal.replace("-WI-", "8")
    tabadal = tabadal.replace("-ZF-", "9")
    tabadal = tabadal.replace("-XC-", "a")
    tabadal = tabadal.replace("-YU-", "b")
    tabadal = tabadal.replace("-OL-", "c")
    tabadal = tabadal.replace("MV-", "d")
    tabadal = tabadal.replace("-RS-", "e")
    tabadal = tabadal.replace("-EV-", "f")
    tabadal = tabadal.replace("-WZ-", "g")
    tabadal = tabadal.replace("DP-", "h")
    tabadal = tabadal.replace("-IJ-", "i")
    tabadal = tabadal.replace("-KN-", "j")
    tabadal = tabadal.replace("-CA-", "k")
    tabadal = tabadal.replace("-TW-", "l")
    tabadal = tabadal.replace("-BI-", "m")
    tabadal = tabadal.replace("-JH-", "n")
    tabadal = tabadal.replace("-MW-", "o")
    tabadal = tabadal.replace("-IS-", "p")
    tabadal = tabadal.replace("-LA-", "q")
    tabadal = tabadal.replace("-ME-", "r")
    tabadal = tabadal.replace("-EP-", "s")
    tabadal = tabadal.replace("-ON-", "t")
    tabadal = tabadal.replace("-WK-", "u")
    tabadal = tabadal.replace("-NB-", "v")
    tabadal = tabadal.replace("-BA-", "w")
    tabadal = tabadal.replace("-RE-", "x")
    tabadal = tabadal.replace("-IN-", "y")
    tabadal = tabadal.replace("-LU-", "z")
    return tabadal
try:
    initrq = requests.post(eauth_sens[0], data = {'s0rt': wahid('init'), '111110': wahid(eauth_sens[1]), '001011': wahid(eauth_sens[2]), '011001': wahid(e_hwid)})
    if aithnayn(initrq.text) == "incorrect_application_details":
        os.system('cls')
        print("Incorrect application details!")
        time.sleep(1)
        exit()
    elif aithnayn(initrq.text) == "banned_user":
        exit()
    elif aithnayn(initrq.text) == "down":
        os.system('cls')
        print("Eauth is down at the moment, come back later!")
        time.sleep(1)
        exit()
    elif initrq.text == "":
        os.system('cls')
        print("Oops, something went wrong!")
        time.sleep(1)
        exit()
    else:
        responser = initrq.json()
        for app_json_encode in responser:
            Status = aithnayn(app_json_encode[aithnayn('STATUS')])
            ApplicationName = aithnayn(app_json_encode[aithnayn('APPNAME')])
            Loggedmessage =aithnayn( app_json_encode[aithnayn('LOGGED')])
            Registeredmessage = aithnayn(app_json_encode[aithnayn('REGISTERED')])
            Pausedmessage = aithnayn(app_json_encode[aithnayn('PAUSED')])
            system("title " + ApplicationName)
            if Status == "0":
                os.system('cls')
                print(Pausedmessage)
                time.sleep(2)
                exit()
except:
    exit()

class User_Info:
    Username = ""
    Rank = ""
    CreateDate = ""
    ExpireDate = ""
    HardwareID = e_hwid

ins = User_Info()

def tashfir(tajzia):
    e_c = \
        hashlib.sha512(tajzia.encode()).hexdigest()
    return e_c

def signin(username,password):
    try:
        passrq = tashfir(password)
        loginrq = requests.post(eauth_sens[0], data = {'s0rt': wahid('l0gin'), 'username': wahid(username), 'passw0rd': wahid(passrq), 'hwid': wahid(e_hwid),'appkey': wahid(eauth_sens[1]),'acckey': wahid(eauth_sens[2])})
        if aithnayn(loginrq.text) == "incorrect_login_details":
            os.system('cls')
            print("Incorrect login details!")
            time.sleep(2)
            exit()
        if aithnayn(loginrq.text) == "incorrect_user_details":
            os.system('cls')
            print("Incorrect login details!")
            time.sleep(2)
            exit()
        elif aithnayn(loginrq.text) == "hwid_does_not_match":
            os.system('cls')
            print("Hwid doesn't match!")
            time.sleep(2)
            exit()
        elif aithnayn(loginrq.text) == "subscription_has_expired":
            os.system('cls')
            print("Your subscription has expired!")
            time.sleep(2)
            exit()
        else:
            responser = loginrq.json()
            for user_json_encode in responser:
                ins.Username = aithnayn(user_json_encode[aithnayn('NAME')])
                ins.Rank = aithnayn(user_json_encode[aithnayn('RANKUSER')])
                ins.CreateDate = aithnayn(user_json_encode[aithnayn('CREATEDATE')])
                ins.ExpireDate = aithnayn(user_json_encode[aithnayn('EXPIREDATE')])
    except:
        exit()

def signup(username,password,invite):
    try:
        passrq = tashfir(password)
        registerrq = requests.post(eauth_sens[0], data = {'s0rt': wahid('register'), 'username': wahid(username), 'passw0rd': wahid(passrq),'invite': wahid(invite), 'hwid': wahid(e_hwid),'appkey': wahid(eauth_sens[1]),'acckey': wahid(eauth_sens[2])})
        if aithnayn(registerrq.text) == "name_already_used":
            os.system('cls')
            print("Name already used!")
            time.sleep(2)
            exit()
        if aithnayn(registerrq.text) == "incorrect_register_details":
            os.system('cls')
            print("Incorrect register details!")
            time.sleep(2)
            exit()
        elif aithnayn(registerrq.text) == "key_not_found":
            os.system('cls')
            print("Key not found!")
            time.sleep(2)
            exit()
        elif aithnayn(registerrq.text) == "maximum_users":
            os.system('cls')
            print("The Application reached maximum users, it's time for an upgrade!")
            time.sleep(2)
            exit()
    except:
        exit()

def grabvariable(varid):
    try:
        varrq = requests.post(eauth_sens[0], data = {'s0rt': wahid('var'), 'varid': wahid(varid),'appkey': wahid(eauth_sens[1]),'acckey': wahid(eauth_sens[2])})
        if aithnayn(varrq.text) == "var_not_found":
            return ">_<"
        elif aithnayn(varrq.text) == "incorrect_application_details":
            exit()
        else:
            return aithnayn(varrq.text)
    except:
        exit()
