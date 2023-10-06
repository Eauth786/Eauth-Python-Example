import requests
import json
import platform
import hashlib
import os
import datetime
import subprocess
import webbrowser
import sys

# Required configuration
account_key = "" # Your account key goes here
application_key = "" # Your application key goes here
application_ID = "" # Your application ID goes here
application_version = "1.0" # Your application version goes here

# Advanced configuration
invalid_account_key_message = "Invalid account key!"
invalid_application_key_message = "Invalid application key!"
invalid_request_message = "Invalid request!"
outdated_version_message = "Outdated version, please upgrade!"
busy_sessions_message = "Please try again later!"
unavailable_session_message = "Invalid session. Please re-launch the app!"
used_session_message = "Why did the computer go to therapy? Because it had a case of 'Request Repeatitis' and couldn't stop asking for the same thing over and over again!"
overcrowded_session_message = "Session limit exceeded. Please re-launch the app!"
expired_session_message = "Your session has timed out. Please re-launch the app!"
invalid_user_message = "Incorrect login credentials!"
banned_user_message = "Access denied!"
incorrect_hwid_message = "Hardware ID mismatch. Please try again with the correct device!"
expired_user_message = "Your subscription has ended. Please renew to continue using our service!"
used_name_message = "Username already taken. Please choose a different username!"
invalid_key_message = "Invalid key. Please enter a valid key!"
upgrade_your_eauth_message = "Upgrade your Eauth plan to exceed the limits!"

# Dynamic configuration
init = False
login = False
register = False

session_id = ""
app_status = ""
app_name = ""
logged_message = ""
registered_message = ""
error_message = ""

rank = ""
register_date = ""
expire_date = ""
hwid = ""
user_hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

def compute_sha512(input_string):
    sha512 = hashlib.sha512()
    sha512.update(input_string.encode('utf-8'))
    return sha512.hexdigest()

def generate_auth_token(message, app_id):
    timestamp = str(int(datetime.datetime.utcnow().timestamp()))[:-5]
    auth_token = timestamp + message + app_id
    return compute_sha512(auth_token)

# Pause command
def run_pause_command():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        input('Press Enter to continue...')

# Send post request to Eauth
def run_request(params):
    response = requests.post('https://eauth.us.to/api/1.1/',
                             headers={"User-Agent": 'e_a_u_t_h'},
                             data=params)
                                     
    # JSON string
    json_string = response.text

    # Parse the JSON string into a dictionary
    data = json.loads(json_string)

    # Get the values from the dictionary using the keys
    message = data['message']
    
    # Read signature
    if (message == "init_success" or message == "login_success" or message == "register_success" or message == "var_grab_success"):
        auth_header = response.headers.get('Signature')
        if (auth_header != generate_auth_token(response.text, application_ID)):
            sys.exit(0)
   
    return response.text

def raise_error(error):
    global error_message
    error_message = error

# Eauth init request
def init_request():
    global init, session_id, app_status, app_name, logged_message, registered_message, error_message

    if (init):
        return init
    
    data = {
        'sort': 'init',
        'appkey': application_key,
        'acckey': account_key,
        'hwid': user_hwid,
        'version': application_version
    }

    # JSON string
    json_string = run_request(data)

    # Parse the JSON string into a dictionary
    data = json.loads(json_string)

    # Get the values from the dictionary using the keys
    message = data['message']

    # Check response
    if (message == 'init_success'):
        init = True
        session_id = data['session_id']
        app_status = data['app_status']
        app_name = data['app_name']
        logged_message = data['logged_message']
        registered_message = data['registered_message']
    elif (message == 'invalid_account_key'):
        raise_error(invalid_account_key_message)
    elif (message == 'invalid_application_key'):
        raise_error(invalid_application_key_message)
    elif (message == 'invalid_request'):
        raise_error(invalid_request_message)
    elif (message == 'version_outdated'):
        download_link = data['download_link']
        if (download_link != ''):
            webbrowser.open(download_link)
        raise_error(outdated_version_message)
    elif (message == 'maximum_sessions_reached'):
        raise_error(busy_sessions_message)
    elif (message == 'user_is_banned'):
        raise_error(banned_user_message)
    elif (message == 'init_paused'):
        raise_error(data['paused_message'])

    # Return
    return init

# Eauth login request
def login_request(username, password):
    global login, rank, register_date, expire_date, hwid, error_message

    if (login):
        return login
    
    data = {
        'sort': 'login',
        'sessionid': session_id,
        'username': username,
        'password': password,
        'hwid': user_hwid,
    }

    # JSON string
    json_string = run_request(data)

    # Parse the JSON string into a dictionary
    data = json.loads(json_string)

    # Get the values from the dictionary using the keys
    message = data['message']

    # Check response
    if (message == 'login_success'):
        login = True
        rank = data['rank']
        register_date = data['register_date']
        expire_date = data['expire_date']
        hwid = data['hwid']
    elif (message == 'invalid_account_key'):
        raise_error(invalid_account_key_message)
    elif (message == 'invalid_application_key'):
        raise_error(invalid_application_key_message)
    elif (message == 'invalid_request'):
        raise_error(invalid_request_message)
    elif (message == 'session_unavailable'):
        raise_error(unavailable_session_message)
    elif (message == 'session_already_used'):
        raise_error(used_session_message)
    elif (message == 'session_overcrowded'):
        raise_error(overcrowded_session_message)
    elif (message == 'session_expired'):
        raise_error(expired_session_message)
    elif (message == 'account_unavailable'):
        raise_error(invalid_user_message)
    elif (message == 'user_is_banned'):
        raise_error(banned_user_message)
    elif (message == 'hwid_incorrect'):
        raise_error(incorrect_hwid_message)
    elif (message == 'subscription_expired'):
        raise_error(expired_session_message)

    return login

# Eauth register request
def register_request(username, password, key):
    global register, error_message

    if (register):
        return register
    
    data = {
        'sort': 'register',
        'sessionid': session_id,
        'username': username,
        'password': password,
        'key': key,
        'hwid': user_hwid,
    }

    # JSON string
    json_string = run_request(data)

    # Parse the JSON string into a dictionary
    data = json.loads(json_string)

    # Get the values from the dictionary using the keys
    message = data['message']

    # Check response
    if (message == 'register_success'):
        register = True
    elif (message == 'invalid_account_key'):
        raise_error(invalid_account_key_message)
    elif (message == 'invalid_request'):
        raise_error(invalid_request_message)
    elif (message == 'session_unavailable'):
        raise_error(unavailable_session_message)
    elif (message == 'session_already_used'):
        raise_error(used_session_message)
    elif (message == 'session_overcrowded'):
        raise_error(overcrowded_session_message)
    elif (message == 'session_expired'):
        raise_error(expired_session_message)
    elif (message == 'account_unavailable'):
        raise_error(invalid_user_message)
    elif (message == 'name_already_used'):
        raise_error(used_name_message)
    elif (message == 'key_unavailable'):
        raise_error(invalid_key_message)
    elif (message == 'user_is_banned'):
        raise_error(banned_user_message)
    elif (message == 'maximum_users_reached'):
        raise_error(upgrade_your_eauth_message)

    return register
