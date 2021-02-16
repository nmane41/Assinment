import socket
import tqdm
import os

# device's IP address
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
client_socket, address = s.accept()
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
# filesize = int(filesize)
rec_file = open("new_file.txt", 'wb')
private_key = ''
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
with open(filename, "rb") as f:
    bytes_read = client_socket.recv(BUFFER_SIZE)
    # key = Fernet.generate_key()
    # encryption_type = Fernet(key)
    # decrypted_message = encryption_type.decrypt(bytes_read)

    original_message = private_key.decrypt(
        bytes_read,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    rec_file.write(original_message)
rec_file.close()
# close the client socket
client_socket.close()
# close the server socket
s.close()
