import re, pyperclip, sys
from cryptography.fernet import Fernet

key = b'vbBaf5kSdiwjHsB6gRhhz5Vh1f36VEUaDLy4akH9pc8='
fernet_key = Fernet(key)

def load_credentials():
    passwordfile = open("Passwords.txt", 'r')
    readfile = passwordfile.read()
    passwordfile.close()
    websites = re.findall(r"Website:\s*(\S*)", readfile)
    passwords = re.findall(r"Password:\s*(\S*)", readfile)
    return dict(zip(websites, passwords))

def save_credentials(credentials):
    passwordfile = open("Passwords.txt", 'w')
    for k, v in credentials.items():
        passwordfile.write(f"Website: {k}\n")
        passwordfile.write(f"Password: {v}\n\n")
    passwordfile.close()

def changepass(webin, passin, credentials):
    passin = passin.encode("utf-8")
    finalpassin = fernet_key.encrypt(passin)
    credentials[webin] = finalpassin.decode("utf-8")
    save_credentials(credentials)

def addpass(addpasskey, addpassval, credentials):
    addpassval = addpassval.encode("utf-8")
    values = fernet_key.encrypt(addpassval)
    credentials[addpasskey] = values.decode("utf-8")
    save_credentials(credentials)

def displaypass(credentials):
    print("----------------------")
    for k, v in credentials.items():
        print(k, "\nPassword:", v)
        print("----------------------")

def displaykeys(credentials):
    print("--------------")
    for k in credentials.keys():
        print(k)
        print("--------------")

def copypass(tocopy, credentials):
    values = credentials[tocopy]
    values = values.encode("utf-8")
    finalval = fernet_key.decrypt(values)
    pyperclip.copy(finalval.decode("utf-8"))
def masterpass():
    credentials = load_credentials()
    for tries in range(1, 4):
        pin = input("Enter The Master Code: ")
        if pin == "72364899**":
            for triesss in range(1, 4):
                mode = input("Which Mode You Want To Use? COPY OR CHANGE OR ADD: ")
                if mode.lower() == "copy":
                    displaypass(credentials)
                    for countx in range(1, 4):
                        passwordstocopy = input("Which Password You Want To Copy? : ")
                        confirmuser = input("Enter Master Password Again To Copy: ")
                        if passwordstocopy in credentials and confirmuser == "72364899**":
                            copypass(passwordstocopy, credentials)
                            print("Password Copied Successfully!")
                            break
                        else:
                            print("Name or Master Password Not Correct! Try Again!")
                    break
                elif mode.lower() == "change":
                    displaykeys(credentials)
                    for count in range(1, 4):
                        passwordtochange = input("Which Password You Want To Change? : ")
                        if passwordtochange in credentials:
                            tochangewith = input("What Will be Your New Password: ")
                            confirmchangepass = input("Re-enter To Change Password: ")
                            confirmuser = input("Enter Your Master Password Again To Change: ")
                            if confirmchangepass == tochangewith and confirmuser == "72364899**":
                                changepass(passwordtochange, confirmchangepass, credentials)
                                print("Password Changed Successfully!")
                                break
                            else:
                                print("Master Password or Passwords Don't Match. Terminating Program...")
                                sys.exit()
                        else:
                            print("Name or Master Password Not Correct! Try Again!")
                    break
                elif mode.lower() == "add":
                    addkey = input("What Will Be The Website Name: ")
                    addvalue = input("What Will Be The Password: ")
                    for f in range(1, 5):
                        confirm = input("Enter Master Password Again: ")
                        if confirm == "72364899**":
                            addpass(addkey, addvalue, credentials)
                            break
                        else:
                            print("Wrong Master Password!!")
                            f += 1
                            continue
                    break
                else:
                    print(f'Enter Either "COPY" or "CHANGE". "{mode}" Is Not A Mode')
            break
        else:
            print("Wrong Master Password. Try Again!")

masterpass()
