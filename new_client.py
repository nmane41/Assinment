import socket
import tqdm
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step
host = "127.0.0.1"
port = 5001
fileTOSend = open("sample.txt", 'rb')
filename = fileTOSend.name
filesize = os.path.getsize(filename)
s = socket.socket()
print(" Connecting to" + str(host) + ":" + str(port))
s.connect((host, port))
print("[+] Connected.")
file_to_send = F"{filename}{SEPARATOR}{filesize}".encode()
s.send(file_to_send)
public_key = ''
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
with open(filename, "rb") as f:
    bytes_read = f.read(BUFFER_SIZE)
    # key = Fernet.generate_key()
    # encryption_type = Fernet(key)
    # encrypted_message = encryption_type.encrypt(bytes_read)
    encrypted = public_key.encrypt(
        bytes_read,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    s.sendall(encrypted)
    f.close()
print("File sent")
fileTOSend.close()
# close the socket
s.close()
