import socket #import socket Python library
import sys #import OS related Python library
import _thread

HOST = input("Enter your Host computer's IP address: ")
PORT = 45000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	
print('Socket created') #Show feedback to user

#Try create the socket on the local host and specific port or handle an error if it fails
try:
	 s.bind((HOST, PORT))

except socket.error as msg: 
	print('Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

print('Socket bind complete') #Show feedback to user

s.listen(10)

print('Genji is now listening to you')


def Message(c):

	while True:
		message = 'Type in something '
		input = ''
		c.send(message.encode("utf-8"))
		mrecv = c.recv(1024).decode("utf-8")
		print(mrecv)
while 1:
	c, addres = s.accept()
	print('Connected to by %s:%s' % (addres[0], addres[1]))
	
	_thread.start_new_thread(Message, (c,))

s.close()

