import re, pyperclip, sys
from cryptography.fernet import Fernet

key = b'vbBaf5kSdiwjHsB6gRhhz5Vh1f36VEUaDLy4akH9pc8='
fernet_key = Fernet(key)
list = list()

def load_credentials():
    passwordfile = open("Passwords.txt", 'r')
    readfile = passwordfile.read()
    passwordfile.close()
    websites = re.findall(r"Website:\s*(\S*)", readfile)
    inpasswords = re.findall(r"Password:\s*(\S*)", readfile)
    for z in inpasswords:
        passwords = z.encode("utf-8")
        passwordas = fernet_key.decrypt(passwords)
        list.append(passwordas.decode("utf-8"))
    return dict(zip(websites, list))

def save_credentials(credentials):
    passwordfile = open("Passwords.txt", 'w')
    for k, v in credentials.items():
        v = v.encode("utf-8")
        vv = fernet_key.encrypt(v).decode("utf-8")
        passwordfile.write(f"Website: {k}\n")
        passwordfile.write(f"Password: {vv}\n\n")
    passwordfile.close()

def changepass(webin, passin, credentials):
    credentials[webin] = passin
    save_credentials(credentials)

def addpass(addpasskey, addpassval, credentials):
    credentials[addpasskey] = addpassval
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
    pyperclip.copy(values)

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
                        passwordtocopy = input("Which Password You Want To Copy? : ")
                        confirmuser = input("Enter Master Password Again To Copy: ")
                        if passwordtocopy in credentials and confirmuser == "72364899**":
                            copypass(passwordtocopy, credentials)
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