import re, pyperclip, sys

def load_credentials():
    passwordfile = open("Passwords.txt", 'r')
    readfile = passwordfile.read()
    passwordfile.close()
    websites = re.findall(r"Website:\s*(\S*)", readfile)
    passwords = re.findall(r"Password:\s*(\S*)", readfile)
    return dict(zip(websites, passwords))

def save_credentials(file_path, credentials):
    passwordfile = open(file_path, 'w')
    for k, v in credentials.items():
        passwordfile.write(f"Website: {k}\n")
        passwordfile.write(f"Password: {v}\n\n")
    passwordfile.close()

def changepass(webin, passin, credentials):
    credentials[webin] = passin
    save_credentials("Passwords.txt", credentials)

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
    pyperclip.copy(credentials[tocopy])

def masterpass():
    credentials = load_credentials("Passwords.txt")
    for tries in range(1, 4):
        pin = input("Enter The Master Code: ")
        if pin == "72364899**":
            for triesss in range(1, 4):
                mode = input("Which Mode You Want To Use? COPY OR CHANGE: ")
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
                else:
                    print(f'Enter Either "COPY" or "CHANGE". "{mode}" Is Not A Mode')
            break
        else:
            print("Wrong Master Password. Try Again!")

masterpass()
