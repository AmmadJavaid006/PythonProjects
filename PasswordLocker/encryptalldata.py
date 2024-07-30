from cryptography.fernet import Fernet
import re

key = b'vbBaf5kSdiwjHsB6gRhhz5Vh1f36VEUaDLy4akH9pc8='
fernet = Fernet(key)

file = open("Passwords.txt", "r")
readfile = file.read()
websites = re.findall(r"Website:\s*(\S*)", readfile)
passwords = re.findall(r"Password:\s*(\S*)", readfile)
dict = dict(zip(websites, passwords))

for k, v in dict.items():
    val = dict[k]
    val = val.encode("utf-8")
    encrypteddata = fernet.encrypt(val)
    dict[k] = encrypteddata.decode("utf-8")

filer = open("Passwords.txt", "w")
for x, y in dict.items():
    filer.write(f"Website: {x}\n")
    filer.write(f"Password: {y}\n\n")