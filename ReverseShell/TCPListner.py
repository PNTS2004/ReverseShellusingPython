import socket
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 44444))
s.listen(1)

print("Listening on 0.0.0.0 ..........")

conn, addr = s.accept()

print(f"Connection recieved from {addr}")

conn.close()
s.close()
