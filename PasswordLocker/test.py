from cryptography.fernet import Fernet

key = b'vbBaf5kSdiwjHsB6gRhhz5Vh1f36VEUaDLy4akH9pc8='
fernet = Fernet(key)
data = b"Hello World"
val = fernet.encrypt(data)
print("Encrypted:", val)
print("Decrypted:", fernet.decrypt(val).decode("utf-8"))
print("Original Key:", key)
print("Object:", fernet)
